import json
import os
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if urlsplit(self.path).path != "/api/health":
            self.send_error(HTTPStatus.NOT_FOUND)
            return

        payload = {
            "status": "ok",
            "service": os.environ.get("SMOKE_NAME", "patrol-sim-smoke"),
        }
        body = json.dumps(payload).encode("utf-8")

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    with ThreadingHTTPServer(("0.0.0.0", 8000), HealthHandler) as server:
        server.serve_forever()
