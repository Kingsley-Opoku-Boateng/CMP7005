
import streamlit as st
from multiapp import MultiApp

# from app import calculator,bmi
import calculator
import bmi_calculator
import area_calculator

app = MultiApp()

#Add all your application here
#app.add_app("Data page for demo", data.app)
app.add_app("Calculator", calculator.app)
app.add_app("BMI Calculator", bmi_calculator.app)
app.add_app("Area Calculator", area_calculator.app)

# The main app
app.run()
