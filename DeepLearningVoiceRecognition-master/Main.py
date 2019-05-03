import speech_recognition as sr
from gtts import gTTS
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui
import os
import sys





metin=""
listWidget=""
def Mywindow():
    global listWidget
    global metin                           
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setGeometry(100, 100, 600, 700)                                 
    listWidget = QtWidgets.QListWidget(window)                                 
  
    listWidget.setFixedHeight(500)
    listWidget.setFixedWidth(600)
    listWidget.move(0,455)
    listWidget.setStyleSheet("""QListWidget{background: #e5e5e5;font-size:25px;Height:200;Width:500;color:#444;font:bold}""" )
                                   
                                    
                                    
    
                                    
    label1 = QtWidgets.QLabel(window)
    label1.setPixmap(QtGui.QPixmap("speaker.jpg"))
    label2 = QtWidgets.QLabel(window)
    movie=QtGui.QMovie("speaker.gif")
    label2.setMovie(movie)
    movie.start()
    buton_a = QtWidgets.QPushButton(window)
    buton_a.clicked.connect(aa)
    buton_a.setGeometry(1,1,600,100)
    buton_a.setStyleSheet("background-color: black ; color:#CCC5C3 ; font-size:25px ;font:italic")
    buton_a.setText('Konuşmak İçin Dokun')
    
   
    window.show()
    sys.exit(app.exec())
                                    
                                        
def aa():
    r = sr.Recognizer()
    m = sr.Microphone()
    global metin
    global listWidget
    try:
        metin=("hazırlanıyor\n"+metin)  
       
        listWidget.addItem(metin)                          
        print("hazırlanıyor..")
        with m as source: r.adjust_for_ambient_noise(source)
        print("Minimum enerji eşiğini{} :".format(r.energy_threshold))
        print("Konuşun!")
        with m as source: audio = r.listen(source)
        print("Ses tanınıyor")
        try:
            # Google Konuşma Tanıma'yı kullanarak konuşmayı tanır
            value = r.recognize_google(audio,language = "tr-TR")
                                
                                
            # unicode karakterleri standart çıktılara doğru şekilde basmak için bazı özel işlemlere ihtiyacımız var
            if str is bytes:
                print("Ses Analizi :{}".format(value).encode("utf-8"))
                                            
            elif ("{}".format(value)=="Selam"):
                # Burada kullanacağımız 2 parametre bulunuyor, Dil ve Text
                tts = gTTS(text='Merhaba', lang='tr')
                # Burada oluşturduğumuz ses dosyasını konuma merhaba.mp3 diye kaydediyoruz
                tts.save("merhaba.mp3")
                # şimdi ise bu dosyayı açalım.
                os.system("merhaba.mp3")
                                
            elif ("{}".format(value)=="çal"):
                os.system("cal.mp3")
            elif("{}".format(value)=="nasılsın"):
                print("İyiyim sahip Sen nasılsın")
            elif ("{}".format(value)=="Müzik çaları aç"):
                print("Müzik çalar açılıyor")
            else:
                print("Ses Analizi :{}".format(value))
                                
        except sr.UnknownValueError:
            print("Sesi algılayamadım")
        except sr.RequestError as e:
             print("Sistem dosyası eksik".format(e))
    except KeyboardInterrupt:
       pass
                                
Mywindow()
