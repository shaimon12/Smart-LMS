# AI-Powered Multi-Agent LMS Assistant – COMP8420 Major Project

This project implements a role-based, AI-powered LMS assistant that supports **Students**, **Teachers**, and **Admins**. Built with LangChain, OpenAI’s GPT models, ChromaDB, and Whisper, this system offers powerful tools like Q&A, quiz generation, analytics, and voice interaction to automate academic tasks.

---

## 🤖 Agents Overview

### 🧑‍🎓 Student Agent
Helps students interact with the COMP8420 course through intelligent text or voice-based queries.

#### Features:
1. **Student Q&A** – RAG-based retrieval from lectures using ChromaDB.
2. **Weekly Summary Fetcher** – Returns weekly content summaries.
3. **Deadline Extractor** – Pulls structured deadlines from `deadlines.json`.
4. **Quiz Generator** – Creates MCQs on demand using OpenAI.
5. **Lecture Topic Finder** – Locates files or weeks containing a keyword.
6. **Course Info Retriever** – Fetches tools, instructors, and course policies.
7. **Voice Query Handler** – Parses transcribed questions from Whisper.

---

### 👨‍🏫 Teacher Agent
Supports teachers by summarizing common queries, evaluating content delivery, and auto-generating quizzes.

#### Features:
1. **Student Query Summary** – Extracts trending topics or concerns from student questions.
2. **Lecture Quiz Generator** – Produces 3–5 MCQs from `.txt` lecture files.
3. **Confusion Topic Analytics** – Detects confusing terms in `qna.json` via word frequency and visualization.

---

### 🛠 Admin Agent
Helps course admins monitor usage, answer FAQs, and respond to system alerts.

#### Features:
1. **Usage Statistics Dashboard** – Counts voice vs. text queries and overall activity.
2. **Admin FAQ Bot** – Answers structured administrative questions.
3. **Alert Generator** – Detects low engagement and suggests actions.

---

## 📁 Dataset Structure

```
StudentAgentDataset/
└── COMP8420/
    ├── ambiguous_qna.json
    ├── announcements.json
    ├── audio_input/
    ├── chroma_store/
    ├── course_info.txt
    ├── deadlines.json
    ├── discussions.json
    ├── lectures/
    ├── practicals/
    ├── qna.json
    └── weekly_summaries.json
```

---

## 🧠 Technologies Used

- **LangChain** – Agent tool management
- **OpenAI GPT-3.5** – QA, summarization, quiz creation
- **ChromaDB** – Vector store for retrieval-augmented generation (RAG)
- **Whisper** – Converts spoken questions to text
- **WordCloud / Matplotlib** – Visual analytics
- **BLEU & Cosine Similarity** – Evaluation of generated content

---

## 📊 Evaluation Metrics

Each tool was tested individually with:

- **BLEU Score** – Accuracy of generated answers vs. reference
- **Cosine Similarity** – Semantic relevance of responses
- **Tool Execution Latency** – Average time per call
- **Structural Validation** – For quizzes (answer format, completeness)

---

## 🔍 RAG vs Non-RAG Evaluation

To test the effect of retrieval-augmented generation:

### RAG-Enabled (ChromaDB):
- Accesses vector index of lectures
- Contextual and grounded answers
- Higher BLEU and semantic similarity

### RAG-Disabled:
- Uses only GPT model without retrieval
- Generic answers with lower accuracy
- Less relevance to course-specific queries

This highlights the importance of RAG in academic NLP tools.

---

## 🚀 Getting Started

1. **Open Notebook**

   Use Jupyter to open the main notebook (e.g., `AI-Powered Multi-Agent LMS Assistant.ipynb`).

2. **Install Requirements**
```bash
pip install openai langchain chromadb sentence-transformers nltk wordcloud matplotlib
```

3. **Set API Key**

   Create a `.env` file or export your OpenAI key safely:
```bash
export OPENAI_API_KEY=your-key
```

---

## 🔐 Security Note

**DO NOT upload notebooks with your API keys to public GitHub repositories.** Always use environment variables or `.env` for credentials.

---

## 👤 Author

**Shaimon Rahman**  
Final Year Master's Student – Software Engineering  
Federation University Australia

---

## 📄 License

This project is for academic use and released under the [MIT License](LICENSE).