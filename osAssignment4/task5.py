#!/usr/bin/env python3

class CPUScheduler:
    def __init__(self):
        self.processes = []
    
    def input_processes(self):
        """Get process information from user"""
        print("Enter process details:")
        n = int(input("Enter number of processes: "))
        
        for i in range(n):
            print(f"\nProcess {i+1}:")
            arrival_time = int(input("Enter arrival time: "))
            burst_time = int(input("Enter burst time: "))
            priority = int(input("Enter priority (lower number = higher priority): "))
            
            self.processes.append({
                'pid': i + 1,
                'arrival_time': arrival_time,
                'burst_time': burst_time,
                'priority': priority,
                'remaining_time': burst_time
            })
        
        return self.processes
    
    def sample_processes(self):
        """Use sample processes for demonstration"""
        self.processes = [
            {'pid': 1, 'arrival_time': 0, 'burst_time': 8, 'priority': 3, 'remaining_time': 8},
            {'pid': 2, 'arrival_time': 1, 'burst_time': 4, 'priority': 1, 'remaining_time': 4},
            {'pid': 3, 'arrival_time': 2, 'burst_time': 9, 'priority': 4, 'remaining_time': 9},
            {'pid': 4, 'arrival_time': 3, 'burst_time': 5, 'priority': 2, 'remaining_time': 5}
        ]
        print("Using sample processes:")
        for p in self.processes:
            print(f"P{p['pid']}: AT={p['arrival_time']}, BT={p['burst_time']}, Priority={p['priority']}")
        return self.processes

    def calculate_metrics(self, processes):
        """Calculate waiting time and turnaround time"""
        total_wt = 0
        total_tat = 0
        n = len(processes)
        
        print("\nPID\tArrival\tBurst\tPriority\tWaiting\tTurnaround")
        print("-" * 60)
        
        for p in processes:
            wt = p['waiting_time']
            tat = p['turnaround_time']
            total_wt += wt
            total_tat += tat
            
            print(f"P{p['pid']}\t{p['arrival_time']}\t{p['burst_time']}\t{p['priority']}\t\t{wt}\t{tat}")
        
        print("-" * 60)
        print(f"Average Waiting Time: {total_wt / n:.2f}")
        print(f"Average Turnaround Time: {total_tat / n:.2f}")
        
        return total_wt / n, total_tat / n

    def fcfs_scheduling(self):
        """First Come First Serve Scheduling"""
        print("\n" + "=" * 60)
        print("FIRST COME FIRST SERVE (FCFS) SCHEDULING")
        print("=" * 60)
        
        # Sort processes by arrival time
        sorted_processes = sorted(self.processes, key=lambda x: x['arrival_time'])
        
        current_time = 0
        gantt_chart = []
        
        for i, p in enumerate(sorted_processes):
            if current_time < p['arrival_time']:
                current_time = p['arrival_time']
            
            # Calculate times
            start_time = current_time
            completion_time = start_time + p['burst_time']
            turnaround_time = completion_time - p['arrival_time']
            waiting_time = start_time - p['arrival_time']
            
            # Update process info
            sorted_processes[i]['completion_time'] = completion_time
            sorted_processes[i]['turnaround_time'] = turnaround_time
            sorted_processes[i]['waiting_time'] = waiting_time
            
            # Add to Gantt chart
            gantt_chart.append((f"P{p['pid']}", start_time, completion_time))
            current_time = completion_time
        
        # Display results
        self.calculate_metrics(sorted_processes)
        self.display_gantt_chart(gantt_chart)
        
        return sorted_processes

    def sjf_scheduling(self):
        """Shortest Job First Scheduling (Non-preemptive)"""
        print("\n" + "=" * 60)
        print("SHORTEST JOB FIRST (SJF) SCHEDULING")
        print("=" * 60)
        
        processes = self.processes.copy()
        n = len(processes)
        completed = 0
        current_time = 0
        gantt_chart = []
        
        # Initialize process metrics
        for p in processes:
            p['completed'] = False
            p['waiting_time'] = 0
            p['turnaround_time'] = 0
            p['completion_time'] = 0
        
        while completed < n:
            # Find processes that have arrived and not completed
            available = [p for p in processes if p['arrival_time'] <= current_time and not p['completed']]
            
            if not available:
                current_time += 1
                continue
            
            # Select process with shortest burst time
            next_process = min(available, key=lambda x: x['burst_time'])
            pid = next_process['pid'] - 1
            
            # Calculate times
            start_time = current_time
            completion_time = start_time + next_process['burst_time']
            turnaround_time = completion_time - next_process['arrival_time']
            waiting_time = start_time - next_process['arrival_time']
            
            # Update process info
            processes[pid]['completion_time'] = completion_time
            processes[pid]['turnaround_time'] = turnaround_time
            processes[pid]['waiting_time'] = waiting_time
            processes[pid]['completed'] = True
            
            # Add to Gantt chart
            gantt_chart.append((f"P{next_process['pid']}", start_time, completion_time))
            current_time = completion_time
            completed += 1
        
        # Display results
        self.calculate_metrics(processes)
        self.display_gantt_chart(gantt_chart)
        
        return processes

    def priority_scheduling(self):
        """Priority Scheduling (Non-preemptive)"""
        print("\n" + "=" * 60)
        print("PRIORITY SCHEDULING (Non-preemptive)")
        print("=" * 60)
        
        processes = self.processes.copy()
        n = len(processes)
        completed = 0
        current_time = 0
        gantt_chart = []
        
        # Initialize process metrics
        for p in processes:
            p['completed'] = False
            p['waiting_time'] = 0
            p['turnaround_time'] = 0
            p['completion_time'] = 0
        
        while completed < n:
            # Find processes that have arrived and not completed
            available = [p for p in processes if p['arrival_time'] <= current_time and not p['completed']]
            
            if not available:
                current_time += 1
                continue
            
            # Select process with highest priority (lowest priority number)
            next_process = min(available, key=lambda x: x['priority'])
            pid = next_process['pid'] - 1
            
            # Calculate times
            start_time = current_time
            completion_time = start_time + next_process['burst_time']
            turnaround_time = completion_time - next_process['arrival_time']
            waiting_time = start_time - next_process['arrival_time']
            
            # Update process info
            processes[pid]['completion_time'] = completion_time
            processes[pid]['turnaround_time'] = turnaround_time
            processes[pid]['waiting_time'] = waiting_time
            processes[pid]['completed'] = True
            
            # Add to Gantt chart
            gantt_chart.append((f"P{next_process['pid']}", start_time, completion_time))
            current_time = completion_time
            completed += 1
        
        # Display results
        self.calculate_metrics(processes)
        self.display_gantt_chart(gantt_chart)
        
        return processes

    def round_robin_scheduling(self):
        """Round Robin Scheduling"""
        print("\n" + "=" * 60)
        print("ROUND ROBIN SCHEDULING")
        print("=" * 60)
        
        time_quantum = int(input("Enter time quantum: "))
        
        processes = self.processes.copy()
        n = len(processes)
        completed = 0
        current_time = 0
        gantt_chart = []
        
        # Initialize process metrics
        for p in processes:
            p['remaining_time'] = p['burst_time']
            p['waiting_time'] = 0
            p['turnaround_time'] = 0
            p['completion_time'] = 0
            p['started'] = False
        
        queue = []
        while completed < n:
            # Add processes that have arrived to queue
            for p in processes:
                if (p['arrival_time'] <= current_time and 
                    not p['started'] and 
                    p['remaining_time'] > 0 and
                    p not in queue):
                    queue.append(p)
                    p['started'] = True
            
            if not queue:
                current_time += 1
                continue
            
            # Get next process from queue
            current_process = queue.pop(0)
            pid = current_process['pid'] - 1
            
            # Execute process for time quantum or remaining time
            start_time = current_time
            execution_time = min(time_quantum, current_process['remaining_time'])
            completion_time = start_time + execution_time
            
            # Add to Gantt chart
            gantt_chart.append((f"P{current_process['pid']}", start_time, completion_time))
            
            # Update remaining time
            current_process['remaining_time'] -= execution_time
            current_time = completion_time
            
            # Add processes that arrived during execution
            for p in processes:
                if (p['arrival_time'] <= current_time and 
                    not p['started'] and 
                    p['remaining_time'] > 0 and
                    p not in queue):
                    queue.append(p)
                    p['started'] = True
            
            # If process not completed, add back to queue
            if current_process['remaining_time'] > 0:
                queue.append(current_process)
            else:
                # Process completed
                current_process['completion_time'] = current_time
                current_process['turnaround_time'] = current_time - current_process['arrival_time']
                current_process['waiting_time'] = current_process['turnaround_time'] - current_process['burst_time']
                completed += 1
        
        # Display results
        self.calculate_metrics(processes)
        self.display_gantt_chart(gantt_chart)
        
        return processes

    def display_gantt_chart(self, gantt_chart):
        """Display Gantt chart"""
        print("\nGANTT CHART:")
        print("-" * 50)
        
        # Print top line
        for process, start, end in gantt_chart:
            print(f" {process} ", end="")
        print()
        
        # Print timeline
        print("0", end="")
        for process, start, end in gantt_chart:
            print(f"---{end}", end="")
        print()

    def compare_algorithms(self):
        """Compare all scheduling algorithms"""
        print("\n" + "=" * 70)
        print("COMPARISON OF ALL SCHEDULING ALGORITHMS")
        print("=" * 70)
        
        results = {}
        
        # Run all algorithms
        results['FCFS'] = self.fcfs_scheduling()
        results['SJF'] = self.sjf_scheduling()
        results['Priority'] = self.priority_scheduling()
        results['Round Robin'] = self.round_robin_scheduling()
        
        # Calculate averages for comparison
        print("\n" + "=" * 70)
        print("SUMMARY COMPARISON")
        print("=" * 70)
        print("Algorithm\t\tAvg Waiting Time\tAvg Turnaround Time")
        print("-" * 70)
        
        comparison_data = []
        for algo_name, processes in results.items():
            avg_wt = sum(p['waiting_time'] for p in processes) / len(processes)
            avg_tat = sum(p['turnaround_time'] for p in processes) / len(processes)
            comparison_data.append((algo_name, avg_wt, avg_tat))
            print(f"{algo_name:<20}{avg_wt:<20.2f}{avg_tat:<20.2f}")
        
        # Find best algorithm
        best_wt = min(comparison_data, key=lambda x: x[1])
        best_tat = min(comparison_data, key=lambda x: x[2])
        
        print("\n" + "-" * 70)
        print(f"Best for Waiting Time: {best_wt[0]} (Avg WT: {best_wt[1]:.2f})")
        print(f"Best for Turnaround Time: {best_tat[0]} (Avg TAT: {best_tat[2]:.2f})")

    def main_menu(self):
        """Main menu for CPU scheduling simulator"""
        while True:
            print("\n" + "=" * 60)
            print("CPU SCHEDULING ALGORITHMS SIMULATOR")
            print("=" * 60)
            print("1. Input Custom Processes")
            print("2. Use Sample Processes")
            print("3. First Come First Serve (FCFS)")
            print("4. Shortest Job First (SJF)")
            print("5. Priority Scheduling")
            print("6. Round Robin Scheduling")
            print("7. Compare All Algorithms")
            print("8. Exit")
            
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '1':
                self.input_processes()
            elif choice == '2':
                self.sample_processes()
            elif choice == '3':
                if not self.processes:
                    print("No processes loaded. Using sample processes.")
                    self.sample_processes()
                self.fcfs_scheduling()
            elif choice == '4':
                if not self.processes:
                    print("No processes loaded. Using sample processes.")
                    self.sample_processes()
                self.sjf_scheduling()
            elif choice == '5':
                if not self.processes:
                    print("No processes loaded. Using sample processes.")
                    self.sample_processes()
                self.priority_scheduling()
            elif choice == '6':
                if not self.processes:
                    print("No processes loaded. Using sample processes.")
                    self.sample_processes()
                self.round_robin_scheduling()
            elif choice == '7':
                if not self.processes:
                    print("No processes loaded. Using sample processes.")
                    self.sample_processes()
                self.compare_algorithms()
            elif choice == '8':
                print("Exiting CPU Scheduling Simulator.")
                break
            else:
                print("Invalid choice! Please enter 1-8.")
            
            input("\nPress Enter to continue...")

def main():
    """Main function"""
    scheduler = CPUScheduler()
    scheduler.main_menu()

if __name__ == "__main__":
    main()
