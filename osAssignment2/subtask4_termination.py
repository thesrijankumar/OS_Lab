#!/usr/bin/env python3
import multiprocessing
import logging
from subtask3_creation import create_processes

def terminate_processes(processes):
    """Wait for processes to complete - Sub-Task 4"""
    for process in processes:
        process.join()
    print("All processes terminated successfully!")

if __name__ == '__main__':
    from subtask1_logging import setup_logging
    setup_logging()
    
    processes = create_processes()
    terminate_processes(processes)
    
    print("Check 'process_log.txt' for logs!")
