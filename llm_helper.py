from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model="llama-3.1-70b-versatile")


if __name__ == "__main__":
    response = llm.invoke("What are ML and DL?")
    print(response.content)
