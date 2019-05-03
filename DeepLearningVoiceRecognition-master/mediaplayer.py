import subprocess
import threading


def windowsmedia(filename):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    a = subprocess.call('C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe /play /close "C:/Kullanıcılar/Serhat/Müzikler/ses.mp3"',startupinfo=startupinfo)

