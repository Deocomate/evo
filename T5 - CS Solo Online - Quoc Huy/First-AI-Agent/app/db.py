import mysql.connector
from mysql.connector import Error
import os
from tabulate import tabulate


class DatabaseHandler:
    def __init__(self, _=None):
        # Biến _=None để giữ tương thích tham số đầu vào nếu file agent.py truyền path cũ
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = os.getenv("DB_PORT", "3306")
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        self.database = os.getenv("DB_NAME", "cafe_management")

        self.init_db()

    def get_connection(self, check_db_exists=True):
        """Tạo kết nối tới MySQL"""
        try:
            config = {
                'host': self.host,
                'port': self.port,
                'user': self.user,
                'password': self.password,
            }
            if check_db_exists:
                config['database'] = self.database

            conn = mysql.connector.connect(**config)
            return conn
        except Error as e:
            print(f"[!] Lỗi kết nối MySQL: {e}")
            return None

    def init_db(self):
        """Khởi tạo database và bảng từ file sql nếu chưa có"""
        # 1. Kết nối không cần tên DB để tạo DB nếu chưa có
        conn = self.get_connection(check_db_exists=False)
        if conn:
            cursor = conn.cursor()
            try:
                # Tạo DB nếu chưa tồn tại
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
                print(f"[*] Đã kiểm tra database '{self.database}'.")
            except Error as e:
                print(f"[!] Lỗi tạo Database: {e}")
            finally:
                cursor.close()
                conn.close()

        # 2. Kết nối vào DB vừa tạo để chạy script tạo bảng
        conn = self.get_connection(check_db_exists=True)
        if conn:
            cursor = conn.cursor()
            try:
                # Kiểm tra xem đã có bảng employees chưa (để tránh chạy lại file sql nhiều lần)
                cursor.execute("SHOW TABLES LIKE 'employees'")
                result = cursor.fetchone()

                if not result:
                    print(f"[*] Đang nạp cấu trúc bảng từ docs/database.sql ...")
                    with open('docs/database.sql', 'r', encoding='utf-8') as f:
                        sql_script = f.read()

                    # MySQL cần chỉnh lại cú pháp một chút nếu file SQL viết kiểu SQLite
                    # Nhưng logic dưới đây hỗ trợ chạy nhiều lệnh (multi=True)
                    # Lưu ý: File database.sql nên dùng cú pháp chuẩn MySQL
                    for result in cursor.execute(sql_script, multi=True):
                        pass  # Duyệt qua các lệnh để thực thi

                    conn.commit()
                    print("[*] Khởi tạo bảng dữ liệu thành công.")
                else:
                    # DB đã có dữ liệu, không cần nạp lại
                    pass

            except Error as e:
                print(f"[!] Lỗi khởi tạo bảng: {e}")
            except FileNotFoundError:
                print("[!] Không tìm thấy file docs/database.sql")
            finally:
                cursor.close()
                conn.close()

    def execute_query(self, query):
        """Thực thi câu query SELECT và trả về kết quả dạng string"""
        conn = self.get_connection(check_db_exists=True)
        if not conn:
            return "Lỗi kết nối CSDL."

        try:
            cursor = conn.cursor()
            cursor.execute(query)

            # Nếu câu lệnh không trả về dữ liệu (VD: UPDATE, DELETE, INSERT)
            if cursor.description is None:
                conn.commit()
                affected = cursor.rowcount
                return f"Thực thi thành công. Số dòng bị ảnh hưởng: {affected}"

            # Lấy tên cột
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                return "Truy vấn thành công nhưng không tìm thấy dữ liệu nào phù hợp."

            # Format dữ liệu thành bảng text
            return tabulate(rows, headers=columns, tablefmt="grid")

        except Error as e:
            return f"Lỗi SQL từ MySQL Server: {e}"
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()