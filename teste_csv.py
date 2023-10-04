import pywhatkit
import keyboard
import time
from datetime import datetime
import csv

contatos = []

# Abrir arquivo CSV
with open('csvplanilhaprovi.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for row in csv_reader:
        telefone = row[0]
        contatos.append(telefone)

# Enviar mensagens
while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0],
                          'Eaii, tudo bem? Thiago aqui, do time do Filipe Furtado ! Vi que preencheu o formulário do parcelamento no boleto da mentoria on-line . Estou entrando em contato para saber o motivo de não ter avançado o processo. Qual o melhor horário para te ligar ??',
                          datetime.now().hour, datetime.now().minute + 1)
    del contatos[0]
    time.sleep(10)
    keyboard.press_and_release('ctrl + w')

contatos = []
contatos.append(row[0])

print(contatos)
