"""
Input file access.log:
GET /app HTTP/1.0 
POST /app2 HTTP/1.1
DELETE /app3 HTTP/1.0
GET /app HTTP/1.0

Output:
GET - 2
POST - 1
DELETE - 1
"""

def count_http_methods(file_path):
    method_counts = {}  # Dictionary to store method counts

    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if parts:  # Ensure the line is not empty
                method = parts[0]  # HTTP method is the first word
                if method in method_counts:
                    method_counts[method] += 1
                else:
                    method_counts[method] = 1

    # Print output in the required format
    for method, count in method_counts.items():
        print(f"{method} - {count}")

# Example usage:
count_http_methods("access.log")

"""
LET'S EXTEND THE EXERCISE:

Input file access.log:
GET /app HTTP/1.0
GET /app HTTP/1.0
POST /app2 HTTP/1.1
DELETE /app3 HTTP/1.0
GET /app2 HTTP/1.0
	
Output:
GET /app 2
GET /app2 1
POST /app2 1
DELETE /app3 1
"""

def count_http_requests(file_path):
    request_counts = {}  # Dictionary to store counts for "METHOD PATH"

    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 2:  # Just a check to see there is a METHOD and a PATH
                request = f"{parts[0]} {parts[1]}"  # Combine METHOD and PATH
                if request in request_counts:
                    request_counts[request] += 1
                else:
                    request_counts[request] = 1

    # Print output in the required format
    for request, count in request_counts.items():
        print(f"{request} {count}")

# Example usage:
count_http_requests("access.log")