# save this as app.py
from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/hola")
def hello():
    print(__name__)
    return "Hello, World!"

@app.route("/test")
def hello2():
    return "Hello World in Flask!"

if __name__ == '__main__':
    app.run()


@app.route("/saludar")
@app.route("/saludar/<hi>")
@app.route("/saludar/<hi>/<lang>")
def saludar(hi = "Ricardo", lang = "en"):
    return "Hello! " + hi + ' ' + lang


@app.route("/html")
@app.route("/html/<name>")
def html(name = 'Andres'):
    return '''
    <html>
        <body>
            <h1>
                This is html
            </h1>
            <p> Hola %s<p>
            <ul>
                <li>
                    <p> Primer item en la lista</p>
                </li>
                <li>
                    <p> Segundo item en la lista</p>
                </li>
                <li>
                    <p> Tercer item en la lista</p>
                </li>
            </ul>
        </body>
    </html>
    ''' %name

@app.route('/static_file')
def static_file():
    return "<img src='" + url_for("static", filename = "img/Zjpg.jpg") + "'>"

@app.route('/template')
@app.route('/template/<Tittle>')
def tempalte(title = 'Python'):
    return render_template('view.html', title = title)

if __name__ == '__main__':
    app.run()