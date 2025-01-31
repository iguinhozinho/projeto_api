<<<<<<< HEAD
=======

>>>>>>> 5d56f8762c88caa38e31df2a32f2f84b46644a71
# Validação de CEP e CPF

Este projeto é uma aplicação web simples que permite a busca de informações de endereço a partir de um CEP e a validação de um CPF. Utilizamos uma API pública (ViaCEP) para buscar dados de endereço e implementamos uma validação básica de CPF. O projeto foi desenvolvido utilizando **Flask**, **Python**, e **Bootstrap** para o frontend, com suporte para APIs REST.

## Captura de Tela

![Captura de Tela](https://github.com/user-attachments/assets/e02ac965-39fa-4d9e-b3ed-990583d00505)

## Funcionalidades

1. **Busca de endereço por CEP**: Ao inserir um CEP válido, a aplicação consulta a API ViaCEP e retorna informações como logradouro, bairro, cidade e estado.
2. **Validação de CPF**: O CPF inserido é validado conforme regras simples de verificação. A validação retorna se o CPF é válido ou inválido.

## Tecnologias Utilizadas

### Linguagens e Frameworks

- **Python**: Linguagem principal utilizada no backend.
- **Flask**: Framework web em Python usado para criar as rotas e processar os formulários.
- **HTML/CSS**: Linguagens utilizadas para estruturar e estilizar a interface da aplicação.
- **Bootstrap**: Biblioteca de CSS para estilização e responsividade da interface.
<<<<<<< HEAD
- **Font Awesome**: Biblioteca de ícones utilizada para melhorar a interface do usuário.
=======
>>>>>>> 5d56f8762c88caa38e31df2a32f2f84b46644a71

### APIs Utilizadas

- **ViaCEP API**: Usada para buscar informações de endereço a partir de um CEP. A API retorna dados como logradouro, bairro, cidade e estado.
  - **Documentação**: [ViaCEP API](https://viacep.com.br)
<<<<<<< HEAD

=======
  
>>>>>>> 5d56f8762c88caa38e31df2a32f2f84b46644a71
### Bibliotecas Externas

- **Requests**: Utilizada para fazer requisições HTTP à API ViaCEP.
- **re (Expressões Regulares)**: Usada para manipulação e validação de dados de CPF.

## Como Rodar o Projeto

### Pré-requisitos

- **Python 3.x** instalado no sistema.
- **pip** (gerenciador de pacotes do Python).

### Passos para Executar

1. Clone o repositório:
<<<<<<< HEAD

=======
>>>>>>> 5d56f8762c88caa38e31df2a32f2f84b46644a71
   ```bash
   git clone https://github.com/iguinhozinho/projeto_api.git
   ```

2. Navegue até o diretório do projeto:
<<<<<<< HEAD

=======
>>>>>>> 5d56f8762c88caa38e31df2a32f2f84b46644a71
   ```bash
   cd nome-do-projeto
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
<<<<<<< HEAD

=======
>>>>>>> 5d56f8762c88caa38e31df2a32f2f84b46644a71
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

4. Instale as dependências:
<<<<<<< HEAD

=======
>>>>>>> 5d56f8762c88caa38e31df2a32f2f84b46644a71
   ```bash
   pip install -r requirements.txt
   ```

5. Execute a aplicação:
<<<<<<< HEAD

   ```bash
   python app.py
=======
   ```bash
   flask run
>>>>>>> 5d56f8762c88caa38e31df2a32f2f84b46644a71
   ```

6. Acesse o projeto no navegador em `http://127.0.0.1:5000/`.

## Estrutura do Projeto

```bash
.
├── app.py                 # Arquivo principal do Flask com as rotas
<<<<<<< HEAD
├── static/               # Arquivos estáticos
│   └── css/             # Estilos CSS
│       └── style.css    # Arquivo CSS principal
├── templates/           # Templates HTML
│   └── index.html      # Página HTML principal
├── README.md           # Este arquivo
├── requirements.txt    # Dependências do Python
└── .gitignore         # Arquivos a serem ignorados no Git
=======
├── templates
│   └── index.html         # Página HTML principal
├── static
│   └── ...                # Arquivos de estilo ou JavaScript (se necessário)
├── README.md              # Este arquivo
├── requirements.txt       # Dependências do Python
└── .gitignore             # Arquivos a serem ignorados no Git
>>>>>>> 5d56f8762c88caa38e31df2a32f2f84b46644a71
```

## Endpoints

### 1. Página inicial (`/`)

- Exibe o formulário para inserir o CEP e CPF.
<<<<<<< HEAD

=======
  
>>>>>>> 5d56f8762c88caa38e31df2a32f2f84b46644a71
### 2. Rota de busca (`/buscar`)

- Processa os dados do formulário e exibe os resultados da busca de endereço e validação de CPF.

## Como Contribuir

1. Faça um fork do projeto.
2. Crie uma nova branch:
   ```bash
   git checkout -b feature/nova-feature
   ```
3. Faça suas alterações e commite:
   ```bash
   git commit -m "Adiciona nova feature"
   ```
4. Envie para o seu fork:
   ```bash
   git push origin feature/nova-feature
   ```
5. Abra um Pull Request para o repositório original.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
