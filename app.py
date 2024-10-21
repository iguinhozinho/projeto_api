from flask import Flask, render_template, request
import requests
import re

app = Flask(__name__)

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    
    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * len(cpf):
        return False
    
    return True

@app.route('/')
def index():
    return render_template('index.html', endereco=None, cpf_valido=None)

@app.route('/buscar', methods=['POST'])
def buscar():
    cep = request.form['cep']
    cpf = request.form['cpf']
    
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json')
    endereco = response.json() if response.status_code == 200 else None
    
    cpf_valido = validar_cpf(cpf)
    
    return render_template('index.html', endereco=endereco, cpf_valido=cpf_valido)

if __name__ == '__main__':
    app.run(debug=True)