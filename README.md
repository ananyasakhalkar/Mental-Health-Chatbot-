# 🧠 Mental Health Chatbot

A lightweight, interactive mental health chatbot powered by **HuggingFace Transformers** and built with **Streamlit**. The chatbot uses sentiment detection to tailor its responses and suggests personalized coping strategies — all without requiring a GPU.

## 🌐 Live on Hugging Face Spaces

> You can deploy this easily on [Hugging Face Spaces](https://huggingface.co/spaces) by including the following files:
> - `app.py`
> - `requirements.txt`
> - `space.yaml`

## ✨ Features

- 💬 Natural responses using Hugging Face's `distilgpt2` (CPU-friendly)
- 🧠 Real-time sentiment detection via HuggingFace `distilbert-base-uncased-finetuned-sst-2-english`
- 🌿 Personalized coping recommendations based on mood
- 🧪 Built-in rating system for future RL fine-tuning
- ⚡ Deployed with Streamlit UI

## 📁 Files Required

### 🔹 `app.py`

> Full app logic (chatbot, sentiment detection, UI)

### 🔹 `requirements.txt`

```txt
streamlit
transformers
torch
```

### 🔹 `space.yaml` (for Hugging Face Spaces)

```yaml
title: "Mental Health Chatbot"
sdk: streamlit
app_file: app.py
python_version: 3.10
```

> 🔧 You can tweak `python_version` as needed.

-
## 🚀 Getting Started (Locally or on Spaces)

### ➤ Deploy on Hugging Face Spaces

1. Create a new Space: [huggingface.co/spaces](https://huggingface.co/spaces)
2. Choose **Streamlit** as your SDK
3. Upload `app.py`, `requirements.txt`, and `space.yaml`
4. That’s it — your chatbot is live!

### ➤ Run Locally

```bash
git clone https://huggingface.co/spaces/your-username/mental-health-chatbot
cd mental-health-chatbot

pip install -r requirements.txt
streamlit run app.py
```

---

## 🧠 How It Works

1. **User input** → Sentiment classified as POSITIVE / NEGATIVE / NEUTRAL
2. **Lightweight LLM** generates a helpful response
3. **Coping strategies** are recommended based on mood
4. **User rates the advice** (can be logged for future learning)

---

## 📊 Example Use Case

```plaintext
User: I'm feeling really overwhelmed today.

→ Sentiment: NEGATIVE (0.98 confidence)
→ Chatbot Response: I'm really sorry you're feeling that way. You're not alone — it's okay to take a moment for yourself.
→ Suggested Technique: Take deep breaths
→ User Rating: 8
```

---

## 💡 Future Enhancements

- Logging feedback to CSV or DB
- RL-based improvement of recommendations
- Multi-turn conversation memory
- Admin dashboard for tracking mental health trends

---

## 📄 License

MIT License — use, share, and modify freely.
