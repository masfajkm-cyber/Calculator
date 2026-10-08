import streamlit as st
import re

st.set_page_config(
    page_title="M.calculate",
    page_icon="🧮"
)

# =========================
# PROFESSIONAL DESIGN
# =========================

st.markdown("""
<style>

/* Page */
.stApp {
    background: #f3f4f6;
}

/* Small calculator title */
.calc-title {
    text-align: center;
    font-size: 22px;
    font-weight: 700;
    color: #374151;
    margin: 8px 0 14px 0;
}

/* Calculator panel */
div[data-testid="stVerticalBlockBorderWrapper"] {
    max-width: 390px !important;
    margin: auto !important;
    background: #20242a !important;
    border-radius: 30px !important;
    border: 1px solid #30353d !important;
    padding: 18px !important;
}

/* Display */
.display {
    background: #15181c;
    color: #f3f4f6;
    border: 1px solid #30353d;
    border-radius: 20px;
    padding: 18px;
    text-align: right;
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 16px;
    min-height: 42px;
    overflow-x: auto;
}

/* Four equal columns */
div[data-testid="stHorizontalBlock"] {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 10px !important;
}

div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
    width: 100% !important;
    min-width: 0 !important;
}

/* ROUND BUTTONS */
div.stButton > button {
    width: 100% !important;
    height: 64px !important;
    min-height: 64px !important;
    border-radius: 50% !important;
    border: 1px solid #3a4048 !important;
    background: #30353d !important;
    color: #f5f5f5 !important;
    font-size: 21px !important;
    font-weight: 700 !important;
    padding: 0 !important;
    transition: background 0.08s ease, transform 0.08s ease !important;
}

/* Button press */
div.stButton > button:active {
    transform: scale(0.94) !important;
}

/* Hover */
div.stButton > button:hover {
    background: #3b424c !important;
    color: #ffffff !important;
}

/* Operators */
div.stButton > button[kind="secondary"] {
    background: #3a414b !important;
}

/* Equals */
div.stButton > button[kind="primary"] {
    background: #4f6f95 !important;
    color: white !important;
    border: none !important;
}

div.stButton > button[kind="primary"]:hover {
    background: #5b7da6 !important;
}

/* Remove extra spacing */
div[data-testid="stVerticalBlock"] {
    gap: 0.5rem !important;
}

</style>
""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================

st.markdown(
    '<div class="calc-title">M.calculate</div>',
    unsafe_allow_html=True
)


# =========================
# CALCULATOR
# =========================

if "display" not in st.session_state:
    st.session_state.display = ""


def add(value):
    # If the previous result was an error, start fresh
    if st.session_state.display == "Error":
        st.session_state.display = ""

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
        result = eval(
            expression,
            {"__builtins__": None},
            {}
        )

        # Cleaner result
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        st.session_state.display = str(result)

    except Exception:
        st.session_state.display = "Error"


# =========================
# ISOLATE CALCULATOR
# =========================

@st.fragment
def calculator():

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
        if st.button(
            "=",
            key="equals",
            type="primary",
            use_container_width=True
        ):
            calculate()


calculator()
