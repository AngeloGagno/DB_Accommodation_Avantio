# API de Acomodações - Integração com Banco de Dados

Este projeto realiza a integração com a API de acomodações da Avantio para consumir informações de acomodações e armazená-las em um banco de dados. Ele automatiza o processo de coleta e organização de dados, facilitando o acesso e gerenciamento das informações.

## Funcionalidades

- Consumo de dados da API de acomodações.
- Processamento e validação dos dados recebidos.
- Armazenamento das informações em um banco de dados.

## Requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados:

- [Python 3.8+](https://www.python.org/downloads/)
- Banco de dados de sua preferência (PostgreSQL, SQLite, MySQL)
- Possuir Docker na máquina

## Configuração do Ambiente

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/AngeloGagno/DB_Accommodation_Avantio.git
    ```

2. **Criar a pasta .env, enviar a URL de conexao com o banco e o API key da avantio**
    ```bash
    touch .env 
    ```
3. **Executar o docker compose**
    ```bash
   docker-compose up --build
    ```