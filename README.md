# Legal Drafter ⚖️

Legal Drafter is a real-time, AI-powered writing assistant designed specifically for legal documents. As you type, the application uses a custom-trained ONNX model to predict the next words, displaying them as inline "ghost text." Users can seamlessly accept these predictions using the TAB key, significantly accelerating the drafting process.

**Click on the Live Demo link:** https://nosid-star.github.io/legal-draft/static

*(Note: Please access the live link on a PC or laptop. Mobile phone keyboards do not have a TAB key, which is required to accept the AI suggestions.)*

## Features

* Real-Time AI Predictions: Powered by a lightweight ONNX model running on the CPU for high-speed, low-latency text generation.
* Ghost Text Interface: Suggestions appear perfectly aligned behind your current text, mimicking the GitHub Copilot experience.
* Live WebSocket Connection: Continuous, low-overhead communication between the frontend and backend for instant token predictions.
* Auto-Expanding Canvas: The text editor automatically resizes itself to fit your content and the AI's suggestions.
* Dark/Light Mode: Full theme support with system preference detection and a manual toggle.
* Connection Status Indicator: A live UI element showing the real-time health of the WebSocket connection.

## Tech Stack

Frontend (GitHub Pages):
* HTML5
* Vanilla JavaScript (WebSocket Client)
* Tailwind CSS (via CDN)

Backend (Google Cloud Run):
* Python 3.10
* FastAPI (REST & WebSockets)
* ONNX Runtime (CPU Inference)
* Hugging Face Tokenizers
* NumPy

## Project Structure
```
├── main.py                     # FastAPI server and WebSocket handler
├── Dockerfile                  # Container configuration for Google Cloud Run
├── requirements.txt            # Python dependencies
├── legal_drafting_model.onnx   # Trained AI model weights
├── legal_tokenizer.json        # Tokenizer vocabulary configuration
└── index.html                  # Frontend user interface
```
## Cloud Architecture & Deployment

This application uses a decoupled architecture:
1. Frontend: Hosted statically on GitHub Pages.
2. Backend: Containerized using Docker and deployed to Google Cloud Run (wss://legal-ws-163217414481.asia-south1.run.app/ws). The API is configured with CORS middleware to accept secure connections from the frontend.

## Local Development Setup

To run the Legal Drafter locally on your machine:

1. Clone the repository
```
git clone https://github.com/nosid-star/legal-draft.git
cd legal-draft
```
2. Set up a Python virtual environment
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Run the FastAPI server
```
uvicorn main:app --host 0.0.0.0 --port 8080 --reload 
```
5. Connect the frontend

* Open index.html in your code editor.
* Temporarily change the WebSocket URL to localhost for local testing:
 ```
const ws = new WebSocket("ws://localhost:8080/ws");
 ```
* Open index.html in your browser (or use VS Code Live Server).
## Usage

1. Open the application in your PC/laptop browser.
2. Ensure the connection indicator in the top right says "Live AI Connection".
3. Begin typing in the main text area (e.g., "The learned counsel for").
4. Gray ghost text will appear ahead of your cursor.
5. Press TAB to accept the suggestion and integrate it into your document.
