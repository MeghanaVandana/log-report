import json
from pathlib import Path


def load_report():
    with open("/app/report.json") as f:
        return json.load(f)


def test_report_exists():
    """Success criterion 1: The output file exists at /app/report.json."""
    assert Path("/app/report.json").exists(), "report.json not found"


def test_report_valid_json():
    """Success criterion 2: The report is valid JSON."""
    report = load_report()
    assert isinstance(report, dict), "Report must be a JSON object"


def test_total_requests():
    """Success criterion 3: The report contains the total number of requests found in the access log."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success criterion 4: The report contains the number of unique client IP addresses found in the access log."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 5: The report identifies the most frequently requested path in the access log."""
    report = load_report()
    assert report["top_path"] == "/index.html"
