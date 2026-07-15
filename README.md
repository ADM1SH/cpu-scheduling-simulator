# Mini OS Sim

A small Python simulator of a mini operating system's CPU scheduler. It demonstrates six scheduling algorithms over the same set of processes and prints a Gantt chart plus turnaround/waiting time stats for each.

## Algorithms

- Round Robin (quantum 3)
- Preemptive SJF (Shortest Job First / SRTF)
- Non-Preemptive SJF
- Preemptive Priority
- Non-Preemptive Priority
- First Come First Serve (FCFS)

## Requirements

- Python 3.7+ (no external packages)

## How to run

**Easiest — run script:**

```bash
./run.sh
```

**Or directly with Python:**

```bash
python3 scheduler.py
```

Either way, you'll be asked whether to enter processes manually or use the built-in sample set, then shown a menu to run any single algorithm or all six at once (`g`).

## Running the tests

```bash
python3 test_scheduler.py
```

Checks every algorithm's output against a hand-computed 4-process example.

## Files

- `scheduler.py` — process model, all six scheduling algorithms, and the interactive menu
- `test_scheduler.py` — assert-based self-check
- `run.sh` — convenience launcher for `scheduler.py`
