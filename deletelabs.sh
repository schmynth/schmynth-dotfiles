#! /usr/bin/bash

#Before installing, the vst2 (dll) and vst3 files of LABS have to be deleted. They are regenerated when installing a new instrument.
#This script does the deleting.

rm -rf /home/$USER/.wine/drive_c/'Program Files'/'Common Files'/VST3/LABS.vst3
echo "removed /home/$USER/.wine/drive_c/Program Files/Common Files/VST3/LABS.vst3"
rm -rf /home/$USER/.wine/drive_c/'Program Files'/VstPlugins/LABS.dll
echo "removed /home/$USER/.wine/drive_c/Program Files/VstPlugins/LABS.dll"


