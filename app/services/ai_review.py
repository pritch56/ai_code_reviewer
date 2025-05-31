import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_ai_review(code: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Please review the following Python code for readability, maintainability, and potential bugs:\n\n{code}"}
        ]
    )
    return response['choices'][0]['message']['content']
