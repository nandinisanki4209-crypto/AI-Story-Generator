import streamlit as st
from story_generator import generate_story

st.title("AI Story Generator")

st.write("Create a creative story using AI-inspired story generation.")

topic = st.text_input("Enter your story topic")

genre = st.selectbox(
    "Choose a genre",
    ["Adventure", "Fantasy", "Horror", "Mystery", "Romance", "Science Fiction"]
)

length = st.selectbox(
    "Choose story length",
    ["Short", "Medium", "Long"]
)

if st.button("Generate Story"):
    if topic:
        story = generate_story(topic, genre, length)
        st.subheader("Your Story")
        st.write(story)
    else:
        st.warning("Please enter a story topic.")