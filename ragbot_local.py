#from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain.document_loaders.directory import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import Chroma
from langchain_ollama import OllamaLLM
from langchain.chains import ConversationalRetrievalChain

def print_hello():
    print('Hello from ragbot local')


def load_dir(path: str):
    documents = DirectoryLoader(path=path).load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = text_splitter.split_documents(documents)
    embeddings = HuggingFaceBgeEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory="chromadb"
    )
    vectordb.persist()
    return split_docs

 
def init_chat():
    global conversation

    embeddings = HuggingFaceBgeEmbeddings(model_name='all-MiniLM-L6-v2')
    vectordb = Chroma(persist_directory='chromadb', embedding_function=embeddings)

    llm = OllamaLLM(
        model="jobautomation/OpenEuroLLM-Slovak:latest",
        base_url="http://localhost:11434",
        verbose=True
    )

    conversation = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True,
        verbose=True
    )

def llm_answer(question:str, user_id):
    global conversation

    chat_history = []

    response = conversation({"question": question, "chat_history": chat_history})
    answer = response["answer"]

    print(f"RAG llm response is {answer}")

    return answer


