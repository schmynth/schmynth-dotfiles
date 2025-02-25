- [Tools](#tools)
  - [CPU Governor steuern:](#cpu-governor-steuern)
- [Peripherals](#peripherals)
  - [nuphy air75](#nuphy-air75)
  - [wacom tablet](#wacom-tablet)
- [Gnome Desktop](#gnome-desktop)
  - [themes](#themes)
  - [country flags as keyboard layout indicator:](#country-flags-as-keyboard-layout-indicator)
  - [screen brightness](#screen-brightness)
  - [.desktop files](#desktop-files)
  - [Install cursors](#install-cursors)
  - [icons von Overview search entfernen (zb vst plugins)](#icons-von-overview-search-entfernen-zb-vst-plugins)
- [Pro Audio](#pro-audio)
  - [alsa](#alsa)
  - [midi settings:](#midi-settings)
  - [Midi Controller](#midi-controller)
  - [Realtime Audio](#realtime-audio)
  - [Bitwig](#bitwig)
- [grub](#grub)
- [Gaming](#gaming)
- [Wine](#wine)
- [general linux tips](#general-linux-tips)
  - [Environment Variables](#environment-variables)
  - [Shell Configuration](#shell-configuration)
  - [fstab](#fstab)
  - [hidden files (no dot):](#hidden-files-no-dot)
  - [copy over ssh](#copy-over-ssh)
  - [best practice](#best-practice)
- [pacman](#pacman)
  - [update mirrors](#update-mirrors)
  - [tipps and tricks](#tipps-and-tricks)
- [vim](#vim)
  - [plugins](#plugins)
    - [ale](#ale)
- [Hyprland](#hyprland)
  - [mime dolphin](#mime-dolphin)
  - [wallpapers:](#wallpapers)
  - [gtk dark theme](#gtk-dark-theme)
  - [launcher](#launcher)
    - [theming](#theming)
  - [blue light filter (flux)](#blue-light-filter-flux)


## Tools

Fullscreen hotkey terminal:<br>
**ddterm** gnome extension


tool um Platz zu schaffen:<br>
**ncdu**<br>

Ordner synchronisieren:<br>
**rsync**<br>

    rsync -az source destination

### CPU Governor steuern:<br>
**cpupower-gui** 	Programm um Performance governor zu steuern<br>

**cpufrequtils**	Programm um CPU Frequenz zu printen<br>

	cpufreq-info

## Peripherals

### nuphy air75

Um FN+Fx als F Key zu benutzen:

    sudo bash -c "echo 0 > /sys/module/hid_apple/parameters/fnmode" 

(Schreibt eine 0 in die angegebene Datei. Danach funktionieren die Fn+F Kombinationen und es kann sogar mit Fn+Tab+f umgeschaltet werden.)<br>
Um das permanent zu machen:<br>

Datei erstellen:

    sudo nano /etc/modprobe.d/hid_apple.conf

Und darein schreiben:

    options hid_apple fnmode=0options 

und anschließend

    mkinitcpio -P

### wacom tablet

To change projection of Wacom tablet issue:

    xsetwacom set 'Wacom Intuos S Pen stylus' MapToOutput HEAD-1
    xrandr --listactivemonitors
    HEAD-1-> Monitor 1
    HEAD-0-> Monitor 0


## Gnome Desktop

### themes 

The default themes are saved in /usr/share/themes

### country flags as keyboard layout indicator:

	yay -S x11-keyboard-flags
    sudo x11-keyboard-flags

then log off and on


### screen brightness

    sudo pacman -S ddcutil i2c-tools
    sudo modprobe i2c-dev

Gnome erweiterung installieren.

Alternativ in cli:

    ddcutil setvcp 10 + 10 

zum Erhöhen der Helligkeit. Sonst am Ende - 10.

### .desktop files

eigene .desktop files in ~/.local/share/applications
Beispiel matlab.desktop

### Install cursors

extract to ~/.icons<br>

auch für Flatpak ändern:

	flatpak --user override --filesystem=/home/$USER/.icons/:ro

### icons von Overview search entfernen (zb vst plugins)
erst:

	echo "[Desktop Entry] Hidden=true" > /tmp/1

dann:

	find /usr -name "*lsp_plug*desktop" 2>/dev/null | cut -f 5 -d '/' | xargs -I {} cp /tmp/1 ~/.local/share/applications/{}



	
## Pro Audio

### alsa

alsamixer nicht gefunden, obwohl alsa-utils installiert ist? Das bedeutet nur, dass die Soundkarte nicht gefunden wurde.\
Also eine andere ausprobieren:

    alsamixer -c 1 (card no. 1)

### midi settings:

Jack midi driver -> none

### Midi Controller

In Bitwig mpk mini als generic keyboard+knobs (nicht mpk mini) konfigurieren.
Beim neueren mpk plus allerdings nicht nötig.

### Realtime Audio

- pipewire installieren (alles aus den repos)
- config ändern (deutsches tutorial für ubuntu yt)
- realtime-privileges installieren
- user zu audio und realtime groups hinzufügen
- Bitwig aus aur installieren
- threadirqs kernel parameter hinzufügen in grub, dann:<br>

        grub-mkconfig -o /boot/grub/grub.cfg

- mit cpupower-gui auf performance stellen<br>

___	
yabridge wine vst gui aktualisiert nicht? 
	
	winetricks dxvk

### Bitwig

plugins alle individuell sandboxen<br>

Bitwig findet plugins nicht? ->	Lösche vst meta data in /home/sebastian/.BitwigStudio/cache


## grub

Arch grub config aktualisieren:

    nano /etc/default/grub

dann

    grub-mkconfig -o /boot/grub/grub.cfg





## Gaming
	map count!


## Wine

Wine prefixes erstellen in Terminal:

    WINEPREFIX=~/.newPrefix WINEARCH="win32" winecfg

WINEARCH ist optional, winecfg startet einfach winecfg für das neue Prefix.\
newPrefix ist der Name des neuen Prefix, kann frei gewählt werden.\
Um das Prefix später zu verwenden: 

    WINEPREFIX=~/.newPrefix app.exe

oder um es zu verändern: 

    WINEPREFIX=~/.newPrefix winecfg oder winetricks



## general linux tips

### Environment Variables

Environment variables setzen:
in .zshrc:

    export VARNAME="variable" # (ohne space geht auch ohne "")

### Shell Configuration

.zshrc aktualisiert? Mach:

    source .zshrc 

### fstab

nas mounten: (fstab) (Manjaro)

    192.168.178.35:/nas 		/home/sebastian/NAS 	nfs 	defaults 	0 	0

Arch:
    192.168.178.35:/nas   /home/sebastian/NAS   nfs   defaults,timeo=900,retrans=5,_netdev  0 0
    server-address:/folder  mountpoint

### hidden files (no dot):

hide files without renaming them:

    echo Folder Name >> ~/.hidden
		
### copy over ssh


    scp file1.txt file2.txt pi@192.168.1.3:folder1/

kopiert file1.txt und file2.txt in /home/pi/folder1.
Absolute Pfade gehen auch.
Das Passwort von pi (user) auf dem Server (RPi) muss eingegeben werden.

### best practice

Software von Drittanbietern in /opt installieren



## pacman

### update mirrors

Arch pacman mirrorlists:<br>
1. https://archlinux.org/mirrorlist/    Mirrorlist für DE erstellen und zb als ~/full-mirrorlist speichern<br>
2. alle in der liste unkommentieren:  	sed -i 's/#Server/Server/g' ~/full-mirrorlist<br>
3. Nach Geschwindigkeit sortieren:	rankmirrors ~/full-mirrorlist > ~/ranked-mirrors<br>
4. /etc/pacman.d/mirrorlist durch ranked-mirros Inhalt ersetzen<br>

oder einfach reflector benutzen:

    reflector --country France,Germany --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist 

### tipps and tricks

show installed aur packages:

	pacman -Qm

## vim

### plugins

Um Plugins zu installieren:\

    mkdir ~/.vim
    mkdir ~/.vim/bundle

Für Plugin-Management wird vundle verwendet.\

Vundle installieren:

    cd ~/.vim/bundle
    git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

Nach Installation eines Plugins in vim folgenden Befehl ausführen:

    :PluginInstall

#### ale

ale ist ein Plugin für Syntax-Highlighting (Farben etc.). Zum Installieren:

    cd ~/.vim/bundle
    git clone https://github.com/dense-analysis/ale

## Hyprland

To list all open windows (to find out the name or class):
    
    hyprctl clients

### mime dolphin

If dolphin can not open any file:

    cp /etc/xdg/menus/gnome-applications.menu applications.menu
    XDG_MENU_PREFIX=arch- kbuildsycoca6

### wallpapers:

    sudo pacman -S hyprpaper
    yay -S waypaper

Dabei ist hyprpaper das backend und waypaper der GUI wallpaper selector.

### gtk dark theme

If gtk apps are not respecting dark theme:

https://wiki.hyprland.org/Configuring/Environment-variables/#xdg-specifications

### launcher

rofi ist ein App-Launcher.
> You can learn how to set Rofi shortcuts and more [here.](https://github.com/davatorium/rofi)


#### theming


1. Clone this repository and change to its directory:
```
git clone https://github.com/lr-tech/rofi-themes-collection.git
cd rofi-themes-collection
```

2. If you don't have the directories needed for the install create them with:
```
mkdir -p ~/.local/share/rofi/themes/
```

```
cp themes/<your-selected-theme> ~/.local/share/rofi/themes/
```

4. Run Rofi in `run` mode, then run `rofi-theme-selector`.

5. Search for your desired theme, press `enter` to preview, then `Alt+a` to accept the new theme.

6. Enjoy your new Rofi theme!


### blue light filter (flux)

    yay -S hyprshade
    hyprshade on blue-light-filter