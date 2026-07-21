# Log Report Task

Analyze the provided access.log file and generate a JSON report.

The agent must:

1. Read and parse all log entries from /app/access.log.
2. Calculate the total number of requests.
3. Count the number of unique client IP addresses.
4. Identify the most frequently requested URL path.
5. Save the final result as /app/report.json.

The output file must be valid JSON with the following format:

{
  "total_requests": <number>,
  "unique_ips": <number>,
  "top_path": "<path>"
}

The solution should handle repeated requests correctly and produce deterministic output.
