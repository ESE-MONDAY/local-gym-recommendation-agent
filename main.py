from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever


model = OllamaLLM(model="llama3.2:1b")

template = """
You are an expert in answering questions about gyms

Here are some relevant reviews: {reviews}

Here is the question: {question}
Please provide a detailed but brief answer.

""" 

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("\n\n------------------------")
    user_input = input("Enter your question about the gym (or type 'exit' to quit): ")
    print("------------------------\n\n")
    if user_input.lower() == 'exit':
        break

    # Example reviews for demonstration purposes
    reviews = retriever.invoke(user_input)
    result = chain.invoke({
    "reviews": reviews,
    "question": {user_input}
    })

    print(result)