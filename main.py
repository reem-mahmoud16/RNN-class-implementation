from clients.sentence_transformers_client import SentenceTransformerClient

def main():
    client = SentenceTransformerClient()
    sent1 = input("Enter first sentence: ")
    sent2 = input("Enter first sentence: ")
 
    embedding_vec_1 = client.get_embedding(sent1)
    embedding_vec_2 = client.get_embedding(sent2)

    similarity_measure = client.cosine_similarity(embedding_vec_1, embedding_vec_2)
    print(similarity_measure)


if __name__ == "__main__":
    main()