from flask import Flask, render_template, request, redirect, url_for
from model import predict_price
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('data.csv')
locations = df['location'].unique().tolist()
del df


@app.route("/", methods=["GET", "POST"])
def index():
    predicted_price = None
    if request.method == "POST":
        # Get input features from form
        try:
            bedrooms = float(request.form["bedrooms"])
            bathrooms = float(request.form["bathrooms"])
            sqft = float(request.form["sqft"])
            location = request.form["location"]
            # You can extend with more features as needed

            # Predict the house price
            predicted_price = predict_price(bedrooms, bathrooms, sqft, location)
        except Exception as e:
            print("Error: ", e)
    return render_template("index.html", predicted_price=predicted_price, locations=locations)


@app.route("/locations")
def get_locations():
    return {'locations': locations}


if __name__ == "__main__":
    app.run(debug=True)
