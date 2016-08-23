from flask import Flask, Response


app = Flask(__name__)


@app.route('/')
def index():
    """
    Simple server for local testing purposes

    :return:
    """
    return Response("""
    <doctype html>
    <html>
    <head>
        <title>Test Shiva</title>
    </head>
    <body>
        <p>Heeeeeello</p>
        <script async src="http://127.0.0.1:3000/shiva.js"></script>
    </body>
    </html>
    """)


app.run(host='127.0.0.1', port=3030, debug=True)
