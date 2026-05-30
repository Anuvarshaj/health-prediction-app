from flask import Flask, render_template, request, redirect, flash
import sqlite3
from datetime import datetime
from models.predictor import predict_health

app = Flask(__name__)
app.secret_key = "health_app_secret"


# --------------------------
# Database Connection
# --------------------------
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# --------------------------
# Calculate Age
# --------------------------
def calculate_age(dob):

    birth_date = datetime.strptime(
        dob,
        "%Y-%m-%d"
    )

    today = datetime.today()

    age = (
        today.year
        - birth_date.year
        - (
            (today.month, today.day)
            <
            (birth_date.month, birth_date.day)
        )
    )

    return age


# --------------------------
# Initialize Database
# --------------------------
def init_db():

    conn = get_db_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS patients (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        full_name TEXT NOT NULL,
        dob TEXT NOT NULL,
        age INTEGER,

        email TEXT NOT NULL,

        glucose REAL,
        haemoglobin REAL,
        cholesterol REAL,

        remarks TEXT
    )
    """)

    conn.commit()
    conn.close()


# --------------------------
# HOME PAGE
# --------------------------
@app.route("/", methods=["GET", "POST"])
def home():

    conn = get_db_connection()

    if request.method == "POST":

        full_name = request.form["full_name"]
        dob = request.form["dob"]
        email = request.form["email"]

        glucose = float(request.form["glucose"])
        haemoglobin = float(
            request.form["haemoglobin"]
        )
        cholesterol = float(
            request.form["cholesterol"]
        )

        # Validation
        birth_date = datetime.strptime(
            dob,
            "%Y-%m-%d"
        )

        if birth_date > datetime.today():
            flash(
                "DOB cannot be future date!"
            )
            return redirect("/")

        age = calculate_age(dob)

        remarks = predict_health(
            glucose,
            haemoglobin,
            cholesterol
        )

        conn.execute("""
        INSERT INTO patients(
            full_name,
            dob,
            age,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            full_name,
            dob,
            age,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        ))

        conn.commit()
        conn.close()

        flash(
            "Patient Added Successfully!"
        )

        return redirect("/")

    patients = conn.execute(
        "SELECT * FROM patients"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        patients=patients
    )


# --------------------------
# EDIT PATIENT
# --------------------------
@app.route("/edit/<int:id>",
           methods=["GET", "POST"])
def edit_patient(id):

    conn = get_db_connection()

    patient = conn.execute(
        "SELECT * FROM patients WHERE id=?",
        (id,)
    ).fetchone()

    if request.method == "POST":

        full_name = request.form["full_name"]
        dob = request.form["dob"]
        email = request.form["email"]

        glucose = float(
            request.form["glucose"]
        )

        haemoglobin = float(
            request.form["haemoglobin"]
        )

        cholesterol = float(
            request.form["cholesterol"]
        )

        age = calculate_age(dob)

        remarks = predict_health(
            glucose,
            haemoglobin,
            cholesterol
        )

        conn.execute("""
        UPDATE patients
        SET
            full_name=?,
            dob=?,
            age=?,
            email=?,
            glucose=?,
            haemoglobin=?,
            cholesterol=?,
            remarks=?
        WHERE id=?
        """, (
            full_name,
            dob,
            age,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks,
            id
        ))

        conn.commit()
        conn.close()

        flash(
            "Patient Updated!"
        )

        return redirect("/")

    return render_template(
        "edit.html",
        patient=patient
    )


# --------------------------
# DELETE PATIENT
# --------------------------
@app.route("/delete/<int:id>")
def delete_patient(id):

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM patients WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    flash("Patient Deleted!")

    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)