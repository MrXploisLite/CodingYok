"""
Simple web framework foundation for CodingYok
Provides basic HTTP server and routing capabilities
"""

import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Dict, List, Callable, Any, Optional
from .errors import CodingYokRuntimeError


class CodingYokWebServer:
    """Simple web server for CodingYok applications"""
    
    def __init__(self, host: str = 'localhost', port: int = 8000):
        self.host = host
        self.port = port
        self.routes: Dict[str, Dict[str, Callable]] = {}
        self.static_files: Dict[str, str] = {}
        
    def route(self, path: str, method: str = 'GET'):
        """Decorator to register route handlers"""
        def decorator(handler_func):
            if path not in self.routes:
                self.routes[path] = {}
            self.routes[path][method.upper()] = handler_func
            return handler_func
        return decorator
    
    def static(self, url_path: str, file_path: str):
        """Register static file"""
        self.static_files[url_path] = file_path
    
    def run(self):
        """Start the web server"""
        handler_class = self._create_handler_class()
        server = HTTPServer((self.host, self.port), handler_class)
        print(f"Server CodingYok berjalan di http://{self.host}:{self.port}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer dihentikan")
            server.shutdown()
    
    def _create_handler_class(self):
        """Create HTTP request handler class"""
        routes = self.routes
        static_files = self.static_files
        
        class CodingYokRequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self._handle_request('GET')
            
            def do_POST(self):
                self._handle_request('POST')
            
            def do_PUT(self):
                self._handle_request('PUT')
            
            def do_DELETE(self):
                self._handle_request('DELETE')
            
            def _handle_request(self, method):
                # Parse URL
                parsed_url = urllib.parse.urlparse(self.path)
                path = parsed_url.path
                query_params = urllib.parse.parse_qs(parsed_url.query)
                
                # Check static files first
                if path in static_files:
                    self._serve_static_file(static_files[path])
                    return
                
                # Check routes
                if path in routes and method in routes[path]:
                    try:
                        # Prepare request data
                        request_data = {
                            'method': method,
                            'path': path,
                            'query': query_params,
                            'headers': dict(self.headers)
                        }
                        
                        # Get request body for POST/PUT
                        if method in ['POST', 'PUT']:
                            content_length = int(self.headers.get('Content-Length', 0))
                            if content_length > 0:
                                body = self.rfile.read(content_length).decode('utf-8')
                                request_data['body'] = body
                                
                                # Try to parse JSON
                                if self.headers.get('Content-Type') == 'application/json':
                                    try:
                                        request_data['json'] = json.loads(body)
                                    except json.JSONDecodeError:
                                        pass
                        
                        # Call handler
                        handler = routes[path][method]
                        response = handler(request_data)
                        
                        # Send response
                        self._send_response(response)
                        
                    except Exception as e:
                        self._send_error_response(500, str(e))
                else:
                    self._send_error_response(404, "Halaman tidak ditemukan")
            
            def _serve_static_file(self, file_path):
                """Serve static file"""
                try:
                    with open(file_path, 'rb') as f:
                        content = f.read()
                    
                    # Determine content type
                    content_type = 'text/plain'
                    if file_path.endswith('.html'):
                        content_type = 'text/html'
                    elif file_path.endswith('.css'):
                        content_type = 'text/css'
                    elif file_path.endswith('.js'):
                        content_type = 'application/javascript'
                    elif file_path.endswith('.json'):
                        content_type = 'application/json'
                    
                    self.send_response(200)
                    self.send_header('Content-Type', content_type)
                    self.send_header('Content-Length', len(content))
                    self.end_headers()
                    self.wfile.write(content)
                    
                except FileNotFoundError:
                    self._send_error_response(404, "File tidak ditemukan")
                except Exception as e:
                    self._send_error_response(500, str(e))
            
            def _send_response(self, response):
                """Send HTTP response"""
                if isinstance(response, dict):
                    # JSON response
                    json_data = json.dumps(response, ensure_ascii=False)
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json; charset=utf-8')
                    self.send_header('Content-Length', len(json_data.encode('utf-8')))
                    self.end_headers()
                    self.wfile.write(json_data.encode('utf-8'))
                elif isinstance(response, str):
                    # HTML/Text response
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html; charset=utf-8')
                    self.send_header('Content-Length', len(response.encode('utf-8')))
                    self.end_headers()
                    self.wfile.write(response.encode('utf-8'))
                else:
                    # Default string conversion
                    content = str(response)
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/plain; charset=utf-8')
                    self.send_header('Content-Length', len(content.encode('utf-8')))
                    self.end_headers()
                    self.wfile.write(content.encode('utf-8'))
            
            def _send_error_response(self, status_code, message):
                """Send error response"""
                self.send_response(status_code)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                
                error_html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Error {status_code}</title>
                    <meta charset="utf-8">
                </head>
                <body>
                    <h1>Error {status_code}</h1>
                    <p>{message}</p>
                    <hr>
                    <p><em>CodingYok Web Server</em></p>
                </body>
                </html>
                """
                self.wfile.write(error_html.encode('utf-8'))
            
            def log_message(self, format, *args):
                """Override to customize logging"""
                print(f"[{self.log_date_time_string()}] {format % args}")
        
        return CodingYokRequestHandler


def buat_server_web(host: str = 'localhost', port: int = 8000) -> CodingYokWebServer:
    """Create a new web server instance"""
    return CodingYokWebServer(host, port)


def render_template(template_path: str, **context) -> str:
    """Simple template rendering"""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
        
        # Simple variable substitution
        for key, value in context.items():
            placeholder = f"{{{{{key}}}}}"
            template = template.replace(placeholder, str(value))
        
        return template
    except FileNotFoundError:
        raise CodingYokRuntimeError(f"Template '{template_path}' tidak ditemukan")


def json_response(data: Any, status: int = 200) -> Dict[str, Any]:
    """Create JSON response"""
    return {
        'status': status,
        'data': data
    }


def redirect_response(url: str) -> str:
    """Create redirect response"""
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="refresh" content="0; url={url}">
        <title>Redirect</title>
    </head>
    <body>
        <p>Redirecting to <a href="{url}">{url}</a></p>
    </body>
    </html>
    """


# HTTP client functions
def http_get(url: str, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Make HTTP GET request"""
    try:
        import urllib.request
        
        req = urllib.request.Request(url)
        if headers:
            for key, value in headers.items():
                req.add_header(key, value)
        
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            return {
                'status': response.getcode(),
                'headers': dict(response.headers),
                'content': content
            }
    except Exception as e:
        raise CodingYokRuntimeError(f"HTTP GET error: {str(e)}")


def http_post(url: str, data: Any = None, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Make HTTP POST request"""
    try:
        import urllib.request
        
        # Prepare data
        if isinstance(data, dict):
            data = json.dumps(data).encode('utf-8')
            if not headers:
                headers = {}
            headers['Content-Type'] = 'application/json'
        elif isinstance(data, str):
            data = data.encode('utf-8')
        
        req = urllib.request.Request(url, data=data, method='POST')
        if headers:
            for key, value in headers.items():
                req.add_header(key, value)
        
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            return {
                'status': response.getcode(),
                'headers': dict(response.headers),
                'content': content
            }
    except Exception as e:
        raise CodingYokRuntimeError(f"HTTP POST error: {str(e)}")


def get_web_functions() -> Dict[str, Callable]:
    """Get all web-related functions"""
    return {
        'buat_server_web': buat_server_web,
        'render_template': render_template,
        'json_response': json_response,
        'redirect_response': redirect_response,
        'http_get': http_get,
        'http_post': http_post,
    }
