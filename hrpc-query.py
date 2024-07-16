from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
import openai

import streamlit as st

def query(question,chat_history):
    openai_api_key = "sk-None-76c8SHmPFGOTFHd3wQ2wT3BlbkFJLqMDqmdPdX7ODg7N"
    embeddings= OpenAIEmbeddings(api_key=openai_api_key)
    new_db= FAISS.load_local("faiss_index",embeddings,allow_dangerous_deserialization=True)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0)
    try:
        query = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=new_db.as_retriever(),
            return_source_documents=True
        )

        return query({"question": question, "chat_history":chat_history})
    except openai.RateLimitError:
            print("Rate limit exceeded. Retrying...")
    return {"answer": "Error: Rate limit exceeded after multiple attempts."}
    
def show_ui():

    st.image("logo_pc.png")
    st.subheader("Por favor ingrese su consulta ")

    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.chat_history = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Ingrese su Consulta: "):
        with st.spinner("Trabajando en su consulta...."):
            response = query(question=prompt,chat_history=st.session_state.chat_history)
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant"):
                st.markdown(response["answer"])
            
            st.session_state.messages.append({"role":"user","content": prompt})
            st.session_state.messages.append({"role":"assistant","content":response["answer"]})
            st.session_state.chat_history.extend([(prompt, response["answer"])])
        
if __name__ == "__main__":
    show_ui()

                
                