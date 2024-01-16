import pytest
import monitor

def test_check_port_status():
    # Suponiendo que esta función devuelve True/False
    assert monitor.check_port_status("http://www.example.com/") is not None

def test_check_service_response():
    # Suponiendo que esta función devuelve True/False
    assert monitor.check_service_response("http://www.example.com/") is not None

# Aquí puedes agregar más pruebas para las funciones específicas en monitor.py



