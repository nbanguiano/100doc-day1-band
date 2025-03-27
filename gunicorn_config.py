bind = "127.0.0.1:8080"  # Internal bind address - Nginx will proxy to this
workers = 3  # Number of worker processes
accesslog = "access.log"  # Log file for access logs
errorlog = "error.log"    # Log file for error logs
