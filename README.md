# 🎙️ GenAI RAG Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application built with **Python** and **Streamlit** that enables users to transcribe audio, generate concise summaries, and ask intelligent questions about the content using Large Language Models (LLMs).

---

## 🚀 Features

- 🎤 Upload audio files for processing
- 📝 Convert speech to text using Whisper
- 📄 Generate AI-powered summaries
- 💬 Ask questions about the transcribed content using RAG
- ⚡ Interactive and user-friendly Streamlit interface
- 🔍 Semantic retrieval for context-aware responses

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Mistral AI**
- **Whisper**
- **Sarvam AI**
- **LangChain**
- **Vector Store**

---

## 📂 Project Structure

```text
GenAI-RAG-Assistant/
│── app.py
│── main.py
│── requirements.txt
│── .env.example
│── .gitignore
│── README.md
│
├── core/
│   ├── extractor.py
│   ├── rag_engine.py
│   ├── summarize.py
│   ├── transcriber.py
│   └── vector_store.py
│
├── utils/
│   └── audio_processor.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/diiksha-verma/GenAI-RAG-Assistant.git
cd GenAI-RAG-Assistant
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Use the provided `.env.example` as a template and add your own API keys.

Example:

```env
MISTRAL_API_KEY=your_mistral_api_key
SARVAM_API_KEY=your_sarvam_api_key
WHISPER_MODEL=small
```

---

## ▶️ Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open automatically in your default web browser.

---

## 🔄 How It Works

1. Upload an audio file.
2. The audio is transcribed using Whisper.
3. The transcript is processed and indexed for retrieval.
4. A concise summary is generated.
5. Users can ask questions about the transcript.
6. The RAG pipeline retrieves relevant context and generates accurate responses using an LLM.

---

## 📌 Future Improvements

- Support additional audio and document formats
- Deploy the application on the cloud
- Improve retrieval performance
- Add multilingual transcription and summarization
- Store chat history
- Support multiple vector database backends

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is intended for educational and portfolio purposes.

---

## 👩‍💻 Author

**Diksha Verma**

GitHub: https://github.com/diiksha-verma
