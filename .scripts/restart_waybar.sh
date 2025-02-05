#!/bin/bash

echo "restarting waybar"
killall -q waybar
hyprctl dispatch exec waybar