from sentence_transformers import SentenceTransformer
import numpy as np

print("Endee Vector Search Project Running")

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example documents
documents = [
    "Machine learning is a part of artificial intelligence",
    "Vector databases store embeddings efficiently",
    "Semantic search understands context",
    "Endee is a high-performance vector database",
    "Artificial intelligence improves automation"
]

# Generate embeddings
embeddings = model.encode(documents)

# User query
query = input("Enter your query: ")

# Convert query to vector
query_vector = model.encode([query])[0]

# Similarity calculation
scores = np.dot(embeddings, query_vector)

best_match = np.argmax(scores)

print("Best Result:")
print(documents[best_match])