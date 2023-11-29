import time


def watch():
    result_time = start_time = 0
    is_start = False
    is_pause = False
    while True:
        command = int(input("Enter command: "))
        match command:
            case 1:
                if not is_start:
                    start_time = time.time()
                    is_start = True
                    print("Start")
            case 2:
                if is_start:
                    if not is_pause:
                        result_time += time.time() - start_time
                        is_pause = True
                        start_time = 0
                        print(f"Pause. {int(result_time)} s")
            case 3:
                if is_start:
                    if is_pause:
                        start_time = time.time()
                        is_pause = False
                        print("Restart")
            case 4:
                if is_start:
                    if not  is_pause:
                        result_time += time.time() - start_time
                    print(f"Break. {int(result_time)} s")
                    break
            case _:
                print("Repeat enter: ")


if __name__ == '__main__':
    watch()
