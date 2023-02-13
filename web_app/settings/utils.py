from typing import Optional, List, Union

from envparse import env


def parse_str_to_list(name: str, default: Optional[Union[List[str], str]] = None) -> List[str]:
    """
    Преобразование строки в список
    :param name: имя переменной окружения
    :param default: значение по умолчанию
    :return:
    """
    if default and isinstance(default, str):
        default = [default]

    data = env.str(name, default=None)
    return [v for v in data.split(",") if v] if data else default
