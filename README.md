ну, крч, эта штука работает только для X11 или для Wayland
прежде всего надо установить пайтон, xdotool и/или wtype, а затем библиотеки пайтон
после этого прописать штуку в автозапуск

# установка зависимостей

## для Ubuntu/Debian
```
sudo apt-get update && sudo apt-get install -y git python3 xdotool wtype
pip install Pillow pystray
```
## для Fedora
```
sudo dnf install git python3 xdotool wtype
pip install Pillow pystray
```
## для арча
```
sudo pacman -S git python xdotool wtype 
```



# установка
скачайте репозиторий (для этого требуется git):
```
git clone https://github.com/timscreep/blintyper.git
```
засуньте штуку в автозапуск, команда должна выглядеть как-то так:
```
cd blintyper && python3 quotim_wl.py
```
