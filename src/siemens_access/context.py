# src/siemens_access/context.py
from __future__ import annotations

from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent
SRC_DIR = PACKAGE_DIR.parent
PROJECT_ROOT = SRC_DIR.parent

APP_NAME = "siemens-access"
APP_NAME_PRETTY = "Siemens Access"
IMPORT_NAME = "siemens_access"
SRC_FOLDER_NAME = "siemens_access"
DESCRIPTION_STR = "An attempt to access Siemens hardare using open source Python libraries, like s7commplus and python-snap7."
APP_DIR = Path.home() / ".siemens-access"
LOG_FILE_PATH = APP_DIR / "siemens-access.log"
SERVICE = APP_NAME
CONFIG_PATH = APP_DIR / "config.json"
SECRET_PATH = APP_DIR / "vault.db"
ENV_PATH = PROJECT_ROOT / ".env"
