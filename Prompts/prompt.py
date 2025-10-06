from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

app = FastAPI()
model = ChatOpenAI()

template = load_prompt('template.json')

@app.get("/summarize")
def greet(paper: str, style: str, length: str):
    
    chain = template | model
    result = chain.invoke({'paper':paper,
                  'style':style,
                  'length':length
    })
 
    return result.content
  