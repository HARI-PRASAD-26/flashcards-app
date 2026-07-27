import streamlit as st
import openai

# Replace with your API key
openai.api_key = "YOUR_API_KEY"

st.title("AI Flashcard Generator")
st.write("Paste your notes and get instant flashcards!")

topic_text = st.text_area("Enter your notes here:")
num_cards = st.slider("Number of flashcards", 1, 10, 5)

if st.button("Generate Flashcards"):
    prompt = f"Create {num_cards} flashcards (Q&A) from the following text:\n\n{topic_text}"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )

    flashcards = response.choices[0].text.strip()
    st.text_area("Your Flashcards:", flashcards, height=300)
