from flask import Flask, render_template, request
from markupsafe import Markup


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        
        # Simulação de vulnerabilidade XSS
        message = Markup(user_input)
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, port=5030)