
import streamlit as st
import re

st.set_page_config(page_title="Masfa's Calculator", page_icon="🩷")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f6, #ffe0ec);
}

h1 {
    text-align: center;
    color: #c2185b;
    font-weight: 800;
}

.calculator {
    max-width: 420px;
    margin: auto;
}

.display {
    background: #ffb6d5;
    color: #8a1748;
    border-radius: 20px;
    padding: 22px;
    text-align: right;
    font-size: 38px;
    font-weight: bold;
    margin-bottom: 18px;
    box-shadow: 0 5px 15px rgba(194, 24, 91, 0.15);
    overflow-x: auto;
}

div.stButton > button {
    width: 100%;
    height: 65px;
    border-radius: 18px;
    border: none;
    background: #ff8fba;
    color: white;
    font-size: 24px;
    font-weight: 700;
    box-shadow: 0 4px 8px rgba(194, 24, 91, 0.18);
    transition: 0.15s;
}

div.stButton > button:hover {
    background: #ff6fa5;
    transform: scale(1.03);
}

div.stButton > button:active {
    transform: scale(0.96);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="calculator">', unsafe_allow_html=True)

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

    # Only allow calculator characters
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
cols = st.columns(4)

with cols[0]:
    if st.button("7", key="7"):
        add("7")

with cols[1]:
    if st.button("8", key="8"):
        add("8")

with cols[2]:
    if st.button("9", key="9"):
        add("9")

with cols[3]:
    if st.button("÷", key="divide"):
        add("/")

# ROW 2
cols = st.columns(4)

with cols[0]:
    if st.button("4", key="4"):
        add("4")

with cols[1]:
    if st.button("5", key="5"):
        add("5")

with cols[2]:
    if st.button("6", key="6"):
        add("6")

with cols[3]:
    if st.button("×", key="multiply"):
        add("*")

# ROW 3
cols = st.columns(4)

with cols[0]:
    if st.button("1", key="1"):
        add("1")

with cols[1]:
    if st.button("2", key="2"):
        add("2")

with cols[2]:
    if st.button("3", key="3"):
        add("3")

with cols[3]:
    if st.button("−", key="minus"):
        add("-")

# ROW 4
cols = st.columns(4)

with cols[0]:
    if st.button("C", key="clear"):
        clear()

with cols[1]:
    if st.button("0", key="0"):
        add("0")

with cols[2]:
    if st.button(".", key="decimal"):
        add(".")

with cols[3]:
    if st.button("+", key="plus"):
        add("+")

# EQUAL BUTTON
if st.button("=", key="equals"):
    calculate()

st.markdown("</div>", unsafe_allow_html=True)
