import google.generativeai as genai
from google.ai.generativelanguage_v1beta import Candidate

def get_invalid_stop_reason(response: genai.types.GenerateContentResponse):
    if response.prompt_feedback.block_reason:
        return f"[사용자 입력: {response.prompt_feedback.block_reason.name}]"
    for candidate in response.candidates:
        if candidate.finish_reason != Candidate.FinishReason.STOP:
            return f"[모델 응답: {response.candidates[0].finish_reason.name}]"
    return None     

if __name__  == "__main__":
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("당신은 뛰어난 연극 배우입니다. 격하게 화난 대사를 읊어보세요")
        #response = model.generate_content("나는 네가 싫어!")
        stop_reason = get_invalid_stop_reason(response)
        if stop_reason:
            print(f"다음의 문제가 발생하여 응답이 중단되었습니다: {stop_reason}")
        else:
            print(response.text)
    except Exception as e:
        print(f"콘텐츠 생성 중 에러가 발생했습니다: {e}")
