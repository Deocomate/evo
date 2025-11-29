import os
from openai import OpenAI
from .db import DatabaseHandler


class CoffeeAgent:
    def __init__(self):
        self.client = OpenAI(
            base_url=os.getenv("OPENROUTER_BASE_URL"),
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )
        self.model = os.getenv("MODEL_NAME")
        self.db = DatabaseHandler(os.getenv("DB_PATH"))
        self.messages = []  # Lưu lịch sử hội thoại

    def set_system_prompt(self, prompt_content):
        self.messages.append({"role": "system", "content": prompt_content})

    def chat(self, user_input):
        # 1. Thêm câu hỏi người dùng vào lịch sử
        self.messages.append({"role": "user", "content": user_input})

        # 2. Gọi AI lần 1 để xem có cần query DB không
        print("... AI đang suy nghĩ ...")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            extra_body={"reasoning": {"enabled": True}}
        )

        ai_msg = response.choices[0].message
        content = ai_msg.content.strip()

        # Logic kiểm tra xem AI có trả về SQL không (Dựa trên quy tắc trong instructions)
        if content.startswith("SQL_QUERY:"):
            sql_query = content.replace("SQL_QUERY:", "").strip()
            print(f"\n[AI Query Generator]: {sql_query}")

            # 3. Thực thi query lấy dữ liệu
            db_result = self.db.execute_query(sql_query)
            print(f"[Database Result]:\n{db_result}\n")

            # 4. Gửi kết quả DB lại cho AI
            # Lưu message cũ của AI (chứa SQL)
            self.messages.append({
                "role": "assistant",
                "content": content,
                "reasoning_details": ai_msg.reasoning_details
            })

            # Gửi kết quả dữ liệu dưới dạng system/tool message
            self.messages.append({
                "role": "user",
                "content": f"Kết quả từ database:\n{db_result}\n\nHãy trả lời câu hỏi gốc của tôi dựa trên dữ liệu này."
            })

            # 5. Gọi AI lần 2 để phân tích dữ liệu và trả lời
            print("... AI đang phân tích dữ liệu ...")
            final_response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                extra_body={"reasoning": {"enabled": True}}
            )

            final_content = final_response.choices[0].message.content
            # Lưu câu trả lời cuối vào lịch sử
            self.messages.append({
                "role": "assistant",
                "content": final_content,
                "reasoning_details": final_response.choices[0].message.reasoning_details
            })

            return final_content

        else:
            # Nếu không phải SQL (câu hỏi thường), trả về luôn
            self.messages.append({
                "role": "assistant",
                "content": content,
                "reasoning_details": ai_msg.reasoning_details
            })
            return content