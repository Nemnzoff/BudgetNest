# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: BudgetNest
SETTINGS = {
    "currency": "RUB",
    "date_format": "%d.%m.%Y",
    "default_category": "Other",
    "auto_save_interval": 5,
}


def get_setting(key: str) -> any:
    return SETTINGS.get(key)


def set_setting(key: str, value: any):
    if key in SETTINGS and not isinstance(value, dict):
        SETTINGS[key] = value
        print(f"Setting '{key}' updated to {value}")
    else:
        raise ValueError(f"Invalid setting key or type for '{key}'")


def reset_settings():
    global SETTINGS
    SETTINGS.update({
        "currency": "RUB",
        "date_format": "%d.%m.%Y",
        "default_category": "Other",
        "auto_save_interval": 5,
    })
    print("Settings reset to defaults.")


def validate_settings():
    required_keys = ["currency", "date_format"]
    for key in required_keys:
        if key not in SETTINGS:
            raise ValueError(f"Missing required setting: {key}")
