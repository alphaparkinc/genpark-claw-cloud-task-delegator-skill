import hashlib, time

class ClawCloudTaskDelegatorClient:
    def delegate_task(self, task_description: str, priority: str = "normal") -> dict:
        task_id = hashlib.md5(f"{task_description}{time.time()}".encode()).hexdigest()[:12]
        eta_map = {"high": 30, "normal": 120, "low": 600}
        eta = eta_map.get(priority.lower(), 120)
        return {
            "task_id": f"claw-{task_id}",
            "status": "QUEUED",
            "eta_seconds": eta
        }
