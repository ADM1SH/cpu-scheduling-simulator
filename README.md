# Mini OS Sim

[![C++](https://img.shields.io/Language-C%2B%2B17-00599C.svg?logo=cplusplus)](https://github.com/ADM1SH/cpu-scheduling-simulator)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/ADM1SH/cpu-scheduling-simulator)](https://github.com/ADM1SH/cpu-scheduling-simulator/issues)


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

**Easiest : run script:**

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

- `scheduler.py` : process model, all six scheduling algorithms, and the interactive menu
- `test_scheduler.py` : assert-based self-check
- `run.sh` : convenience launcher for `scheduler.py`

## Support
Submit issues, questions, or bug reports to the GitHub issue tracker:
https://github.com/ADM1SH/cpu-scheduling-simulator/issues


## Roadmap
* [x] Core architecture and baseline implementation.
* [x] Functional verification and test coverage.
* [ ] Add multi-level feedback queue (MLFQ) algorithm
* [ ] Implement memory paging and TLB hit/miss simulation


## Contributing
Contributions are welcome.
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/improvement`.
3. Commit your changes: `git commit -m "feat: enhance functionality"`.
4. Push to the branch: `git push origin feature/improvement`.
5. Open a Pull Request.


## Authors and Acknowledgment
* **Adam Anwar** (ADM1SH) - Lead architect and developer.
* Designed by Adam Anwar for OS scheduling theory and process lifecycle study.


## License
Licensed under the MIT License. See `LICENSE` for details.


## Project Status
Completed systems simulation project. Stable and verified.
