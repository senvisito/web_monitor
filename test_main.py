import pytest
import monitor

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


import pytest_asyncio

# Test for enviar_mensaje_telegram function
@pytest_asyncio.fixture
async def test_enviar_mensaje_telegram():
    # Using dummy token and chat_id for testing purposes
    token = "123456789:ABCDEFGHIJKLMNO"
    chat_id = "123456789"
    mensaje = "Test message"
    result = await monitor.enviar_mensaje_telegram(token, chat_id, mensaje)
    assert result is None


