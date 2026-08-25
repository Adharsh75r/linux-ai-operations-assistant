def format_response(command, result):
    if not result["success"]:
        return f"❌ Command failed: {result.get('error', 'Unknown error')}"

    output = result.get("output", "").strip()

    if command == "free -h":
        return format_memory(output)

    if command == "df -h":
        return format_disk(output)

    if command == "ps aux --sort=-%cpu":
        return format_processes(output, "CPU")

    if command == "ps aux --sort=-%mem":
        return format_processes(output, "RAM")

    if command == "pwd":
        return f"📁 Current directory:\n{output}"

    if command == "whoami":
        return f"👤 Current user:\n{output}"

    if command == "hostname":
        return f"💻 Hostname:\n{output}"

    if command == "uptime":
        return f"⏱️ System uptime:\n{output}"

    if command == "date":
        return f"📅 Current date and time:\n{output}"

    if command == "ls":
        return f"📂 Files and directories:\n{output}"

    if command == "uname":
        return f"🖥️ System Information:\n{output}"

    return output


def format_memory(output):
    lines = output.splitlines()

    if len(lines) < 2:
        return output

    headers = lines[0].split()
    values = lines[1].split()

    data = dict(zip(headers, values))

    return (
        "🧠 Memory Information\n"
        "---------------------\n"
        f"Total:     {data.get('total', 'N/A')}\n"
        f"Used:      {data.get('used', 'N/A')}\n"
        f"Free:      {data.get('free', 'N/A')}\n"
        f"Available: {data.get('available', 'N/A')}"
    )


def format_disk(output):
    lines = output.splitlines()

    if len(lines) < 2:
        return output

    for line in lines[1:]:
        parts = line.split()

        if len(parts) >= 6 and parts[-1] == "/":
            return (
                "💾 Disk Information\n"
                "------------------\n"
                f"Total:     {parts[1]}\n"
                f"Used:      {parts[2]}\n"
                f"Available: {parts[3]}\n"
                f"Usage:     {parts[4]}\n"
                f"Mount:     {parts[5]}"
            )

    return output


def format_processes(output, sort_type):
    lines = output.splitlines()

    if len(lines) < 2:
        return "No process information available."

    header = lines[0]
    processes = lines[1:6]

    return (
        f"⚙️ Top Processes by {sort_type}\n"
        "----------------------------\n"
        f"{header}\n"
        + "\n".join(processes)
    )