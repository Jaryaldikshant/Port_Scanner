# **Port Scanner Tool**

## **Overview**  
The **Port Scanner Tool** is a Python-based utility that scans open ports on a target system or network. It helps identify active services running on a host by checking for open TCP ports. This tool is useful for security audits, network troubleshooting, and learning about network communications.

## **Features**  
✅ Scans a range of ports on a target IP or domain  
✅ Supports **TCP scanning**  
✅ Displays open ports  
✅ Fast and efficient scanning using **multi-threading**  
✅ Simple and easy-to-use **CLI interface**  

## **Installation**  
Ensure you have Python installed (Python 3.x recommended).  
```bash
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
pip install -r requirements.txt
```

## **Usage**  
Run the script with basic options:  
```bash
python3 port.py <target IP or domain> <start_port> <end_port>
```
Example:  
```bash
python3 port.py 192.168.1.1 1 1000
```

### **Available Options:**  
| Argument | Description |
|----------|-------------|
| `<target>` | Target IP or domain |
| `<start_port>` | Starting port number |
| `<end_port>` | Ending port number |

## **Example Output**  
```
PORT SCANNER
----------------------------------------------------------------------
Scanning Target: 192.168.1.1
Port 22 is OPEN
Port 80 is OPEN
Port 443 is OPEN
Scanning completed
```

## **Technology Stack**  
- **Language:** Python  
- **Libraries:** `socket`, `sys`, `threading`  

## **Future Enhancements**  
- Add UDP scanning support  
- Implement OS detection & banner grabbing  
- Export scan results to a file (CSV/JSON)  


