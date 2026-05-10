# 🔍 Lexis Intellect: Universal Document Intelligence

**Lexis Intellect** is a professional-grade AI tool designed for instant document synthesis and intelligence. Unlike general-purpose chatbots, Lexis Intellect uses a **Retrieval-Augmented Generation (RAG)** pipeline to interact directly with your files, ensuring that every response is grounded in the specific data you provide.

---

## 🚀 Live Demo
Experience the interface live on Hugging Face Spaces:
**[👉 Click Here to View Live Demo](https://huggingface.co/spaces/mubashrawaqar123/lexis-intellect)**

---

## ✨ Key Features
* **Multi-Format Support:** Seamlessly process PDFs, text files, and docx formats for comprehensive analysis.
* **Grounded Intelligence:** Eliminates hallucinations by restricting the AI's knowledge base to your uploaded files.
* **Enterprise-Grade UI:** A clean, minimalist interface optimized for professional workflows and high readability.
* **Privacy-Centric:** Your documents are processed within your session environment and are never used for model training.

## 🛠️ Technical Architecture
Lexis Intellect leverages a high-performance AI stack:
* **LLM:** OpenAI GPT-3.5 Turbo
* **Orchestration:** LangChain
* **Vector Store:** FAISS (Facebook AI Similarity Search)
* **Frontend:** Gradio
* **Data Ingestion:** Community loaders for multi-document support

## 📖 How to Use
1.  **Upload:** Drop any document (PDF, TXT, etc.) into the dashboard.
2.  **Inquire:** Ask a question regarding the content, data, or summary of the file.
3.  **Analyze:** Receive a direct, accurate answer extracted from your document in real-time.


### Environment Variables
To run this application, you must configure your **OpenAI API Key**.

### Local Installation
```bash
# 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME/lexis-intellect.git](https://github.com/YOUR_USERNAME/lexis-intellect.git)

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the application
python app.py
