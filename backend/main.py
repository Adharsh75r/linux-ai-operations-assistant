from fastapi import FastAPI
from pydantic import BaseModel

from agent.system_monitor import get_system_info
from agent.process_monitor import get_top_processes
from agent.command_executor import execute_command
from agent.command_interpreter import interpret_command

from agent.response_formatter import format_response

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

    command = interpret_command(request.query)

    if command is None:
        return {
            "success": False,
            "query": request.query,
            "message": "I don't understand that request yet."
        }

    result = execute_command(command)

    answer = format_response(command, result)

    return {
        "success": result["success"],
        "query": request.query,
        "command": command,
        "answer": answer
    }