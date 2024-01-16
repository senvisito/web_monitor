import os
import asyncio
import monitor

TOKEN_TELEGRAM_BOT = os.getenv('6972501031:AAFi8k3AqAU0mjFiFg7CrreH5XPwZPAFabM')
id_chat = os.getenv('6424284777')
URL = "http://scanme.nmap.org/"

async def main():
        try:
            if not monitor.check_port_status(URL):
                mensaje = "El puerto del servicio web no responde o está cerrado."
            elif not monitor.check_service_response(URL):
                mensaje = "El puerto responde pero el servicio web no está activo."
            else:
                mensaje = "El servicio web está activo y respondiendo."
            # Llamada a función para enviar mensaje a Telegram (Asumiendo que esta función existe en monitor.py)
            await monitor.enviar_mensaje_telegram(TOKEN_TELEGRAM_BOT, id_chat, mensaje)
        except Exception as e:
            print(f"Error: {e}")
        

if __name__ == '__main__':
    asyncio.run(main())
