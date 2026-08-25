import subprocess


ALLOWED_COMMANDS = {
    "ls",
    "pwd",
    "whoami",
    "uname",
    "df",
    "free",
    "uptime",
    "date",
    "hostname",
}


def execute_command(command: str):
    parts = command.strip().split()

    if not parts:
        return {
            "success": False,
            "output": "No command provided."
        }

    command_name = parts[0]

    if command_name not in ALLOWED_COMMANDS:
        return {
            "success": False,
            "output": f"Command '{command_name}' is not allowed."
        }

    try:
        result = subprocess.run(
            parts,
            capture_output=True,
            text=True,
            timeout=10
        )

        return {
            "success": result.returncode == 0,
            "command": command,
            "output": result.stdout.strip(),
            "error": result.stderr.strip()
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "command": command,
            "output": "",
            "error": "Command timed out."
        }

    except Exception as e:
        return {
            "success": False,
            "command": command,
            "output": "",
            "error": str(e)
        }