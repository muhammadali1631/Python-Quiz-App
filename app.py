import streamlit as st

st.set_page_config(page_title="Python Quiz App", page_icon="🎯")

if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False

questions = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "16"],
        "correct": "8"
    },
    {
        "question": "Which of these is NOT a Python data type?",
        "options": ["list", "tuple", "array", "dictionary"],
        "correct": "array"
    },
    {
        "question": "What does len([1, 2, 3]) return?",
        "options": ["1", "2", "3", "4"],
        "correct": "3"
    },
    {
        "question": "Which method is used to add an element to a list?",
        "options": ["append()", "extend()", "add()", "insert()"],
        "correct": "append()"
    },
    {
        "question": "What is the result of True and False?",
        "options": ["True", "False", "None", "Error"],
        "correct": "False"
    }
]

def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.current_question = 0
    st.session_state.score = 0

def next_question():
    st.session_state.current_question += 1

def main():
    st.title("🐍 Python Quiz")
    
    if not st.session_state.quiz_started:
        st.write("Welcome to the Python Quiz! Test your Python knowledge with these questions.")
        st.write("There are", len(questions), "questions in total.")
        if st.button("Start Quiz"):
            start_quiz()
        return

    st.progress((st.session_state.current_question) / len(questions))
    
    st.write(f"Score: {st.session_state.score}/{len(questions)}")
    
    if st.session_state.current_question >= len(questions):
        st.success(f"Quiz completed! Final score: {st.session_state.score}/{len(questions)}")
        if st.button("Restart Quiz"):
            start_quiz()
        return

    current_q = questions[st.session_state.current_question]
    st.write(f"### Question {st.session_state.current_question + 1}:")
    st.write(current_q["question"])
    
    answer = st.radio("Choose your answer:", current_q["options"], key=f"q_{st.session_state.current_question}")
    
    if st.button("Submit Answer"):
        if answer == current_q["correct"]:
            st.success("Correct! 🎉")
            st.session_state.score += 1
        else:
            st.error(f"Wrong! The correct answer was: {current_q['correct']}")
        next_question()
        st.rerun()

if __name__ == "__main__":
    main()
