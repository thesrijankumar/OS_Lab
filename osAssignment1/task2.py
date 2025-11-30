import os

def main():
    print("Task 2: Command Execution Using exec()")
    
    commands = [["ls", "-l"], ["date"], ["pwd"]]
    
    for i, cmd in enumerate(commands):
        pid = os.fork()
        if pid == 0:
            print(f"Executing: {' '.join(cmd)}")
            os.execvp(cmd[0], cmd)
        else:
            os.waitpid(pid, 0)
    
    print("Task 2 completed")

if __name__ == "__main__":
    main()

