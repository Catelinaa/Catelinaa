import openai
import json

# Load your OpenAI API key (replace with your actual API key)
openai.api_key = "<API_KEY>" 

# Load the first template
with open("first_template.json", "r") as file:
    first_template = json.load(file)["prompt"]

# Fill placeholders
first_prompt = first_template.format(order="large coffee with oat milk")

# Print to debug
print("First Prompt:", first_prompt)

# Send first request
response1 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": first_prompt}],
    max_tokens=100
)

# Print response
print("First Response:", response1["choices"][0]["message"]["content"].strip())


# Load second template
with open("second_template.json", "r") as file:
    second_template = json.load(file)["prompt"]

# Fill placeholders using first response
second_prompt = second_template.format(details=response1["choices"][0]["message"]["content"].strip())

# Print to debug
print("Second Prompt:", second_prompt)

# Send second request
response2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": second_prompt}],
    max_tokens=100
)

# Print response
print("Final Response:", response2["choices"][0]["message"]["content"].strip())

