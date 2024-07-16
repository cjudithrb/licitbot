import pandas as pd
#from dotenv import load_dotenv
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import OpenAI
import streamlit as st

api_key = "sk-None-JcrdY7dThe977ykRW2ZNT3BlbkFJgmx1EQljr6QUcvoqnlnE"
#api_key = "sk-None-JcrdY7dThe977ykRW2ZNT3BlbkFJgmx1EQljr6QUcvoqnlnX"

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

    user_question = st.text_input("Haga su pregunta sobre los datos.. 👇", key="user_question", max_chars=100, help="Escribe tu pregunta aquí")
    
    agent = create_csv_agent(
        OpenAI(api_key=api_key, temperature=0),
        "data.csv",
        verbose=True,
        AgentType=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        allow_dangerous_code=True,
    )

    answer = agent.run(user_question)

    st.write(answer)

if __name__ == "__main__":
    main()
