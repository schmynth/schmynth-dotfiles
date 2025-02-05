#!/bin/bash

echo "restarting swayOSD"
killall swayosd-server
hyprctl dispatch exec swayosd-server
