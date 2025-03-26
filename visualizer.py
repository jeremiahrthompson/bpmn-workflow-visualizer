#!/usr/bin/env python3
import http.server
import socketserver
import os
import webbrowser

PORT = 8000

class BPMNHandler(http.server.SimpleHTTPRequestHandler):
    """Custom request handler for BPMN files."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def end_headers(self):
        """Add CORS headers to allow browser access."""
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
    
    def guess_type(self, path):
        """Override to add BPMN MIME type."""
        if path.endswith('.bpmn'):
            return 'application/xml'
        return super().guess_type(path)


def start_server():
    """Start the HTTP server and open the visualization in a browser."""
    # Change to the project root directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Set up the handler
    handler = BPMNHandler
    
    # Create the server
    httpd = socketserver.TCPServer(("", PORT), handler)
    
    print(f"Server started at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.")
    
    # Open the browser
    webbrowser.open(f"http://localhost:{PORT}")
    
    # Start the server
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")


if __name__ == "__main__":
    # Ensure the BPMN file exists
    bpmn_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "bpmn", "retirement_sample.bpmn")
    if not os.path.exists(bpmn_file_path):
        print(f"Error: BPMN file not found at {bpmn_file_path}")
        print("Please ensure the file exists before running this script.")
        exit(1)
    
    # Start the server
    start_server() 