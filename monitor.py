import requests
from telegram import Bot
import time
import asyncio

def check_port_status(url):
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error en check_port_status: {e}")
        return False

def check_service_response(url):
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error en check_service_response: {e}")
        return False

def check_http_status(url):
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error en check_http_status: {e}")
        return False 

async def enviar_mensaje_telegram(token, chat_id, mensaje):
    try:
        bot = Bot(token=token)
        await bot.send_message(chat_id=chat_id, text=mensaje)
        print("Mensaje de Telegram enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar mensaje de Telegram: {e}")

    return None  # Devuelve un objeto None al finalizar la función