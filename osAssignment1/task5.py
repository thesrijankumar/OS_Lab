import os
import time

def main():
    print("Task 5: Process Prioritization")
    
    def heavy_task():
        for i in range(10000000):
            i * i
    
    for nice_val in [0, 5, 10]:
        pid = os.fork()
        if pid == 0:
            os.nice(nice_val)
            start = time.time()
            heavy_task()
            end = time.time()
            print(f"Nice {nice_val}: {end-start:.2f}s")
            os._exit(0)
        else:
            os.waitpid(pid, 0)
    
    print("Task 5 completed")

if __name__ == "__main__":
    main()
