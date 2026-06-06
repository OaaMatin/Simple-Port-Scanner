import argparse
import socket
import sys
import time
import json

from concurrent.futures import ThreadPoolExecutor

def get_args():
    parser = argparse.ArgumentParser(
        description="Simple Multi-threaded TCP Port Scanner"
    )

    parser.add_argument("host", help="Target host or IP address")
    parser.add_argument("start", type=int, help="Start port number")
    parser.add_argument("end", type=int, help="End port number")
    parser.add_argument(
        "--threads",
        type=int,
        default=100,
        help="Number of worker threads (default: 100)",
    )
    parser.add_argument("--output", help="Save scan results to a JSON file")

    return parser.parse_args()


def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
        scanner.settimeout(1)
        return scanner.connect_ex((ip, port)) == 0

print('\n"Simple-Port-Scanner"\n')

args = get_args()
thread_count = args.threads
if thread_count < 1 or thread_count > 1000:
    print("\nThread count must be between 1 and 1000.\n")
    sys.exit(1)
output_file = args.output

try:
    host_ip = args.host
    resolved_ip = socket.gethostbyname(host_ip)
    print(f"\nResolved IP: {resolved_ip}\n")
except socket.gaierror:
    print("\nInvalid host or IP address!\n")
    sys.exit(1)


start_port = args.start
if start_port < 0 or start_port > 65535:
    print("\nPort must be between 0 and 65535.\n")
    sys.exit(1)

end_port = args.end
if end_port < 0 or end_port > 65535:
    print("\nPort must be between 0 and 65535.\n")
    sys.exit(1)

if end_port < start_port:
    end_port, start_port = start_port, end_port

print("\nStarting scan...\n")

open_ports = 0
open_ports_list = []

start_time = time.perf_counter()

with ThreadPoolExecutor(max_workers=thread_count) as executor:
    future_to_port = {}

    for port in range(start_port, end_port + 1):
        future = executor.submit(scan_port, resolved_ip, port)
        future_to_port[future] = port

    for future in future_to_port:
        port = future_to_port[future]
        if future.result():
            print(f"    Port {port} is open.")
            open_ports += 1
            open_ports_list.append(port)

end_time = time.perf_counter()

if open_ports == 0:
    print("\nNo open ports found.")
else:
    port_word = "port" if open_ports == 1 else "ports"
    print(f"\nFound {open_ports} open {port_word}.")

latency = end_time - start_time
print(f"\nScan completed in {latency:.3f} seconds.\n")

results = {
    "host": host_ip,
    "resolved_ip": resolved_ip,
    "open_ports": open_ports_list,
    "total_open_ports": open_ports,
    "scan_duration": round(latency, 3),
    "thread_count": thread_count,
}

if output_file:
    with open(output_file, "w") as file:
        json.dump(results, file, indent=4)

    print(f"Results saved to {output_file}\n")