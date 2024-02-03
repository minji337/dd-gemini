import google.generativeai as genai
model = genai.GenerativeModel('gemini-pro')
user_message = "겨울에 대한 짧은 시를 20자 이내로 지으세요."

print("\ntop_p=0:")
generation_config = genai.GenerationConfig(top_p=0)
for _ in range(3):
    response = model.generate_content(user_message , generation_config=generation_config)
    print(f'{"="*50}{'\n'}{response.text}')

print("\ntop_p=1:")
generation_config = genai.GenerationConfig(top_p=1)
for _ in range(3):
    response = model.generate_content(user_message , generation_config=generation_config)
    print(f'{"="*50}{'\n'}{response.text}')
