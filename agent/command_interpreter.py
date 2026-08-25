def interpret_command(query: str):
    query = query.lower().strip()

    # Disk / Storage
    if any(word in query for word in [
        "storage",
        "disk space",
        "disk usage",
        "free space",
        "hard disk"
    ]):
        return "df -h"

    # Memory / RAM
    if any(word in query for word in [
        "ram",
        "memory",
        "available memory",
        "memory usage"
    ]):
        return "free -h"

    # Current directory
    if any(phrase in query for phrase in [
        "where am i",
        "current directory",
        "current folder",
        "current location"
    ]):
        return "pwd"

    # Files / directories
    if any(phrase in query for phrase in [
        "show files",
        "list files",
        "list folder",
        "show folder",
        "files here",
        "what files"
    ]):
        return "ls"

    # Current user
    if any(phrase in query for phrase in [
        "who am i",
        "current user",
        "logged in user"
    ]):
        return "whoami"

    # Hostname
    if any(phrase in query for phrase in [
        "hostname",
        "computer name",
        "system name"
    ]):
        return "hostname"

    # System uptime
    if any(phrase in query for phrase in [
        "uptime",
        "how long has the system been running",
        "system running time"
    ]):
        return "uptime"

    # Date
    if any(word in query for word in [
        "date",
        "today",
        "current date"
    ]):
        return "date"

    return None