from flask import Flask, render_template, request, flash
import requests
import re
from typing import Optional, Dict, Any

app = Flask(__name__)
app.secret_key = 'your-secret-key' 

class CEPValidator:
    @staticmethod
    def format_cep(cep: str) -> str:
        """Remove non-numeric characters from CEP."""
        return re.sub(r'\D', '', cep)

    @staticmethod
    def is_valid(cep: str) -> bool:
        """Check if CEP is valid (8 digits)."""
        cep = CEPValidator.format_cep(cep)
        return len(cep) == 8 and cep.isdigit()

class CPFValidator:
    @staticmethod
    def format_cpf(cpf: str) -> str:
        """Remove non-numeric characters from CPF."""
        return re.sub(r'\D', '', cpf)

    @staticmethod
    def is_valid(cpf: str) -> bool:
        """Validate CPF using proper algorithm."""
        cpf = CPFValidator.format_cpf(cpf)
        
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        sum_of_products = sum(
            int(cpf[i]) * (10 - i) for i in range(9)
        )
        expected_digit = (sum_of_products * 10 % 11) % 10
        if int(cpf[9]) != expected_digit:
            return False

        sum_of_products = sum(
            int(cpf[i]) * (11 - i) for i in range(10)
        )
        expected_digit = (sum_of_products * 10 % 11) % 10
        return int(cpf[10]) == expected_digit

class ViaCEPAPI:
    BASE_URL = 'https://viacep.com.br/ws'

    @staticmethod
    def fetch_address(cep: str) -> Optional[Dict[str, Any]]:
        """Fetch address information from ViaCEP API."""
        try:
            response = requests.get(
                f'{ViaCEPAPI.BASE_URL}/{CEPValidator.format_cep(cep)}/json',
                timeout=5
            )
            response.raise_for_status()
            data = response.json()
            
            if 'erro' in data:
                return None
                
            return data
        except (requests.RequestException, ValueError):
            return None

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html', endereco=None, cpf_valido=None)

@app.route('/buscar', methods=['POST'])
def buscar():
    """Handle form submission and validate CEP/CPF."""
    cep = request.form.get('cep', '')
    cpf = request.form.get('cpf', '')

    if not CEPValidator.is_valid(cep):
        flash('CEP inválido. Digite um CEP com 8 dígitos.', 'error')
        return render_template('index.html', endereco=None, cpf_valido=None)

    endereco = ViaCEPAPI.fetch_address(cep)
    if not endereco:
        flash('Não foi possível encontrar o endereço para o CEP informado.', 'error')

    cpf_valido = CPFValidator.is_valid(cpf)

    return render_template(
        'index.html',
        endereco=endereco,
        cpf_valido=cpf_valido
    )

if __name__ == '__main__':
    app.run(debug=True)