import os
import tempfile
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from fastapi import UploadFile
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Upload:
    @staticmethod
    def uploadDocument(file: UploadFile):
        """
        Processes the uploaded document and prepares it for querying using LLM.
        """
        try:
            # Ensure OpenAI API key is set
            openai_api_key = os.getenv("OPENAI_API_KEY")
            if not openai_api_key:
                raise ValueError("Missing OpenAI API key. Set OPENAI_API_KEY in .env file.")

            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(file.file.read())
                temp_file_path = temp_file.name
            
            # Load the document using PyPDFLoader
            loader = PyPDFLoader(temp_file_path)
            pages = loader.load_and_split()
            
            if not pages:
                raise ValueError("The document contains no readable content.")

            # Split text into chunks
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            all_splits = text_splitter.split_documents(pages)

            # Generate vector store
            vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

            # Set up retrieval-based QA chain
            llm = OpenAI(temperature=0)
            retriever = vectorstore.as_retriever()
            qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

            # Example query
            output = qa_chain.run("Summarize the main points of the document.")

            # Cleanup: Delete temporary file
            os.remove(temp_file_path)

            return {"status": "success", "result": output}

        except Exception as e:
            return {"status": "error", "message": str(e)}
