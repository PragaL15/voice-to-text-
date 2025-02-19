# 🎤 Audio to Text Converter API 🎧

A **Flask-based API** that converts speech in audio files (**WAV format**) to text using **Google Speech Recognition**! This API seamlessly integrates with frontend applications, enabling **real-time audio-to-text conversion** from web clients. 🚀

---

## 📜 Table of Contents
- [✨ Features](#-features)
- [📦 Requirements](#-requirements)
- [⚙️ Setup](#-setup)
- [🔧 Configuration](#-configuration)
- [▶️ Running the Application](#-running-the-application)
- [🌐 API Endpoint](#-api-endpoint)
- [🚨 Error Handling](#-error-handling)
- [🔒 Security](#-security)
- [📜 License](#-license)

---

## ✨ Features

✅ Converts **WAV audio** files to text using **Google Speech Recognition** 🗣️➡️📜  
✅ Provides **detailed logging** for debugging 📝  
✅ Custom **error handling** for unsupported formats & large file sizes ❌  
✅ **Secure API** with CORS, CSP, and other security headers 🔒

---

## 📦 Requirements

Ensure you have the following installed on your machine:  
💻 **Python 3.7+**  
🐍 **Flask** (`pip install flask`)  
🌍 **Flask-CORS** (`pip install flask-cors`)  
🎙 **SpeechRecognition** (`pip install SpeechRecognition`)  
🎛 **pyaudio** (For real-time recognition, but not required for file processing)

> ⚠️ This app **requires an internet connection** as it uses Google Web Speech API. 🌐

---

## ⚙️ Setup

1️⃣ Clone the repository:
   ```bash
   git clone https://github.com/PragaL15/voice-to-text-
   cd backend
   ```

2️⃣ Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Configuration

⚙️ **CORS**: By default, requests are allowed from `http://localhost:5173` for local development.  
⚙️ **Security Headers**: The app enforces security headers like CSP & X-Frame-Options.  
⚙️ **File Size Limit**: **Max file size: 5MB** to ensure smooth performance! 🚀

---

## ▶️ Running the Application

Run the Flask app with:
```bash
python app.py
```
🌟 Your API will be live at **http://localhost:5000** 🌍

---

## 🌐 API Endpoint

🎯 **Function**: Accepts a WAV audio file and returns the converted text.

### 🔄 Request Format:
📌 **URL**: `http://localhost:5000/convert`  
📌 **Method**: `POST`  
📌 **Headers**: `Content-Type: multipart/form-data`  
📌 **Body**: `audio_data` (File) - **WAV file** for conversion 🎵

---

## 🚨 Error Handling

The API includes **custom error responses** for:
❌ Missing audio files 🎵🚫  
❌ Unsupported file formats 📂⚠️  
❌ Exceeding the **5MB file size limit** 🚀  
❌ **Unrecognizable speech** or failed requests to Google Speech Recognition 🎤❌

---

## 🔒 Security

🛡 Configured with essential **security headers**:
- **Content Security Policy (CSP)** 🛑
- **X-Content-Type-Options** 🚨
- **X-Frame-Options** 🔒
- **CORS support** for specified origins 🌍

---

🚀 Ready to convert speech to text? **Let’s go!** 🎙➡️📜

