from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import onnxruntime as ort
from tokenizers import Tokenizer
import numpy as np

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

tokenizer = Tokenizer.from_file("legal_tokenizer.json")
session = ort.InferenceSession("legal_drafting_model.onnx")

SEQ_LEN = 15
PAD_ID = tokenizer.token_to_id("[PAD]")

@app.get("/")
async def get():
    with open("static/index.html", "r") as f:
        return HTMLResponse(f.read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            text = await websocket.receive_text()
            if not text.strip():
                await websocket.send_text("")
                continue
                
            # Tokenize the current text typed by the user
            encoded = tokenizer.encode(text).ids
            
            # Pad or truncate to strictly 15 tokens for the sliding window
            if len(encoded) < SEQ_LEN:
                input_ids = ([PAD_ID] * (SEQ_LEN - len(encoded))) + encoded
            else:
                input_ids = encoded[-SEQ_LEN:]
                
            # Run fast CPU inference via ONNX
            input_tensor = np.array([input_ids], dtype=np.int64)
            outputs = session.run(["logits", "attention_weights"], {"input_sequence": input_tensor})
            
            # Extract the highest probability word ID and decode it
            logits = outputs[0][0]
            predicted_id = np.argmax(logits)
            predicted_word = tokenizer.decode([predicted_id])
            
            await websocket.send_text(predicted_word)
            
    except WebSocketDisconnect:
        print("Client disconnected")