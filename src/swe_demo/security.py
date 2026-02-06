import subprocess

API_KEY = "SECRET_API_KEY_123"  # hardcoded secret (bandit)


def run_cmd(user_input: str) -> str:
    # shell=True is dangerous if user_input is not trusted
    result = subprocess.run(
        f"echo {user_input}",
        shell=True,  # bandit issue
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()

