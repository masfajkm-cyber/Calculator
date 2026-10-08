import streamlit as st

st.set_page_config(page_title="Masfa's Calculator")

st.markdown("""
<style>
div[data-testid="stTextInput"] input {
    background-color: #ffd6e7;
    color: #8b174f;
    font-size: 28px;
    font-weight: bold;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

st.title("🧮 Masfa's Calculator")

if "display" not in st.session_state:
    st.session_state.display = ""

def press(value):
    st.session_state.display += value

def clear():
    st.session_state.display = ""

def calculate():
    try:
        st.session_state.display = str(eval(st.session_state.display))
    except:
        st.session_state.display = "Error"

st.text_input(
    "Display",
    value=st.session_state.display,
    disabled=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7"):
        press("7")
    if st.button("4"):
        press("4")
    if st.button("1"):
        press("1")
    if st.button("C"):
        clear()

with col2:
    if st.button("8"):
        press("8")
    if st.button("5"):
        press("5")
    if st.button("2"):
        press("2")
    if st.button("0"):
        press("0")

with col3:
    if st.button("9"):
        press("9")
    if st.button("6"):
        press("6")
    if st.button("3"):
        press("3")
    if st.button("."):
        press(".")

with col4:
    if st.button("÷"):
        press("/")
    if st.button("×"):
        press("*")
    if st.button("−"):
        press("-")
    if st.button("+"):
        press("+")

if st.button("="):
    calculate()
