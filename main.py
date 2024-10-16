import streamlit as st

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

# Submit button
if st.button("Submit"):
    if user_input:
        # Placeholder result - replace with actual content generation logic
        st.write("## Generated Content")
        st.write(f"**Platform:** {platform}")
        st.write(f"**Content Type:** {content_type}")
        st.write(f"**Idea:** {user_input}")
        st.write("Generated content will be displayed here.")
    else:
        st.warning("Please enter an idea to generate content.")
