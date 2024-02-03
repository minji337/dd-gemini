import google.generativeai as genai

generation_config = genai.GenerationConfig(candidate_count=2)
model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)
response = model.generate_content("인공지능에 대해 한 문장으로 설명하세요.")
print(response.text)
print(f"canidate 생성 건수: {len(response.candidates)}")