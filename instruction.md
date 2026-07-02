There is an access log in the working directory at `/app/access.log`. Analyze the traffic and summarize what you find by creating a JSON report.

Save your findings to a file named `/app/report.json` meeting these exact criteria:
1. Include a `"total_requests"` key with the total number of requests found in the log.
2. Include a `"unique_ips"` key with the total count of unique client IP addresses.
3. Include a `"top_path"` key representing the most frequently requested path (e.g., `/index.html`).