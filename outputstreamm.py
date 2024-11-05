import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Tennis Ball Tracking and Region Detection", layout="wide")

# Apply custom CSS for button and progress bar styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50; /* Green background */
        color: white; /* White text */
        border: none; /* Remove borders */
        padding: 10px 24px; /* Add some padding */
        text-align: center; /* Center the text */
        font-size: 16px; /* Increase font size */
        margin: 4px 2px; /* Add some margin */
        cursor: pointer; /* Pointer/hand icon */
        border-radius: 8px; /* Rounded corners */
    }

    .stButton>button:hover {
        background-color: #45a049; /* Darker green on hover */
    }

    .stProgress>div>div>div {
        background-color: #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the title of the application
st.title("Tennis Game Tracking")

# Create layout with two columns
col1, col2 = st.columns([2, 1])

# Left column for video
with col1:
    # Create a file uploader for selecting input video files
    uploaded_file = st.file_uploader("Select Input File", type=["mp4", "avi", "mov"])

    # Display video preview if a file is uploaded
    if uploaded_file is not None:
        st.video(uploaded_file, format="video/mp4", start_time=0)

# Right column for controls
with col2:
    # Create a placeholder for a progress bar
    progress_bar = st.progress(0)

    # Buttons for interacting with the video processing workflow
    if st.button("Preview Video"):
        st.write("Previewing video...")

    # Display a progress bar with a placeholder value
    progress_percentage = 20  # Example value for the progress
    progress_bar.progress(progress_percentage / 100)

    if st.button("Process Video"):
        st.write("Processing video...")

    if st.button("Show Output"):
        st.write("Showing processed output...")

    if st.button("Download Output"):
        st.write("Preparing download...")
        # Code to generate downloadable file link goes here
