import os
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

def main1():
    directory_path = r"C:\Users\miguela.silva\Downloads\Proyecto2\ola"
    documents = []

    # Recorrer todos los archivos en el directorio
    for filename in os.listdir(directory_path):
        if filename.endswith(".xlsx"):
            file_path = os.path.join(directory_path, filename)
            df = pd.read_excel(file_path)
            
            # Concatenar columnas para crear el contenido del documento
            if set(['Estado', 'Fideicomiso', 'Ruc', 'Razon Social', 'Tipo de Formulario', 'Telefono', 'Email', 'Ola']).issubset(df.columns):
                for index, row in df.iterrows():
                    content = (
                        f"Estado: {row['Estado']}\n"
                        f"Fideicomiso: {row['Fideicomiso']}\n"
                        f"Ruc: {row['Ruc']}\n"
                        f"Razon Social: {row['Razon Social']}\n"
                        f"Tipo de Formulario: {row['Tipo de Formulario']}\n"
                        f"Telefono: {row['Telefono']}\n"
                        f"Email: {row['Email']}\n"
                        f"Ola: {row['Ola']}"
                    )
                    doc = Document(page_content=content, metadata={"source": f"{filename} Row {index}"})
                    documents.append(doc)
            else:
                print(f"El archivo {filename} no contiene las columnas necesarias.")

    print(f"{len(documents)} Páginas descargadas")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50, separators=["\n\n", "\n", " ", ""]
    )

    split_documents = text_splitter.split_documents(documents=documents)
    print(f"Dividido en {len(split_documents)} Documentos...")

    print(split_documents[0].metadata)

    openai_api_key = "sk-None-JcrdY7dThe977ykRW2ZNT3BlbkFJgmx1EQljr6QUcvoqn"
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    db = FAISS.from_documents(split_documents, embeddings)
    db.save_local("faiss_index")

def main():
    openai_api_key = "sk-None-JcrdY7dThe977ykRW2ZNT3BlbkFJgmx1EQljr6QqnlnE"
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

    query = "cual es el telefono  email de MEGARCON CONTRATISTAS GENERALES SAC"
    docs = new_db.similarity_search(query)

    for doc in docs:
        print("##----Página ----#")
        print(doc.metadata['source'])
        print("##---- Contenido ---##")
        print(doc.page_content)

if __name__ == "__main__":
    main()
