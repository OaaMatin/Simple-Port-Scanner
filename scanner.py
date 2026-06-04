import socket
import time
import sys
from concurrent.futures import ThreadPoolExecutor

def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
        scanner.settimeout(1)
        return scanner.connect_ex((resolved_ip, port)) == 0

print('\n"Simple-Port-Scanner"\n')

try:
    host_ip = input("Enter host or IP: ")
    resolved_ip = socket.gethostbyname(host_ip)
    print(f"\nResolved IP: {resolved_ip}\n")
except socket.gaierror:
    print("\nInvalid host or IP address!\n")
    sys.exit(1)

try:
    start_port = int(input("Enter Start Port: "))
except ValueError:
    print("\nInvalid input!\n")
    sys.exit(1)
if start_port < 0 or start_port > 65535:
    print("\nPort must be between 0 and 65535.\n")
    sys.exit(1)

try:
    end_port = int(input("Enter End Port: "))
except ValueError:
    print("\nInvalid input!\n")
    sys.exit(1)
if end_port < 0 or end_port > 65535:
    print("\nPort must be between 0 and 65535.\n")
    sys.exit(1)

if end_port < start_port:
    end_port, start_port = start_port, end_port

print("\nStart scanning...\n")

open_ports = 0

start_time = time.perf_counter()

with ThreadPoolExecutor(max_workers=100) as executor:
    future_to_port = {}

    for port in range(start_port, end_port + 1):
        future = executor.submit(scan_port, port)
        future_to_port[future] = port

    for future in future_to_port:
        port = future_to_port[future]
        if future.result():
            print(f"    Port {port} is open.")
            open_ports += 1

end_time = time.perf_counter()

if open_ports == 0:
    print("\nNo open ports found.")
else:
    port_word = "port" if open_ports == 1 else "ports"
    print(f"\nFound {open_ports} open {port_word}.")

latency = end_time - start_time
print(f"\nScan completed in {latency:.3f} seconds.\n")
