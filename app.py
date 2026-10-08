import streamlit as st
import re

st.set_page_config(page_title="Masfa's Calculator", page_icon="🩷")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f6, #ffe1ed);
}

h1 {
    text-align: center;
    color: #c2185b;
}

/* FORCE 4 BUTTONS IN EVERY ROW */
div[data-testid="stHorizontalBlock"] {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 10px !important;
}

div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
    width: 100% !important;
    min-width: 0 !important;
    flex: none !important;
}

/* DISPLAY */
.display {
    background: #ffb6d5;
    color: #8a1748;
    border-radius: 20px;
    padding: 20px;
    text-align: right;
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 15px;
    overflow-x: auto;
}

/* BUTTONS */
div.stButton > button {
    width: 100% !important;
    height: 62px !important;
    border-radius: 18px !important;
    border: none !important;
    background: #ff91bd !important;
    color: white !important;
    font-size: 24px !important;
    font-weight: bold !important;
    box-shadow: 0 4px 8px rgba(194, 24, 91, 0.18);
}

div.stButton > button:hover {
    background: #ff6fa5 !important;
}

div.stButton > button:active {
    transform: scale(0.95);
}
</style>
""", unsafe_allow_html=True)

st.title("🩷 Masfa's Calculator")

if "display" not in st.session_state:
    st.session_state.display = ""

def add(value):
    st.session_state.display += value

def clear():
    st.session_state.display = ""

def calculate():
    expression = st.session_state.display

    if not expression:
        return

    if not re.fullmatch(r"[0-9+\-*/.() ]+", expression):
        st.session_state.display = "Error"
        return

    try:
        result = eval(expression, {"__builtins__": None}, {})
        st.session_state.display = str(result)
    except:
        st.session_state.display = "Error"

display = st.session_state.display or "0"

st.markdown(
    f'<div class="display">{display}</div>',
    unsafe_allow_html=True
)

# ROW 1
row = st.columns(4)

with row[0]:
    if st.button("7", key="seven"):
        add("7")
with row[1]:
    if st.button("8", key="eight"):
        add("8")
with row[2]:
    if st.button("9", key="nine"):
        add("9")
with row[3]:
    if st.button("÷", key="divide"):
        add("/")

# ROW 2
row = st.columns(4)

with row[0]:
    if st.button("4", key="four"):
        add("4")
with row[1]:
    if st.button("5", key="five"):
        add("5")
with row[2]:
    if st.button("6", key="six"):
        add("6")
with row[3]:
    if st.button("×", key="multiply"):
        add("*")

# ROW 3
row = st.columns(4)

with row[0]:
    if st.button("1", key="one"):
        add("1")
with row[1]:
    if st.button("2", key="two"):
        add("2")
with row[2]:
    if st.button("3", key="three"):
        add("3")
with row[3]:
    if st.button("−", key="minus"):
        add("-")

# ROW 4
row = st.columns(4)

with row[0]:
    if st.button("C", key="clear"):
        clear()
with row[1]:
    if st.button("0", key="zero"):
        add("0")
with row[2]:
    if st.button(".", key="decimal"):
        add(".")
with row[3]:
    if st.button("+", key="plus"):
        add("+")

if st.button("=", key="equals", use_container_width=True):
    calculate()
