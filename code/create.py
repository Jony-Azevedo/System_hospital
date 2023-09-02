from urllib import request
from conecta import obter_conexao
from flask import Flask, jsonify

app = Flask(__name__)


# Rota para receber os dados do formulário
@app.route('/processar_formulario', methods=['POST'])
def processar_formulario():
    try:
        # Recupere os dados do formulário
        data = request.get_json()

        # Obtenha uma conexão com o banco de dados usando a função de 'conecta.py'
        conn = obter_conexao()
        cursor = conn.cursor()

        # Insira os dados no banco de dados
        query = "INSERT INTO paciente (id_paciente, nome, data_nascimento, endereco) VALUES (%s, %s, %s, %s)"
        values = (data['id'], data['name'], data['nasc'], data['endereco'])
        cursor.execute(query, values)

        conn.commit()
        conn.close()

        return jsonify({"message": "Dados inseridos com sucesso no banco de dados!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
