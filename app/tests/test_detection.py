from app.detection.llm_detector import detect_sensitive_data

def test_detect_sensitive_data():
    text = "John Doe's SSN is 123-45-6789"
    result = detect_sensitive_data(text)
    
    assert len(result) > 0
    assert result[0]['type'] == 'PII'
    assert result[0]['value'] == 'John'
