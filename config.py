import os
from dataclasses import dataclass
import json
from pathlib import Path


#establishes parent file for audit
APP_ROOT = Path(__file__).resolve().parent
CONFIG_PATH = APP_ROOT / "app_config.json"


@dataclass
class MapsAPIConfig:

    #env variables
    maps_api_key: str

    #json config
    api_base_url: str

    @classmethod
    def from_sources(cls) -> "MapsAPIConfig":
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            file_config = json.load(f)

        api_config_json = file_config["api"]

        config = cls(
            maps_api_key = required_env(api_config_json.get("mapsKeyEnv")),
            api_base_url = api_config_json.get("baseURL")
            )   
        
        return config


def required_env(variable_name: str) -> str:
    value = os.getenv(variable_name)
    if not value:
        raise ValueError(f"Missing required environment variable: {variable_name}")
    return value