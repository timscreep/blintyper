ну, крч, эта штука работает только для Wayland и Винды.

она создана для отправки заготовленных фраз и милоты через love.
Все работает по правой кнопки мыши из трея.
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
yay python-pillow python-pystray
```

## для Windows
батник от имени администратора установит нужную версию пайтона и зависимости
я бы полностью допилил бы еще и распаковку архива, но мне легче показать вам, как должны выглядеть папки

![image](https://github.com/timscreep/blintyper/assets/81462085/5e078370-d63e-4707-9972-40eee1faad9a)


# установка
скачайте репозиторий (для этого требуется git):
```
git clone https://github.com/timscreep/blintyper.git
```
засуньте следующую команду в автозапуск:
```
cd blintyper && python3 quotim_wl.py
```
![image](https://github.com/timscreep/blintyper/assets/81462085/042f83cd-29ed-4862-b1f6-7ed7a5b2fa0d)




вы в праве изменять абсолютно все файлы как хотите
