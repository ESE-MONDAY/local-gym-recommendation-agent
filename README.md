
# 🏋️ Gym Recommendation AI Agent

This project is a **local AI-powered agent** that recommends gyms based on user queries. It uses **LangChain**, **Ollama Embeddings**, and **Chroma Vector DB** to process, embed, and retrieve gym data from a CSV file. Perfect for creating a chatbot, search assistant, or localized fitness recommender.

---

## 📦 Features

- Semantic search over 200–500 gym listings
- Local inference using `Ollama` (e.g., `mxbai-embed-large`)
- Vector database with `Chroma`
- Fast natural-language queries (e.g., "Affordable gyms with yoga in Lagos")
- Metadata filtering (e.g., by price, location, amenities)

---

## 🧠 Tech Stack

| Tool            | Purpose                         |
|-----------------|----------------------------------|
| `LangChain`     | Orchestration of agents, tools  |
| `Ollama`        | Local embedding + inference      |
| `Chroma`        | Vector store & document retrieval |
| `Pandas`        | CSV parsing                     |

---

## 🗂️ Folder Structure

```

.
├── gym\_recommendations.csv      # Your structured gym data
├── main.py                      # Example query runner
├── vector.py                    # Embedding & vector store setup
├── README.md                    # This file

````

---

## 🧪 Sample Gym Data Format

Your CSV file should include the following headers:

```csv
gym_name,location,membership_cost,amenities,website
Fitness First,Ikoyi,20000,"Pool,Yoga,Sauna",https://fitnessfirst.ng
FitHub,Abuja,15000,"CrossFit,Boxing",https://fithub.com
````

---

## 🚀 Setup Instructions

### 1. Install Requirements

```bash
pip install langchain langchain-ollama langchain-chroma pandas

```

or 

```bash
pip install -r requirements.txt
```
to install from the requirements file

Ensure that **Ollama** is running locally and has the embedding model:

```bash
ollama run mxbai-embed-large
```

### 2. Run Vector Store Setup

```bash
python vector.py
```

This script:

* Reads the CSV
* Embeds each gym entry
* Stores vectors in Chroma DB

### 3. Query Your Agent

```bash
python main.py
```

In `main.py`, you can write queries like:

```python
query = "Affordable gyms with swimming pool in Lagos"
results = retriever.get_relevant_documents(query)
```

---

## 🤖 Example Query Output

```
🏋️ FitZone Lekki 15000
ℹ️ {'amenities': 'Yoga, Swimming Pool', 'contact_info': 'http://fitzone.com'}
--------
```

---

## 📌 Notes

* All processing is local and privacy-respecting.
* You can modify the retriever to add custom filters (e.g., city, amenities).
* The embedding model must support sentence-level embeddings (like `mxbai-embed-large`).

---

## 💡 Ideas for Expansion

* Add a Streamlit or Flask UI
* Integrate filters (price, city, features)
* Use LangChain agents for multi-turn Q\&A
* Extend to hotels, clinics, or schools

---

## 🧑‍💻 Author

Built with ❤️ by [Ese Monday](https://x.com/EseMonday1)




