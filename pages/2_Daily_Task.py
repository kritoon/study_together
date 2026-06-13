import streamlit as st
import json
from utils.style_loader import load_css
from utils.sidebar import show_sidebar
from utils.gamification import (
    initialize_gamification,
    add_xp,
    add_badge
)
from utils.mission import initialize_mission
import time
import os
import nbformat
from nbconvert import HTMLExporter

# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="Daily Task",
    page_icon="📝",
    layout="wide"
)
load_css()
show_sidebar()
initialize_gamification()
initialize_mission()

# -------------------------
# Load Task Data
# -------------------------

with open("data/tasks.json", "r", encoding="utf-8") as file:
    tasks = json.load(file)


# For now always load Day 1
task = tasks[0]


# -------------------------
# Header
# -------------------------

st.title("📝 Today's Challenge")


st.success(
    f"""
    Day {task['day']} - {task['title']}

    Difficulty: {task['difficulty']}
    """
)


# -------------------------
# Question
# -------------------------

st.subheader("🎯 Problem")

st.write(task["question"])


# -------------------------
# Student Workspace
# -------------------------

st.subheader("💻 Your Workspace")

student_code = st.text_area(
    "Write your Python code here:",
    height=250,
    placeholder="""
# Example:

my_code = "I will solve this myself!"
"""
)


# -------------------------
# Hint Section
# -------------------------

with st.expander("💡 Need a Hint?"):
    st.info(task["hint"])


# -------------------------
# Solution Section
# -------------------------

with st.expander("👀 View Solution (Try yourself first)"):
    st.code(
        task["solution"],
        language="python"
    )


# -------------------------
# Completion Button
# -------------------------

if st.button("✅ I Completed Today's Task"):

    add_xp(25)
    add_badge("📝 First Challenge Completed")

    st.session_state.task_done = True

    st.balloons()

    st.success(
        """
        🎉 Amazing work!

        ⭐ +25 XP earned.
        Keep going!
        """
    )

    st.info("Redirecting to Home Page in 3 seconds...")

    time.sleep(3)

    st.switch_page("app.py")


# -------------------------
# Daily Motivation
# -------------------------

st.divider()


quotes = [
    "A good Data Scientist is not someone who knows everything, but someone who keeps learning.",
    
    "Errors are not failures; they are clues that guide you to the solution.",
    
    "One notebook a day is better than ten notebooks that you never finish."
]


import random

st.info(
    "🌱 Today's Motivation:\n\n"
    + random.choice(quotes)
)