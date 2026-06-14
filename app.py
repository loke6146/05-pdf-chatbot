import streamlit as st
from PyPDF2 import PdfReader
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

st.title("🤖 Chat With Your PDF")

st.write("Upload a PDF and chat with it!")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type="pdf"
)

if uploaded_file is not None:

    st.success("PDF uploaded successfully!")
    st.write(uploaded_file.name)

    # Read PDF
    pdf_reader = PdfReader(uploaded_file)

    text = ""

    # Extract text from all pages
    for page in pdf_reader.pages:
        text += page.extract_text()

    with st.expander("📄 View Extracted Text"):
        st.write(text[:1000])
    if st.button("Summarize PDF"):

        with st.spinner("AI is reading your PDF..."):

            response = client.chat.completions.create(
                model="deepseek/deepseek-chat-v3-0324",
                messages=[
                    {
                        "role": "system",
                        "content": """
    You are a helpful document summarizer.

    Summarize the PDF clearly in bullet points.
    Focus on key ideas.
    Keep it concise and easy to understand.
    """
                    },
                    {
                        "role": "user",
                        "content": text
                    }
                ]
            )

            summary = response.choices[0].message.content

            st.subheader("📌 Summary")
            st.write(summary)
    
    st.subheader("💬 Ask Questions About PDF")

    question = st.text_input(
        "Ask something from the PDF"
    )

    if st.button("Ask PDF"):

        if question:

            with st.spinner("Thinking..."):

                response = client.chat.completions.create(
                    model="deepseek/deepseek-chat-v3-0324",
                    messages=[
                        {
                            "role": "system",
                            "content": """
    You are a helpful PDF assistant.

    Answer ONLY based on the uploaded document.

    If the answer is not in the PDF,
    say:
    'I could not find that in the document.'
    """
                        },
                        {
                            "role": "user",
                            "content": f"""
    PDF Content:

    {text}

    Question:
    {question}
    """
                        }
                    ]
                )

                answer = response.choices[0].message.content

                st.subheader("📌 Answer")
                st.write(answer)