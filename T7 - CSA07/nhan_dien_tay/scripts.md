# Tất cả chạy lệnh này để cài venv
Linux/Mac:
    python3 -m venv .venv
Windows:
    python -m venv .venv

# Kích hoạt môi trường ảo
Linux/Mac:
    source .venv/bin/activate
Windows:
    .venv\Scripts\activate

# Cài thư viện
pip install -r requirements.txt

# Thực thi chương trình
python main.py