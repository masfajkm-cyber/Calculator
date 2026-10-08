import streamlit as st

st.title("🧮 Masfa's Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operation = st.selectbox(
    "Choose an operation",
    ["+", "-", "×", "÷"]
)

if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "×":
        result = num1 * num2
    else:
        if num2 == 0:
            st.error("You can't divide by zero!")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"Answer: {result}")
