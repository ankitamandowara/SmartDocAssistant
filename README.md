# **SmartDocAssistant**

SmartDocAssistant is an AI-powered assistant that allows users to upload PDF, DOCX, or TXT files and ask intelligent questions based on the document's content. It leverages advanced Language Learning Models (LLMs) to provide accurate and context-specific answers.

---

## **Features**
- Upload and process multiple document formats (PDF, DOCX, TXT).
- Intelligent question-answering based on document content.
- Easy integration with OpenAI for advanced natural language processing.
- Secure user authentication for personalized experience.

---

## **Technologies Used**
- **Backend Framework:** FastAPI  
- **Database:** MySQL  
- **AI/ML:** LangChain, OpenAI GPT Models  
- **Visualization:** Matplotlib  
- **Storage and Retrieval:** Chroma for vector storage  

---

## **Setup Instructions**
1. **Clone the Repository**:
   ```
   git clone https://github.com/your-username/SmartDocAssistant.git
   cd SmartDocAssistant
   ```


2. **Set Up a Virtual Environment**:

    ```
    python -m venv venv
    source venv/bin/activate    # For Linux/Mac
    venv\Scripts\activate       # For Windows
    ```

3. **Install Dependencies**:

    ```
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:


    Create a .env file in the project root and add the following:
    makefile
    ```
    OPENAI_API_KEY=your_openai_api_key
    DB_HOST=localhost
    DB_USER=your_user
    DB_PASSWORD=your_password
    DB_NAME=your_database
    ```

5. **Run the Application**:

    ```
    uvicorn src.main:app --reload
    ```

6. **Access the API**:

   Open your browser and visit: http://127.0.0.1:8000/docs to explore the Swagger UI.

## **Project Structure**

```
SmartDocAssistant/
├── src/
│   ├── main.py               # Entry point for the FastAPI app
│   ├── document_handler.py   # Handles document processing and querying
│   ├── user.py               # Manages user-related database operations
├── requirements.txt          # List of dependencies
├── README.md                 # Project documentation
├── .gitignore                # Files and folders to ignore in Git
├── tests/
│   ├── test_main.py          # Unit tests for the application
```

## **How It Works**
1. **Upload a Document**: Users upload a PDF, DOCX, or TXT file via the API.  
2. **Document Processing**: The system splits the document into manageable chunks, creates embeddings using OpenAI, and stores them for retrieval.  
3. **Ask Questions**: Users can ask questions, and the system retrieves answers based on the document's content.

---

## **Future Enhancements**
- Add a user-friendly web interface.
- Enable multi-language document support.
- Expand to support additional file formats.

---

## **Contributing**
Contributions are welcome! Please fork this repository and submit a pull request for any feature enhancements or bug fixes.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.
