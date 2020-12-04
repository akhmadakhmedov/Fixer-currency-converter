from flask import Flask, render_template, request
import requests

api_key = "758e4be9109b4ab5a67204e3aba91353"
url = "http://data.fixer.io/api/latest?access_key=" + api_key

app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])

def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")
        amount = request.form.get("amount")
        response = requests.get(url)
        infos = response.json()
        firstValue = infos["rates"][firstCurrency]
        secondValue = infos["rates"][secondCurrency]
        result = (secondValue/firstValue) *float(amount)

        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        return render_template("index.html", info = currencyInfo)

    return render_template("index.html")








if __name__ == "__main__":
    app.run(debug=True)