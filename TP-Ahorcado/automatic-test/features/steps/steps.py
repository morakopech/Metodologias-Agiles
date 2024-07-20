from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('launch chrome browser')
def launchBrowser(context):
    service = Service(r"C:\Users\juanc\Desktop\Metodologias Agiles\TPI\Metodologias-Agiles\TP-Ahorcado\automatic-test\features\steps\chromedriver.exe")
    context.driver = webdriver.Chrome(service=service)

@when('Ingreso a la pagina del juego')
def step_ingreso_pagina(context):
    context.driver.get("http://127.0.0.1:5000/")
    time.sleep(5)

@then('el usuario elige la dificultad "{nivel}"')
def step_impl(context, nivel):
    button = context.driver.find_element(By.XPATH, f"//*[@id='{nivel}']")
    button.click()
    time.sleep(5)

@then('el numero de intentos debe ser 7')
def numero_de_intentos(context):
    intentos = context.driver.find_element(By.ID, "intentos")
    texto_completo = intentos.text
    partes = texto_completo.split(':')
    texto = partes[0].strip()
    numero_intentos = int(partes[1].strip())
    assert numero_intentos == 7
    time.sleep(3)


@given('un juego de Ahorcado con la palabra "{palabra}", "{pista}"')
def inicio_juego_con_palabra(context, palabra, pista):
    service = Service(r"C:\Users\juanc\Desktop\Metodologias Agiles\TPI\Metodologias-Agiles\TP-Ahorcado\automatic-test\features\steps\chromedriver.exe")
    context.driver = webdriver.Chrome(service=service)
    context.driver.get(f"http://127.0.0.1:5000/inicio?palabra={palabra}&pista={pista}")
    time.sleep(5)

@when('valido la letra "{letra}"')
def ingreso_una_letra(context, letra):
    input_letra = context.driver.find_element(By.ID, "letra")
    submit_button = context.driver.find_element(By.XPATH, f"//*[@id='boton_intentar']")
    input_letra.clear()
    input_letra.send_keys("a")
    submit_button.click()
    time.sleep(2)

@then('la letra es correcta')
def letra_correcta(context):
    palabra_mostrada = context.driver.find_element(By.ID, "palabra_mostrada")
    texto_completo = palabra_mostrada.text
    partes = texto_completo.split(':')
    texto = partes[0].strip()
    palabra = partes[1].strip()
    assert palabra == 'a _ _ _ _ _ _ a'
    time.sleep(3)

@then('el numero de intentos restantes debe ser 7')
def numero_de_intentos2(context):
    intentos = context.driver.find_element(By.ID, "intentos")
    texto_completo = intentos.text
    partes = texto_completo.split(':')
    texto = partes[0].strip()
    numero_intentos = int(partes[1].strip())
    assert numero_intentos == 7
    time.sleep(3)

@then('la letra "{letra}" esta en la lista de letras usadas')
def letra_usada2(context,letra):
    letras_usadas = context.driver.find_element(By.ID, "letras_usadas")
    texto_completo = letras_usadas.text
    partes = texto_completo.split(':')
    texto = partes[0].strip()
    letra_usada = partes[1].strip()
    assert letra in letra_usada.split()
    time.sleep(3)


@given('un juego de Ahorcado con la palabra "{palabra}", "{pista}" para validar letra incorrecta')
def inicio_juego_con_palabra_2(context, palabra, pista):
    service = Service(r"C:\Users\juanc\Desktop\Metodologias Agiles\TPI\Metodologias-Agiles\TP-Ahorcado\automatic-test\features\steps\chromedriver.exe")
    context.driver = webdriver.Chrome(service=service)
    context.driver.get(f"http://127.0.0.1:5000/inicio?palabra={palabra}&pista={pista}")
    time.sleep(3)

@when('valido la letra "{letra}" incorrecta')
def ingreso_una_letra_In(context, letra):
    input_letra = context.driver.find_element(By.ID, "letra")
    submit_button = context.driver.find_element(By.XPATH, f"//*[@id='boton_intentar']")
    input_letra.clear()
    input_letra.send_keys(letra)
    submit_button.click()
    time.sleep(2)

@then('la letra es incorrecta')
def letra_incorrecta(context):
    palabra_mostrada = context.driver.find_element(By.ID, "palabra_mostrada")
    texto_completo = palabra_mostrada.text
    partes = texto_completo.split(':')
    texto = partes[0].strip()
    palabra = partes[1].strip()
    assert palabra == '_ _ _ _ _ _ _'
    time.sleep(3)

@then('el numero de intentos debe ser 6')
def numero_de_intentos(context):
    intentos = context.driver.find_element(By.ID, "intentos")
    texto_completo = intentos.text
    partes = texto_completo.split(':')
    texto = partes[0].strip()
    numero_intentos = int(partes[1].strip())
    assert numero_intentos == 6
    time.sleep(3)

@then('la letra "{letra}" esta en letras usadas')
def letra_usada(context,letra):
    letras_usadas = context.driver.find_element(By.ID, "letras_usadas")
    texto_completo = letras_usadas.text
    partes = texto_completo.split(':')
    texto = partes[0].strip()
    letra_usada = partes[1].strip()
    assert letra in letra_usada.split()
    time.sleep(3)

@given('un juego del Ahorcado con la palabra "{palabra}", "{pista}"')
def inicio_juego_con_palabra_2(context, palabra, pista):
    service = Service(r"C:\Users\juanc\Desktop\Metodologias Agiles\TPI\Metodologias-Agiles\TP-Ahorcado\automatic-test\features\steps\chromedriver.exe")
    context.driver = webdriver.Chrome(service=service)
    context.driver.get(f"http://127.0.0.1:5000/inicio?palabra={palabra}&pista={pista}")
    time.sleep(3)

@when('valido las letras "{letra1}" "{letra2}" "{letra3}" "{letra4}" "{letra5}" "{letra6}"')
def ingreso_una_letra_In(context, letra1, letra2 ,letra3 ,letra4 ,letra5 ,letra6 ):
    letras = [letra1, letra2, letra3, letra4, letra5, letra6]
    for letra in letras:
        input_letra = context.driver.find_element(By.ID, "letra")
        submit_button = context.driver.find_element(By.XPATH, f"//*[@id='boton_intentar']")
        input_letra.clear()
        input_letra.send_keys(letra)
        submit_button.click()
        time.sleep(1)
    time.sleep(2)

@then('gano la partida')
def ganar_partida(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "mensaje_final"))
    )
    frase_mostrada = context.driver.find_element(By.ID, "mensaje_final").text.strip()
    print(f"Mensaje mostrado: '{frase_mostrada}'")
    assert frase_mostrada == '¡Felicidades, has ganado!'
    time.sleep(3)