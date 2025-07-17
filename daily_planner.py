import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyDMTeCR4lgcE5c4bfWM6B7iDxas-tj28ck")
st.markdown("""<style>.stApp{background-color: #3386ff;} </style>""",unsafe_allow_html=True)
def create_daily_plan(prompt):
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content(prompt)
    return response.text

st.title("Daily Planner 🗓️")
user_input=st.text_input("What do you plan for today?")
if st.button("Create Plan"):
    with st.spinner("Talking to Gemini..."):
        result=create_daily_plan(user_input)
        st.write("Your plan: ",result)
    
