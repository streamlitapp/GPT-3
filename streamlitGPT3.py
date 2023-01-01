import streamlit as st
import openai

st.subheader('GPT-3')

openai.api_key = st.text_input('API Key')

engine = st.selectbox('Engine', 
                            ('text-davinci-003', 'text-curie-001', 'text-babbage-001', 'text-ada-001',
                             'code-davinci-002', 'code-cushman-001'))

prompt = st.text_input('Prompt')

max_tokens = st.number_input('Max Tokens', value = 4000, step = 1)

if openai.api_key and prompt:
  completion = openai.Completion.create(engine = engine, prompt = prompt, max_tokens = max_tokens)
  st.write(completion.choices[0].text)
