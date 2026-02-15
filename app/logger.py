import json
from datetime import datetime
from pathlib import Path
from app.config import LOG_PATH


def log_inference(payload: dict) -> None:
    path = Path(LOG_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "timestamp": datetime.now().isoformat(),
            **payload
        }) + "\n")