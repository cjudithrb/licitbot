import pandas as pd
#from dotenv import load_dotenv
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_groq import ChatGroq
import streamlit as st

api_key = "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"

def main():
    df = pd.read_csv("data.csv")

    st.set_page_config(
        page_title="Documentacion ChatBot",
        page_icon=":books:",
    )
    
 # Divide la fila en dos columnas
    col1, col2 = st.columns([2, 1])

    # Primera columna: Subheader
    with col1:
        st.title("LicitBot - ChatBot de análisis")
        st.subheader("Descubrir ideas a partir de los datos!")

    # Segunda columna: Logo
    with col2:
        st.image("logo_solo_sf.png", width=200)
    
    st.markdown(
        """
        Este ChatBot fue creado para responder preguntas a partir de Olas de Licitaciones. 
        Haga una pregunta y el chatbot responderá con el análisis apropiado.
        """
    )

    st.write(df.head(3))

    query = st.text_input("Haga su pregunta sobre los datos.. 👇", key="user_question", max_chars=100, help="Escribe tu pregunta aquí")
    
    llm = ChatGroq(temperature=0, model="llama3-70b-8192", api_key=api_key)
    
    agent = create_csv_agent(
        llm,
        "data.csv",
        verbose=True,
        allow_dangerous_code=True
    )

    def query_data(query):
        response = agent.invoke(query)
        return response
    
    if query:
        try:
            #query = "[ {"role": "user", "content":" user_question}] 
            response = query_data(query)
            st.write(response)
        except Exception as e:
            st.error(f"Error al procesar la pregunta: {e}")

if __name__ == "__main__":
    main()
