from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        name = request.form.get('username')
        if name.lower() == 'rashed':
            message = "خوش آمدی راشد!"
        else:
            message = "بای بای!"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
