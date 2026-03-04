import streamlit as st
from functions.addition_rechner import add  

st.title("Addition Rechner.")

st.write("Hier ist mein Addition Rechner. Er addiert zwei Zahlen.")

with st.form("Additions_form"):     
    number1 = st.number_input("Number 1")
    number2 = st.number_input("Number 2")
    button = st.form_submit_button("Berechnen")

if button:
    result = add(number1, number2)
    st.write(f"Das Ergebnis ist: {result}")