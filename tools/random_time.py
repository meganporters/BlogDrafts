from __future__ import annotations

import random
from datetime import datetime, timedelta


def random_hobby_time(start: datetime) -> datetime:
    gap_days = random.choice([1, 2, 3, 4, 5, 7, 9, 11, 13])
    hour = random.choice([19, 20, 21, 22, 23, 0])
    minute = random.randint(1, 57)
    second = random.randint(2, 58)
    return start + timedelta(days=gap_days, hours=hour, minutes=minute, seconds=second)


if __name__ == "__main__":
    cur = datetime.fromisoformat("2025-01-27T09:43:36")
    for _ in range(8):
        cur = random_hobby_time(cur)
        print(cur.isoformat(timespec="seconds"))

