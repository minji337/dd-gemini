import vertexai.preview.generative_models as models
import vertexai

vertexai.init(project="cogent-weaver-412406", location="asia-northeast3")
model = models.GenerativeModel(model_name='gemini-pro')
generation_config = models.GenerationConfig(max_output_tokens=10)
model = models.GenerativeModel('gemini-pro', generation_config=generation_config)
user_message = "인공지능에 대해 한 문장으로 설명하세요."
response = model.generate_content(user_message)
print(f'토큰 수: {model.count_tokens(response.text).total_tokens}')
print(response._raw_response)


