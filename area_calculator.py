import streamlit as st
import math

def app():

  # Title of the app
  st.title("Area Calculator")

  # Select the shape
  shape = st.selectbox("Select a shape", ["Circle", "Rectangle", "Triangle"])

  # Calculate area based on the selected shape
  if shape == "Circle":
    #Input for radius
    radius = st.number_input("Enter the radius (in meters):", min_value=0.0)
    if radius > 0:
      area = math.pi * radius ** 2
      st.write(f"The area of the circle is: {area:.2f} square meters")
    else:
      st.write("Please enter a valid radius.")

  elif shape == "Rectangle":
    # Input for length and width
      length = st.number_input("Enter the length (in meters):", min_value=0.0)
      width = st.number_input("Enter the width (in meters):", min_value=0.0)
      if length > 0 and width > 0:
        area = length * width
        st.write(f"The area of the rectangle is: {area:.2f} square meters")
      else:
        st.write("Please enter valid length and width.")

  elif shape == "Triangle":
    # Input for base and height
    base = st.number_input("Enter the base (in meters):", min_value=0.0)
    height = st.number_input("Enter the height (in meters):", min_value=0.0)
    if base > 0 and height > 0:
       area = 0.5 * base * height
       st.write(f"The area of the triangle is: {area:.2f} square meters")
  else:
       st.write("Please enter valid base and height.")

