from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional


DATA_DIR = Path("data")
DATA_DIR.mkdir(parents=True, exist_ok=True)


@dataclass
class Draft:
    id: str
    title: str
    tags: List[str]
    body: str
    created_at: str

    @staticmethod
    def new(id: str, title: str, tags: Iterable[str], body: str) -> "Draft":
        return Draft(
            id=id,
            title=title,
            tags=sorted({t.strip() for t in tags if t.strip()}),
            body=body,
            created_at=datetime.utcnow().isoformat(timespec="seconds") + "Z",
        )


def _path_for(draft_id: str) -> Path:
    return DATA_DIR / f"{draft_id}.json"


def save(draft: Draft) -> None:
    _path_for(draft.id).write_text(json.dumps(asdict(draft), ensure_ascii=False, indent=2))


def load(draft_id: str) -> Optional[Draft]:
    p = _path_for(draft_id)
    if not p.exists():
        return None
    obj = json.loads(p.read_text())
    return Draft(**obj)


def list_by_tag(tag: Optional[str] = None) -> List[Draft]:
    drafts: List[Draft] = []
    for p in sorted(DATA_DIR.glob("*.json")):
        obj = json.loads(p.read_text())
        draft = Draft(**obj)
        if tag is None or tag in draft.tags:
            drafts.append(draft)
    drafts.sort(key=lambda d: d.created_at, reverse=True)
    return drafts

