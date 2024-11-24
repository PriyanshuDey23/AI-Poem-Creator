from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from prompt import *


# Load environment variables from the .env file
load_dotenv()

# Access the environment variables just like you would with os.environ
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# Response Format For my LLM Model
def poem_generation(user_input, poem_type, theme ,tone,mood,length,rhyme,meter,keywords):
    # Define the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002", temperature=1, api_key=GOOGLE_API_KEY)  

    # Define the prompt
    PROMPT_TEMPLATE = PROMPT  # Imported
    prompt = PromptTemplate(
            input_variables=["user_input", "poem_type","theme", "tone","mood","length","rhyme","meter","keywords"], # input in prompt
            template=PROMPT_TEMPLATE,
        )
      
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Generate Response
    response=llm_chain.run({"user_input":user_input, 
                            "poem_type":poem_type ,
                            "theme":theme,
                            "tone":tone,
                            "mood":mood,
                            "length":length,
                            "rhyme":rhyme,
                            "meter":meter,
                            "keywords":keywords})
    return response

# Streamlit app
st.set_page_config(page_title="Poem Generation")
st.header("Poem Generation")

# Input text
user_input = st.text_area("Enter your poem topic", height=200)


# Side bar for parameters
with st.sidebar:
    st.title("Parameters:")
    poem_type=st.selectbox("Select The Specific Type of poem ",["Sonnet","Haiku","Free Verse","Ballad","None"])
    theme=st.selectbox("Select The Theme of poem ",["Love","Nature","Life","Death","None"])
    tone=st.selectbox("Select The Tone of poem ",["Happy","Sad","Melancholic","Inspirational","None"])
    mood=st.selectbox("Select The Mood of poem ",["Peaceful","Energetic","Contemplative","Humorous","None"])
    length=st.text_input("Select The Length of poem ")
    rhyme=st.selectbox("Select The rhyme of poem ",["End Rhyme","Internal Rhyme","None"])
    meter=st.selectbox("Select The meter of poem ",["Lambic","Trochaic","Anapestic","None"])
    keywords=st.text_area("Provide a list of keywords related to theme ")

if st.button("Generate"):
        response=poem_generation(user_input, poem_type, theme ,tone,mood,length,rhyme,meter,keywords)
        st.write(response)



