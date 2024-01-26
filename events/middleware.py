from django.shortcuts import render

class CustomErrorMiddleware:
    """Middleware to handle errors."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if 400 <= response.status_code < 500:
            # Handle client errors (status codes 400-499)
            return self.handle_client_error(request, response)
        elif 500 <= response.status_code < 600:
            # Handle server errors (status codes 500-599)
            return self.handle_server_error(request, response)

        return response

    def handle_client_error(self, request, response):
        """Handle client errors."""
        if response.status_code == 404:
            return render(request, 'error.html', status=404)
        # Add more client error handling here if needed
        return response

    def handle_server_error(self, request, response):
        """Handle server errors."""
        if response.status_code >= 500:
            return render(request, 'error.html', status=500)
        # Add more server error handling here if needed
        return response
