import json
from pathlib import Path
from datetime import datetime

def save_document_record(user, doc_type, content, version_label=None):
    folder = Path("generated_docs") / user["login_id"]
    folder.mkdir(parents=True, exist_ok=True)

    filename = f"{doc_type}_{version_label or '기본'}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    path = folder / filename

    with open(path, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

    return str(path)