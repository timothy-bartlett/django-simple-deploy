"""Check the output of valid platform-agnostic cli commands.
"""

from pathlib import Path
import subprocess

import pytest

from ..utils import manage_sample_project as msp


# --- Fixtures ---

# --- Helper functions ---


# --- Test valid platform-agnostic simple_deploy calls ---

def test_help_output(tmp_project, capfd):
    """Call `manage.py simple_deploy --help`."""
    valid_sd_command = "python manage.py simple_deploy --help"

    # stdout, stderr = make_valid_call(tmp_project, valid_sd_command)
    stdout, stderr = msp.call_simple_deploy(tmp_project, valid_sd_command)
    # captured = capfd.readouterr()

    # reference_help_output = Path('platform_agnostic_tests/reference_files/sd_help_output.txt').read_text()
    current_test_dir = Path(__file__).parent
    reference_help_output = (current_test_dir / 'reference_files/sd_help_output.txt').read_text()

    # assert captured.out == reference_help_output
    assert stdout == reference_help_output
