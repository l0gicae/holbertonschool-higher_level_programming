#!/usr/bin/python3
"""
Simple HTTP API server using http.server.

Endpoints:
- GET /        -> "Hello, this is a simple API!"
- GET /data    -> JSON: {"name": "John", "age": 30, "city": "New York"}
- GET /status  -> "OK"
- GET /info    -> JSON: {"version": "1.0", "description": "A simple API built with http.server"}
- Any other    -> 404 "Endpoint not found"
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom request handler for a very simple HTTP API."""

    def _send_text(self, text, status=200):
        """Send a plain text response."""
        payload = text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def _send_json(self, data, status=200):
        """Send a JSON response."""
        payload = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        """Handle GET requests for different endpoints."""
        if self.path == "/":
            # Root endpoint
            self._send_text("Hello, this is a simple API!")
        elif self.path == "/data":
            # JSON data endpoint
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(data)
        elif self.path == "/status":
            # Status endpoint
            self._send_text("OK")
        elif self.path == "/info":
            # Extra info endpoint
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self._send_json(info)
        else:
            # Unknown endpoint
            self._send_text("Endpoint not found", status=404)

    def do_POST(self):
        """Simple handling for POST (not required, but present)."""
        self._send_text("POST method is not implemented for this API.", status=405)


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Run the HTTP server on the given port."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run()
