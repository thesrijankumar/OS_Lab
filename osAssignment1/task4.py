import os

def main():
    print("Task 4: Inspecting Process Info from /proc")
    
    pid = input("Enter PID (or press Enter for current): ") or os.getpid()
    
    try:
        pid = int(pid)
        if os.path.exists(f"/proc/{pid}"):
            with open(f"/proc/{pid}/status") as f:
                for line in f:
                    if "Name:" in line or "State:" in line or "Pid:" in line:
                        print(line.strip())
            
            exe_path = os.readlink(f"/proc/{pid}/exe")
            print(f"Executable: {exe_path}")
        else:
            print("Process not found")
    except:
        print("Invalid PID")
    
    print("Task 4 completed")

if __name__ == "__main__":
    main()
