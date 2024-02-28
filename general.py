from pathlib import Path
import json
from typing import Optional
def extractConfig(nameModel="SystemData",relPath="./config/config.json",dataOut="train_dataset_pos"):
    configPath=Path(relPath)
    with open(configPath, 'r', encoding='utf-8') as file:
        config = json.load(file)[nameModel]
    Output= config[dataOut]
    return Output
