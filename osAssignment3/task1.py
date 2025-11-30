
def priority_scheduling():
    """Priority Scheduling Algorithm"""
    print("=== Priority Scheduling ===")

    processes = [
        (1, 10, 3),  
        (2, 5, 1),
        (3, 8, 2)
    ]

    processes.sort(key=lambda x: x[2])
    wt = 0
    total_wt = 0
    total_tt = 0
    
    print("\nPriority Scheduling Results:")
    print("PID\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    
    gantt_chart = []
    current_time = 0
    
    for pid, bt, pr in processes:
        tat = wt + bt
        print(f"P{pid}\t{bt}\t\t{pr}\t\t{wt}\t\t{tat}")
        gantt_chart.append((f"P{pid}", current_time, current_time + bt))
        current_time += bt
        
        total_wt += wt
        total_tt += tat
        wt += bt
    print(f"\nAverage Waiting Time: {total_wt / len(processes):.2f}")
    print(f"Average Turnaround Time: {total_tt / len(processes):.2f}")
    print("\nGantt Chart:")
    for process, start, end in gantt_chart:
        print(f"{process}: [{start}-{end}]", end=" ")
    print()

def round_robin_scheduling():
    """Round Robin Scheduling Algorithm"""
    print("\n=== Round Robin Scheduling ===")
    processes = [
        [1, 10, 0],  
        [2, 5, 0],
        [3, 8, 0]
    ]
    time_quantum = 3
    n = len(processes)
    remaining_bt = [process[1] for process in processes]
    wt = [0] * n
    tat = [0] * n
    current_time = 0
    completed = 0
    gantt_chart = []
    while completed < n:
        for i in range(n):
            if remaining_bt[i] > 0:
                if remaining_bt[i] > time_quantum:
                    gantt_chart.append((f"P{processes[i][0]}", current_time, current_time + time_quantum))
                    current_time += time_quantum
                    remaining_bt[i] -= time_quantum
                else:
                    gantt_chart.append((f"P{processes[i][0]}", current_time, current_time + remaining_bt[i]))
                    current_time += remaining_bt[i]
                    wt[i] = current_time - processes[i][1]
                    remaining_bt[i] = 0
                    completed += 1
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]
    print("\nRound Robin Scheduling Results:")
    print("PID\tBurst Time\tWaiting Time\tTurnaround Time")
    total_wt = 0
    total_tat = 0
    
    for i in range(n):
        print(f"P{processes[i][0]}\t{processes[i][1]}\t\t{wt[i]}\t\t{tat[i]}")
        total_wt += wt[i]
        total_tat += tat[i]
    
    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")
    print("\nGantt Chart:")
    for process, start, end in gantt_chart:
        print(f"{process}: [{start}-{end}]", end=" ")
    print()

def main():
    """Main function for CPU scheduling"""
    print("CPU Scheduling Algorithms - Demonstration")
    print("Using sample data:")
    print("Processes: P1(10,3), P2(5,1), P3(8,2)")
    print("Time Quantum: 3")
    
    priority_scheduling()
    round_robin_scheduling()

if __name__ == "__main__":
    main()
