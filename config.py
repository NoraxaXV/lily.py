import os
import dotenv
import yaml

with open("./default.settings.yaml") as fp:
    _config = yaml.safe_load(fp)
try:
    with open(os.getenv("HOME") + "/.config/lily.py/settings.yaml") as fp:
        _config.update(yaml.safe_load(fp))
except FileNotFoundError:
    pass

dotenv.load_dotenv()
# Remember to add .env variables to here to be automatically loaded into the config
for secret in ["DISCORD_BOT_TOKEN", "SHAPES_API_TOKEN"]:
    _config[secret] = os.getenv(secret)


def get(key):
    return _config.get(key)
