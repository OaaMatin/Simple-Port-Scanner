import socket

print("\n\"Simple Port Scanner\"\n")

ip_address = input("Enter IP: ")

start_port = int(input("Enter Start Port: "))

end_port = int(input("Enter End Port: "))

for port in range(start_port, end_port + 1):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    res = scanner.connect_ex((ip_address, port))
    if res == 0:
        print(f"port {port} is OPEN")
    scanner.close()