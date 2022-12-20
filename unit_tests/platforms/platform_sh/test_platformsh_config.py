"""Unit tests for django-simple-deploy, targeting Platform.sh."""

from pathlib import Path
import subprocess

import pytest

import unit_tests.utils.ut_helper_functions as hf


# --- Fixtures ---


# --- Test modifications to project files. ---

def test_settings(tmp_project):
    """Verify settings have been changed for Platform.sh."""
    hf.check_reference_file(tmp_project, 'blog/settings.py', 'platform_sh')

def test_requirements_txt(tmp_project, pkg_manager):
    """Test that the requirements.txt file is correct."""
    if pkg_manager == "req_txt":
        hf.check_reference_file(tmp_project, 'requirements.txt', 'platform_sh')
    elif pkg_manager in ["poetry", "pipenv"]:
        assert not Path("requirements.txt").exists()

def test_pyproject_toml(tmp_project, pkg_manager):
    """Test that pyproject.toml is correct."""
    if pkg_manager in ("req_txt", "pipenv"):
        assert not Path("pyproject.toml").exists()
    elif pkg_manager == "poetry":
        hf.check_reference_file(tmp_project, "pyproject.toml", "platform_sh")

def test_pipfile(tmp_project, pkg_manager):
    """Test that Pipfile is correct."""
    if pkg_manager in ("req_txt", "poetry"):
        assert not Path("Pipfile").exists()
    elif pkg_manager == "pipenv":
        hf.check_reference_file(tmp_project, "Pipfile", "platform_sh")

def test_gitignore(tmp_project):
    """Test that .gitignore has been modified correctly."""
    hf.check_reference_file(tmp_project, '.gitignore', 'platform_sh')


# --- Test Platform.sh yaml files ---

def test_platform_app_yaml_file(tmp_project, pkg_manager):
    """Test for a correct .platform.app.yaml file."""
    if pkg_manager == "req_txt":
        hf.check_reference_file(tmp_project, '.platform.app.yaml', 'platform_sh')
    elif pkg_manager == "poetry":
        hf.check_reference_file(tmp_project, '.platform.app.yaml', 'platform_sh',
                reference_filename="poetry.platform.app.yaml")
    elif pkg_manager == "pipenv":
        hf.check_reference_file(tmp_project, '.platform.app.yaml', 'platform_sh',
                reference_filename="pipenv.platform.app.yaml")

def test_services_yaml_file(tmp_project):
    hf.check_reference_file(tmp_project, '.platform/services.yaml', 'platform_sh')


# --- Test logs ---

def test_log_dir(tmp_project):
    """Test that the log directory exists, and contains an appropriate log file."""
    log_path = Path(tmp_project / 'simple_deploy_logs')
    assert log_path.exists()

    # DEV: After implementing friendly summary for Platform.sh, this file 
    #   will need to be updated.
    # There should be exactly two log files.
    log_files = sorted(log_path.glob('*'))
    log_filenames = [lf.name for lf in log_files]
    # Check for exactly the log files we expect to find.
    # assert 'deployment_summary.html' in log_filenames
    # DEV: Add a regex text for a file like "simple_deploy_2022-07-09174245.log".
    assert len(log_files) == 1   # update on friendly summary

    # Read log file.
    # DEV: Look for specific log file; not sure this log file is always the second one.
    #   We're looking for one similar to "simple_deploy_2022-07-09174245.log".
    log_file = log_files[0]   # update on friendly summary
    log_file_text = log_file.read_text()

    # DEV: Update these for more platform-specific log messages.
    # Spot check for opening log messages.
    assert "INFO: Logging run of `manage.py simple_deploy`..." in log_file_text
    assert "INFO: Configuring project for deployment to Platform.sh..." in log_file_text

    # Spot check for success messages.
    assert "INFO: --- Your project is now configured for deployment on Platform.sh. ---" in log_file_text
    assert "INFO: To deploy your project, you will need to:" in log_file_text
