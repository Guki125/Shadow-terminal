import socket

def check_port(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)
    try:
        client.connect((ip, port))
        client.close()
        return True
    except:
        client.close()
        return False
    
if __name__ == "__main__":
    ip = input("Type ip or DNS name: ")
    port = int(input("Type port for checking: "))

    if check_port(ip, port):
        print(f"Port: {port} is open") 
    else:
        print(f"Port: {port} is close")
