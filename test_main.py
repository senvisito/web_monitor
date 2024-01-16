import pytest
import monitor

def test_check_port_status():
    assert monitor.check_port_status("http://www.example.com/") is not None

def test_check_service_response():
    assert monitor.check_service_response("http://www.example.com/") is not None




