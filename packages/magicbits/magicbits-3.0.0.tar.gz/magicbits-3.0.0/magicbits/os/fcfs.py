from tabulate import tabulate

def fcfs_scheduling(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n

    for i in range(n-1):
        completion_time[i]+=processes[i][1]

        next = processes[i+1][1] + completion_time[i]

        completion_time[i+1] = next

    print(completion_time)
    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_time[i] = processes[i - 1][1] + waiting_time[i - 1]


    average_waiting_time = sum(waiting_time) / n
    average_turnaround_time = sum(turnaround_time) / n

    data = []
    for id, i in enumerate(range(n), start=1):
        data.append([f'P{id}', processes[i][0], processes[i][1], waiting_time[i], turnaround_time[i]])

    headers = ["Process", "Arrival Time", "Burst Time", "Waiting Time", "Turnaround Time"]
    table = tabulate(data, headers=headers, tablefmt="psql", numalign='center', stralign='center')
    print(table)
    print(f"Average Waiting Time: {average_waiting_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

if __name__ == "__main__":
    #sample input: list of tuples with arrival time and burst time for each process
    processes=[(0,6),(3,2),(5,1),(9,7),(10,5)]
    fcfs_scheduling(processes)