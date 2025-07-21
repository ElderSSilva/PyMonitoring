import time
import utils
import schedule

process = utils.process_sys()
count = 1


def rodar_rotina():
    global count
    print("")
    print(f"Rotina numero: {count}")
    for i in process:
        print(i)
    print(f"Fim da rotina numero: {count}")
    print("")
    print("----------------------------------------------")
    print("")

    count += 1


if __name__ == "__main__":
    schedule.every(5).seconds.do(rodar_rotina)
    print("O robo ira começar dentro de 1 minuto!")
    print("")
    while True:
        schedule.run_pending()
        time.sleep(1)
