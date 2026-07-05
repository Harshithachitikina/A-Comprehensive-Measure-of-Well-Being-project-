from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Current folder (Flask folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Flask application
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# Load trained model
model_path = os.path.join(BASE_DIR, "HDI.pkl")

with open(model_path, "rb") as file:
    model = pickle.load(file)


# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("home.html")


# ---------------- PREDICTION PAGE ----------------
@app.route("/prediction")
def prediction():
    return render_template("indexnew.html")


# ---------------- PREDICT ----------------
@app.route("/predict", methods=["POST"])
def predict():

    try:
        life_expectancy = float(request.form["life_expectancy"])
        mean_schooling = float(request.form["mean_schooling"])
        expected_schooling = float(request.form["expected_schooling"])
        gni = float(request.form["gni"])

        features = np.array([[

            life_expectancy,
            mean_schooling,
            expected_schooling,
            gni

        ]])

        prediction = model.predict(features)

        result = round(float(prediction[0]), 3)

        return render_template(

            "result.html",

            prediction=result

        )

    except Exception as e:

        return render_template(

            "result.html",

            prediction=f"Error : {e}"

        )


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)