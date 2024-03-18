from http.server import BaseHTTPRequestHandler, HTTPServer
import numpy
# Define the HTTP request handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Send response body
        self.wfile.write(b"Hello, worddddld!, This is an edit in bra3")

# Define the main function to run the server
def main():
    # Set server address and port
    server_address = ('0.0.0.0', 8000)
    
    # Create an HTTP server with our custom request handler
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    # Print a message indicating the server is running
    print('Server running on port 8000...')
    
    # Start the server
    httpd.serve_forever()

# Run the main function
if __name__ == '__main__':
    main()
