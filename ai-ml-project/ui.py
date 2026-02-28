import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np

st.title("AI Semantic Search using Endee Vector Database")

st.write("Search knowledge using AI vector search")

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load file
with open("data.txt","r") as file:
    documents = file.readlines()

documents = [d.strip() for d in documents]

embeddings = model.encode(documents)

query = st.text_input("Enter your query")

if query:

    query_vector = model.encode([query])[0]

    scores = np.dot(embeddings, query_vector)

    top_k = np.argsort(scores)[-5:][::-1]

    st.write("Top Results:")

    for i,index in enumerate(top_k):
        st.write(str(i+1)+". "+documents[index])