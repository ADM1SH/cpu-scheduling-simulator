"""Mini OS CPU scheduling simulator: FCFS, SJF (P/NP), Priority (P/NP), Round Robin."""
from dataclasses import dataclass, field
from collections import deque
from typing import List, Tuple

Gantt = List[Tuple[str, int, int]]  # (pid, start, end)


@dataclass
class Process:
    pid: str
    arrival: int
    burst: int
    priority: int = 0  # lower number = higher priority
    remaining: int = field(init=False)
    completion: int = field(init=False, default=0)

    def __post_init__(self):
        self.remaining = self.burst


def _clone(procs: List[Process]) -> List[Process]:
    return [Process(p.pid, p.arrival, p.burst, p.priority) for p in procs]


def fcfs(procs: List[Process]) -> Gantt:
    procs = sorted(procs, key=lambda p: p.arrival)
    time, gantt = 0, []
    for p in procs:
        time = max(time, p.arrival)
        gantt.append((p.pid, time, time + p.burst))
        time += p.burst
        p.completion = time
    return gantt


def _non_preemptive(procs: List[Process], key) -> Gantt:
    time, gantt = 0, []
    remaining = list(procs)
    while remaining:
        available = [p for p in remaining if p.arrival <= time]
        if not available:
            time = min(p.arrival for p in remaining)
            continue
        p = min(available, key=key)
        gantt.append((p.pid, time, time + p.burst))
        time += p.burst
        p.completion = time
        remaining.remove(p)
    return gantt


def sjf_non_preemptive(procs: List[Process]) -> Gantt:
    return _non_preemptive(procs, key=lambda p: (p.burst, p.arrival))


def priority_non_preemptive(procs: List[Process]) -> Gantt:
    return _non_preemptive(procs, key=lambda p: (p.priority, p.arrival))


def _preemptive(procs: List[Process], key) -> Gantt:
    time, gantt = 0, []
    n = len(procs)
    completed = 0
    while completed < n:
        available = [p for p in procs if p.arrival <= time and p.remaining > 0]
        if not available:
            time += 1
            continue
        p = min(available, key=key)
        p.remaining -= 1
        if gantt and gantt[-1][0] == p.pid and gantt[-1][2] == time:
            gantt[-1] = (p.pid, gantt[-1][1], time + 1)
        else:
            gantt.append((p.pid, time, time + 1))
        time += 1
        if p.remaining == 0:
            p.completion = time
            completed += 1
    return gantt


def sjf_preemptive(procs: List[Process]) -> Gantt:
    return _preemptive(procs, key=lambda p: (p.remaining, p.arrival))


def priority_preemptive(procs: List[Process]) -> Gantt:
    return _preemptive(procs, key=lambda p: (p.priority, p.arrival))


def round_robin(procs: List[Process], quantum: int = 3) -> Gantt:
    procs = sorted(procs, key=lambda p: p.arrival)
    n = len(procs)
    queue: deque = deque()
    time, i, completed = 0, 0, 0
    gantt = []
    while completed < n:
        while i < n and procs[i].arrival <= time:
            queue.append(procs[i])
            i += 1
        if not queue:
            time = procs[i].arrival
            continue
        p = queue.popleft()
        run = min(quantum, p.remaining)
        gantt.append((p.pid, time, time + run))
        time += run
        p.remaining -= run
        while i < n and procs[i].arrival <= time:
            queue.append(procs[i])
            i += 1
        if p.remaining > 0:
            queue.append(p)
        else:
            p.completion = time
            completed += 1
    return gantt


ALGORITHMS = {
    "a": ("Round Robin (quantum 3)", lambda ps: round_robin(ps, 3)),
    "b": ("Preemptive SJF", sjf_preemptive),
    "c": ("Non-Preemptive SJF", sjf_non_preemptive),
    "d": ("Preemptive Priority", priority_preemptive),
    "e": ("Non-Preemptive Priority", priority_non_preemptive),
    "f": ("First Come First Serve", fcfs),
}


def summarize(name: str, gantt: Gantt, procs: List[Process]) -> None:
    print(f"\n=== {name} ===")
    print("Gantt chart:")
    print(" | ".join(f"{pid}[{s}-{e}]" for pid, s, e in gantt))

    print(f"\n{'PID':<5}{'Arrival':<9}{'Burst':<7}{'Completion':<12}{'Turnaround':<12}{'Waiting':<8}")
    total_tat = total_wait = 0
    for p in sorted(procs, key=lambda p: p.pid):
        tat = p.completion - p.arrival
        wait = tat - p.burst
        total_tat += tat
        total_wait += wait
        print(f"{p.pid:<5}{p.arrival:<9}{p.burst:<7}{p.completion:<12}{tat:<12}{wait:<8}")
    n = len(procs)
    print(f"\nAverage turnaround time: {total_tat / n:.2f}")
    print(f"Average waiting time:    {total_wait / n:.2f}")


def default_processes() -> List[Process]:
    return [
        Process("P1", arrival=0, burst=5, priority=3),
        Process("P2", arrival=1, burst=3, priority=1),
        Process("P3", arrival=2, burst=8, priority=4),
        Process("P4", arrival=3, burst=6, priority=2),
    ]


def input_processes() -> List[Process]:
    try:
        n = int(input("Number of processes: "))
    except ValueError:
        print("Invalid number, using default process set.")
        return default_processes()
    procs = []
    for i in range(n):
        pid = f"P{i + 1}"
        arrival = int(input(f"{pid} arrival time: "))
        burst = int(input(f"{pid} burst time: "))
        priority = input(f"{pid} priority (lower = higher, default 0): ").strip()
        procs.append(Process(pid, arrival, burst, int(priority) if priority else 0))
    return procs


def run_menu() -> None:
    print("=== Mini OS: CPU Scheduling Simulator ===")
    choice = input("Enter processes manually? (y/N): ").strip().lower()
    procs = input_processes() if choice == "y" else default_processes()

    while True:
        print("\nAlgorithms:")
        for key, (name, _) in ALGORITHMS.items():
            print(f"  {key}) {name}")
        print("  g) Run all and compare")
        print("  q) Quit")
        choice = input("Select: ").strip().lower()

        if choice == "q":
            break
        elif choice == "g":
            for key, (name, algo) in ALGORITHMS.items():
                run = _clone(procs)
                summarize(name, algo(run), run)
        elif choice in ALGORITHMS:
            name, algo = ALGORITHMS[choice]
            run = _clone(procs)
            summarize(name, algo(run), run)
        else:
            print("Unknown option.")


if __name__ == "__main__":
    run_menu()
