import yaml
from pathlib import Path


def load_config(config_path: str | None = None) -> dict:
    if config_path is None:
        project_root = Path(__file__).resolve().parent.parent
        config_path = project_root / "config" / "config.yaml"
    else:
        config_path = Path(config_path)

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    return config
