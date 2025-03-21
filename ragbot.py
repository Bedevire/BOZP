from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjBkY2M5YzIwYjI5Y2UzNjY0NzY2ZjhhNDEwNDRmM2JlIn0.mIIt1JQSSquMS5Quae00cn4-xP_mQCWVe1olx8jkIUY"
BASE_URL = "https://ai.exxeta.com/api/v2/azure"
LLM_API_VERSION = "2023-07-01-preview"
LLM_MODEL_NAME = "gpt-35-turbo"
LLM_DEPLOYMENT_NAME = "gpt-35-turbo"

EMBED_API_VERSION = "2023-05-15"
EMBED_MODEL_NAME = "text-embedding-ada-002"
EMBED_DEPLOYMENT_NAME = "text-embedding-ada-002"


question = "What is Sora?"

exxeta_ai_llm = AzureOpenAI(
    model = LLM_MODEL_NAME,
    deployment=LLM_DEPLOYMENT_NAME,
    api_key=API_KEY,
    azure_endpoint=BASE_URL,
    api_version=LLM_API_VERSION
)

#answer = exxeta_ai_llm.complete(question)

docs = SimpleDirectoryReader(input_files=['docs/Sora.pdf']).load_data()
print(f'Nr. of docs: {len(docs)}')

exxeta_embedding = AzureOpenAIEmbedding(
    model=EMBED_MODEL_NAME,
    deployment_name=EMBED_DEPLOYMENT_NAME,
    api_key=API_KEY,
    azure_endpoint=BASE_URL,
    api_version=EMBED_API_VERSION
)

index = VectorStoreIndex.from_documents(documents=docs, embed_model=exxeta_embedding)

query_engine = index.as_query_engine(llm=exxeta_ai_llm)
answer = query_engine.query(question)
print(f'{question} : {answer.response}')