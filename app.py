from flask import Flask, jsonify

import service

app = Flask(__name__)


@app.route('/<numero>')
def main(numero):
    return jsonify({'extenso': service.extenso(int(numero))})


if __name__ == "__main__":
    app.run()
