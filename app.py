from flask import Flask, jsonify

import service

app = Flask(__name__)


@app.route('/<numero_str>')
def main(numero_str):
    try:
        extenso = service.extenso(numero_str)
    except (ValueError,TypeError) as err:
        return jsonify({'error': err.args[0]}), 400

    return jsonify({'extenso': extenso})


if __name__ == "__main__":
    app.run()
