#!/bin/bash

DIR="$(dirname "$0")"

feh --fullscreen --auto-zoom --hide-pointer "$DIR/logo6.png" &
sleep 1
feh --fullscreen --auto-zoom --hide-pointer "$DIR/logo7.png" &
sleep 1
feh --fullscreen --auto-zoom --hide-pointer "$DIR/logo8.png" &
sleep 2
pkill feh


python3 "$DIR/lockscreen.py"

#mpv --no-border --fullscreen --ontop \
 #   --no-osc --no-input-default-bindings \
  #  --loop-file=no --really-quiet \
   # --vf="fade=t=in:st=0:d=0.5,fade=t=out:st=2:d=0.5" \
    #/data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/debian/usr/share/conky_theme/macos-lock/apel.mp4

# 3. Tunggu sedikit agar transisi halus
#sleep 0.3



