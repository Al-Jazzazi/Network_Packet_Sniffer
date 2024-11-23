import socket
import struct
from packet_parser import parse_packet

def sniff_packets():
    try:
        # Create a raw socket
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP) as sock:
            # Bind to the IP address of the active interface
            host = "172.20.10.5".strip()
            port = 0 
            sock.bind((host, port))

            # Include IP headers in the captured packets
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

            print("Listening for packets on en0 " + host +  "... Press Ctrl+C to stop.")
            while True:
                # Capture a single packet
                packet, addr = sock.recvfrom(65535)
                print(f"Packet received from {addr}:")
                parse_packet(packet)
    except KeyboardInterrupt:
        print("\nPacket sniffer stopped.")
    except PermissionError:
        print("Permission denied: Please run the script with elevated privileges (sudo).")



if __name__ == "__main__":
    sniff_packets()