from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# Criando o diretório 'templates' e adicionando o arquivo HTML
import os
os.makedirs('templates', exist_ok=True)
html_content = """
<!DOCTYPE html>
<html lang=\"pt-br\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Para Minha Namorada</title>
    <style>
        body {
            background-color: pink;
            text-align: center;
            font-family: Arial, sans-serif;
            overflow: hidden;
        }
        h1 {
            color: red;
            font-size: 2em;
            margin-top: 20px;
        }
        img {
            width: 300px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
        }
        .heart {
            position: absolute;
            width: 20px;
            height: 20px;
            background-color: red;
            clip-path: polygon(50% 0%, 100% 35%, 80% 100%, 50% 80%, 20% 100%, 0% 35%);
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <h1>Eu te amo demais! ❤️</h1>
    <img src=\"/static/foto.jpg\" alt=\"Nossa foto juntos\">
    <script>
        function createHeart() {
            const heart = document.createElement('div');
            heart.classList.add('heart');
            heart.style.left = Math.random() * window.innerWidth + 'px';
            heart.style.top = '-20px';
            heart.style.animation = `fall ${Math.random() * 3 + 2}s linear infinite`;
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 3000);
        }
        setInterval(createHeart, 300);
    </script>
</body>
</html>
"""
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
