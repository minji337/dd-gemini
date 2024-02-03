import google.generativeai as genai 

model = genai.GenerativeModel('gemini-pro')
chat_session = model.start_chat(history=[
    {'role':'user', 'parts': ["당신은 예술가입니다. 예술가의 언어로 두 문장 이내로 답하세요."]},
    {'role':'model', 'parts': ["네, 그렇게 하겠습니다."]}
]) 
response = chat_session.send_message("인공지능에 뭐예요?")
print(f'[모델]: {response.text}') 
