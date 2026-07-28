import sys, os
os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
for card in flashcards:
    safe_card = card.encode("utf-8", "ignore").decode("utf-8")
    st.write(safe_card)

import os
import sys
import streamlit as st
from openai import OpenAI

# Force UTF-8 encoding everywhere
os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit page setup (no icons/emojis)
st.set_page_config(
    page_title="AI Flashcard Generator",
    layout="centered"
)

st.title("AI Flashcard Generator")
st.write("Paste your notes below and generate study flashcards.")

# Input fields
notes = st.text_area("Enter your notes:", height=200)
num_cards = st.slider("Number of flashcards:", 2, 10, 5)

def generate_flashcards(text, count):
    """Generate flashcards using OpenAI Chat Completions."""
    prompt = f"Create {count} flashcards from the following notes:\n\n{text}\n\nFormat each as 'Q: ... A: ...'."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    flashcards_text = response.choices[0].message.content.strip()
    return flashcards_text.split("\n\n")

# Button to generate
if st.button("Generate Flashcards"):
    if notes.strip():
        try:
            flashcards = generate_flashcards(notes, num_cards)
            st.subheader("Your Flashcards:")
            for card in flashcards:
                st.write(card)
        except Exception as e:
            st.error(f"Error generating flashcards: {e}")
    else:
        st.warning("Please enter some notes first.")
