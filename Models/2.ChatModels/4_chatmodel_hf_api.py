from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    # provider="together"
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is langchain?")

print(result.content)