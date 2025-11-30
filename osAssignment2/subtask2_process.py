#!/usr/bin/env python3
import time
import logging

def system_process(task_name, duration=2):
    """Simulate a process task - Sub-Task 2"""
    logging.info(f"{task_name} started")
    print(f"{task_name} is running for {duration} seconds...")
    time.sleep(duration)
    logging.info(f"{task_name} ended")
    print(f"{task_name} completed")

if __name__ == '__main__':
    # Test the process function
    system_process("Test-Process", 1)
