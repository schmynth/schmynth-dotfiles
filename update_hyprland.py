import modules.update_palette as u
import subprocess



def restart_waybar():
    subprocess.call("./.scripts/restart_waybar.sh", shell=True)

u.update_palette()

restart_waybar()