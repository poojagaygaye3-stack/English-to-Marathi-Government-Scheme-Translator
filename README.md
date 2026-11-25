# 🌾 English to Marathi Government Scheme Translator
## 📖 About the Project

The **English to Marathi Government Scheme Translator** is an AI-powered Natural Language Processing (NLP) application developed to translate English government scheme information into Marathi.

Many Indian government schemes provide important information about eligibility criteria, financial benefits, application procedures, and other services. However, language barriers can make this information difficult to understand for regional-language users.

This project aims to reduce that barrier by using Transformer-based machine learning models to generate Marathi translations of English text.

The application is developed using Python, Flask, Hugging Face Transformers, and PyTorch, with additional government scheme-related data to support its domain-specific focus.

**Project Objective:** To improve accessibility and understanding of Indian government scheme information through English-to-Marathi translation.

## ✨ Key Features

- 🌐 **English to Marathi Translation:** Converts English text into Marathi.
- 🤖 **AI-Powered NLP:** Uses Transformer-based sequence-to-sequence models.
- 🏛️ **Government Scheme Focus:** Designed around Indian government scheme-related information.
- 📚 **Custom Dataset:** Includes a custom Excel dataset named `farmer_scheme_data.xlsx`.
- ⚡ **Flask REST API:** Provides backend functionality for processing translation requests.
- 🔗 **CORS Integration:** Supports communication with a separately hosted frontend.
- 🇮🇳 **Regional Language Accessibility:** Helps Marathi-speaking users understand government-related information.
- 🔧 **Expandable Architecture:** Can be extended with additional schemes, datasets, and Indian languages.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Backend web framework |
| Flask-CORS | Cross-origin resource sharing |
| Hugging Face Transformers | NLP model and tokenizer |
| PyTorch | Deep learning framework |
| Pandas | Dataset processing |
| Excel | Custom dataset storage |
| NLP | Natural Language Processing |

## 🗂️ Project Structure

```text
English-to-Marathi-Government-Scheme-Translator/
│
├── app.py
│
├── farmer_scheme_data.xlsx
│
├── model/
│   ├── config.json
│   ├── model weights
│   ├── tokenizer files
│   └── other model configuration files
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

**Important:**

The `model/` folder is required for the Flask application to run if the application loads the model from a local directory.

Currently, the GitHub repository may contain only:

- `app.py`
- `farmer_scheme_data.xlsx`

However, these two files alone are not sufficient to run the complete application if the model files are missing.

Make sure to provide the required model weights, tokenizer files, and configuration files in the configured model directory.

If the model files are large, consider using Git LFS or Hugging Face Hub to host them.

## 📚 Dataset Information

This project uses government scheme-related information and custom data to support its domain-specific translation objective.

### 1. 🤗 Hugging Face Resources

Hugging Face provides pretrained Transformer models, tokenizers, and datasets that can be used for multilingual NLP applications.

**Platform:** [Hugging Face](https://huggingface.co/)

The selected model should support the English-to-Marathi translation task.

### 2. 📊 Custom Dataset – farmer_scheme_data.xlsx

The project includes a custom Excel dataset:

**File Name:** `farmer_scheme_data.xlsx`

**Dataset Focus:**
- Farmer-related government schemes.
- Agricultural scheme information.
- Government assistance and benefits.
- Scheme-related reference information.

The dataset supports the project's government-scheme domain focus.

### 3. 🏛️ Government Information Sources

The project references information from the following government portals:

**MahaDBT – Maharashtra Direct Benefit Transfer**

Website: https://mahadbt.maharashtra.gov.in/

Provides information about various Maharashtra government schemes, including agricultural assistance and other citizen-benefit programs.

**PM-KISAN – Pradhan Mantri Kisan Samman Nidhi**

Website: https://pmkisan.gov.in/

Provides information about the PM-KISAN scheme, which offers financial assistance to eligible farmer families.

*Note: These websites are reference sources. Their inclusion does not imply that all website content has been downloaded or used for model training.*

## 🤖 Model Configuration

The project uses Hugging Face Transformer architecture for sequence-to-sequence translation.

The main components include:

- **AutoTokenizer:** Converts input text into tokens that the model can understand.
- **AutoModelForSeq2SeqLM:** Loads the sequence-to-sequence translation model.
- **PyTorch:** Handles model execution and inference.

Example model-loading implementation:

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_PATH = "./model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)
```

