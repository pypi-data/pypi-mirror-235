from werkzeug.wrappers import Request
import io
import json
import re


class RejectRequest(Exception):
    def __init__(self, status_code, reason):
        self.status_code = status_code
        self.reason = reason

def reject(status_code, reason):
    raise RejectRequest(status_code, reason)

def handle(original_request, new_data=None, new_headers=None):
        """Create a new request object with modified headers and/or body."""

        new_request_environ = original_request.environ.copy()

        # Modify the body if new_data is provided
        if new_data:
            json_data = json.dumps(new_data)
            byte_data = json_data.encode('utf-8')
            input_stream = io.BytesIO(byte_data)
            new_request_environ['wsgi.input'] = input_stream
            new_request_environ['CONTENT_LENGTH'] = str(len(byte_data))

        # Modify the headers if new_headers is provided
        if new_headers:
            for key, value in new_headers.items():
                wsgi_key = 'HTTP_' + key.upper().replace('-', '_')
                new_request_environ[wsgi_key] = value

        new_request = Request(new_request_environ)

        # If new_data was provided, set the data attribute of the new request
        if new_data:
            new_request.data = byte_data

        return new_request

class SDK:
    def __init__(self):
        self.middlewares = []

    def pattern_to_regex(self, pattern):
        """Convert a pattern to a regular expression"""
        return re.compile('^' + pattern.replace('*', '.*').replace('<id>', '[^/]+') + '$')

    def use(self, middleware_obj):
        """Register a middleware function with its routes and methods"""
        middleware_func = middleware_obj['function']
        routes = [self.pattern_to_regex(route) for route in middleware_obj['routes']]
        methods = middleware_obj.get('methods', [])  # Extract methods from the middleware object
        self.middlewares.append({'function': middleware_func, 'routes': routes, 'methods': methods})


    def process(self, request, path, method):
        """Process a request through the middleware chain"""
        resp = None
        for middleware in self.middlewares:
            for route in middleware['routes']:
                if route.match(path) and method in middleware.get('methods', []):
                    try:
                        resp = middleware['function'](request)
                    except RejectRequest as e:
                        return {'error': f"{e.reason}"}, e.status_code
                    except Exception as e:
                        return {'error': str(e)}, 500
        return resp
