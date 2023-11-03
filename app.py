import openai
import gradio

openai.api_key = '###'
messages = [{ "role" : "system", "content" : "You are an assistant creating CV summary and writing cover letters to the expectations contained in the job offer. You want your customized CV summary to highlight the candidate's skills required for a given position. You want the candidate to seem like the perfect candidate for the job. You will receive a job offer and a CV, return CV summary and cover letter. Returned CV summary should be specific and consist of 2 sentences. Respond in a pattern: CV SUMMARY: '''generated cv summary'' COVER LETTER: '''generated cover letter'''."}]

def recruitmentAssistant(cv, job_offer):
    message = f"Create CV summary and generate cover letter. Job offer: {job_offer} CV: {cv}" 
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=recruitmentAssistant, theme='freddyaboulton/test-blue@=0.0.1', inputs = ["text", "text"], outputs = ["text"], title = "recruitment assistant")
demo.launch(share=True)
