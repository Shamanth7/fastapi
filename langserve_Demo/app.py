from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langserve import add_routes
import uvicorn

llm = ChatOllama(model="llama3.2")

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

add_routes(
    app,
    llm,
    path="/ollama"
)

prompt = ChatPromptTemplate.from_template("provide me an essay about {topic}")
prompt1 = ChatPromptTemplate.from_template("provide me a poem about {topic}")

add_routes(
    app,
    prompt | llm,
    path="/essay"
)

add_routes(
    app,
    prompt1 | llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)