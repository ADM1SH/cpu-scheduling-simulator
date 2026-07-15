"""Self-check: hand-computed expected schedules for a fixed process set."""
from scheduler import (
    Process, fcfs, sjf_non_preemptive, sjf_preemptive,
    priority_non_preemptive, priority_preemptive, round_robin,
)


def procs():
    return [
        Process("P1", arrival=0, burst=5, priority=3),
        Process("P2", arrival=1, burst=3, priority=1),
        Process("P3", arrival=2, burst=8, priority=4),
        Process("P4", arrival=3, burst=6, priority=2),
    ]


def completions(ps):
    return {p.pid: p.completion for p in ps}


def test_fcfs():
    ps = procs()
    gantt = fcfs(ps)
    assert gantt == [("P1", 0, 5), ("P2", 5, 8), ("P3", 8, 16), ("P4", 16, 22)]
    assert completions(ps) == {"P1": 5, "P2": 8, "P3": 16, "P4": 22}


def test_sjf_non_preemptive():
    ps = procs()
    gantt = sjf_non_preemptive(ps)
    assert gantt == [("P1", 0, 5), ("P2", 5, 8), ("P4", 8, 14), ("P3", 14, 22)]
    assert completions(ps) == {"P1": 5, "P2": 8, "P4": 14, "P3": 22}


def test_sjf_preemptive():
    ps = procs()
    gantt = sjf_preemptive(ps)
    assert gantt == [("P1", 0, 1), ("P2", 1, 4), ("P1", 4, 8), ("P4", 8, 14), ("P3", 14, 22)]
    assert completions(ps) == {"P1": 8, "P2": 4, "P4": 14, "P3": 22}


def test_priority_non_preemptive():
    ps = procs()
    gantt = priority_non_preemptive(ps)
    assert gantt == [("P1", 0, 5), ("P2", 5, 8), ("P4", 8, 14), ("P3", 14, 22)]
    assert completions(ps) == {"P1": 5, "P2": 8, "P4": 14, "P3": 22}


def test_priority_preemptive():
    ps = procs()
    gantt = priority_preemptive(ps)
    assert gantt == [("P1", 0, 1), ("P2", 1, 4), ("P4", 4, 10), ("P1", 10, 14), ("P3", 14, 22)]
    assert completions(ps) == {"P1": 14, "P2": 4, "P4": 10, "P3": 22}


def test_round_robin():
    ps = procs()
    gantt = round_robin(ps, quantum=3)
    assert gantt == [
        ("P1", 0, 3), ("P2", 3, 6), ("P3", 6, 9), ("P4", 9, 12),
        ("P1", 12, 14), ("P3", 14, 17), ("P4", 17, 20), ("P3", 20, 22),
    ]
    assert completions(ps) == {"P1": 14, "P2": 6, "P3": 22, "P4": 20}


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print(f"PASS {name}")
    print("All scheduler tests passed.")
