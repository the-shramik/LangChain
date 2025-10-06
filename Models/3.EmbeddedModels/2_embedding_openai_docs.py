from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

documents = [
    "MS Dhoni is most successfull captain of India",
    "MS Dhoni is fromn Ranchi",
    "MS Dhoni play for CSK & he won 5 IPL trophies",
    "MS Dhoni made CSK franchise more successfull in IPL",
    "MS Dhoni won all ICC trophies"
]

result = embedding.embed_documents(documents)

print(str(result))