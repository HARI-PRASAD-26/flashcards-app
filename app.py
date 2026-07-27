import streamlit as st
import openai
import os

# ✅ Securely load your API key from Streamlit Secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

# 🧠 Function to generate flashcards
def generate_flashcards(notes, num_cards):
    prompt = f"Create {num_cards} educational flashcards from the following notes:\n{notes}\nFormat each flashcard as 'Q: question' and 'A: answer'."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that creates clear, concise educational flashcards."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    flashcards_text = response.choices[0].message.content
    return flashcards_text

# 🎨 Streamlit UI
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
