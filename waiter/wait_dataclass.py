from dataclasses import dataclass
from datetime import datetime

@dataclass
class wait_obj:
  start: datetime
  end: datetime
  name: str | None
  description: str | None
  uid: int | float | str