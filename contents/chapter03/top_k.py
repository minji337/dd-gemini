import google.generativeai as genai

# generation_config = genai.GenerationConfig(top_p=0, top_k=40)
# for _ in range(3):
#     model = genai.GenerativeModel('gemini-pro')
#     user_message = "사랑에 관한 시를 30자로 이내로 지으세요."
#     response = model.generate_content(user_message, generation_config=generation_config)
#     print(f'{"="*50}{'\n'}{response.text}')
    

generation_config = genai.GenerationConfig(top_k=0)

model = genai.GenerativeModel('gemini-pro')
user_message = "사랑에 관한 시를 30자로 이내로 지으세요."
response = model.generate_content(user_message, generation_config=generation_config)
print(f'{"="*50}{'\n'}{response.text}')

