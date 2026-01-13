"""
Example backend server for full-stack demo.
This is a placeholder - replace with your actual FastAPI/Django/Flask app.
"""
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler


def main():
    port = int(os.environ.get("PORT", os.environ.get("BACKEND_PORT", 8000)))
    print(f"Starting backend server on port {port}")
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
