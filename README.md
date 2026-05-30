# health-prediction-app
AI-powered Health Prediction Application using Flask, SQLite and Python
# Health Prediction App

An AI-powered Health Prediction Application built using **Python, Flask, SQLite, HTML, CSS, and Bootstrap**.

The application collects patient blood test details and predicts possible health risks based on glucose, haemoglobin, and cholesterol values.

---

## Features

### CRUD Operations

* Create patient records
* Read/View patient records
* Update patient details
* Delete patient details

### Health Prediction

The application predicts possible health risks using patient blood test values:

* Glucose
* Haemoglobin
* Cholesterol

Generated health remarks include:

* Healthy
* Possible Diabetes Risk
* Low Haemoglobin (Anemia Risk)
* High Cholesterol Risk

### Validation

* Valid email input
* Date of Birth cannot be a future date
* Numeric input validation for blood test values

### User Interface

* Attractive responsive UI
* Bootstrap-based design
* Animated dashboard layout
* Patient records table
* Edit and delete actions

### Persistent Storage

Patient data is stored using **SQLite database**.

---

## Tech Stack

### Frontend

* HTML
* CSS
* Bootstrap

### Backend

* Python
* Flask

### Database

* SQLite

---

## Project Structure

```text
health_prediction_app/
│── app.py
│── database.db
│── requirements.txt
│── README.md
│
├── models/
│   └── predictor.py
│
├── templates/
│   ├── index.html
│   └── edit.html
│
└── static/
    └── style.css
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/Anuvarshaj/health-prediction-app.git
```

### 2. Navigate to Project Folder

```bash
cd health_prediction_app
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

If `pip` does not work:

```bash
python3 -m pip install -r requirements.txt
```

### 4. Run Application

```bash
python3 app.py
```

---

## Application Features

* Add patient details
* Auto age calculation from Date of Birth
* Automatic health prediction remarks
* Edit patient details
* Delete patient records
* Store data in SQLite database

---

## CRUD Operations

| Operation | Description              |
| --------- | ------------------------ |
| Create    | Add patient record       |
| Read      | View patient record      |
| Update    | Edit patient information |
| Delete    | Remove patient record    |

---

## Sample Prediction Logic

* Glucose > 140 → Possible Diabetes Risk
* Haemoglobin < 12 → Low Haemoglobin (Anemia Risk)
* Cholesterol > 200 → High Cholesterol Risk

---

## Future Improvements

* External AI/ML Health API integration
* Search patient records
* Charts and analytics dashboard
* Export reports

---

## Author

**Anu Varsha J**
