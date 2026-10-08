import streamlit as st

st.set_page_config(page_title="Masfa's Calculator")

st.markdown("""
<style>
.calculator-display {
    background-color: #ffd6e7;
    color: #8b174f;
    padding: 20px;
    border-radius: 12px;
    text-align: right;
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 15px;
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

display = st.session_state.display if st.session_state.display else "0"

st.markdown(
    f'<div class="calculator-display">{display}</div>',
    unsafe_allow_html=True
)

row1 = st.columns(4)

with row1[0]:
    if st.button("7", use_container_width=True):
        press("7")

with row1[1]:
    if st.button("8", use_container_width=True):
        press("8")

with row1[2]:
    if st.button("9", use_container_width=True):
        press("9")

with row1[3]:
    if st.button("÷", use_container_width=True):
        press("/")

row2 = st.columns(4)

with row2[0]:
    if st.button("4", use_container_width=True):
        press("4")

with row2[1]:
    if st.button("5", use_container_width=True):
        press("5")

with row2[2]:
    if st.button("6", use_container_width=True):
        press("6")

with row2[3]:
    if st.button("×", use_container_width=True):
        press("*")

row3 = st.columns(4)

with row3[0]:
    if st.button("1", use_container_width=True):
        press("1")

with row3[1]:
    if st.button("2", use_container_width=True):
        press("2")

with row3[2]:
    if st.button("3", use_container_width=True):
        press("3")

with row3[3]:
    if st.button("−", use_container_width=True):
        press("-")

row4 = st.columns(4)

with row4[0]:
    if st.button("C", use_container_width=True):
        clear()

with row4[1]:
    if st.button("0", use_container_width=True):
        press("0")

with row4[2]:
    if st.button(".", use_container_width=True):
        press(".")

with row4[3]:
    if st.button("+", use_container_width=True):
        press("+")

if st.button("=", use_container_width=True):
    calculate()
