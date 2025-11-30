#!/usr/bin/env python3

import os
import time
import subprocess

def basic_fork_example():
    """Demonstrate basic fork() system call"""
    print("=== Basic Fork Example ===")
    
    pid = os.fork()
    
    if pid > 0:
        # Parent process
        print(f"Parent Process: PID = {os.getpid()}, Child PID = {pid}")
        print("Parent is waiting for child to complete...")
        os.wait()  # Wait for child process to finish
        print("Parent: Child process completed")
    else:
        # Child process
        print(f"Child Process: PID = {os.getpid()}, Parent PID = {os.getppid()}")
        print("Child is executing...")
        time.sleep(2)
        print("Child: Execution completed")
    
    print("-" * 40)

def fork_with_exec():
    """Demonstrate fork() with exec() system calls"""
    print("=== Fork with Exec Example ===")
    
    pid = os.fork()
    
    if pid > 0:
        # Parent process
        print(f"Parent: Created child process with PID {pid}")
        print("Parent waiting for child to finish...")
        os.wait()
        print("Parent: Child process finished execution")
    else:
        # Child process
        print(f"Child: About to execute a new program")
        try:
            # Execute 'ls' command using exec
            os.execvp('ls', ['ls', '-l'])
        except FileNotFoundError:
            print("Child: Command not found, executing alternative")
            # If ls fails, execute pwd
            os.execvp('pwd', ['pwd'])
    
    print("-" * 40)

def pipe_communication():
    """Demonstrate IPC using pipes"""
    print("=== Pipe Communication Example ===")
    
    # Create a pipe
    r, w = os.pipe()
    
    pid = os.fork()
    
    if pid > 0:
        # Parent process - Writer
        os.close(r)  # Close reading end in parent
        
        messages = [
            "Hello from parent process!",
            "This is message number 2",
            "Message number 3",
            "END"  # Termination signal
        ]
        
        print("Parent: Sending messages to child...")
        
        for message in messages:
            print(f"Parent: Sending -> {message}")
            os.write(w, message.encode())
            time.sleep(1)  # Simulate processing time
        
        os.close(w)  # Close writing end
        os.wait()    # Wait for child to finish
        print("Parent: All messages sent and child completed")
        
    else:
        # Child process - Reader
        os.close(w)  # Close writing end in child
        
        print("Child: Ready to receive messages...")
        
        while True:
            message = os.read(r, 1024).decode()
            if not message:
                break
            
            print(f"Child: Received -> {message}")
            
            if message == "END":
                print("Child: Received termination signal")
                break
        
        os.close(r)  # Close reading end
        print("Child: All messages received")
    
    print("-" * 40)

def bidirectional_pipe():
    """Demonstrate bidirectional communication using two pipes"""
    print("=== Bidirectional Pipe Communication ===")
    
    # Create two pipes: one for parent->child, one for child->parent
    parent_to_child_r, parent_to_child_w = os.pipe()
    child_to_parent_r, child_to_parent_w = os.pipe()
    
    pid = os.fork()
    
    if pid > 0:
        # Parent process
        os.close(parent_to_child_r)  # Close reading end of parent->child pipe
        os.close(child_to_parent_w)  # Close writing end of child->parent pipe
        
        # Send message to child
        message_to_child = "Hello child, how are you?"
        print(f"Parent: Sending to child -> {message_to_child}")
        os.write(parent_to_child_w, message_to_child.encode())
        os.close(parent_to_child_w)  # Close after sending
        
        # Wait for response from child
        response = os.read(child_to_parent_r, 1024).decode()
        print(f"Parent: Received from child -> {response}")
        os.close(child_to_parent_r)
        
        os.wait()
        print("Parent: Communication completed")
        
    else:
        # Child process
        os.close(parent_to_child_w)  # Close writing end of parent->child pipe
        os.close(child_to_parent_r)  # Close reading end of child->parent pipe
        
        # Receive message from parent
        message_from_parent = os.read(parent_to_child_r, 1024).decode()
        print(f"Child: Received from parent -> {message_from_parent}")
        os.close(parent_to_child_r)
        
        # Send response to parent
        response_to_parent = "Hello parent, I'm doing well! Current time: " + time.ctime()
        print(f"Child: Sending to parent -> {response_to_parent}")
        os.write(child_to_parent_w, response_to_parent.encode())
        os.close(child_to_parent_w)
        
        print("Child: Communication completed")
    
    print("-" * 40)

