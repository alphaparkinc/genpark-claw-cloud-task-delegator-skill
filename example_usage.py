from client import ClawCloudTaskDelegatorClient
client = ClawCloudTaskDelegatorClient()
result = client.delegate_task("Analyze 50 competitor pricing pages and return comparison table", "high")
print(f"Task delegated: {result['task_id']}")
print(f"Status: {result['status']} | ETA: {result['eta_seconds']}s")
