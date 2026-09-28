from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    bmi = None
    result = None

    if request.method == "POST":

        weight = float(request.form["weight"])
        height = float(request.form["height"])

        # Convert height from centimeters to meters
        height_m = height / 100

        # BMI formula
        bmi = weight / (height_m * height_m)

        # BMI category
        if bmi < 18.5:
            result = "Underweight"
        elif bmi < 25:
            result = "Normal Weight"
        elif bmi < 30:
            result = "Overweight"
        else:
            result = "Obesity"

    return render_template(
        "index.html",
        bmi=bmi,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)