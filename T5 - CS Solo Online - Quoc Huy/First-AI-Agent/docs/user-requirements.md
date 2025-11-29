Help me to build an AI Agent Chat app can connect to My Database to select information I need.

Luồng hoạt động:
1. Người dùng sẽ đặt câu hỏi, thông tin về hệ thống.
2. Nếu câu hỏi có liên quan đến thông tin database (hệ thống quản lý nhân viên trong quán cafe của tôi) thì AI sẽ viết câu lệnh query dữ liệu để nắm bắt thông tin người dùng yêu cầu.
3. Sau khi AI trả về câu query dữ liệu, hệ thống sẽ thực hiện câu query đó để lấy dữ liệu từ database, sau đó gửi dữ liệu đó ngay lập tức cho AI phân tích.
4. Sau khi AI phân tích xong, trả về câu trả lời chi tiết cho người dùng

Thư viện sử dụng
Thư viện của openai, openrouter
code mẫu: 
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="<OPENROUTER_API_KEY>",
)

# First API call with reasoning
response = client.chat.completions.create(
  model="x-ai/grok-4.1-fast:free",
  messages=[
          {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?"
          }
        ],
  extra_body={"reasoning": {"enabled": True}}
)

# Extract the assistant message with reasoning_details
response = response.choices[0].message

# Preserve the assistant message with reasoning_details
messages = [
  {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
  {
    "role": "assistant",
    "content": response.content,
    "reasoning_details": response.reasoning_details  # Pass back unmodified
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# Second API call - model continues reasoning from where it left off
response2 = client.chat.completions.create(
  model="x-ai/grok-4.1-fast:free",
  messages=messages,
  extra_body={"reasoning": {"enabled": True}}
)
=====================================

Hoàn thiện app đầy đủ cho tôi, viết file "requirements.txt" đầy đủ và các key ".env" cần thiết cho dự án một cách chi tiết.

Code logic app nằm trong folder app/

File chạy sẽ là main.py ở ngoài

Ứng dụng sẽ chạy trên command line (terminal)

Cấu trúc dự án:
.venv : Môi trường python của dự án
app/ : Toàn bộ code logic app của tôi
docs/
    database.sql : Cung cấp cho AI cấu trúc database (Tôi sử dụng mysql)
    instructions.md: Instruction cho AI agent
.env : Lưu toàn bộ những key, thông tin bảo mật
main.py : File chạy chính
requirements.txt : Các thư viện sẽ sử dụng trong dự án.
