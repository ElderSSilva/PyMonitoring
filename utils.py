import psutil
from colorama import init, Fore, Style

init()


def process_sys():
    process_list = []
    processos = []
    count = 0

    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            mem = proc.memory_info().rss / (1024 * 1024)
            processos.append((proc.pid, proc.name(), mem))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    processos.sort(key=lambda x: x[2], reverse=True)

    for pid, nome, mem in processos[:10]:
        memoria = mem
        pid_cor = Fore.YELLOW + f'PID: {proc.pid}'
        name_cor = Fore.RED + f'Nome: {proc.name()}'
        mem_cor = Fore.GREEN + f'Memória: {memoria: .2f} MB'

        process_list.append(f'{pid_cor} | {nome} | {mem_cor}{Style.RESET_ALL}')

    return process_list

