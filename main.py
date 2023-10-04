import pywhatkit
import keyboard
import time
from datetime import datetime

#definir contatos
contatos = ['+5511953212795']

#intervalo
while len(contatos) >=1:
    #enviar msg
    pywhatkit.sendwhatmsg(contatos[0], 'Eaii, tudo bem? Thiago aqui, do time do Filipe Furtado ! Vi que preencheu o formulário do parcelamento no boleto da mentoria on-line . Estou entrando em contato para saber o motivo de não ter avançado o processo. Qual o melhor horário para te ligar ??', datetime.now().hour,datetime.now().minute + 1)
    del contatos[0]
    time.sleep(10)
    keyboard.press_and_release('ctrl + w')
