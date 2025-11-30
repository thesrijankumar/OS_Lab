#!/usr/bin/env python3

def MFT():
    """Multiprogramming with Fixed number of Tasks (Fixed Partitions)"""
    print("\n" + "="*50)
    print("MFT - Multiprogramming with Fixed Tasks")
    print("="*50)
    
    # Sample data for demonstration
    mem_size = 100
    part_size = 25
    processes = [20, 15, 30, 10, 5]
    
    # Calculate number of partitions
    num_partitions = mem_size // part_size
    remaining_memory = mem_size % part_size
    
    print(f"Memory Details:")
    print(f"Total Memory: {mem_size}")
    print(f"Partition Size: {part_size}")
    print(f"Number of Partitions: {num_partitions}")
    print(f"Wasted Memory (due to fixed partitions): {remaining_memory}")
    
    # Process allocation
    print(f"\nProcess Allocation:")
    allocated_processes = 0
    internal_fragmentation = 0
    
    for i, psize in enumerate(processes):
        if psize <= part_size:
            if allocated_processes < num_partitions:
                print(f"✓ Process {i+1} (Size: {psize}) allocated to partition {allocated_processes + 1}")
                internal_fragmentation += (part_size - psize)
                allocated_processes += 1
            else:
                print(f"✗ Process {i+1} (Size: {psize}) cannot be allocated - No free partitions")
        else:
            print(f"✗ Process {i+1} (Size: {psize}) too large for fixed partition (Max: {part_size})")
    
    print(f"\nTotal Internal Fragmentation: {internal_fragmentation}")
    print(f"Partitions Used: {allocated_processes}/{num_partitions}")

def MVT():
    """Multiprogramming with Variable number of Tasks (Variable Partitions)"""
    print("\n" + "="*50)
    print("MVT - Multiprogramming with Variable Tasks")
    print("="*50)
    
    # Sample data for demonstration
    mem_size = 100
    processes = [40, 25, 30, 15]
    
    available_memory = mem_size
    
    print(f"Initial Available Memory: {available_memory}")
    
    # Process allocation
    print(f"\nProcess Allocation:")
    for i, psize in enumerate(processes):
        if psize <= available_memory:
            available_memory -= psize
            print(f"✓ Process {i+1} (Size: {psize}) allocated")
            print(f"  Memory used: {psize}, Remaining: {available_memory}")
        else:
            print(f"✗ Process {i+1} (Size: {psize}) cannot be allocated")
            print(f"  Required: {psize}, Available: {available_memory}")
    
    # Display summary
    print(f"\nMemory Management Summary:")
    total_used = mem_size - available_memory
    print(f"Total Memory: {mem_size}")
    print(f"Memory Used: {total_used}")
    print(f"Memory Available: {available_memory}")
    print(f"Utilization: {(total_used / mem_size) * 100:.2f}%")

def main():
    """Main function for memory management"""
    print("Memory Management Techniques - Demonstration")
    print("Using sample data for MFT and MVT")
    
    MFT()
    MVT()

if __name__ == "__main__":
    main()
