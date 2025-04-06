import openai
from dotenv import load_dotenv

load_dotenv()

# Replace this with your fine-tuned model name
model_name = 'your-fine-tuned-model-name-here'

template = '''You are a movie Q&A bot. Answer questions about movies in a clear and brief way.
For example:
Question: Who directed the movie Inception? Christopher Nolan.
Provide the answer to the following question:
Question: '''

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    message = [{'role': 'user', 'content': template + prompt}]

    response = openai.chat.completions.create(
        model=model_name,
        temperature=0,
        stop=['\n'],
        messages=message
    )

    print("assistant: " + response.choices[0].message.content)
