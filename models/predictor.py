def predict_health(
    glucose,
    haemoglobin,
    cholesterol
):

    remarks = []

    if glucose > 140:
        remarks.append(
            "Possible Diabetes Risk"
        )

    if haemoglobin < 12:
        remarks.append(
            "Low Haemoglobin (Anemia Risk)"
        )

    if cholesterol > 200:
        remarks.append(
            "High Cholesterol Risk"
        )

    if len(remarks) == 0:
        return "Healthy"

    return ", ".join(remarks)