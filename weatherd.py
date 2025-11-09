#!/usr/bin/env python3
import os
import json

config_paths = [
	"~/.config/weatherd/config.json",
	"/etc/weatherd/config.json"
]

def checkConfigPath() -> str:
	for path in config_paths:
		if os.path.exists(path):
			return path

def loadConfig(path: str):
	if path == None:
		return {
			"latitude": 50.088,
			"longitude": 14.4208,
			"timezone": "Europe/Prague",
			"temperature_unit": "celsius",
			"frequency": 300
		}
	with open(path, 'r', encoding='utf-8') as config_raw:
		config_json = json.load(config_raw)
		return config_json

def main():
	config = loadConfig(checkConfigPath())
	print(config)

if __name__ == "__main__":
	main()
