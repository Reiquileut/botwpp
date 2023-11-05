import pywhatkit
import time
from datetime import datetime, timedelta
import pandas as pd
import keyboard


# Função para calcular o próximo horário de envio
def get_next_send_time(current_time, interval):
    return current_time + timedelta(minutes=interval)


# Inicializar o horário de início para a primeira mensagem
initial_start_time = datetime.now() + timedelta(minutes=2)
interval_between_messages = 1  # Definir um intervalo entre as mensagens em minutos

# Carregar o arquivo .xlsx usando pandas
df = pd.read_excel(r'C:\Users\thiago\Desktop\botwpp\src\Formulário Live.xlsx')

# Iterar sobre os contatos no DataFrame
for i, row in df.iterrows():
    contact_number = str(row['number'])  # Assegure-se de que o número de telefone é uma string
    # Supondo que todos os números devem começar com '+55'
    if not contact_number.startswith('+'):
        contact_number = '+55' + contact_number
    print('Iniciando envio para:', contact_number)

    # Defina a mensagem que você quer enviar
    message = 'Olá, meu amigo!\nLembrando daquela promessa que fiz a você? Pois é, chegou a hora de cumprir!\nPara potencializar ainda mais o seu sucesso nos investimentos, estou disponibilizando a *planilha de gerenciamento de risco* que vai revolucionar a sua gestão estratégica e de capital. Prepare-se para alcançar novos patamares!\nMas isso não é tudo. Quero te convidar para uma experiência verdadeiramente transformadora. Uma *imersão intensiva*, onde *compartilharei todos os meus segredos operacionais e minha leitura de mercado* afiada.\nSerão *três dias repletos de conteúdo prático*, insights valiosos e, é claro, muita prática para solidificar seu conhecimento.\nSe você está ansioso para dar um passo à frente em sua jornada financeira, essa é a sua chance. Quer saber mais detalhes, como datas e investimento? É só me enviar uma mensagem. Estou aqui para te guiar e esclarecer todas as suas dúvidas.\nNão perca essa oportunidade única! Vamos juntos em busca do sucesso e crescimento. Até breve, meu amigo!\n *LINK DA PLANILHA:* https://docs.google.com/spreadsheets/d/1aNfs6RJeYhpRPjBxE3vsT9ihV3JyLvoM/edit?usp=drive_link&ouid=113966064698480964309&rtpof=true&sd=true\n *LINK DA AULA:* https://www.youtube.com/live/1gjum_3V75c?si=YrgbKp3eHCWvIMx9  '

    # Calcular o horário de envio para este contato
    current_time = datetime.now()
    if current_time < initial_start_time:
        send_time = initial_start_time
    else:
        send_time = get_next_send_time(current_time, interval_between_messages)

    # Enviar a mensagem
    pywhatkit.sendwhatmsg(contact_number, message, send_time.hour, send_time.minute)

    # Aguardar a mensagem ser enviada e o WhatsApp Web ser fechado
    time_to_wait = (send_time - datetime.now()).total_seconds() + 20  # Adiciona uma margem de segurança
    time.sleep(time_to_wait)

    print('Mensagem enviada para:', contact_number)
    keyboard.send('ctrl+w')
