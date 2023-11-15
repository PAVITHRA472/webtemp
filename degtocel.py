from flask import Flask, render_template_string, request

app = Flask(__name__)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fahrenheit to Celsius Converter</title>
</head>
<body>
    <h1>Fahrenheit to Celsius Converter</h1>
    <form method="post">
        <label for="fahrenheit">Enter Fahrenheit temperature:</label>
        <input type="text" name="fahrenheit" required>
        <button type="submit">Convert</button>
    </form>
    
    {% if result %}
        <p>{{ result }} °C</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        try:
            fahrenheit = float(request.form['fahrenheit'])
            result = fahrenheit_to_celsius(fahrenheit)
        except ValueError:
            result = "Invalid input. Please enter a valid number."

    return render_template_string(template, result=result)

if __name__ == '__main__':
    app.run(debug=True)
