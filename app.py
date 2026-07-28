import sys
import os

# Force UTF-8 everywhere
os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

import streamlit as st
import openai
import os

#  Create a client using the new API
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#  Function to generate flashcards
def generate_flashcards(notes, num_cards):
    prompt = f"Create {num_cards} educational flashcards from the following notes:\n{notes}\nFormat each flashcard as 'Q: question' and 'A: answer'."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that creates clear, concise educational flashcards."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    flashcards_text = response.choices[0].message.content
    return flashcards_text

#  Streamlit UI
st.set_page_config(page_title="AI Flashcard Generator", page_icon="🧠", layout="centered")
st.title("AI Flashcard Generator")
st.write("Paste your notes and get instant flashcards!")

notes = st.text_area("Enter your notes here:")
num_cards = st.slider("Number of flashcards", 1, 10, 5)

if st.button("Generate Flashcards"):
    if notes.strip():
        with st.spinner("Generating flashcards..."):
            flashcards = generate_flashcards(notes, num_cards)
            st.success("Here are your flashcards:")
            st.write(flashcards)
    else:
        st.warning("Please enter some notes before generating flashcards.")
