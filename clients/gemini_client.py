import google.generativeai as genai
import numpy as np
from numpy.linalg import norm
from config.api_config import API_KEY, MODEL, GEMINI_EMBEDDING_MODEL

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=API_KEY)
        self.generation_config = {"temperature":0.9, "top_p":1, "top_k":1, "max_output_tokens":2048}
        self.model = genai.GenerativeModel(MODEL, generation_config=self.generation_config)


    def generate_content(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
    
    def get_embedding(self, text):
        result = genai.embed_content(
            model= GEMINI_EMBEDDING_MODEL,
            content= text)
        return np.array(result["embedding"])
    
    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (norm(a) * norm(b))
    