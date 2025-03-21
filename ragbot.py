from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjBkY2M5YzIwYjI5Y2UzNjY0NzY2ZjhhNDEwNDRmM2JlIn0.mIIt1JQSSquMS5Quae00cn4-xP_mQCWVe1olx8jkIUY"

class Ragbot:

    BASE_URL = "https://ai.exxeta.com/api/v2/azure"
    LLM_API_VERSION = "2023-07-01-preview"
    LLM_MODEL_NAME = "gpt-35-turbo"
    LLM_DEPLOYMENT_NAME = "gpt-35-turbo"

    EMBED_API_VERSION = "2023-05-15"
    EMBED_MODEL_NAME = "text-embedding-ada-002"
    EMBED_DEPLOYMENT_NAME = "text-embedding-ada-002"

    question = "What is Sora?"

    def __init__(self) -> None:


        self.exxeta_ai_llm = AzureOpenAI(
            model=self.LLM_MODEL_NAME,
            deployment=self.LLM_DEPLOYMENT_NAME,
            api_key=API_KEY,
            azure_endpoint=self.BASE_URL,
            api_version=self.LLM_API_VERSION
        )

        self.exxeta_embedding = AzureOpenAIEmbedding(
            model=self.EMBED_MODEL_NAME,
            deployment_name=self.EMBED_DEPLOYMENT_NAME,
            api_key=API_KEY,
            azure_endpoint=self.BASE_URL,
            api_version=self.EMBED_API_VERSION
        )

    def ingest(self, input_files: dict):
        docs = SimpleDirectoryReader(input_files=input_files).load_data()
        print(f'Ragbot > Ingest: nr. of docs: {len(docs)}')
        index = VectorStoreIndex.from_documents(documents=docs, embed_model=self.exxeta_embedding)
        self.query_engine = index.as_query_engine(llm=self.exxeta_ai_llm)

    def answer_question(self, question: str):
        answer = self.query_engine.query(question)
        print(f'{question} : {answer.response}')
    

ragbot = Ragbot()
ragbot.ingest(['docs/Sora.pdf'])
ragbot.answer_question('What is Sora?')



