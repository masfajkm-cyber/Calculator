import streamlit as st
import re

st.set_page_config(
    page_title="Masfa's Calculator",
    page_icon="🩷"
)

# =========================
# DESIGN
# =========================

st.markdown("""
<style>

/* Normal page background */
.stApp {
    background: white;
}

/* Your name */
h1 {
    text-align: center !important;
    color: #b1124a !important;
    font-weight: 800 !important;
}

/* Calculator panel */
div[data-testid="stVerticalBlockBorderWrapper"] {
    max-width: 430px !important;
    margin: auto !important;
    background: #f8c8dc !important;
    border-radius: 32px !important;
    border: none !important;
    padding: 20px !important;
}

/* Display */
.display {
    background: #f4a9c4;
    color: #b1124a;
    border-radius: 22px;
    padding: 18px;
    text-align: right;
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 15px;
    min-height: 42px;
    overflow-x: auto;
}

/* Keep 4 buttons in every row */
div[data-testid="stHorizontalBlock"] {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 10px !important;
}

div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
    width: 100% !important;
    min-width: 0 !important;
}

/* Calculator buttons */
div.stButton > button {
    width: 100% !important;
    height: 58px !important;
    border-radius: 18px !important;
    border: none !important;
    background: #f4a9c4 !important;
    color: #b1124a !important;
    font-size: 23px !important;
    font-weight: 800 !important;
}

/* Button hover */
div.stButton > button:hover {
    background: #ef98b8 !important;
    color: #8f0d3b !important;
}

/* Equals button */
div.stButton > button[kind="primary"] {
    background: #e88aaa !important;
    color: #b1124a !important;
}

</style>
""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================

st.title("🩷 Masfa's Calculator")


# =========================
# CALCULATOR
# =========================

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
        result = eval(
            expression,
            {"__builtins__": None},
            {}
        )

        st.session_state.display = str(result)

    except:
        st.session_state.display = "Error"


# Rounded calculator container
with st.container(border=True):

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


    # EQUALS
    if st.button("=", key="equals", type="primary", use_container_width=True):
        calculate()
