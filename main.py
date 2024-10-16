import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Initialize chat
chat = model.start_chat(history=[])

# Function to get response from Gemini model
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Page configuration
st.set_page_config(page_title="Headlines AI", page_icon=":newspaper:", layout="centered")

# App Title
st.title("Headlines AI")

# Sidebar for Filters
st.sidebar.header("Platform and Content Type")

# Platform selection
platform = st.sidebar.selectbox("Choose a Platform:", ["YouTube", "Instagram"])

# Platform-specific options
if platform == "YouTube":
    content_type = st.sidebar.radio(
        "Choose Content Type:",
        ["Video Ideas", "Title", "Description", "Hashtag"]
    )
elif platform == "Instagram":
    content_type = st.sidebar.radio(
        "Choose Content Type:",
        ["Photo Ideas", "Captions", "Hashtag"]
    )

# Main section for user input
st.header("Describe Your Idea")
user_input = st.text_input("Enter your idea here...")

# Drafting a message to send to Gemini
message = f"Generate a {content_type.lower()} idea for {platform} based on the following description: {user_input}. Provide suggestions that are engaging, relevant, and optimized for {platform}.Give your response/answers in markdown language format."

# Submit button
if st.button("Submit"):
    if user_input:
        # Display user input details
        st.write("## Generated Content")
        st.write(f"**Platform:** {platform}")
        st.write(f"**Content Type:** {content_type}")
        st.write(f"**Idea:** {user_input}")

        # Get and display response from Gemini AI in markdown format
        st.subheader("The Response is:")
        response = get_gemini_response(message)
        for chunk in response:
            st.markdown(chunk.text)
            # Append each response chunk to chat history
            st.session_state['chat_history'].append(("Bot", chunk.text))
    else:
        st.warning("Please enter an idea to generate content.")
