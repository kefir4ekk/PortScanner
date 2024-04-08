import socket

def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
    except:
        service_name = "Unknown"
    return service_name

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            service_name = get_service_name(port)
            print(f"Port {port} ({service_name}) is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
    except socket.error:
        print(f"Could not connect to Port {port}")

def scan(target, start_port, end_port):
    open_ports = []
    print(f"Scanning {target} for open ports...")
    for port in range(start_port, end_port+1):
        if scan_port(target, port) == 0:
            open_ports.append(port)
    return open_ports

target = input('Enter target IP - ')
start_port = int(input('Enter start port - '))
end_port = int(input('Enter end port - '))

open_ports = scan(target, start_port, end_port)
print(f"\nSummary: {len(open_ports)} open ports found on {target} - {', '.join([str(port) for port in open_ports])}")

# This code scans ports from start_port to end_port on the specified target. Please note that port scanning он remote systems without permission from the system owner may violate security laws. Use this code only for testing on your own systems or with appropriate permission.