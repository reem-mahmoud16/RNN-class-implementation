import google.generativeai as genai

from config.api_config import API_KEY, MODEL, system_prompt3

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=API_KEY)
        self.generation_config = {"temperature":0.9, "top_p":1, "top_k":1, "max_output_tokens":2048}
        self.model = genai.GenerativeModel(MODEL, generation_config=self.generation_config)
        self.system_prompt = system_prompt3

    def generate_content(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text