import pytest
import monitor
import asyncio
import pytest_asyncio

def test_check_port_status():
    assert monitor.check_port_status("http://www.example.com/") is not None

def test_check_service_response():
    assert monitor.check_service_response("http://www.example.com/") is not None
    
def test_check_service_response_success():
    assert monitor.check_service_response("http://www.example.com/") == True
def test_check_service_response_failure():
    assert monitor.check_service_response("http://invalid-url.com/") == False


# Test for check_http_status function
def test_check_http_status_success():
    assert monitor.check_http_status("http://www.example.com/") == True

def test_check_http_status_failure():
    assert monitor.check_http_status("http://invalid-url.com/") == False


@pytest.mark.asyncio
async def test_enviar_mensaje_telegram():
    token = "6972501031:AAFi8k3AqAU0mjFiFg7CrreH5XPwZPAFabM"
    chat_id = "6424284777"
    mensaje = "Prueba de funcionamiento"
    result = await monitor.enviar_mensaje_telegram(token, chat_id, mensaje)
    assert result is None
