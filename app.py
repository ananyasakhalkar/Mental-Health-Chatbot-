import streamlit as st
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch
import random

# ----- Sentiment Analysis Pipeline (HuggingFace) -----
sentiment_analyzer = pipeline("sentiment-analysis")

def get_sentiment(text):
    result = sentiment_analyzer(text)[0]
    return result['label'].upper(), result['score']

# ----- Lightweight LLM Setup (for CPU use) -----
@st.cache_resource
def load_llm():
    model_name = "distilgpt2"  # Lightweight & fast, ideal for CPU
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_llm()

def get_llm_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        temperature=0.7,
        do_sample=True,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response[len(prompt):].strip()

# ----- Coping Technique Recommender -----
coping_techniques = {
    'POSITIVE': ['Practice gratitude', 'Celebrate a small win', 'Share your joy with someone'],
    'NEGATIVE': ['Take deep breaths', 'Write in a journal', 'Listen to calming music'],
    'NEUTRAL': ['Go for a short walk', 'Read a book', 'Do a 2-minute breathing exercise']
}

def get_recommendation(sentiment):
    return random.choice(coping_techniques.get(sentiment.upper(), coping_techniques['NEUTRAL']))

# ----- Streamlit UI -----
st.set_page_config(page_title="Mental Health Chatbot", page_icon="🧠")
st.title("🧠 Mental Health Chatbot")

user_input = st.text_input("How are you feeling today?")

if user_input:
    sentiment, confidence = get_sentiment(user_input)
    st.write(f"**Detected Emotion:** `{sentiment}` ({confidence:.2f} confidence)")

    prompt = f"The user says: \"{user_input}\"\nChatbot response:"
    llm_response = get_llm_response(prompt)
    st.markdown(f"**Chatbot**: {llm_response}")

    recommendation = get_recommendation(sentiment)
    st.markdown(f"🌿 **Suggested Coping Technique**: *{recommendation}*")

    rating = st.slider("Rate the recommendation (0 = Not helpful, 10 = Very helpful):", 0, 10, 5)
    st.write("✅ Feedback recorded (can be used for RL fine-tuning later)")
