def test_integration():
    try:
        import subprocess
        subprocess.run(["python", "issue_commenter.py"])
    except subprocess.CalledProcessError as e:
        assert False, f"Script exited with non-zero exit code: {e.returncode}"
    except Exception as e:
        assert False, f"Script encountered an error: {e}"
