# Patient Data AI App

Simple AI-powered Python application that reads patient data from a JSON file and provides AI-based recommendations.

## Features

* View patient details
* Dropdown patient selection
* AI medical question assistant
* No API key required
* Uses local Flan-T5 model
* Updates patient conditions

## Tech Stack

* Python
* Flask
* HuggingFace Transformers
* HTML

## Installation

Clone the repository

```
git clone https://github.com/yourusername/patient-ai-app
cd patient-ai-app
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
python app.py
```

Open browser

```
http://127.0.0.1:5000
```

## Example AI Question

```
Patient has diabetes. What should be done next?
Explain in three steps.
```

## Project Structure

```
patient-ai-app
 ├── app.py
 ├── patients.json
 ├── requirements.txt
 ├── templates
 │   └── index.html
 └── README.md
```

## Future Improvements

* Add Streamlit version
* Add patient search
* Add AI summarization
* Add database support
