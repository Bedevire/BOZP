import streamlit as st

from llama_index.core.base.llms.types import ChatMessage
from ragbot import Ragbot

st.set_page_config(page_title="Intro to RAG Chatbots", page_icon=":robot_face:")

st.title("RAGbot: Talk to Your Data")
st.caption("Powered by LlamaIndex & Streamlit & ExxetaAI")


@st.cache_resource(show_spinner=False)
def init():
    with st.spinner(text="Loading documents..."):
        pass

        # -------------------------
        # Init RAGbot here
        ragbot = Ragbot()
        ragbot.ingest(['docs/Sora.pdf'])
        return ragbot
        #
        # -------------------------


bot = init()


def add_msg_to_ui_conversation(role: str, content: str) -> None:
    st.session_state.messages.append(ChatMessage(role=role, content=str(content)))


# Initialize the chat message history
if "messages" not in st.session_state.keys():
    initial_msg = ChatMessage(
        role="assistant",
        content="Hi, ask something about your data!",
    )
    st.session_state.messages = [initial_msg]
    st.session_state.history = []

if question := st.chat_input(
    "Your question"
):  # Prompt for user input and save to chat history
    add_msg_to_ui_conversation(role="user", content=question)

# Display the prior chat messages
for message in st.session_state.messages:
    with st.chat_message(message.role):
        st.write(message.content)

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1].role != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("I'm generating answer..."):
            placeholder = st.empty()

            response = bot.chat(question, st.session_state.history) 

            placeholder.markdown(response)
            print(response)
            add_msg_to_ui_conversation(role="assistant", content=response)