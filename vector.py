from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os
from langchain_core.documents import Document
import pandas as pd


df = pd.read_csv("gym_recommendations.csv")

embeddings = OllamaEmbeddings(model="mxbai-embed-large")
db_location = "./chroma_langchain_db"
add_location = not os.path.exists(db_location)

if add_location: 
    documents = []
    ids = []


    for i, row in df.iterrows():
        document = Document(
            page_content=row["gym_name"] + row["location"] + row["membership_cost"] ,
            metadata={"membership_cost": row["membership_cost"],"amenities": row["amenities"],"websitesexit": row["website"]},
            id = str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="gym_recommendations",
    embedding_function=embeddings,
    persist_directory=db_location,
)

if add_location:
    vector_store.add_documents(documents=documents, ids=ids)


retriever = vector_store.as_retriever(
    search_kwargs={"k": 10},
    return_source_documents=True
)