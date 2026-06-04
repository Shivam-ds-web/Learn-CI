import streamlit as st 

st.title("Power Calculator")
st.write("ENter a number to obtain its square, cube and fifth power.")

a = st.number_input("Enter an integer",value = 1,step = 1)

square =  a**2
cube = a**3
fifth = a**5

st.write(f"The square of {a} is {square}")
st.write(f"The cube of {a} is {cube}")
st.write(f"The fifth power of {a} is {fifth}")