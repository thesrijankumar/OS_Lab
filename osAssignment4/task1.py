#!/usr/bin/env python3

import subprocess
import time
import os
import sys

def run_python_file(filename, description):
    """Run a Python file and display results"""
    print(f"\n{'='*60}")
    print(f"RUNNING: {description}")
    print(f"FILE: {filename}")
    print(f"{'='*60}")
    
    try:
        # Check if file exists
        if not os.path.exists(filename):
            print(f"ERROR: File '{filename}' not found!")
            return False
        
        # Run the Python file
        start_time = time.time()
        result = subprocess.run([
            sys.executable, filename
        ], capture_output=True, text=True)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Display output
        if result.stdout:
            print("OUTPUT:")
            print(result.stdout)
        
        if result.stderr:
            print("ERRORS:")
            print(result.stderr)
        
        # Display execution status
        if result.returncode == 0:
            print(f"SUCCESS: {description} completed in {execution_time:.2f} seconds")
            return True
        else:
            print(f"FAILED: {description} returned error code {result.returncode}")
            return False
            
    except Exception as e:
        print(f"EXCEPTION: {str(e)}")
        return False

def create_sample_files():
    """Create sample Python files for batch processing demo"""
    sample_files = {
        'program1.py': '''
#!/usr/bin/env python3
print("=== PROGRAM 1: Number Processing ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
print("Program 1 completed successfully!")
''',
        
        'program2.py': '''
#!/usr/bin/env python3
import time
print("=== PROGRAM 2: File Operations ===")
print("Simulating file operations...")
time.sleep(2)
print("Creating sample data...")
sample_data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
for i, item in enumerate(sample_data, 1):
    print(f"Processing item {i}: {item}")
print("Program 2 completed successfully!")
''',
        
        'program3.py': '''
#!/usr/bin/env python3
print("=== PROGRAM 3: Mathematical Calculations ===")
import math
print("Performing mathematical operations:")
print(f"Square root of 64: {math.sqrt(64)}")
print(f"Factorial of 5: {math.factorial(5)}")
print(f"Value of pi: {math.pi:.4f}")
print("Program 3 completed successfully!")
''',
        
        'program4.py': '''
#!/usr/bin/env python3
print("=== PROGRAM 4: String Manipulation ===")
text = "batch processing simulation in python"
print(f"Original text: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Title case: {text.title()}")
print(f"Word count: {len(text.split())}")
print("Program 4 completed successfully!")
'''
    }
    
    for filename, content in sample_files.items():
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write(content)
            os.chmod(filename, 0o755)
            print(f"Created: {filename}")
    
    return list(sample_files.keys())

def sequential_batch_processing():
    """Simulate sequential batch processing of multiple programs"""
    print("BATCH PROCESSING SIMULATION - SEQUENTIAL EXECUTION")
    print("=" * 60)
    
    # Create sample programs for demonstration
    print("Setting up batch processing environment...")
    program_files = create_sample_files()
    
    # Define batch job sequence
    batch_jobs = [
        ('program1.py', 'Number Processing Task'),
        ('program2.py', 'File Operations Task'),
        ('program3.py', 'Mathematical Calculations Task'),
        ('program4.py', 'String Manipulation Task')
    ]
    
    # Display batch configuration
    print(f"\nBATCH CONFIGURATION:")
    print(f"Total programs in batch: {len(batch_jobs)}")
    print(f"Execution mode: Sequential")
    print(f"Working directory: {os.getcwd()}")
    
    # Execute batch sequentially
    print(f"\nSTARTING SEQUENTIAL BATCH EXECUTION")
    
    successful_jobs = 0
    failed_jobs = 0
    batch_start_time = time.time()
    
    for job_number, (filename, description) in enumerate(batch_jobs, 1):
        print(f"\nBATCH JOB {job_number}/{len(batch_jobs)}")
        
        if run_python_file(filename, description):
            successful_jobs += 1
        else:
            failed_jobs += 1
        
        # Simulate batch processing delay between jobs
        if job_number < len(batch_jobs):
            print(f"\nBatch processor preparing next job...")
            time.sleep(1)
    
    # Batch completion summary
    total_time = time.time() - batch_start_time
    
    print(f"\n{'='*60}")
    print("BATCH PROCESSING COMPLETE - SUMMARY REPORT")
    print(f"{'='*60}")
    print(f"Batch Start Time: {time.ctime(batch_start_time)}")
    print(f"Batch End Time: {time.ctime()}")
    print(f"Total Execution Time: {total_time:.2f} seconds")
    print(f"Programs Executed: {len(batch_jobs)}")
    print(f"Successful Executions: {successful_jobs}")
    print(f"Failed Executions: {failed_jobs}")
    print(f"Success Rate: {(successful_jobs/len(batch_jobs))*100:.1f}%")
    
    # Generate detailed batch log
    with open('batch_processing_log.txt', 'w') as log_file:
        log_file.write("BATCH PROCESSING EXECUTION LOG\n")
        log_file.write("===============================\n")
        log_file.write(f"Execution Date: {time.ctime()}\n")
        log_file.write(f"Total Programs: {len(batch_jobs)}\n")
        log_file.write(f"Successful: {successful_jobs}\n")
        log_file.write(f"Failed: {failed_jobs}\n")
        log_file.write(f"Total Time: {total_time:.2f} seconds\n")
        log_file.write(f"Success Rate: {(successful_jobs/len(batch_jobs))*100:.1f}%\n\n")
        
        log_file.write("PROGRAM EXECUTION SEQUENCE:\n")
        for i, (filename, description) in enumerate(batch_jobs, 1):
            status = "SUCCESS" if os.path.exists(filename) else "FAILED"
            log_file.write(f"{i}. {filename} - {description} - {status}\n")
    
    print(f"\nDetailed log saved to: batch_processing_log.txt")
    print(f"Batch processing simulation completed!")

def main():
    """Main function for batch processing simulation"""
    sequential_batch_processing()

if __name__ == "__main__":
    main()
