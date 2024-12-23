from twilio.rest import Client
from datetime import datetime

# Configurações do Twilio (sugestão: armazene essas credenciais como variáveis de ambiente)
ACCOUNT_SID = 'AC759279**SECRET**f4f5b8e0cdfe7'
AUTH_TOKEN = '343c5d8051**SECRET**b79ffa27ff87c'
WHATSAPP_FROM = 'whatsapp:+14155238886'
WHATSAPP_TO = 'whatsapp:+55419598***2'

# Obter a data e hora atual
current_time = datetime.now().strftime("%d/%m/%Y")

# Função genérica para envio de mensagens
def send_whatsapp_message(body):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        from_=WHATSAPP_FROM,
        body=f'[{current_time}]: {body}',
        to=WHATSAPP_TO
    )
    print(f"Mensagem enviada com sucesso: SID {message.sid}")

# Funções específicas
def msg_ponto():
    send_whatsapp_message("Marcação de ponto realizada com sucesso.")

def start_process():
    send_whatsapp_message("Iniciando marcação automática.")

def msg_connect_vpn():
    send_whatsapp_message("VPN conectada.")

def msg_disconnect_vpn():
    send_whatsapp_message("VPN desconectada.")

def end_process():
    send_whatsapp_message("Processo concluído com êxito.")
