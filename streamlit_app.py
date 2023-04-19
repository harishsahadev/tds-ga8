import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

st.title("Find the largest among three numbers")
st.write("Enter three numbers below:")

a = st.number_input("Enter the first number")
b = st.number_input("Enter the second number")
c = st.number_input("Enter the third number")

if st.button("Find largest"):
    largest = find_largest(a, b, c)
    st.write(f"The largest number is: {largest}")