The actual model path must match the configuration used in `app.py`.

The model files must be available locally or accessible through the configured Hugging Face model repository.

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### Step 2: Navigate to the Project Directory

```bash
cd your-repository-name
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install flask flask-cors transformers torch pandas openpyxl
```

Alternatively, install dependencies using:

```bash
pip install -r requirements.txt
```

### Step 5: Add the Model Folder

Ensure that the model folder contains all required model weights, tokenizer files, and configuration files.

The folder must be available at the path configured in `app.py`.

### Step 6: Run the Application

```bash
python app.py
```

The Flask server will start, and the application will be available at the local address displayed in your terminal.

## 🔌 API Documentation

The application uses Flask to provide backend translation functionality through HTTP requests.

The following is an example API structure. Update the endpoint and JSON field names if your actual `app.py` implementation uses different names.

### Translation Endpoint

**Method:** `POST`

**Example Endpoint:**

```http
http://127.0.0.1:5000/translate
```

### Request Body

```json
{
  "text": "The government provides financial assistance to eligible farmers."
}
```

### Example Response

```json
{
  "translation": "पात्र शेतकऱ्यांना सरकार आर्थिक सहाय्य प्रदान करते."
}
```

### Example cURL Request

```bash
curl -X POST http://127.0.0.1:5000/translate \
-H "Content-Type: application/json" \
-d "{\"text\":\"The government provides financial assistance to eligible farmers.\"}"
```

**API Workflow:**

1. Receives English text from the user.
2. Processes the request through Flask.
3. Tokenizes the input using the Hugging Face tokenizer.
4. Generates Marathi translation using the Transformer model.
5. Returns the translated output as a JSON response.

## 🔄 How It Works

The application follows a simple NLP-based translation workflow.

```text
       User Input
           |
           ▼
    English Text Input
           |
           ▼
      Flask Backend
           |
           ▼
   Hugging Face Tokenizer
           |
           ▼
    Transformer Model
           |
           ▼
    Marathi Translation
           |
           ▼
     API JSON Response
```

### Step-by-Step Process

**1. User Input**

The user provides English government scheme-related information.

**2. Request Processing**

Flask receives the input through an API request.

**3. Tokenization**

The Hugging Face tokenizer converts the input into numerical tokens.

**4. Model Inference**

The Transformer-based sequence-to-sequence model generates the Marathi translation.

**5. Output Generation**

The Flask backend returns the translated text to the user.

## 🚀 Future Enhancements

The project can be improved with the following features:

- 🎨 Develop a modern and responsive user interface.
- 📱 Add mobile-friendly translation support.
- 🏛️ Include more central and state government schemes.
- 📄 Support PDF and document translation.
- 🔍 Add government scheme search functionality.
- 🌐 Expand translation support to additional Indian languages.
- 🧠 Improve translation quality using domain-specific datasets.
- ☁️ Deploy the application on a cloud platform.
- 🔐 Implement better API security and input validation.
- 📊 Add translation evaluation and performance monitoring.

## ⚠️ Limitations and Responsible Use

- Machine-generated translations may contain grammatical or contextual errors.
- Translation accuracy depends on the selected model and its training data.
- Government scheme information may change over time.
- Users should verify important eligibility conditions, benefits, and application procedures through official government portals.
- This application is an informational translation tool and is not an official government service.
- It is not affiliated with MahaDBT, PM-KISAN, or any government department.
- Users should avoid submitting sensitive personal information unless appropriate privacy and security protections are implemented.

## 👩‍💻 Author

### Pooja Gaygaye

**MCA Student | Aspiring Software Developer | Python & NLP Enthusiast**

This project demonstrates practical implementation of:

- Python Programming
- Flask Backend Development
- Natural Language Processing
- Hugging Face Transformers
- PyTorch
- Dataset Management
- REST API Development

I developed this project with the objective of applying AI and NLP technologies to solve a real-world language accessibility problem.

---

<p align="center">
  🌾 <strong>Bridging the Language Gap Through Technology.</strong>
</p>

<p align="center">
  ⭐ If you find this project interesting, consider giving it a star on GitHub!
</p>
