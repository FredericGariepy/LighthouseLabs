import socket
from concurrent import futures

def verify_port(targetIp, p_Number, timeout):
    # Create a TCP socket
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set socket option to reuse the address
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Set socket timeout for connection attempt
    TCPsock.settimeout(timeout)
    try:
        # Attempt to connect to the specified IP address and port
        TCPsock.connect((targetIp, p_Number))
        # If connection succeeds, return the port number
        return p_Number
    except:
        # If connection fails (or times out), return None implicitly
        return

def find_port(targetIp, timeout):
    # Number of threads to use
    tpSize = 500
    # Total number of ports to check
    portsToCheck = 10000

    # Create a ThreadPoolExecutor with specified number of workers
    executor = futures.ThreadPoolExecutor(max_workers=tpSize)
    # List to hold futures (results) of port verification tasks
    checks = [
        executor.submit(verify_port, targetIp, port, timeout)
        for port in range(0, portsToCheck, 1)
    ]

    # Iterate through completed futures as they become available
    for response in futures.as_completed(checks):
        # Check if the port number is returned (not None)
        if response.result():
            # Print port number with status if connection succeeded
            print('Port: {}'.format(response.result()), " - Ok")

def main():
    # Prompt user to enter IP address to test
    targetIp = input("Enter IP address to test: ")
    # Prompt user to enter timeout duration in seconds
    timeout = int(input("Timeout connection in seconds: "))
    # Call find_port function with user input
    find_port(targetIp, timeout)

if __name__ == "__main__":
    main()
