import streamlit as st
def app():

#Title of the app
  st.title("BMI Calculator")

# Accept weight input in kilograms
weight = st.number_input("Enter your weight (in kilograms):", min_value=0.0)

# Accept height input in meters
height = st.number_input("Enter your height (in meters):", min_value=0.0)

# Calculate BMI
if weight > 0 and height > 0:
   bmi = weight / (height ** 2)
   st.write(f"Your BMI is: {bmi:.2f}")
   
 # Interpret the BMI category
   if bmi < 18.5:
    st.write("Category:Underweight")
   elif 18.5 <= bmi < 24.9:
    st.write("Category: Normal weight")
   elif 25 <= bmi < 29.9:
     st.write("Category: Overweight")
   else:
     st.write("Category: Obese")

else:
  st.write("Please enter valid weight and height values.")
