import os
import gradio as gr
from groq import Groq
from langchain_community.document_loaders import UnstructuredFileLoader, UnstructuredPowerPointLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# --- CSS: Minimalist Enterprise Aesthetic ---
custom_css = """
body, .gradio-container, button, input, textarea, .label-wrap span {
    font-family: 'Inter', 'Segoe UI', sans-serif !important;
    font-size: 13px !important; 
}
button.primary {
    background-color: #334155 !important; 
    border: none !important;
    border-radius: 4px !important;
    color: white !important;
    font-weight: 500 !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
button.primary:hover { background-color: #1e293b !important; }
.message-wrap .bot { font-size: 13px !important; color: #1e293b !important; line-height: 1.5 !important; }
.message-wrap .user { background-color: #fef3c7 !important; border: 1px solid #fde68a !important; color: #92400e !important; }
"""

class UniversalRAG:
    def __init__(self):
        # All lines inside the class must be indented exactly 4 spaces
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vector_store = None
        try:
            self.api_key = os.environ.get('RAGchatbot')
            self.client = Groq(api_key=self.api_key)
        except: 
            self.client = None

    def process_document(self, file_obj):
        # This line must align vertically with def __init__
        if not self.client: return "❌ Error: API Key not found."
        if not file_obj: return "⚠️ Status: No file uploaded."
        try:
            file_path = file_obj.name
            if file_path.endswith(('.ppt', '.pptx')):
                loader = UnstructuredPowerPointLoader(file_path)
            else:
                loader = UnstructuredFileLoader(file_path)
                
            docs = loader.load()
            chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)
            self.vector_store = FAISS.from_documents(chunks, self.embeddings)
            return f"✅ Knowledge base active ({len(chunks)} chunks ready)"
        except Exception as e: 
            return f"❌ System Error: {str(e)}"

    def chat_query(self, message, history):
        # This line must align vertically with def process_document
        if not self.vector_store: return "Please upload a document to begin."
        try:
            related_docs = self.vector_store.similarity_search(message, k=3)
            context = "\n\n".join([d.page_content for d in related_docs])
            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": f"Answer concisely based strictly on context: {context}"},
                    {"role": "user", "content": message}
                ],
                model="llama-3.1-8b-instant",
            )
            return response.choices[0].message.content
        except Exception as e: return f"⚠️ API Error: {str(e)}"

# --- UI Setup ---
bot_engine = UniversalRAG()

with gr.Blocks() as demo:
    gr.Markdown("# Lexis Intellect")
    gr.Markdown("*General Purpose Document Intelligence*")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("#### 📂 Source Data")
            file_uploader = gr.File(label="Upload Document", height=120)
            build_btn = gr.Button("Build Index", variant="primary")
            status_indicator = gr.Textbox(label="Status", interactive=False)
            
        with gr.Column(scale=1):
            gr.ChatInterface(
                fn=bot_engine.chat_query,
                examples=["Summarize this document.", "What are the key takeaways?"]
            )

    build_btn.click(fn=bot_engine.process_document, inputs=[file_uploader], outputs=[status_indicator])

demo.launch(theme=gr.themes.Default(spacing_size="sm", text_size="sm"), css=custom_css)
