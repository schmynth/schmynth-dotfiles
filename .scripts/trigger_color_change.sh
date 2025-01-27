#!/bin/bash

SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_PATH="$(dirname "$SCRIPT_PATH")"
echo /home/sebastian/.config/waypaper/config.ini | entr -n python "$ROOT_PATH"/update_hyprland.py