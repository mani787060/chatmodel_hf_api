# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)

# result = model.invoke("What is the capital of Australia?")

# print(result.content)


#  ===> through this method "hugging_face_api-key" we are talking with a model through an API 


import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Use a model that is definitely supported by the Hugging Face API
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", 
    task="text-generation",
    # Set a timeout so it doesn't wait forever if the server is busy
    timeout=30 
)

model = ChatHuggingFace(llm = llm)

try:
    result = model.invoke("What is the capital of Iran?")
    print(f"AI Response: {result.content}")
except Exception as e:
    print(f"Error occurred: {e}")


