import socket
import time

print("\n\"Simple-Port-Scanner\"\n")

ip_address = input("Enter IP: ")

start_port = int(input("Enter Start Port: "))

end_port = int(input("Enter End Port: "))

if end_port < start_port:
    end_port, start_port = start_port, end_port

open_ports = 0

print("\nStart scanning...\n")

start_time = time.perf_counter()

for port in range(start_port, end_port + 1):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    res = scanner.connect_ex((ip_address, port))
    if res == 0:
        print(f"Port {port} is OPEN")
        open_ports += 1
    scanner.close()
end_time = time.perf_counter()

if open_ports == 0:
    print("\nNo open ports found.\n")
else:
    port_word = "port" if open_ports == 1 else "ports"
    print(f"\nFound {open_ports} open {port_word}.\n")

latency = end_time - start_time
print(f"Scan completed in {latency:.3f} seconds.")