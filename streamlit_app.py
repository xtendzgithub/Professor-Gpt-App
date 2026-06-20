from openai import OpenAI
import streamlit as st






st.markdown("""                                                      
<style>
.stApp {
    background-color: #0E1117;               # styling the Words ....
}
</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #141e30, #243b55);   # styling the background 
    color: white;
}
h1, h2, h3, p, div, span, label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stButton > button {
    color: white !important;
    background-color: #1f77b4 !important;
    border-radius: 10px;
    border: none;
}
</style>
""", unsafe_allow_html=True)


client = OpenAI(api_key ="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")
gptmodel = "gpt-5.4mini"
clientrole = "user"                # used api for openai


pre_prompt = "Teach me the following Machine Learning concept: "  # input to teach 

st.title("ProfessorGPT App") # Title  o fthe app
st.divider()

prompt = st.text_input("What do you want to Learn... ?")
gptbutton = st.button("Teach Me")

st.caption("Professor GPT will work when you press the button.") # captions niche dene ke liye 
st.divider()

if gptbutton and prompt:       

    with st.spinner("I am preparing your lecture..."):

        response = client.chat.completions.create(
            model="gpt-5.4-mini",
            messages=[
                {
                    "role": "user",
                    "content": pre_prompt + prompt
                }
            ]
        )
        
if gptbutton:
    with st.spinner("Preparing lecture..."):
        ...

    st.toast("Lecture Generated Successfully !!!!")
    st.success("Done!!!")
    st.write(response.choices[0].message.content) 
    
    st.snow()
    st.write(response.choices[0].message.content)  
    
    
       

    st.snow()
    st.write(response.choices[0].message.content)
   