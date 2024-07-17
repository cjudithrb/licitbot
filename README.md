

# Documentación del Proyecto ChatBot para Análisis de Datos CSV

## 1. Descripción del Proyecto

Este proyecto consiste en un ChatBot desarrollado con Python que permite realizar análisis de datos a partir de un archivo CSV. Utiliza la biblioteca `langchain` para la creación del agente y `Streamlit` para la interfaz web. El objetivo es permitir a los usuarios hacer preguntas sobre los datos y obtener respuestas basadas en el análisis del archivo CSV.

## 2. Estructura del Código

### Importaciones

```python
import pandas as pd  # Importa la biblioteca pandas para manipulación de datos
#from dotenv import load_dotenv  # Esta línea está comentada; se utilizaría para cargar variables de entorno
from langchain.agents.agent_types import AgentType  # Importa el tipo de agente de langchain
from langchain_experimental.agents.agent_toolkits import create_csv_agent  # Importa la función para crear un agente CSV
from langchain_openai import OpenAI  # Importa la clase OpenAI de langchain
import streamlit as st  # Importa la biblioteca streamlit para crear la interfaz web
```

```python
def main():
    # Lee el archivo CSV en un DataFrame de pandas
    df = pd.read_csv("data.csv")

    # Configuración de la página de Streamlit
    st.set_page_config(
        page_title="Documentacion ChatBot",  # Título de la página
        page_icon=":books:",  # Icono de la página
    )

    # Divide la fila en dos columnas
    col1, col2 = st.columns([2, 1])

    # Primera columna: Logo
    with col1:
        st.image("logo_pc.png")  # Muestra una imagen en la primera columna

    # Segunda columna: Logo
    with col2:
        st.image("logo_solo_sf.png", width=200)  # Muestra otra imagen en la segunda columna con un ancho de 200

    # Texto descriptivo del ChatBot
    st.markdown(
        """
        Este ChatBot fue creado para responder preguntas a partir de Olas de Licitaciones. 
        Haga una pregunta y el chatbot responderá con el análisis apropiado.
        """
    )

    # Muestra las primeras 3 filas del DataFrame
    st.write(df.head(3))

    # Entrada de texto para la pregunta del usuario
    user_question = st.text_input("Haga su pregunta sobre los datos.. 👇", key="user_question", max_chars=100, help="Escribe tu pregunta aquí")
    
    # Crea un agente CSV usando la API de OpenAI
    agent = create_csv_agent(
        OpenAI(api_key=api_key, temperature=0),  # Configuración del agente OpenAI con clave API y temperatura
        "data.csv",  # El archivo CSV a usar
        verbose=True,  # Modo detallado
        AgentType=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Tipo de agente
        allow_dangerous_code=True,  # Permitir código peligroso (usar con precaución)
    )

    # Ejecuta el agente con la pregunta del usuario y obtiene la respuesta
    answer = agent.run(user_question)

    # Muestra la respuesta en la interfaz
    st.write(answer)

# Ejecuta la función principal si este archivo es el principal
if __name__ == "__main__":
    main()
```
## 3. Explicación del Código
- Importaciones: Se importan las bibliotecas necesarias para la manipulación de datos (pandas), la creación del agente (langchain y langchain_openai), y la construcción de la interfaz web (streamlit).

- Función main():

Se lee el archivo data.csv en un DataFrame de pandas.
Se configura la página de Streamlit con un título y un icono.
Se divide la interfaz en dos columnas y se muestran imágenes en cada una.
Se muestra una descripción del ChatBot.
Se muestran las primeras tres filas del DataFrame.
Se crea una entrada de texto para que el usuario haga preguntas sobre los datos.
Se crea un agente CSV utilizando la API de OpenAI, configurado para responder preguntas basadas en el archivo CSV.
Se ejecuta el agente con la pregunta del usuario y se muestra la respuesta en la interfaz.
Ejecución de la Función Principal: La función main() se ejecuta si el archivo es el principal.


### 1.-Instalar Dependencias necesarias
```pip install pandas streamlit langchain_openai```

###2.-Ejecuta el archivo
streamlit run nombre_del_archivo.py

###3.- Abre el navegador y navega a la dirección que se muestra en la terminal para interactuar con el ChatBot.



Descripción del Dataset
El dataset utilizado en este proyecto contiene información detallada sobre procesos de licitación y contratación. A continuación se describe el contenido del dataset:

Columnas del Dataset
Entidad: Nombre de la entidad responsable de la licitación.
Fecha y Hora de Publicacion: Fecha y hora en que se publicó la licitación.
Nomenclatura: Código único que identifica la licitación.
Objeto de Contratacion: Tipo de contrato (e.g., obra, servicio).
Descripcion del Objeto: Descripción detallada del objeto de la contratación.
Valor Referencial: Valor estimado del contrato.
Moneda: Moneda en la que se expresa el valor referencial.
Fecha Fin Formulación de consultas y observaciones (Electrónica): Fecha límite para la presentación de consultas y observaciones de manera electrónica.
Absolución de consultas y observaciones (Electrónica): Fecha en la que se absolverán las consultas y observaciones presentadas electrónicamente.
Integración de las Bases: Fecha en la que se integrarán las bases de la licitación.
Fecha Presentacion de Propuesta: Fecha en la que se deben presentar las propuestas.
Fecha de Buena Pro: Fecha en la que se otorgará la buena pro.
Estado: Estado actual de la licitación (e.g., convocado, adjudicado).
Fideicomiso: Indica si la licitación está bajo fideicomiso (Sí o No).
RUC: Registro Único de Contribuyentes de la empresa participante.
Razon Social: Razón social de la empresa participante.
Tipo de Formulario: Tipo de formulario utilizado en el proceso.
Telefono: Número de teléfono de contacto.
Email: Dirección de correo electrónico de contacto.
Ola: Ola a la que pertenece la licitación.

## Authors
- [@licibot]([https://github.com/cjudithrb/licitbot/])
