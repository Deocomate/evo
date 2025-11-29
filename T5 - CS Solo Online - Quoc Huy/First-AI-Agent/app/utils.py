import os

def load_instructions(schema_path='docs/database.sql', instructions_path='docs/instructions.md'):
    """Đọc schema và ghép vào file instruction"""
    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema = f.read()

        with open(instructions_path, 'r', encoding='utf-8') as f:
            instructions = f.read()

        # Thay thế placeholder {SCHEMA} trong instruction
        return instructions.replace("{SCHEMA}", schema)
    except Exception as e:
        return f"Lỗi đọc file hướng dẫn: {e}"