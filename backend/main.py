from fastapi import FastAPI
from pydantic import BaseModel

from agent.system_monitor import get_system_info
from agent.process_monitor import get_top_processes
from agent.command_executor import execute_command
from agent.command_interpreter import interpret_command

from agent.response_formatter import format_response
from agent.ai_service import understand_query

app = FastAPI(
    title="Linux AI Operations Assistant",
    description="API for interacting with the Linux system",
    version="0.1.0"
)


class CommandRequest(BaseModel):
    command: str


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def root():
    return {
        "message": "Linux AI Operations Assistant API is running"
    }


@app.get("/system")
def system_info():
    return get_system_info()


@app.get("/processes")
def processes():
    return get_top_processes()


@app.post("/command")
def run_command(request: CommandRequest):
    return execute_command(request.command)


@app.post("/query")
def natural_language_query(request: QueryRequest):

    ai_result = understand_query(request.query)

    if not ai_result.get("success"):
        return ai_result

    command = ai_result.get("command")

    allowed_commands = {
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
        "ps aux --sort=-%mem"
    }

    if command not in allowed_commands:
        return {
            "success": False,
            "query": request.query,
            "message": "The requested operation is not allowed."
        }

    result = execute_command(command)

    answer = format_response(command, result)

    return {
        "success": result["success"],
        "query": request.query,
        "intent": ai_result.get("intent"),
        "command": command,
        "confidence": ai_result.get("confidence"),
        "answer": answer
    }