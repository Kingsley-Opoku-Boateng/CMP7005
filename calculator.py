import streamlit as st

#Define functions for Calculator
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
        return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        st.error("Error: Cannot divide by zero.")
        return None

def si(p, r, t):
    return (p * r * t) / 100
    
def ci(p, r, t, n):
    return p * (1 + r/n)**(n*t) - p

def sqr(num):
    return num ** 2

def sqrt(num):
    return num**0.5


 
#Create Streamlit app
def app():
   st.title("Calculator")

#Select operation 
   operation = st.selectbox("Choose an operation", ("Addition", "Subtraction", "Multiplication", "Division", "Simple Interest", "Compound Interest", "Square", "Square Root"))

#Get Input values based on operation
   if operation == "Addition":
     num1 = st.number_input("Enter the first number")
     num2 = st.number_input("Enter the second number")
     result = add(num1, num2)
   elif operation == "Subtraction":
     num1 = st.number_input("Enter the first number")
     num2 = st.number_input("Enter the second number")
     result = sub(num1, num2) 
   elif operation == "Multiplication":
     num1 = st.number_input("Enter the first number")
     num2 = st.number_input("Enter the second number")
     result = mul(num1, num2)
   elif operation == "Division":
     num1 = st.number_input("Enter the first number")
     num2 = st.number_input("Enter the second number")
     result = div(num1, num2)
   elif operation == "Simple Interest":
     p = st.number_input("Enter the principal amount")
     r = st.number_input("Enter the rate of interest")
     t = st.number_input("Enter the time period")
     result = si(p, r, t)
   elif operation == "Compound Interest":
     p = st.number_input("Enter the principal amount")
     r = st.number_input("Enter the rate of interest")
     t = st.number_input("Enter the time period")
     n = st.number_input("Enter the number of times interest is compounded per time period")
     result = ci(p, r, t, n)
   elif operation == "Square":
     num = st.number_input("Enter the number")
     result = sqr(num)
   elif operation == "Square Root":
     num = st.number_input("Enter the number")
     result = sqrt(num)

#Display the results
   if st.button("Calculate"):
      st.write("Result:", result)




