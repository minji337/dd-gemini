import google.generativeai as genai
import PIL.Image

image_data = PIL.Image.open("./images/monalisa.jpg")
model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(["이 그림에 대해 한 문장으로 설명하세요.", image_data])
print(response.text)
print(response._result) #response: GenerateContentResponse 

print(f"건수: {len(response.candidates)}")
print("="*50)
for candidate in response.candidates:
    print(candidate)
print("="*50)
print(f"finish_reason: {response.candidates[0].finish_reason.name}, {response.candidates[0].finish_reason}")

