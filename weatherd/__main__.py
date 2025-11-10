#!/usr/bin/env python3
import os, sys
import json
import requests
import time
import argparse

__version__ = "0.3"

config_paths = [
	f"{os.environ['HOME']}/.config/weatherd/config.json",
	"/etc/weatherd/config.json"
]

default_config = {
	"latitude": 50.088,
	"longitude": 14.4208,
	"timezone": "Europe/Prague",
	"temperature_unit": "celsius",
	"frequency": 300,
	"prettify_output": True
}


parser = argparse.ArgumentParser(description='Weather daemon for fetching data from Open-Meteo')
parser.add_argument('-S', '--systemd', action="store_true")
args = parser.parse_args()

def checkConfigPath() -> str:
	for path in config_paths:
		if os.path.exists(path):
			return path

def loadConfig(path: str):
	if path == None:
		return default_config
	with open(path, 'r', encoding='utf-8') as config_raw:
		config_json = json.load(config_raw)
		return config_json

def generateSystemdUnit():
	systemd_service = """[Unit]
Description=weatherd service

[Service]
Type=Simple
ExecStart=~/.local/bin/weatherd

[Install]
WantedBy=multi-user.target
"""
	
	os.system(f"mkdir -p {os.environ['HOME']}/.config/systemd/user")
	with open(f"{os.environ['HOME']}/.config/systemd/user/weatherd.service", "w") as f:
		f.write(systemd_service)
	
	print("Systemd unit generated! Run \u001b[1msystemd --user daemon-reload && systemd --user --now enable weatherd.service\u001b[0m to start weatherd.")

def main():
	config = {**default_config, **loadConfig(checkConfigPath())}
	running = 1

	if not os.path.exists(f"{os.environ['HOME']}/.var"):
		os.sys(f"mkdir -p {os.environ['HOME']}/.var") 

	while running:
		try:
			req = requests.get("https://api.open-meteo.com/v1/forecast", params = {
				"latitude": config['latitude'],
				"longitude": config['longitude'],
				"timezone": config['timezone'],
				"temperature_unit": config['temperature_unit'],
				"current": "temperature_2m,weather_code",
				"hourly": "weather_code,temperature_2m,precipitation_probability"
			})
			req_json = req.json()
		
			output = {
				"current": {
					"time": req_json['current']['time'],
					"temperature": req_json['current']['temperature_2m'],
					"weather_code": req_json['current']['weather_code'],
				},
				"hourly": req_json['hourly']
			}
			
			with open(f"{os.environ['HOME']}/.var/weatherd.json", "w") as f:
				json.dump(output, f, indent=4 if config['prettify_output'] else None)

			time.sleep(config['frequency'])
		except KeyboardInterrupt:
			running = 0

def run():
	if args.systemd:
		generateSystemdUnit()
	else:
		main()
