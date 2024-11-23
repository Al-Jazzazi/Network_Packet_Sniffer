# Packet Sniffer

This Python script (`sniff.py`) is a simple packet sniffer that captures and processes network packets using raw sockets. It is designed for educational purposes to demonstrate how network traffic can be captured and analyzed.

---

## Features
- Captures raw packets from a specified network interface.
- Processes and analyzes the captured packets using a modular function (`parse_packet`).
- Displays basic information about the packets, such as source and destination IPs and protocols.

---

## Prerequisites
1. **Python 3.x**: Ensure Python 3 is installed on your system.
2. **Root/Administrator Privileges**: Raw sockets require elevated permissions to run.
3. **Network Configuration**: Identify your network IP address.

---

## Setup
1. Clone or download the script to your local machine:
   ```bash
   git clone https://github.com/Al-Jazzazi/Network_Packet_Sniffer.git
   cd packet-sniffer
   ```

2. Open the `sniff.py` file in a text editor and replace the placeholder in the `host` variable with your network's IP address:
   ```python
   host = "Put your network IP here".strip()
   ```

   - To find your network IP:
     - On macOS/Linux: Use `ifconfig` or `ip addr show`.
     - On Windows: Use `ipconfig`.

3. Save the changes.

---

## How to Run
1. Open a terminal and navigate to the directory containing `sniff.py`.
2. Run the script with `sudo` to grant it the necessary permissions:
   ```bash
   sudo python3 sniff.py
   ```

---

## Output Example
The script will display captured packets in real-time. For example:
```
Sniffing browser traffic. Press Ctrl+C to stop.
Packet received from ('172.20.10.5', 443): b'\x45\x00...'
Packet received from ('172.20.10.6', 443): b'\x45\x00...'
```

---

## Notes
- Ensure your IP address is correctly set in the `host` variable to bind to the appropriate network interface.
- This script is designed for educational purposes. Use it responsibly and only on networks you own or have explicit permission to analyze.
- Modern HTTPS traffic is encrypted, so only metadata like IP addresses and ports are visible.

---

## Troubleshooting
### Common Errors
1. **Permission Denied**:
   - Ensure you run the script with `sudo`:
     ```bash
     sudo python3 sniff.py
     ```

2. **`socket.gaierror: [Errno 8] nodename nor servname provided, or not known`**:
   - Verify that the `host` variable contains a valid network IP address.
   - Replace `host` with `"0.0.0.0"` to bind to all interfaces as a fallback:
     ```python
     host = "0.0.0.0"
     ```

---

## Future Enhancements
- Improve the parse_packet function to parse application-layer protocols like HTTP, DNS, or TCP.
- Add functionality to save captured packets to a file for offline analysis.
- Integrate advanced libraries like scapy for enhanced packet processing.


```
