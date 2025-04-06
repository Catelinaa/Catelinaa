import json

class ChatTemplate:
    def __init__(self, prompt_template, temperature=0):
        """
        Initialize the ChatTemplate with a given prompt template and temperature.
        :param prompt_template: A list of message dictionaries.
        :param temperature: The randomness of the response (default is 0 for deterministic answers).
        """
        # If the prompt_template is a list of message dictionaries, join the "content" values
        if isinstance(prompt_template, list):
            self.prompt_template = " ".join([message["content"] for message in prompt_template if "content" in message])
        else:
            self.prompt_template = prompt_template
        self.temperature = temperature

    @classmethod
    def from_file(cls, file_path):
        """
        Load the template from a JSONL file.
        :param file_path: Path to the JSONL file containing the template.
        :return: A ChatTemplate instance.
        """
        with open(file_path, 'r') as f:
            data = json.load(f)
        return cls(data["messages"], temperature=data.get("temperature", 0))

    def completion(self, context):
        """
        Generates a response based on the context (such as 'info' and 'n').
        :param context: A dictionary containing the input data for the prompt.
        :return: The generated response as a string.
        """
        prompt = self.prompt_template.format(**context)
        # Here, you would normally interact with the OpenAI API to generate a completion.
        # For now, we'll simulate a response:
        response = {
            'choices': [
                {
                    'message': {
                        'content': f"Generated response based on prompt: {prompt}"
                    }
                }
            ]
        }
        return response
