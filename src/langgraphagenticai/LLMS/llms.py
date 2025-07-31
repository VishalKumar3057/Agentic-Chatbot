import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

class GroqLLM:
    def __init__(self,user_contols_input):
        self.user_controls_input=user_contols_input

    def get_llm_model(self):
        try:
            groq_api_key=self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model=self.user_controls_input["selected_groq_model"]
            if groq_api_key=='' and os.environ["GROQ_API_KEY"] =='': 
                st.error("Please Enter the Groq API KEY")

            llm=ChatGroq(api_key=groq_api_key,model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error Ocuured With Exception : {e}")
        return llm
    

class OpenAILLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            openai_api_key = self.user_controls_input["OPENAI_API_KEY"]
            selected_openai_model = self.user_controls_input["selected_openai_model"]

            # Validate API key (check both Streamlit input and environment variable)
            if openai_api_key == '' and os.environ["OPENAI_API_KEY"] == '':
                st.error("Please Enter the OpenAI API KEY")

            # Initialize ChatOpenAI model
            llm = ChatOpenAI(
                api_key=openai_api_key,
                model=selected_openai_model
            )

        except Exception as e:
            raise ValueError(f"Error Occurred With Exception: {e}")

        return llm