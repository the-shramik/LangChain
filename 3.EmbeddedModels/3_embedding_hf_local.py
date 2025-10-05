from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

documents = [
    "MS Dhoni is most successfull captain of India",
    "MS Dhoni is fromn Ranchi",
    "MS Dhoni play for CSK & he won 5 IPL trophies",
    "MS Dhoni made CSK franchise more successfull in IPL",
    "MS Dhoni won all ICC trophies"
]

vector = embedding.embed_documents(documents)

print(str(vector))