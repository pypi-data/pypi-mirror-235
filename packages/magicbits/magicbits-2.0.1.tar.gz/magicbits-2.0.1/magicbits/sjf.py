from typing import List
from tabulate import tabulate

class Process:
    def __init__(self,id,arrival_time,burst_time):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time

def sjf_scheduling(processes: List[Process]) :
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    current_time, waiting_time, total_waiting = (0,0,0)
    proc_state = []

    for process in processes:
        if process.arrival_time>current_time:
            current_time=process.arrival_time
        waiting_time = current_time - process.arrival_time
        total_waiting += waiting_time
        proc_state.append([process.id, process.arrival_time, process.burst_time, waiting_time])
        current_time += process.burst_time   
    
    print(tabulate(proc_state, headers=("Process", "Arrival Time", "Burst Time", "Waiting Time"),
                    stralign="center", numalign="center", tablefmt='psql'))
    average_waiting = total_waiting / len(processes)
    print(f"\nAverage Waiting Time : {average_waiting:.2f}")

if __name__ == '__main__':
    process = [Process("P1",5,8),Process("P2",0,5),Process("P3",4,9),Process("P4",1,2)]    
    sjf_scheduling(process)        
