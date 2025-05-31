import openai

openai.api_key = "YOUR_sk-proj-y_ZfpDXgIcQDRd-TzkEFW0sR86ARbq3Qae225jn3Ujya_Et_8V6DjsWCv0izjJAa1HR6J5w0KYT3BlbkFJntha_I3Db-Zbkszrhom9twkHU4dDS_7NMmHrJyEzq6hEp8Lq9aDp3FH0cYRz8rF8ceeKvWzqoAOPENAI_API_KEY"

def generate_ai_review(code: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Please review the following Python code for readability, maintainability, and potential bugs:\n\n{code}"}
        ]
    )
    return response['choices'][0]['message']['content']
