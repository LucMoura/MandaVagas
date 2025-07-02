import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

URL = 'https://api.remotar.com.br/jobs?search=desenvolvedor%20junior'
TOKEN = os.getenv('API_KEY')
CHAT_ID = os.getenv('USER_ID')

vagas_enviadas = set()

def buscar_vagas():
    global vagas_enviadas
    try:
        response = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        data = response.json()

        vagas = data.get('data', [])

        if vagas:
            for vaga in vagas:
                vaga_id = vaga.get('id')
                if vaga_id not in vagas_enviadas:
                    titulo = vaga.get('title', 'Título não disponível')
                    link = vaga.get('externalLink', 'Link não disponível')
                    mensagem = f"<b>{titulo}</b>\n{link}"

                    enviar_telegram(mensagem)
                    vagas_enviadas.add(vaga_id)
                    print(f'Vaga enviada: {titulo}')
                else:
                    print('Vaga já enviada.')
        else:
            print('Nenhuma vaga encontrada.')

    except Exception as e:
        print(f'Erro ao buscar vagas: {e}')


def enviar_telegram(mensagem):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': mensagem,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print('Vaga enviada com sucesso!')
    else:
        print(f'Erro ao enviar mensagem: {response.text}')


if __name__ == '__main__':
    while True:
        buscar_vagas()
        time.sleep(300)
