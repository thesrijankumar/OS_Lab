#!/usr/bin/env python3

import multiprocessing
import time
import logging
import os
import random

def setup_system_logging():
    """Initialize system logging configuration"""
    logging.basicConfig(
        filename='system_startup_log.txt',
        level=logging.INFO,
        format='%(asctime)s - %(processName)s - %(levelname)s - %(message)s',
        filemode='w'
    )
    print("System logging initialized successfully")
    logging.info("SYSTEM STARTUP INITIATED")

def kernel_initialization():
    """Simulate kernel initialization process"""
    process_name = multiprocessing.current_process().name
    logging.info(f"{process_name}: Starting kernel initialization")
    print(f"{process_name}: Loading kernel modules...")
    
    # Simulate kernel loading tasks
    kernel_tasks = [
        "Initializing memory management",
        "Loading device drivers",
        "Setting up system calls",
        "Configuring interrupt handlers",
        "Starting process scheduler"
    ]
    
    for task in kernel_tasks:
        time.sleep(0.5)
        print(f"{process_name}: {task}")
        logging.info(f"{process_name}: {task}")
    
    logging.info(f"{process_name}: Kernel initialization completed")
    print(f"{process_name}: Kernel initialization completed")

def hardware_detection():
    """Simulate hardware detection process"""
    process_name = multiprocessing.current_process().name
    logging.info(f"{process_name}: Starting hardware detection")
    print(f"{process_name}: Detecting hardware components...")
    
    # Simulate hardware detection
    hardware_components = [
        "CPU: Intel Core i7-10700K",
        "RAM: 16GB DDR4",
        "Storage: 512GB SSD",
        "Network: Ethernet Controller",
        "Graphics: NVIDIA GeForce RTX 3060"
    ]
    
    for component in hardware_components:
        time.sleep(0.3)
        print(f"{process_name}: Detected {component}")
        logging.info(f"{process_name}: Detected {component}")
    
    logging.info(f"{process_name}: Hardware detection completed")
    print(f"{process_name}: Hardware detection completed")

def service_manager():
    """Simulate system service manager"""
    process_name = multiprocessing.current_process().name
    logging.info(f"{process_name}: Starting service manager")
    print(f"{process_name}: Initializing system services...")
    
    # Simulate starting system services
    services = [
        "Network Service",
        "File System Service", 
        "Security Service",
        "Print Spooler",
        "Task Scheduler",
        "User Session Manager"
    ]
    
    for service in services:
        time.sleep(0.4)
        status = "STARTED" if random.random() > 0.1 else "FAILED"
        print(f"{process_name}: Service {service} - {status}")
        logging.info(f"{process_name}: Service {service} - {status}")
    
    logging.info(f"{process_name}: Service manager completed")
    print(f"{process_name}: Service manager completed")

def user_interface():
    """Simulate user interface initialization"""
    process_name = multiprocessing.current_process().name
    logging.info(f"{process_name}: Starting user interface")
    print(f"{process_name}: Loading user interface components...")
    
    # Simulate UI components loading
    ui_components = [
        "Desktop Environment",
        "Window Manager",
        "Display Server",
        "Input Devices",
        "Theme Engine"
    ]
    
    for component in ui_components:
        time.sleep(0.6)
        print(f"{process_name}: Loaded {component}")
        logging.info(f"{process_name}: Loaded {component}")
    
    logging.info(f"{process_name}: User interface ready")
    print(f"{process_name}: User interface ready")

def system_monitor():
    """Simulate system monitoring daemon"""
    process_name = multiprocessing.current_process().name
    logging.info(f"{process_name}: Starting system monitor")
    print(f"{process_name}: Initializing system monitoring...")
    
    # Simulate monitoring system resources
    resources = [
        "CPU Usage",
        "Memory Usage", 
        "Disk I/O",
        "Network Traffic",
        "Temperature Sensors"
    ]
    
    for resource in resources:
        time.sleep(0.5)
        value = random.randint(1, 100)
        print(f"{process_name}: Monitoring {resource}: {value}%")
        logging.info(f"{process_name}: Monitoring {resource}: {value}%")
    
    logging.info(f"{process_name}: System monitor running")
    print(f"{process_name}: System monitor running")

def simulate_system_startup():
    """Main function to simulate complete system startup"""
    print("=" * 60)
    print("SYSTEM STARTUP SIMULATION")
    print("=" * 60)
    
    # Setup logging first
    setup_system_logging()
    
    # Define system processes
    system_processes = [
        (kernel_initialization, "Kernel-Init"),
        (hardware_detection, "Hardware-Detect"),
        (service_manager, "Service-Manager"),
        (user_interface, "User-Interface"),
        (system_monitor, "System-Monitor")
    ]
    
    print(f"\nStarting {len(system_processes)} system processes...")
    logging.info(f"Starting {len(system_processes)} system processes")
    
    # Create and start all processes
    processes = []
    for target_func, process_name in system_processes:
        process = multiprocessing.Process(
            target=target_func,
            name=process_name
        )
        processes.append(process)
        process.start()
        time.sleep(0.2)  # Stagger process starts
    
    # Wait for all processes to complete
    print("\nWaiting for system processes to complete...")
    for process in processes:
        process.join()
    
    # System startup completion
    logging.info("SYSTEM STARTUP COMPLETED SUCCESSFULLY")
    print("\n" + "=" * 60)
    print("SYSTEM STARTUP COMPLETED")
    print("=" * 60)
    
    # Display startup summary
    display_startup_summary()

def display_startup_summary():
    """Display system startup summary"""
    print("\nSYSTEM STARTUP SUMMARY")
    print("-" * 30)
    
    # Read and display log entries
    if os.path.exists('system_startup_log.txt'):
        with open('system_startup_log.txt', 'r') as log_file:
            lines = log_file.readlines()
        
        # Count process activities
        process_activities = {}
        for line in lines:
            if ' - ' in line:
                parts = line.split(' - ')
                if len(parts) >= 2:
                    process_name = parts[1]
                    if process_name not in process_activities:
                        process_activities[process_name] = 0
                    process_activities[process_name] += 1
        
        print("Process Activities:")
        for process, count in process_activities.items():
            print(f"  {process}: {count} log entries")
        
        print(f"\nTotal log entries: {len(lines)}")
        print(f"Log file: system_startup_log.txt")
        
        # Display last few log entries
        print("\nRecent log entries:")
        for line in lines[-5:]:
            print(f"  {line.strip()}")
    else:
        print("Log file not found")

def view_log_file():
    """Display the complete log file"""
    if os.path.exists('system_startup_log.txt'):
        print("\n" + "=" * 60)
        print("COMPLETE SYSTEM STARTUP LOG")
        print("=" * 60)
        with open('system_startup_log.txt', 'r') as log_file:
            print(log_file.read())
    else:
        print("Log file not found. Run system startup first.")

def main():
    """Main function for system startup simulation"""
    print("System Startup and Logging Simulation")
    print("1. Run System Startup")
    print("2. View Startup Summary") 
    print("3. View Complete Log")
    print("4. Exit")
    
    try:
        choice = input("Select option (1-4): ").strip()
        
        if choice == '1':
            simulate_system_startup()
        elif choice == '2':
            display_startup_summary()
        elif choice == '3':
            view_log_file()
        elif choice == '4':
            print("Exiting system startup simulation.")
        else:
            print("Invalid choice! Running system startup...")
            simulate_system_startup()
            
    except KeyboardInterrupt:
        print("\nSystem startup simulation interrupted.")

if __name__ == "__main__":
    main()
