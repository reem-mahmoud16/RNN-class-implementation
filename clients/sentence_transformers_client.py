from sentence_transformers import SentenceTransformer
import numpy as np
from numpy.linalg import norm
from config.api_config import SENTENCE_TRANSFORMERS_MODEL



class SentenceTransformerClient:
    def __init__(self):
        self.model = SentenceTransformer(SENTENCE_TRANSFORMERS_MODEL)
    
    def get_embedding(self, sentence):
        embedding = self.model.encode(sentence)
        return np.array(embedding)
    
    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (norm(a) * norm(b))