#Biblioteca para fazermos a leitura dos dados
import pandas as pd
#biblioteca para interação web
from selenium import webdriver
#biblioteca para pausas
import time
#importação para ID's na página web serem encontrados
from selenium.webdriver.common.by import By
#biblioteca para manipulação do teclado
import pyautogui
#importaremos a biblioteca para termos uma interface em nosso app
import tkinter as tk
from tkinter import*


def send_date():
        
    contact = entry_contact.get()
    message = entry_message.get("1.0", tk.END)
    times = int(entry_times.get())
    interval = int(entry_interval.get())
    #instanciamos o driver do nosso navegador 
    browser = webdriver.Chrome()
    #fazemos solicitação para uma determinada URL
    browser.get("https://web.whatsapp.com/")
    #esperar entrarmos no WhatsApp web
    while len(browser.find_elements(By.ID,"side")) < 1:
        time.sleep(2)

    browser.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p').send_keys(contact)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(int(interval))
    count = 0

    while count < int(times):
        pyautogui.write(message)
        pyautogui.press('enter')
        print(count)
        count = count + 1
        time.sleep(1)
    stop()

def stop():
    window.destroy()

window = tk.Tk()
window.title("Informações Necessárias")

label_contact = tk.Label(window, text="Nome do Contato: ")
label_contact.pack()

entry_contact = tk.Entry(window)
entry_contact.pack()

label_message = tk.Label(window, text="Mensagem: ")
label_message.pack()

entry_message = tk.Text(window, height=5, width=40)
entry_message.pack()

label_times = tk.Label(window, text="Número de envios: ")
label_times.pack()

entry_times = tk.Entry(window)
entry_times.pack()

label_interval = tk.Label(window, text="Tempo de Espera: ")
label_interval.pack()

entry_interval = tk.Entry(window)
entry_interval.pack()

button_send = tk.Button(window, text="Enviar", command=send_date)
button_send.pack()

button_stop = tk.Button(window, text="Parar Programa", command=stop)
button_stop.pack()

window.mainloop()