def multiple_process_communication():
    """Demonstrate communication between multiple processes"""
    print("=== Multiple Process Communication ===")
    
    # Create separate pipes for each child
    pipes = []
    for i in range(3):
        r, w = os.pipe()
        pipes.append((r, w))
    
    child_pids = []
    
    for i in range(3):
        r, w = pipes[i]
        pid = os.fork()
        
        if pid == 0:
            # Child process - close all other pipes
            for j in range(3):
                if j != i:
                    os.close(pipes[j][0])
                    os.close(pipes[j][1])
            
            os.close(w)  # Close writing end of own pipe
            
            # Read message from parent
            message = os.read(r, 1024).decode()
            print(f"Child {i+1} (PID {os.getpid()}): Received -> {message}")
            
            os.close(r)
            os._exit(0)  # Child exits
            
        else:
            child_pids.append(pid)
    
    # Parent process continues here
    # Send unique message to each child
    for i in range(3):
        r, w = pipes[i]
        os.close(r)  # Close reading end in parent
        
        message = f"Hello Child {i+1} from parent {os.getpid()}!"
        print(f"Parent: Sending to child {i+1} -> {message}")
        os.write(w, message.encode())
        os.close(w)
    
    # Wait for all children to complete
    for child_pid in child_pids:
        os.waitpid(child_pid, 0)
    
    print("Parent: All children completed")
    print("-" * 40)

def process_hierarchy():
    """Demonstrate process hierarchy with multiple levels"""
    print("=== Process Hierarchy Example ===")
    
    print(f"Root Process: PID = {os.getpid()}")
    
    # First level fork
    pid1 = os.fork()
    
    if pid1 == 0:
        # First child
        print(f"First Child: PID = {os.getpid()}, Parent = {os.getppid()}")
        
        # Second level fork from first child
        pid2 = os.fork()
        
        if pid2 == 0:
            # Grandchild
            print(f"Grandchild: PID = {os.getpid()}, Parent = {os.getppid()}")
            time.sleep(1)
            print("Grandchild: Finished")
            os._exit(0)
        else:
            # First child waits for grandchild
            os.wait()
            print("First Child: Grandchild completed")
            os._exit(0)
    
    else:
        # Root process continues
        # Create another child at first level
        pid3 = os.fork()
        
        if pid3 == 0:
            # Second child
            print(f"Second Child: PID = {os.getpid()}, Parent = {os.getppid()}")
            time.sleep(2)
            print("Second Child: Finished")
            os._exit(0)
        else:
            # Root process waits for all children
            os.waitpid(pid1, 0)
            os.waitpid(pid3, 0)
            print("Root Process: All children and grandchildren completed")
    
    print("-" * 40)

def run_all_demonstrations():
    """Run all demonstrations sequentially without menu"""
    print("SYSTEM CALLS AND INTER-PROCESS COMMUNICATION")
    print("Running all demonstrations sequentially...")
    print("=" * 50)
    
    demonstrations = [
        basic_fork_example,
        fork_with_exec,
        pipe_communication,
        bidirectional_pipe,
        multiple_process_communication,
        process_hierarchy
    ]
    
    for i, demo in enumerate(demonstrations, 1):
        print(f"\nDemonstration {i}/6")
        demo()
        time.sleep(1)
    
    print("\n" + "=" * 50)
    print("ALL DEMONSTRATIONS COMPLETED SUCCESSFULLY")

def main():
    """Main function with menu"""
    print("SYSTEM CALLS AND INTER-PROCESS COMMUNICATION")
    print("=" * 50)
    
    demonstrations = [
        ("Basic Fork", basic_fork_example),
        ("Fork with Exec", fork_with_exec),
        ("Pipe Communication", pipe_communication),
        ("Bidirectional Pipes", bidirectional_pipe),
        ("Multiple Process Communication", multiple_process_communication),
        ("Process Hierarchy", process_hierarchy)
    ]
    
    while True:
        print("\nAvailable Demonstrations:")
        for i, (name, _) in enumerate(demonstrations, 1):
            print(f"{i}. {name}")
        print("7. Run All Demonstrations")
        print("8. Exit")
        
        try:
            choice = input("\nSelect demonstration (1-8): ").strip()
            
            if choice == '1':
                basic_fork_example()
            elif choice == '2':
                fork_with_exec()
            elif choice == '3':
                pipe_communication()
            elif choice == '4':
                bidirectional_pipe()
            elif choice == '5':
                multiple_process_communication()
            elif choice == '6':
                process_hierarchy()
            elif choice == '7':
                run_all_demonstrations()
            elif choice == '8':
                print("Exiting system calls demonstration.")
                break
            else:
                print("Invalid choice! Please select 1-8.")
                
        except KeyboardInterrupt:
            print("\nDemonstration interrupted by user.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Run without menu by default
    run_all_demonstrations()
