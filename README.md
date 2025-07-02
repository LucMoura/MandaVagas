# MandaVagas

Projeto em Python para buscar vagas de emprego na API Remotar e enviar notificações via Telegram automaticamente.

## Funcionalidades

- Busca vagas de desenvolvedor júnior na API Remotar.
- Envia as vagas encontradas para um chat do Telegram usando bot.
- Executa em loop para monitorar novas vagas periodicamente.

## Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/LucMoura/MandaVagas.git
   cd MandaVagas
   
 2. Instale as dependências:
     ```bash
     pip install requests python-dotenv
     
 3. Configure as variáveis de ambiente criando um arquivo .env na raiz do projeto com:
     ```bash
     API_KEY=seu_token_do_telegram_bot
     USER_ID=seu_chat_id_no_telegram

 4. Execute o script:
    ```bash
    python nome_do_seu_arquivo.py

##  Atenção

- Verifique se o bot do Telegram está configurado corretamente e que o USER_ID corresponde ao chat onde deseja receber as mensagens.
- Ajuste o intervalo de busca de vagas conforme necessidade (no código está 20 segundos)

## Tecnologias usadas

- Python 3.x
- Requests
- API Remotar
- Telegram Bot API

<br><br><br>

Feito por Lucas Moura 🚗
