import re
import sys
from pathlib import Path

from wsgi_shim import main

from tests.test_config import app_wrapper


def test_main_normal_module_default(tmp_path):
    log_file = tmp_path / 'logfile'
    config_file = tmp_path / 'config.toml'
    config_file.write_text(f"""
    [passenger]
    passenger_python="{Path(sys.prefix) / 'bin' / 'python'}"
    [wsgi]
    module = "tests.flask_example"
    app = "app"
    [environment]
    LOG_FILENAME = "{log_file}"
    """)
    app = main(tmp_path)
    html, status, headers = app_wrapper(app)
    log = log_file.read_text()
    assert re.search(r'Hello, World', html)
    assert status == '200 OK'
    assert len(headers) == 2
    assert "INFO tests.flask_example MainThread : Request: /" in log
