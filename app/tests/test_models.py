from app.models.scan_model import save_scan, get_all_scans, delete_scan
from app.models.database import db

def test_save_scan():
    save_scan('test_file.txt', [{'type': 'PII', 'value': 'John Doe'}])
    scans = get_all_scans()
    assert len(scans) > 0

def test_delete_scan():
    delete_scan('test_file.txt')
    scans = get_all_scans()
    assert len(scans) == 0
