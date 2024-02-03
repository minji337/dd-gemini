import google.generativeai as genai

generation_config = genai.GenerationConfig(max_output_tokens=10)
model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)
user_message = "인공지능에 대해 한 문장으로 설명하세요."
response = model.generate_content(user_message)
print(response._result)
#print(f'사용자 메시지 토큰 수: {model.count_tokens(user_message)}')
#print(f'모델 응답 메시지 토큰 수: {model.count_tokens(response.text)}')


