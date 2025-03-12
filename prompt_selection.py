import openai
import json
import os

# Load the JSON files for doctor, engineer, and selection templates
with open('doctor_chat.json', 'r') as doctor_file:
    doctor_template = json.load(doctor_file)

with open('engineer_chat.json', 'r') as engineer_file:
    engineer_template = json.load(engineer_file)

with open('selection_chat.json', 'r') as selection_file:
    selection_template = json.load(selection_file)

# Set your OpenAI API key securely from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")  # API Key should be set as an environment variable

# Function to call the model and get a response based on the selected template
def chat_with_model(template):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the OpenAI engine you want to use
        prompt=template["content"],
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example conversation for selection
conversation = "I have a technical problem related to engineering. Can you help me?"
print("Selected Template: Engineer")

# Depending on the conversation, select the appropriate template
if "engineering" in conversation:
    response = chat_with_model(engineer_template)
else:
    response = chat_with_model(doctor_template)

print("Model Response:", response)
