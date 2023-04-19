import streamlit as st

def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

st.title("Find the largest number")
st.write("Enter three numbers and find the largest among them.")

# Take input from user
st.sidebar.write("Enter three numbers:")
a = st.sidebar.text_input("Number 1")
b = st.sidebar.text_input("Number 2")
c = st.sidebar.text_input("Number 3")

# Call the function
if st.sidebar.button("Find the largest number"):
    result = largest_number(float(a), float(b), float(c))
    st.write(f"The largest number is {result}.")
