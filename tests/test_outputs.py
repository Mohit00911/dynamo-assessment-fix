import json
from pathlib import Path

def load_report():
    with open("/app/report.json") as f:
        return json.load(f)

def test_total_requests():
    """Criterion 1: Include a 'total_requests' key with the total number of requests found in the log."""
    data = load_report()
    assert data.get("total_requests") == 6, "Expected 6 total_requests"

def test_unique_ips():
    """Criterion 2: Include a 'unique_ips' key with the total count of unique client IP addresses."""
    data = load_report()
    assert data.get("unique_ips") == 3, "Expected 3 unique_ips"

def test_top_path():
    """Criterion 3: Include a 'top_path' key representing the most frequently requested path."""
    data = load_report()
    assert data.get("top_path") == "/index.html", "Expected /index.html as top_path"