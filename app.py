from flask import Flask, request, render_template_string
from markupsafe import escape  # Importando escape para sanitização

app = Flask(__name__)

# Página inicial com um formulário de pesquisa
@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Laboratório Reflected XSS</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                background-color: #f3f4f6;
            }
            .container {
                max-width: 600px;
                padding: 20px;
                background-color: #ffffff;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                text-align: center;
            }
            h1 {
                color: #333;
            }
            label, input {
                font-size: 1em;
                margin: 10px 0;
            }
            input[type="text"] {
                width: 80%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                margin-bottom: 20px;
            }
            button {
                background-color: #007bff;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Laboratório Reflected XSS</h1>
            <form action="/search" method="get">
                <label for="query">Pesquise por algo:</label><br>
                <input type="text" id="query" name="query" placeholder="Digite um termo...">
                <button type="submit">Pesquisar</button>
            </form>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

# Página de pesquisa vulnerável a Reflected XSS
@app.route('/search')
def search():
    query = request.args.get('query', '')

    html = f'''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Resultados da Pesquisa</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                background-color: #f3f4f6;
            }}
            .container {{
                max-width: 600px;
                padding: 20px;
                background-color: #ffffff;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                text-align: center;
            }}
            h2 {{
                color: #333;
            }}
            p {{
                font-size: 1em;
                color: #555;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Resultados para: {query}</h2>
            <p>Você pesquisou por "<strong>{query}</strong>"</p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True, port=5030)
