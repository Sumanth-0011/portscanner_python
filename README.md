Name:G Sumanth
Project Name: port scanner(python)
NO OF WEEKS: 6 weeks 
Project Scope:Multi-Threaded Port Scanner
Intern ID:CITS2197



# Python Multi-Threaded Port Scanner

A high-performance, multi-threaded port scanner built in Python. This tool is designed to identify open network ports on a target IP or domain, helping users understand network topology and identify potential entry points for security analysis.

## Features

- **Multi-threaded Architecture:** Uses a `Queue` and `threading` to scan multiple ports concurrently, significantly reducing total scan time.
- **Configurable Range:** Users can define specific starting and ending ports.
- **Performance Tuning:** Adjustable thread count allows users to balance speed against system resource usage.
- **Command-Line Interface:** Implemented using `argparse` for professional-grade terminal interaction.
- **Robustness:** Includes basic error handling to ensure network timeouts or connection refusals do not crash the script.

## Technical Implementation

- **Language:** Python 3.x
- **Libraries Used:** - `socket`: Handles the networking and TCP connections.
  - `threading`: Manages concurrency for faster scanning.
  - `queue`: Safely coordinates work between threads.
  - `argparse`: Parses command-line arguments.

## How it Works

The script performs a **TCP Connect Scan**. It attempts to establish a full three-way handshake with the target port.
1. The scanner creates a TCP socket.
2. It attempts to connect to the target IP at the specified port.
3. If the connection is successful (`result == 0`), the port is marked as "Open".
4. The scanner uses a `Queue` to distribute ports to a pool of worker threads, ensuring efficient execution.



## Usage

1. Open your terminal or command prompt.
2. Run the script using the following command structure:

```bash
python portscanner.py <target_ip_or_domain> -s <start_port> -e <end_port> -t <thread_count># portscanner_python
Security & Ethical Warning CRITICAL: This tool is for educational and authorized security testing purposes only. Running a port scanner against devices, networks, or servers you do not own or do not have explicit written permission to test is illegal and may violate company policy or local laws. Always ensure you have the proper authorization before performing any network scans.

License
This project is open-source and intended for learning purposes.
