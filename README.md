ну, крч, эта штука работает только для X11 или для Wayland
она создана, чтобы отправлять заготовленные фразы и милоту
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
## для Arch
```
sudo pacman -S git python xdotool wtype
pip install Pillow pystray
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
![image](https://github.com/timscreep/blintyper/assets/81462085/042f83cd-29ed-4862-b1f6-7ed7a5b2fa0d)




вы в праве изменять абсолютно все файлы как хотите
