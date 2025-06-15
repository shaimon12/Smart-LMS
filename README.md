
# AI-Powered Multi-Agent LMS Assistant – COMP8420 Major Project

This project implements an AI-powered, role-based LMS assistant with three specialized agents for Students, Teachers, and Admins. It uses LangChain, OpenAI’s GPT models, ChromaDB, and Whisper to support query answering, quiz generation, analytics, and voice input – streamlining academic workflows.

---

## 🧠 Overview of Agents

### 👩‍🎓 Student Agent
Helps students interact with COMP8420 content through voice or text-based queries.

#### 🧰 Features / Tools:
1. **Student Q&A** – Course-related Q&A via RetrievalQA over lecture materials.
2. **Weekly Summary Fetcher** – Retrieves summaries from each week's content.
3. **Deadline Extractor** – Lists deadlines from structured `deadlines.json`.
4. **Quiz Generator** – Generates MCQs from NLP topics.
5. **Lecture Topic Finder** – Locates lectures based on keywords.
6. **Course Info Retriever** – Lists tools, instructors, or key info from static FAQ.
7. **Voice Query Handler** – Accepts transcribed `.json` voice input for questions.

---

### 👨‍🏫 Teacher Agent
Assists educators in summarizing student needs, generating quizzes, and identifying difficult topics.

#### 🧰 Features / Tools:
1. **Student Query Summary** – Summarizes key themes from student questions.
2. **Lecture Quiz Generator** – Auto-generates MCQs from `.txt` lecture files.
3. **Confusion Topic Analytics** – Analyzes frequently confusing terms from `qna.json`.

---

### 🛠️ Admin Agent
Supports course administration by monitoring engagement and addressing FAQs.

#### 🧰 Features / Tools:
1. **Usage Statistics Dashboard** – Shows number of voice vs. text queries.
2. **Admin FAQ Bot** – Responds to administrative queries.
3. **Alert Generator** – Raises alerts based on system health or student activity.

---

## 📁 Dataset Structure

```
StudentAgentDataset/
├── COMP8420/
│   ├── lectures/                 # Raw lecture .txt files
│   ├── weekly_summaries.json    # Summarized content by week
│   ├── deadlines.json           # Course deadlines
│   ├── qna.json                 # Text-based student queries
│   ├── audio_input/
│   │   └── voice_questions.json # Transcribed voice queries
```

---

## 🚀 Technologies Used

- **LangChain** – Agent management & tool orchestration
- **OpenAI GPT-3.5** – NLP tasks (QA, quiz generation, summarization)
- **ChromaDB** – Vector store for semantic search
- **Whisper** – Speech-to-text (for voice queries)
- **Matplotlib & WordCloud** – Visualization for confusion analytics
- **BLEU & Cosine Similarity** – Quiz evaluation

---

## 🧪 Evaluation Metrics

- **BLEU Score** – Measures quality of model-generated responses.
- **Cosine Similarity** – Semantic overlap between generated & reference answers.
- **Tool Success Rate** – Each tool tested individually and validated.

---

## ⚙️ Running the System

To test an agent:
```bash
python student_agent.py
python teacher_agent.py
python admin_agent.py
```

---

## 🔒 Security Notice

> 🔑 Do NOT hardcode your API key in public repositories. Use environment variables or `.env` files.

---

## 👤 Author

**Shaimon Rahman**  
COMP8420 – Major Project  
Federation University

---

## 📄 License

This project is licensed for academic use only under [MIT License](LICENSE).
