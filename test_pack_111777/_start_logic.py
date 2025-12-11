import os
import uuid
import datetime
import sys


def _create_detailed_test_file():
    path = f"/home/user/test_pack1_log_{uuid.uuid4()}"

    date_str = datetime.datetime.now().isoformat()
    pid = os.getpid()
    ppid = os.getppid()
    cwd = os.getcwd()
    script_path = os.path.realpath(sys.argv[0]) if sys.argv else "unknown"
    user = os.getenv("USER", "unknown")

    # Команда запуска текущего процесса
    try:
        with open(f"/proc/{pid}/cmdline") as f:
            cmdline = f.read().replace("\x00", " ").strip()
    except FileNotFoundError:
        cmdline = "not available"

    # Имя родительского процесса
    try:
        with open(f"/proc/{ppid}/comm") as f:
            parent_name = f.read().strip()
    except FileNotFoundError:
        parent_name = "unknown"

    content = (
        f"{date_str} - test message from main pack\n\n"

        f"--- Process information ---\n"
        f"PID: {pid} — идентификатор текущего процесса Python, который создал этот файл\n"
        f"Cmdline: {cmdline}\n\n"

        f"PPID: {ppid} — идентификатор родительского процесса, который запустил Python\n"
        f"Parent process name: {parent_name}\n\n"

        f"User: {user} — пользователь от имени которого был создан файл\n"
        f"Script path: {script_path} — путь к Python-скрипту\n"
        f"Working directory: {cwd} — рабочая директория процесса\n"
    )

    with open(path, "w") as f:
        f.write(content)

    return path


_create_detailed_test_file()
