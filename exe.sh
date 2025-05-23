#!/bin/bash

username="$1"
#Setup Icons Menu
wget https://github.com/gorontaloku/debian/raw/refs/heads/main/iconwin.zip
unzip iconwin.zip
cd iconwin
cp start-here.svg $PREFIX/share/icons/Papirus/24x24/panel/
cp start-here.svg $PREFIX/share/icons/Papirus/22x22/panel/
cp start-here.svg $PREFIX/share/icons/Papirus/16x16/panel/
cp start-here.svg $PREFIX/share/icons/ePapirus/24x24/panel/

cp preferences-system-search.svg $PREFIX/share/icons/Papirus/32x32/apps/
cp preferences-system-search.svg $PREFIX/share/icons/Papirus/48x48/apps/
cp preferences-system-search.svg $PREFIX/share/icons/Papirus/64x64/apps/
cp preferences-system-search.svg $PREFIX/share/icons/Papirus/16x16/apps/
cp preferences-system-search.svg $PREFIX/share/icons/Papirus/22x22/apps/
cp preferences-system-search.svg $PREFIX/share/icons/Papirus/24x24/apps/
cd
rm -rf $HOME//iconwin

wget https://raw.githubusercontent.com/gorontaloku/debian/main/word-icon.png
wget https://raw.githubusercontent.com/gorontaloku/debian/main/excel-icon.png
wget https://raw.githubusercontent.com/gorontaloku/debian/main/powerpoint-icon.png
mv word-icon.png $PREFIX/share/icons/
mv excel-icon.png $PREFIX/share/icons/
mv powerpoint-icon.png $PREFIX/share/icons/

#WORD
if [ ! -f $PREFIX/share/applications/wps-office-wps.desktop ];then
  echo "Creating Settings menu button..."
fi
echo "[Desktop Entry]
Name=Microsoft Office Word       
Comment=Configure wps office or create an App
Exec=pd login debian --user hankook --shared-tmp -- env DISPLAY=:1.0 /usr/bin/wps %U
Icon=$PREFIX/share/icons/word-icon.png
Terminal=false
StartupWMClass=wps-office-et   
Type=Application
Categories=Office;                                                    
StartupNotify=true" > $PREFIX/share/applications/wps-office-wps.desktop

#EXCEL
if [ ! -f $PREFIX/share/applications/wps-office-et.desktop ];then
  echo "Creating Settings menu button..."
fi
echo "[Desktop Entry]
Name=Microsoft Office Excel       
Comment=Configure wps office or create an App
Exec=pd login debian --user hankook --shared-tmp -- env DISPLAY=:1.0 /usr/bin/et %F
Icon=$PREFIX/share/icons/excel-icon.png
Terminal=false
StartupWMClass=wps-office-et   
Type=Application
Categories=Office;                                                    
StartupNotify=true" > $PREFIX/share/applications/wps-office-et.desktop

#Powerpoint
if [ ! -f $PREFIX/share/applications/wps-office-wpp.desktop ];then
  echo "Creating Settings menu button..."
fi
echo "[Desktop Entry]
Name=Microsoft Office Powerpoint       
Comment=Configure wps office or create an App
Exec=pd login debian --user hankook --shared-tmp -- env DISPLAY=:1.0 /usr/bin/wpp %F
Icon=$PREFIX/share/icons/powerpoint-icon.png
Terminal=false
StartupWMClass=wps-office-wpp   
Type=Application
Categories=Office;                                                    
StartupNotify=true" > $PREFIX/share/applications/wps-office-wpp.desktop




cp $PREFIX/share/applications/wps-office-et.desktop $HOME/Desktop 
chmod +x $HOME/Desktop/wps-office-et.desktop

cp $PREFIX/share/applications/wps-office-wpp.desktop $HOME/Desktop 
chmod +x $HOME/Desktop/wps-office-wpp.desktop

cp $PREFIX/share/applications/wps-office-wps.desktop $HOME/Desktop 
chmod +x $HOME/Desktop/wps-office-wps.desktop
