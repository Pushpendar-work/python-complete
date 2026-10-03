import streamlit as st
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Complete Python Study Hub",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beauty
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .chapter-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #007bff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .sidebar-content {
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🐍 Study Hub")
    st.markdown("---")
    st.markdown("### Quick Navigation")
    page = st.radio("Go to:", ["🏠 Home", "📚 Curriculum", "🛠️ Tools", "🎯 Progress"])
    st.markdown("---")
    st.info("This app helps you navigate through the Complete Python course materials.")

# Home Page
if page == "🏠 Home":
    st.title("Welcome to Complete Python! 🚀")
    st.subheader("Your Journey from Zero to Streamlit")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        This interactive hub is designed to accompany the **Complete Python** study project.
        Whether you are starting from your very first 'Hello World' or diving into
        API integrations and Web Apps, this hub organizes your learning path.

        **What's inside?**
        - 13 Comprehensive Chapters
        - Hands-on Practice Notebooks
        - Detailed Solution Guides
        - Quick-Reference Cheat Sheets
        """)
        if st.button("Explore Curriculum →"):
            st.balloons()

    with col2:
        st.image("https://img.icons8.com/fluency/240/python.png", width=200)

# Curriculum Page
elif page == "📚 Curriculum":
    st.title("📚 Learning Path")
    st.markdown("Explore the 13 pillars of Python mastery.")

    chapters = [
        ("01", "Your First Python Program", "Basic output, variables, and user input."),
        ("02", "Core Python Basics", "Data types, type casting, and operators."),
        ("03", "Control Flow and Logic", "Conditionals and loops."),
        ("04", "Strings and Text Processing", "Manipulation and formatting."),
        ("05", "Lists, Tuples, Dictionaries, and Sets", "Core data structures."),
        ("06", "Functions and Reusability", "Defining functions and functional tools."),
        ("07", "Classes and Inheritance", "Object-Oriented Programming (OOP)."),
        ("08", "Modules, Packages, and Imports", "Code organization."),
        ("09", "Error Handling and Debugging", "Try-except blocks and exceptions."),
        ("10", "Logging", "Tracking events and debugging."),
        ("11", "Working with Files and System Libs", "File I/O, os, and json."),
        ("12", "Working with APIs and External Data", "HTTP requests and LLM APIs."),
        ("13", "Streamlit Basics", "Building interactive web interfaces."),
    ]

    # Use a grid layout
    cols = st.columns(3)
    for idx, (num, title, desc) in enumerate(chapters):
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="chapter-card">
                    <small>Chapter {num}</small><br>
                    <strong>{title}</strong><br>
                    <p style="font-size: 0.9em; color: #666;">{desc}</p>
                </div>
                """, unsafe_allow_html=True)

# Tools Page
elif page == "🛠️ Tools":
    st.title("🛠️ Study Utilities")
    st.write("Manage your learning materials and exports.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("PDF Exports")
        st.write("Generate high-quality PDFs of the course content.")
        if st.button("Generate Full Guide (Simulated)"):
            st.success("Triggered combined_notebooks_to_pdf.py!")

    with col2:
        st.subheader("Cheat Sheets")
        st.write("Get a condensed version of all recaps.")
        if st.button("Generate Recap Shorts (Simulated)"):
            st.success("Triggered create_python_shorts.py!")

    st.markdown("---")
    st.markdown("### Resource Links")
    st.link_button("View Solution Notebooks", "file:///D:/Study/Complete_Python/solution_notebooks")
    st.link_button("View Practice Notebooks", "file:///D:/Study/Complete_Python/practice_notebooks")

# Progress Page
elif page == "🎯 Progress":
    st.title("🎯 Your Progress")
    st.write("Track your journey through the course.")

    progress_value = st.slider("How much of the course have you completed?", 0, 13, 0)
    st.progress(progress_value / 13)
    st.write(f"You have completed {progress_value} out of 13 chapters!")

    if progress_value == 13:
        st.success("🎉 Congratulations! You've completed the entire Python path!")
        st.snow()
    elif progress_value > 0:
        st.info("Keep going! You're making great progress.")
    else:
        st.warning("Time to start your first lesson!")
