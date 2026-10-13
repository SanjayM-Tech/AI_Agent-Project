import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Study Assistant")
st.caption("Powered by LangChain + Groq")

st.markdown("---")

st.write("### 📚 Ask your study question")

question = st.text_area(
    "Your Question",
    placeholder="Example: Explain Artificial Intelligence in simple words...",
    height=120
)

if st.button("🚀 Ask AI", use_container_width=True):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner("🤖 AI is thinking..."):

            llm = ChatGroq(
                model="openai/gpt-oss-20b",
                temperature=0.3
            )

            prompt = f"""
            You are an AI Study Assistant.

            Answer the student's question clearly and simply.
            Use simple language and examples when useful.

            Student Question:
            {question}
            """

            response = llm.invoke(prompt)

        st.markdown("### 🤖 AI Response")
        st.success(response.content)

st.markdown("---")
st.caption("AI Study Assistant • Built with LangChain & Groq")