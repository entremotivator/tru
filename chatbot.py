import streamlit as st
import os
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from trulens_eval import TruChain, Feedback, OpenAI, Huggingface, Tru

hugs = Huggingface()
openai = OpenAI()
tru = Tru()

# Load environment variables from .streamlit/secrets.toml
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["HUGGINGFACE_API_KEY"] = st.secrets["HUGGINGFACE_API_KEY"]
