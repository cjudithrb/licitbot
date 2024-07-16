from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def main():
    loader = DirectoryLoader(path="hr-policies")
    documents = loader.load()
    print(f"{len(documents)} Pagina descargada")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500, chunk_overlap = 50, separators=["\n\n","\n"," ",""]
    ) 

    split_documents =  text_splitter.split_documents(documents=documents)
    print(f"Split into {len(split_documents)} Documentos....")

    print(split_documents[0].metadata)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(split_documents, embeddings)
    db.save_local("faiss_index")

def faiss_query():
    embeddings = OpenAIEmbeddings()
    new_db = FAISS.load_local("fass_index", embeddings)

    query = "Explain the Candidate Onboarding process."
    docs = new_db.similarity_search(query)

    for doc in docs:
        print("##----Page ----#")
        print(docs.metadata['source'])
        print("##---- Content ---##")
        print(doc.page_content)

if __name__ == "__main__":
    main()