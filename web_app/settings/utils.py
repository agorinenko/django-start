from typing import Optional, List


def parse_str_to_list(data: str, default: Optional[list] = None) -> List[str]:
    """ Преобразование строки в список """
    return [v for v in data.split(",") if v] if data else default
