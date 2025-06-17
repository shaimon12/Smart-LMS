
# AI-Powered Multi-Agent LMS Assistant – COMP8420 Major Project

This project implements an AI-powered, role-based LMS assistant with three specialized agents for Students, Teachers, and Admins. It uses LangChain, OpenAI’s GPT models, ChromaDB, and Whisper to support query answering, quiz generation, analytics, and voice input – streamlining academic workflows.

---

## Overview of Agents

### Student Agent
Helps students interact with COMP8420 content through voice or text-based queries.

#### Features / Tools:
1. **Student Q&A** – Course-related Q&A via RetrievalQA over lecture materials.
2. **Weekly Summary Fetcher** – Retrieves summaries from each week's content.
3. **Deadline Extractor** – Lists deadlines from structured `deadlines.json`.
4. **Quiz Generator** – Generates MCQs from NLP topics.
5. **Lecture Topic Finder** – Locates lectures based on keywords.
6. **Course Info Retriever** – Lists tools, instructors, or key info from static FAQ.
7. **Voice Query Handler** – Accepts transcribed `.json` voice input for questions.

---

### Teacher Agent
Assists educators in summarizing student needs, generating quizzes, and identifying difficult topics.

#### Features / Tools:
1. **Student Query Summary** – Summarizes key themes from student questions.
2. **Lecture Quiz Generator** – Auto-generates MCQs from `.txt` lecture files.
3. **Confusion Topic Analytics** – Analyzes frequently confusing terms from `qna.json`.

---

### Admin Agent
Supports course administration by monitoring engagement and addressing FAQs.

#### Features / Tools:
1. **Usage Statistics Dashboard** – Shows number of voice vs. text queries.
2. **Admin FAQ Bot** – Responds to administrative queries.
3. **Alert Generator** – Raises alerts based on system health or student activity.

---

## Dataset Structure

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

## Technologies Used

- **LangChain** – Agent management & tool orchestration
- **OpenAI GPT-3.5** – NLP tasks (QA, quiz generation, summarization)
- **ChromaDB** – Vector store for semantic search
- **Whisper** – Speech-to-text (for voice queries)
- **Matplotlib & WordCloud** – Visualization for confusion analytics
- **BLEU & Cosine Similarity** – Quiz evaluation

---

## Evaluation Metrics

- **BLEU Score** – Measures quality of model-generated responses.
- **Cosine Similarity** – Semantic overlap between generated & reference answers.
- **Tool Success Rate** – Each tool tested individually and validated.

---

## How to Run the Project

1. **Open the Jupyter Notebook**

   - Launch Jupyter using:
     ```bash
     jupyter notebook
     ```
   - Open the notebook containing the multi-agent LMS assistant logic (e.g., `Smart_LMS.ipynb`).

2. **Install Required Libraries**
   
   Make sure the following libraries are installed in your Python environment:
   ```bash
   pip install openai langchain chromadb sentence-transformers nltk wordcloud matplotlib
   
    ```
---

## Security Notice

> Do NOT hardcode your API key in public repositories. Use environment variables or `.env` files.
---

## Author

**Shaimon Rahman**

---

## License

This project is licensed for academic use only under [MIT License](LICENSE).
