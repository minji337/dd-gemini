import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("인공지능에 대해 한 문장으로 설명하세요.")
print(response.text)
print(response.candidates[0].content)