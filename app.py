from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/consultar_bcb', methods=['GET'])
def consultar_bcb():
    data_inicial = request.args.get('data_inicial')
    data_final = request.args.get('data_final')

    if not data_inicial or not data_final:
        return jsonify({"error": "Parâmetros data_inicial e data_final são obrigatórios"}), 400

    url_bcb = f"http://api.bcb.gov.br/dados/serie/bcdata.sgs.4189/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"
    
    try:
        response = requests.get(url_bcb)
        response.raise_for_status()
    except requests.RequestException as e:
        return jsonify({"error": f"Erro ao consultar API do BCB: {e}"}), 500

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
