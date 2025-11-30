import os

def main():
    print("Task 1: Process Creation Utility")
    n = int(input("Enter number of child processes: "))
    
    children = []
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            print(f"Child PID: {os.getpid()}, Parent PID: {os.getppid()}")
            os._exit(0)
        else:
            children.append(pid)
    
    for pid in children:
        os.waitpid(pid, 0)
    print("Task 1 completed")

if __name__ == "__main__":
    main()
