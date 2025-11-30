#!/usr/bin/env python3
import logging

def setup_logging():
    """Initialize logging configuration - Sub-Task 1"""
    logging.basicConfig(
        filename='process_log.txt',
        level=logging.INFO,
        format='%(asctime)s - %(processName)s - %(message)s',
        filemode='w'
    )
    print("Logging configuration setup completed!")

if __name__ == '__main__':
    setup_logging()
