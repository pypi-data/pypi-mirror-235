# round robin implementation in python
def roundrobin_scheduling(processes: dict , time_quantum = 2):
    n = len(processes.keys())
    ids = list(processes.keys())
    burst_time = list(processes.values())
    remaining_burst_time = burst_time.copy()
    current_time, total_wt, total_turnaround_time = (0,0,0)
    queue = []

    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False
                if remaining_burst_time[i] > time_quantum:
                    current_time += time_quantum
                    remaining_burst_time[i]-=time_quantum
                else:
                    current_time += remaining_burst_time[i]
                    total_turnaround_time += current_time
                    total_wt += current_time - burst_time[i]
                    remaining_burst_time[i] = 0
                    queue.append(ids[i])
        if done:
            break
    average_waiting_time = total_wt / n
    average_turnaround_time = total_turnaround_time / n
    return (queue, average_waiting_time, average_turnaround_time)

if __name__ == "__main__":
    processes = {"P1": 10, "P2": 5, "P3": 8, "P4": 12}
    QUEUE, AWT, ATAT = roundrobin_scheduling(processes, time_quantum=2)

    print("Queue", QUEUE)
    print("Average waiting time: ", AWT)
    print("Average turnaround time: ", ATAT)