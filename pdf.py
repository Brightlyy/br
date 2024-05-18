# Re-generating the PDF and saving it to a specific path to ensure it can be accessed and downloaded properly

from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a cell
pdf.cell(200, 10, txt="Report: Connecting Two Devices Using Python Socket Programming", ln=True, align='C')

# Line break
pdf.ln(10)

# Add content
content = [
    "Introduction",
    "This report demonstrates the process of connecting two devices using Python's socket programming. The connection established allows communication between a server and a client device. The server listens for incoming connections, while the client initiates a connection to the server. The communication involves sending and receiving messages between the devices.",
    
    "Objective",
    "To establish a connection between two devices using socket programming in Python and demonstrate the transmission of messages between a server and a client.",
    
    "Environment Setup",
    "Server Device Configuration",
    "IP Address Configuration:",
    "The server device's IP address is 192.168.116.162, associated with the wlp2s0 network interface.",
    "Command used to find the IP address:",
    "ip addr",
    "The relevant output segment:",
    "4: wlp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000",
    "    link/ether 34:f3:9a:45:11:8b brd ff:ff:ff:ff:ff:ff",
    "    inet 192.168.116.162/24 brd 192.168.116.255 scope global dynamic noprefixroute wlp2s0",
    "       valid_lft 3391sec preferred_lft 3391sec",
    
    "Python Environment",
    "Python Version: Python 3.x",
    "Required Libraries: Standard Python library socket",
    
    "Implementation",
    "Server Code",
    "The server code binds to the specified IP address and port, listens for incoming connections, accepts a connection, and echoes back any data it receives.",
    
    '```python',
    'import socket',
    '',
    '# Define the host and port',
    "HOST = '192.168.116.162'  # Server's IP address",
    'PORT = 65432              # Port to listen on (non-privileged ports are > 1023)',
    '',
    '# Create a socket object',
    'with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:',
    '    s.bind((HOST, PORT))',
    '    s.listen()',
    '    print(f"Server listening on {HOST}:{PORT}")',
    '    ',
    '    conn, addr = s.accept()',
    '    with conn:',
    '        print(f"Connected by {addr}")',
    '        while True:',
    '            data = conn.recv(1024)',
    '            if not data:',
    '                break',
    '            print(f"Received: {data.decode()}")',
    '            conn.sendall(data)',
    '```',
    
    "Client Code",
    "The client code connects to the server's IP address and port, sends a message to the server, and waits for a response.",
    
    '```python',
    'import socket',
    '',
    '# Define the server address and port',
    "HOST = '192.168.116.162'  # The server's IP address",
    'PORT = 65432              # The same port as used by the server',
    '',
    '# Create a socket object',
    'with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:',
    '    s.connect((HOST, PORT))',
    '    s.sendall(b\'Hello, server\')',
    '    data = s.recv(1024)',
    '',
    'print(f"Received: {data.decode()}")',
    '```',
    
    "Execution",
    "1. Start the Server:",
    "   Run the server code on the server device:",
    "   ```bash",
    "   python3 server.py",
    "   ```",
    "   The server starts listening on 192.168.116.162:65432.",
    
    "2. Start the Client:",
    "   Run the client code on the client device:",
    "   ```bash",
    "   python3 client.py",
    "   ```",
    "   The client connects to the server and sends a message 'Hello, server'.",
    
    "3. Output:",
    "   Server Output:",
    "   ```",
    "   Server listening on 192.168.116.162:65432",
    "   Connected by ('192.168.116.XXX', <random_port>)",
    "   Received: Hello, server",
    "   ```",
    "   Client Output:",
    "   ```",
    "   Received: Hello, server",
    "   ```",
    
    "Conclusion",
    "This report outlines the successful establishment of a connection between two devices using Python socket programming. The server and client were able to communicate effectively, demonstrating the basics of network programming. This setup can be further expanded for more complex interactions and data exchanges.",
    
    "References",
    "Python Official Documentation: [Socket Programming](https://docs.python.org/3/library/socket.html)"
]

for line in content:
    if line.startswith('```'):
        # Handle code block
        pdf.set_font("Courier", size=10)
        pdf.multi_cell(0, 10, line[3:])
        pdf.set_font("Arial", size=12)
    else:
        pdf.multi_cell(0, 10, line)

# Save the PDF to a file
pdf_output_path = "/home/bright/Downloads/Socket_Programming_Report_v2.pdf"
pdf.output(pdf_output_path)

pdf_output_path
