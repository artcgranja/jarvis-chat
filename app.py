import streamlit as st
from llama_cpp import Llama
import os
from config import LANGUAGE_PROMPTS
from dotenv import load_dotenv

load_dotenv()

if "MODEL_PATH" not in os.environ:
    st.error("""
    Error: MODEL_PATH environment variable is not set.
    
    Please set the MODEL_PATH environment variable to your Llama model file location:
    
    Windows:
    ```bash
    set MODEL_PATH=path\\to\\your\\llama\\model
    ```
    
    Linux/Mac:
    ```bash
    export MODEL_PATH=path/to/your/llama/model
    ```
    """)
    st.stop()

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'language' not in st.session_state:
    st.session_state.language = "en"

@st.cache_resource
def load_model():
    try:
        model_path = os.getenv("MODEL_PATH")
        if not os.path.exists(model_path):
            st.error(f"Error: Model file not found at {model_path}")
            st.stop()
        return Llama(model_path=model_path)
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.stop()

try:
    llm = load_model()
except Exception as e:
    st.error(f"Failed to initialize the language model: {str(e)}")
    st.stop()

def get_response(user_input, language):
    try:
        prompts = LANGUAGE_PROMPTS[language]
        current_prompt = f"{prompts['system_prompt']}\n"
        
        for msg in st.session_state.conversation_history:
            current_prompt += f"\n{msg['role']}: {msg['content']}"
        
        current_prompt += f"\nMr. Stark: {user_input}\nJarvis:"
        
        response = llm(current_prompt, max_tokens=4096, stop=["\n", "Mr. Stark:"], temperature=0.7)
        return response['choices'][0]['text'].strip()
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return "I apologize, but I encountered an error while processing your request."

st.title("J.A.R.V.I.S. - AI Assistant")

language = st.radio("Select Language / Selecione o Idioma", 
                   ["English", "Português"],
                   horizontal=True)
st.session_state.language = "en" if language == "English" else "pt"

st.markdown("---")
st.markdown(LANGUAGE_PROMPTS[st.session_state.language]["welcome_message"])

for message in st.session_state.conversation_history:
    with st.chat_message(message["role"], avatar="🤖" if message["role"] == "Jarvis" else "🦸"):
        st.write(message["content"])

user_input = st.chat_input(LANGUAGE_PROMPTS[st.session_state.language]["input_placeholder"])

if user_input:
    st.session_state.conversation_history.append({"role": "Mr. Stark", "content": user_input})
    with st.chat_message("Mr. Stark", avatar="🦸"):
        st.write(user_input)
    
    with st.chat_message("Jarvis", avatar="🤖"):
        response = get_response(user_input, st.session_state.language)
        st.write(response)
        st.session_state.conversation_history.append({"role": "Jarvis", "content": response})
        st.rerun()

if st.button("Clear Conversation / Limpar Conversa"):
    st.session_state.conversation_history = []
    st.rerun() 