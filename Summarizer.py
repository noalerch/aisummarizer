import os
import openai

class Summarizer():
    origin_text = ""
    prompt = ""

    def __init__(self):
        pass
    def text_from_file(self, file):
        self.origin_text = open(file, 'r').read()

    def set_text(self, text):
        self.origin_text = text

    # logic for determining prompt
    # TODO: enable custom prompts
    def generate_prompt(self):
        prompt = "summarize:\n" + self.origin_text
        return prompt

    def summarize(self, text=None):
        if text is not None:
            self.set_text(text)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.generate_prompt(),
            temperature=0.3,
            max_tokens=200
        )
        print(response.choices[0].text)
        return response.choices[0].text
