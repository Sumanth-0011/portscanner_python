import socket
import threading
import argparse
from queue import Queue
import time

# Thread safe queue for storing open ports
queue = Queue()
open_ports = []

def port_scan(target, port):
    """Attempt to connect to a specific port."""
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Short timeout for speed
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    except:
        pass

def worker():
    """Worker thread that pulls ports from the queue."""
    while not queue.empty():
        port = queue.get()
        port_scan(target_ip, port)
        queue.task_done()

if __name__ == "__main__":
    # Setup command line arguments
    parser = argparse.ArgumentParser(description="Simple Multi-threaded Port Scanner")
    parser.add_argument("target", help="IP address or domain to scan")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
    args = parser.parse_args()

    target_ip = args.target
    start_port = args.start
    end_port = args.end
    thread_count = args.threads

    print(f"[*] Scanning target: {target_ip}")
    print(f"[*] Scanning range: {start_port}-{end_port} with {thread_count} threads")
    start_time = time.time()

    # Fill the queue
    for port in range(start_port, end_port + 1):
        queue.put(port)

    # Spawn threads
    thread_list = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker)
        thread_list.append(t)
        t.start()

    # Wait for all threads to finish
    for t in thread_list:
        t.join()

    print(f"\n[*] Scan completed in {time.time() - start_time:.2f} seconds")
    print(f"[*] Open ports: {sorted(open_ports)}")