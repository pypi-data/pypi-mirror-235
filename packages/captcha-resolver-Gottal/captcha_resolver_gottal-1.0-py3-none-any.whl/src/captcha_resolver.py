# region Importa as bibliotecas utilizadas
import os
import time
from os import path

import requests
import selenium.common.exceptions
import speech_recognition as sr
from pydub import AudioSegment
from selenium.webdriver.common.by import By
# endregion


# region Define as funções
def verifica_recaptcha(drive):
    # Troca para o frame do recaptcha
    iframe = drive.find_element(By.XPATH, '//*[@id="formulario"]/div[2]/div/div/div/div/iframe')
    drive.switch_to.frame(iframe)

    # Verifica se o recaptcha já foi verificado
    sts = drive.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span').get_attribute('aria-checked')
    drive.switch_to.default_content()

    return sts


def baixar_audio(drive, dest):
    url = drive.find_element(By.XPATH, '//*[@id="audio-source"]').get_attribute('src')

    # baixa o audio

    arquivo = requests.get(url)
    open('audio.mp3', 'wb').write(arquivo.content)

    src = path.join(os.getcwd(), 'audio.mp3')

    # Converte para .wav
    sound = AudioSegment.from_mp3(src)
    sound.export(dest, format="wav")


def transcreve(dest):
    conv = sr.Recognizer()

    # Transcreve o audio
    with sr.AudioFile(dest) as source:
        audio = conv.record(source)

    try:
        textos_captcha = conv.recognize_google(audio)
    except:
        print("O áudio não foi reconhecido tentando de novo.")
        textos_captcha = '.'

    return textos_captcha


def transcrever_audio(drive):
    dest = path.join(os.getcwd(), 'audio.wav')

    baixar_audio(drive, dest)
    texto_captcha = transcreve(dest)

    if texto_captcha == '.':
        i = 0
        while i < 5 and texto_captcha == '.':
            drive.find_element(By.XPATH, '//*[@id="recaptcha-reload-button"]').click()
            time.sleep(2)
            baixar_audio(drive, dest)
            texto_captcha = transcreve(dest)
            i += 1

        if texto_captcha == '.':
            os.remove(path.join(os.getcwd(), 'audio.mp3'))
            os.remove(path.join(os.getcwd(), 'audio.wav'))
            exit("O áudio não pôde ser transcrito.")
        else:
            os.remove(path.join(os.getcwd(), 'audio.mp3'))
            os.remove(path.join(os.getcwd(), 'audio.wav'))
    return texto_captcha
# endregion


# region Executa o código para a resolução do CAPTCHA
def captcha_solver(drive):
    # Clica no botão do reCAPTCHA
    drive.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]').click()
    time.sleep(2)

    # Verifica se o captcha já foi resolvido
    sts = verifica_recaptcha(drive)

    if sts == 'false':
        # troca para o frame do recaptcha
        iframe = drive.find_element(By.XPATH, '//iframe[@title="o desafio reCAPTCHA expira em dois minutos"]')
        drive.switch_to.frame(iframe)
        time.sleep(5)

        # Clica no botao de recaptcha de audio
        drive.find_element(By.ID, 'recaptcha-audio-button').click()
        time.sleep(2)

        # Clica no botão de reprodução de áudio
        try:
            drive.find_element(By.XPATH, '//*[@id=":2"]').click()
        except selenium.common.NoSuchElementException:
            drive.quit()

            exit("O reCAPTCHA bloqueou a requisição, troque de user agent, ou de ip.")
        # Transcreve o áudio
        texto_captcha = transcrever_audio(drive)
        time.sleep(5)

        # Insere o texto transcrito no fomrulario
        drive.find_element(By.XPATH, '//*[@id="audio-response"]').send_keys(texto_captcha)
        time.sleep(2)

        # Clica no botão de verificação
        drive.find_element(By.XPATH, '//*[@id="recaptcha-verify-button"]').click()
        drive.switch_to.default_content()
# endregion
