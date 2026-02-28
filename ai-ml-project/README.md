\# AI Semantic Search using Endee Vector Database



\## Project Overview



This project is an AI-powered semantic search system built using vector embeddings on top of the Endee vector database repository.



Instead of traditional keyword matching, the system understands the meaning of the query and returns the most relevant results using vector similarity. The project demonstrates how vector search can be used in real-world AI applications such as knowledge search and recommendation systems.



Users can search information either through the terminal or a simple web interface.



---



\## Features



\- AI-based semantic search

\- Vector similarity matching

\- Top-K most relevant results

\- Search from a knowledge file (data.txt)

\- Interactive web interface using Streamlit

\- Command-line interface support

\- Built on the Endee repository



---



\## Technologies Used



\- Python

\- Endee Vector Database (base repository)

\- Sentence Transformers

\- NumPy

\- Streamlit



---



\## Project Structure





endee/

└── ai-ml-project/

app.py # Terminal-based search

ui.py # Streamlit web interface

data.txt # Knowledge dataset

requirements.txt

README.md





---



\## How It Works



1\. Text data from `data.txt` is converted into vector embeddings.

2\. The user enters a search query.

3\. The query is converted into an embedding.

4\. Vector similarity is calculated.

5\. The most relevant results are displayed.



This approach allows semantic understanding instead of simple keyword matching.



---



\## Installation and Setup



Clone the repository:





git clone https://github.com/Akshit172005/endee.git





Install dependencies:





pip install -r ai-ml-project/requirements.txt





---



\## Running the Project



\### Terminal Version





cd ai-ml-project

python app.py





\### Web Interface





cd ai-ml-project

python -m streamlit run ui.py





The web interface will open in your browser.



---



\## Example Search



\*\*Query\*\*





neural network





\*\*Results\*\*



\- Neural networks learn patterns from data  

\- Deep learning uses neural networks  

\- Machine learning is a field of artificial intelligence  



---



\## Use Cases



This system can be used for:



\- Knowledge search systems

\- Document retrieval

\- Resume matching

\- Recommendation engines

\- AI chat systems (RAG-style retrieval)



---



\## Author



Akshit Gupta

