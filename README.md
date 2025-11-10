<p align="center">
	<img src=".github/readme-assets/logo.svg">
</p>

<p align="center">
	<img alt="Github last commit" src="https://img.shields.io/github/last-commit/CodyMarkix/weatherd">
	<img alt="AUR Last Modified" src="https://img.shields.io/aur/last-modified/weatherd">
	<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/weatherd">
</p>

`weatherd` is a simple daemon for periodic fetching of weather data from Open-Meteo. I needed to write this for some of my [eww](https://github.com/elkowar/eww) widgets, but I also thought it could be a useful tool to publish. ᕕ( ᐛ )ᕗ 

## Installation

### Arch linux

```sh
yay -S weatherd # Replace yay with your favorite AUR wrapper!
```

### Other

```
pip3 install weatherd
```

## Usage

`weatherd` fetches data from Open-Meteo every 5 minutes by default, the frequency is tweakable in the config file.
It then saves the result to `~/.var/weatherd.json` for your apps to read. 

### Configuration

`weatherd` looks for config files in the following locations:

- `~/.config/weatherd/config.json`
- `/etc/weatherd/config.json`

**When installing via the AUR**, an initial configuration is available in `/etc/weatherd/config.json`.
A copy of the default config file is also available below:

```json
{
	"latitude": 50.088,
	"longitude": 14.4208,
	"timezone": "Europe/Prague",
	"temperature_unit": "celsius",
	"frequency": 300,
	"prettify_output": False
}
```

