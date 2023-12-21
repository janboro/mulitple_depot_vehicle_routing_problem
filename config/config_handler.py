from enum import Enum
from os import path
from typing import Any

import yaml


def get_MDVRP_params() -> dict[str, Any]:
    file_name: str | None = "MDVRP_parameters.yaml"
    assert file_name is not None, "Parameters file path is not defined"
    current_directory: str = path.dirname(path.realpath(__file__))
    file_path: str = path.normpath(path.join(current_directory, file_name))

    with open(file_path, "r", encoding="utf-8") as f:
        handler: dict[str, Any] = yaml.safe_load(f)
        assert handler is not None, "Parameters file is empty"
        return handler
