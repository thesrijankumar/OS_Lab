#!/usr/bin/env python3
import multiprocessing
import logging
from subtask2_process import system_process

def create_processes():
    """Create and start processes - Sub-Task 3"""
    processes = []
    
    # Create multiple processes
    p1 = multiprocessing.Process(
        target=system_process,
        args=('Process-1', 2),
        name='Process-1'
    )
    
    p2 = multiprocessing.Process(
        target=system_process,
        args=('Process-2', 3),
        name='Process-2'
    )
    
    processes = [p1, p2]
    
    # Start processes
    for process in processes:
        process.start()
    
    return processes

if __name__ == '__main__':
    from subtask1_logging import setup_logging
    setup_logging()
    
    processes = create_processes()
    print("Processes created and started!")

