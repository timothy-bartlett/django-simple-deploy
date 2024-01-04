"""Test utility functions for examining git status."""

import simple_deploy.management.commands.utils as sd_utils

import pytest

def test_simple_git_status():
    """Tests for simple `git status --porcelain` and `git diff --unified=0` outputs."""
    status_output = " M .gitignore"
    diff_output = ""
    assert sd_utils.check_status_output(status_output, diff_output)

    status_output = " M .gitignore"
    diff_output = "diff --git a/.gitignore b/.gitignore\nindex 9c96d1b..4279ffb 100644\n--- a/.gitignore\n+++ b/.gitignore\n@@ -8,0 +9,3 @@ db.sqlite3\n+\n+# Ignore logs from simple_deploy.\n+simple_deploy_logs/"
    assert sd_utils.check_status_output(status_output, diff_output)

    status_output = " M blog/settings.py\n?? simple_deploy_logs/"
    diff_output = "diff --git a/blog/settings.py b/blog/settings.py\nindex 6d40136..6395c5a 100644\n--- a/blog/settings.py\n+++ b/blog/settings.py\n@@ -39,0 +40 @@ INSTALLED_APPS = [\n+    'simple_deploy',\n@@ -134 +135 @@ DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'\n-LOGIN_URL = 'users:login'\n\\ No newline at end of file\n+LOGIN_URL = 'users:login'"
    assert sd_utils.check_status_output(status_output, diff_output)