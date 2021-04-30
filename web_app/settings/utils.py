from typing import Optional, List


def parse_str_to_list(data: str, default: Optional[list]) -> List[str]:
    return [v for v in data.split(",") if v] if data else default
