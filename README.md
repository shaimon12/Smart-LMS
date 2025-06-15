
# 🤖 COMP8420 Multi-Agent LMS Assistant

This project implements an AI-powered multi-agent assistant system for the COMP8420 course, comprising three distinct agents: **Student Agent**, **Teacher Agent**, and **Admin Agent**. Each agent is designed with tailored tools to enhance learning, assessment, and management workflows in an educational environment using modern NLP techniques.

---

## 📁 Dataset Structure

| Folder/File              | Purpose                                                             |
|--------------------------|---------------------------------------------------------------------|
| `lectures/`              | Plain-text lecture slides used for retrieval and quiz generation    |
| `practicals/`            | Text versions of Jupyter notebooks for embedding                    |
| `audio_input/`           | Voice recordings and transcriptions of student queries              |
| `chroma_store/`          | Vector embeddings for all content (used by RAG pipeline)            |
| `qna.json`               | Student text-based questions and answers                            |
| `ambiguous_qna.json`     | Clarification-needed queries for evaluation                         |
| `weekly_summaries.json`  | One-paragraph summaries of each week's lecture                      |
| `deadlines.json`         | Assignment and presentation schedules                               |
| `announcements.json`     | System-generated announcements                                      |
| `discussions.json`       | Simulated classroom discussion records                              |
| `course_info.txt`        | General course details, instructors, and technologies used          |

---

## 🧑‍🎓 Student Agent – Tools

| Tool Name                | Purpose                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| `student_qa`             | Answers any course-related question using lecture/practical embeddings |
| `get_week_summary`       | Retrieves summaries for any specified lecture week                     |
| `get_deadlines`          | Lists upcoming deadlines from `deadlines.json`                          |
| `quiz_generator`         | Generates MCQs on any NLP topic using lecture content                   |
| `find_lecture_topic`     | Returns lecture files where a keyword is mentioned                      |
| `course_info_retriever`  | Responds to general questions about the course structure/tools          |
| `voice_query_handler`    | Answers spoken questions (transcribed with Whisper)                     |

---

## 👩‍🏫 Teacher Agent – Tools

| Tool Name                 | Purpose                                                                |
|---------------------------|------------------------------------------------------------------------|
| `student_query_summary`   | Summarizes common student questions from `qna.json` and audio          |
| `lecture_quiz_generator`  | Auto-generates 3–5 MCQs per lecture file with structural validation    |
| `confusion_topic_analytics` | Analyzes frequently occurring confusing terms as a word cloud         |

---

## 🧑‍💼 Admin Agent – Tools

| Tool Name                | Purpose                                                               |
|--------------------------|------------------------------------------------------------------------|
| `usage_stats_dashboard`  | Summarizes number of text and voice-based student queries              |
| `admin_faq_bot`          | Answers admin FAQs using an LLM prompt based on structured data        |
| `alert_generator`        | Suggests actions based on admin-reported system issues (e.g., engagement drop) |

---

## 🧪 Tool Testing Results

### Student Agent

- Assignment deadline query → **June 17, 2025**
- Week summary fetch → **Adapters and LoRA**
- Quiz generator → **2–3 MCQs passed validation checks**
- Topic finder → **Located files mentioning LoRA**
- Course info → **Pulled tools, instructors**
- Voice Q&A → **Correct response with semantic match**
- Deadline extractor → **All key dates listed**

### Teacher Agent

- Query Summary → **12 most frequent student concerns extracted**
- Quiz Generator → **5 valid MCQs saved to JSON + TXT**
- Confusion Analytics → **Top 10 confusing terms with word cloud**

### Admin Agent

- Usage Stats → **22 queries (20 text + 2 voice)**
- FAQ → **Correct response or fallback suggestion**
- Alert Generator → **Suggested actions for engagement drop**

---

## 📊 Evaluation Metrics

- **BLEU Score** – n-gram overlap for answer correctness
- **Cosine Similarity** – Semantic similarity between responses
- **Response Time** – Tool speed benchmarked per run

---

## 🛠️ Tech Stack

- OpenAI GPT-3.5 via `langchain_openai`
- Whisper (for speech-to-text transcription)
- Chroma (vector DB for embedding-based retrieval)
- SentenceTransformers (evaluation)
- NLTK (BLEU metric)
- Python 3.11+, Jupyter Notebook

---

## 🚀 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Export your OpenAI API key:
```bash
export OPENAI_API_KEY=your-key
```

3. Run `student_agent.py`, `teacher_agent.py`, or `admin_agent.py`

---

## 🌱 Future Enhancements

- Real-time student feedback and quiz scoring
- Dashboard UI with Streamlit or Gradio
- Teacher interface for feedback marking
- Voice-based follow-up questions with context

---

## 📬 Maintainer

**Shaimon Rahman** – Final Project for COMP8420 – Macquarie University (S1 2025)
