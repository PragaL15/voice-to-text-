# Audio to Text Converter API

A Flask-based API for converting speech in audio files (WAV format) to text using Google’s Speech Recognition. This API supports integration with frontend applications, allowing for audio-to-text processing directly from web clients.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoint](#api-endpoint)
- [Error Handling](#error-handling)
- [Logging and Security](#logging-and-security)
- [License](#license)

---

## Features

- Converts WAV audio files to text using Google Speech Recognition.
- Provides detailed logging for efficient debugging.
- Custom error handling for unsupported formats and large file sizes.
- Secure with CORS, Content Security Policy, and other security headers.

## Requirements

Ensure you have the following installed on your machine:

- **Python 3.7+**
- **Flask** (`pip install flask`)
- **Flask-CORS** (`pip install flask-cors`)
- **SpeechRecognition** (`pip install SpeechRecognition`)
- **pyaudio** (for speech recognition, though not necessary for non-realtime audio)

> Note: This app uses the Google Web Speech API, which requires internet access.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/PragaL15/voice-to-text-
   cd backend

## Installation 

`pip install -r requirements.txt`

## Configuration

1. CORS: By default, the app allows requests from http://localhost:5173 for local development.
2. Security Headers: Default security headers are set in the app to improve security when hosted publicly.
3. File Size Limit: The app restricts files to a maximum of 5MB to optimize performance

## Running the Application

`python app.py` and the application will run on http://localhost:5000

## API Endpoint

It's functoin --> Accepts a WAV audio file and returns the converted text.

### Request
1. URL: `http://localhost:5000/convert`
2. Method: POST
3. Headers: Content-Type: multipart/form-data
4. Body: audio_data (File) - WAV file for conversion.

## Error Handling

The app includes custom error messages for:

1. Missing audio files.
2. Unsupported file formats.
3. Exceeding file size limits.
4. Unrecognizable speech or failed requests to Google Speech Recognition.

## Security 

Configured with basic headers like Content Security Policy (CSP), X-Content-Type-Options, X-Frame-Options, and CORS support for specified origins.

