# app/student_panel.py

import streamlit as st
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from utils.auth import check_login, update_password
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

def show_student_panel():
    load_dotenv()
    st.title("Student Panel")

    username = st.session_state.get("username")
    user_id = st.session_state.get("user_id")

    if not username or not user_id:
        st.warning("Please login to continue.")
        return

    # Load user-course mapping from users.json
    with open("config/users.json", "r") as f:
        user_data = json.load(f)

    assigned_courses = []
    for user in user_data:
        if username == user.get("username") or user_id == user.get("id"):
            assigned_courses = user.get("courses", [])
            break

    if not assigned_courses:
        st.warning("You are not assigned to any course. Please contact the admin.")
        return

    selected_course = st.selectbox("Select a course:", options=assigned_courses)

    # === Course Announcements ===
    st.subheader("Course Announcements")
    ann_path = f"data/{selected_course}/announcements.json"
    if os.path.exists(ann_path):
        with open(ann_path, "r") as f:
            announcements = json.load(f)
        for ann in reversed(announcements[-5:]):
            st.markdown(f"**{ann['title']}** — *{ann['timestamp']}*")
            st.write(ann['message'])
            st.markdown("---")
    else:
        st.info("No announcements yet.")

    # === Course Materials Viewer ===
    st.subheader("View & Download Course Materials")
    content_type = st.selectbox("Select material type", ["lectures", "practicals", "assignments"])
    material_path = f"data/{selected_course}/{content_type}"
    if os.path.exists(material_path):
        files = os.listdir(material_path)
        if files:
            for file in files:
                file_path = os.path.join(material_path, file)
                with open(file_path, "rb") as f:
                    st.download_button(label=f"📥 Download {file}", data=f, file_name=file)
        else:
            st.info("No files available for this content type.")
    else:
        st.info("No materials uploaded yet.")

    # === Q&A Section ===
    st.subheader("Ask a Question (Text or Voice)")
    persist_path = f"chroma_db/{selected_course}"
    embedding = OpenAIEmbeddings(disallowed_special=())
    vectordb = Chroma(persist_directory=persist_path, embedding_function=embedding)
    retriever = vectordb.as_retriever()
    chain = RetrievalQA.from_chain_type(llm=ChatOpenAI(), retriever=retriever)

    voice_mode = st.toggle("Use Whisper Voice Input")
    question = ""

    if voice_mode:
        audio_file = st.file_uploader("Upload audio file (WAV/MP3)", type=["wav", "mp3"])
        if audio_file:
            import tempfile, whisper
            model = whisper.load_model("base")
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                temp_audio.write(audio_file.read())
                audio_path = temp_audio.name
            transcription = model.transcribe(audio_path)
            os.remove(audio_path)
            question = transcription['text']
            st.write("Recognized Text:", question)
    else:
        question = st.text_input("Enter your question")

    if st.button("Get Answer") and question:
        with st.spinner("Thinking..."):
            answer = chain.run(question)
        st.success("Answer:")
        st.write(answer)

    # === Deadline Agent ===
    st.subheader("Upcoming Deadlines")
    deadline_file = f"data/{selected_course}/deadlines.json"
    if os.path.exists(deadline_file):
        with open(deadline_file, "r") as f:
            deadlines = json.load(f)
        today = datetime.now().date()
        upcoming = [
            (item["title"], datetime.strptime(item["due_date"], "%Y-%m-%d").date())
            for item in deadlines
            if 0 <= (datetime.strptime(item["due_date"], "%Y-%m-%d").date() - today).days <= 14
        ]

        if upcoming:
            st.markdown("**Next 14 Days:**")
            for title, due in upcoming:
                st.markdown(f"- {title} (Due: {due.strftime('%b %d, %Y')})")
        else:
            st.info("No deadlines in the next 14 days.")
    else:
        st.warning("No deadline file found.")

    # === Quiz Generator ===
    st.subheader("Quiz Generator")
    quiz_topic = st.text_input("Enter topic or keyword (e.g., tokenization)")
    if st.button("Generate Quiz") and quiz_topic:
        from langchain.prompts import PromptTemplate
        from langchain.chains import LLMChain

        prompt = PromptTemplate(
            input_variables=["topic"],
            template="""
            You are a quiz generator for university-level course content.
            Create 3 multiple choice questions about the topic: {topic}.
            Each question should have 4 options (A, B, C, D) and one correct answer.
            Provide the answer key below the questions.
            """
        )
        quiz_chain = LLMChain(llm=ChatOpenAI(), prompt=prompt)
        result = quiz_chain.run(topic=quiz_topic)
        if result.strip():
            st.markdown("**Generated Quiz:**")
            st.markdown(result)
        else:
            st.info("No quiz generated.")

    # === Change Password ===
    st.subheader("Change Your Password")
    current_pwd = st.text_input("Current Password", type="password", key="student_current_pwd")
    new_pwd = st.text_input("New Password", type="password", key="student_new_pwd")
    confirm_pwd = st.text_input("Confirm New Password", type="password", key="student_confirm_pwd")

    if st.button("Update Password"):
        if not check_login(username, current_pwd):
            st.error("Current password is incorrect.")
        elif new_pwd != confirm_pwd:
            st.error("New passwords do not match.")
        elif not new_pwd.strip():
            st.error("New password cannot be empty.")
        else:
            update_password(username, new_pwd)
            st.success("Password updated successfully.")
