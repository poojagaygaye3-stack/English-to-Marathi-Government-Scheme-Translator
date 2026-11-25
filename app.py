from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = Flask(__name__)
CORS(app)

print("Loading model, please wait...")

MODEL_PATH = "./farmer_scheme_translation_model"
SRC_LANG = "eng_Latn"
TGT_LANG = "mar_Deva"
MAX_LEN = 128

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, src_lang=SRC_LANG)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH).to(device)

print("Model loaded successfully. Server starting...")

def translate(text):
    tokenizer.src_lang = SRC_LANG
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=MAX_LEN).to(device)
    forced_bos_token_id = tokenizer.convert_tokens_to_ids(TGT_LANG)
    generated = model.generate(
        **inputs,
        forced_bos_token_id=forced_bos_token_id,
        max_length=MAX_LEN,
        num_beams=2,
    )
    return tokenizer.batch_decode(generated, skip_special_tokens=True)[0]

@app.route("/translate", methods=["POST"])
def translate_endpoint():
    data = request.get_json()
    english_text = data.get("text", "")
    if not english_text.strip():
        return jsonify({"error": "No text provided"}), 400
    marathi_text = translate(english_text)
    return jsonify({"english": english_text, "marathi": marathi_text})

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "Server is running"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)