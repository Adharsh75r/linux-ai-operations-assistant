import subprocess


ALLOWED_COMMANDS = {
    "ls",
    "pwd",
    "whoami",
    "uname",
    "df -h",
    "free -h",
    "uptime",
    "date",
    "hostname",
    "ps aux --sort=-%cpu",
    "ps aux --sort=-%mem",
}


def execute_command(command: str):

    if command not in ALLOWED_COMMANDS:
        return {
            "success": False,
            "output": f"Command '{command.split()[0]}' is not allowed."
        }

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode != 0:
            return {
                "success": False,
                "output": result.stderr.strip(),
                "error": result.stderr.strip()
            }

        return {
            "success": True,
            "output": result.stdout.strip()
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "output": "Command timed out.",
            "error": "Command timed out."
        }

    except Exception as e:
        return {
            "success": False,
            "output": str(e),
            "error": str(e)
        }