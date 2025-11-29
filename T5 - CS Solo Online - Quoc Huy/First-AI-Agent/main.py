import os
import sys
from dotenv import load_dotenv
from app.agent import CoffeeAgent
from app.utils import load_instructions

# Load biến môi trường
load_dotenv()

def main():
    # Kiểm tra key
    if not os.getenv("OPENROUTER_API_KEY"):
        print("Lỗi: Chưa cấu hình OPENROUTER_API_KEY trong file .env")
        return

    # Khởi tạo Agent
    agent = CoffeeAgent()

    # Load hướng dẫn và schema
    system_instruction = load_instructions()
    agent.set_system_prompt(system_instruction)

    print("==================================================")
    print("AI ASSISTANT - QUẢN LÝ QUÁN CAFE")
    print("Sử dụng model:", os.getenv("MODEL_NAME"))
    print("Gõ 'exit' hoặc 'quit' để thoát.")
    print("==================================================\n")

    while True:
        try:
            user_input = input("\nBạn: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Tạm biệt!")
                break

            if not user_input.strip():
                continue

            response = agent.chat(user_input)
            print(f"\nAI: {response}")

        except KeyboardInterrupt:
            print("\nĐã dừng chương trình.")
            break
        except Exception as e:
            print(f"\nĐã xảy ra lỗi: {e}")


if __name__ == "__main__":
    main()