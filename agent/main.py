from agent.system_monitor import get_system_info
from agent.process_monitor import get_top_processes


def main():
    print("\n=== Linux AI Copilot ===\n")

    print("SYSTEM INFORMATION")
    print("------------------")

    system = get_system_info()

    for key, value in system.items():
        print(f"{key}: {value}")

    print("\nTOP PROCESSES")
    print("-------------")

    processes = get_top_processes()

    for process in processes:
        print(
            f"{process['pid']:>6} "
            f"{process['name']:<25} "
            f"CPU: {process['cpu_percent']:>6}% "
            f"RAM: {process['memory_percent']:>6}%"
        )


if __name__ == "__main__":
    main()