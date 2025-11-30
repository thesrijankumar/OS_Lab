import os
import time

def main():
    print("Task 3: Zombie & Orphan Processes")
    
    print("Creating zombie process...")
    pid = os.fork()
    if pid == 0:
        print("Zombie child exiting")
        os._exit(0)
    else:
        print("Parent not waiting (zombie created)")
        time.sleep(2)
        input("Check with 'ps -ef | grep defunct'. Press Enter...")
        os.waitpid(pid, 0)
    
    print("Creating orphan process...")
    pid = os.fork()
    if pid == 0:
        time.sleep(2)
        print(f"Orphan PPID: {os.getppid()}")
        os._exit(0)
    else:
        os._exit(0)
    
    print("Task 3 completed")

if __name__ == "__main__":
    main()
