# Hugging Face Inference API Integration

## 🚀 Project Overview
This repository demonstrates how to utilize the **Hugging Face Inference API** to run state-of-the-art open-source models (such as Llama, Mistral, and Phi) in a serverless environment. This approach allows for high-performance AI integration without the overhead of managing local GPU infrastructure.

---

## 🛠️ Key Features

### 1. Serverless Model Access
* **Hub Integration:** Fetching and calling any supported model from the Hugging Face Hub.
* **Text Generation:** Using the `InferenceClient` for chat-based and instruction-based tasks.

### 2. Multi-Model Versatility
* **LLM Orchestration:** Switching between different model architectures (e.g., Mistral-7B, Llama-3) by changing a single model ID.
* **Task Specificity:** Implementation patterns for Text Generation, Summarization, and Sentiment Analysis.

### 3. API Optimization
* **Streaming Responses:** Handling real-time token generation for low-latency user interfaces.
* **Advanced Hyperparameters:** Fine-tuning `top_k`, `top_p`, and `repetition_penalty` for high-quality outputs.

### 4. Security & Best Practices
* **Token Management:** Securely loading `HF_TOKEN` from `.env` files.
* **Error Handling:** Managing API timeouts and model loading states (Wait for model logic).

---

## 💻 Tech Stack
* **Language:** Python
* **Libraries:** `huggingface_hub`, `python-dotenv`
* **Platform:** Jupyter Notebook / Google Colab

