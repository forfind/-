# 引入日历模块
import calendar
# 引入datetime模块，以获取当前日期和时间
import datetime
# 引入QT5相关库
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import ui as ui
from functools import partial
# 引入DATE_2文件，以完成界面布局以及按钮关联
import DATE_ui as uif

# 指定年月为当前年月
yy = datetime.datetime.now().year
mm = datetime.datetime.now().month

# 获取当前年月
def now():
    global yy
    global mm
    yy = datetime.datetime.now().year
    mm = datetime.datetime.now().month
    dd = datetime.datetime.now().day
    pdcstr()


def funl():
    global mm
    global yy
    if mm != 1:
        mm = mm - 1
    else:
        mm = 12
        yy = yy - 1
    pdcstr()


def funn():
    global mm
    global yy
    if mm != 12:
        mm += 1
    else:
        mm = 1
        yy += 1
    pdcstr()


def fung(ui):
    global mm
    global yy
    print("1.yy=", yy, "mm=", mm)
    tmp_y = yy
    tmp_m = mm
    yy = int(ui.lE_y.text())
    mm = int(ui.lE_m.text())
    if mm > 12:
        yy = tmp_y
        mm = tmp_m
        ui.lE_y.setText(str(yy))
        ui.lE_m.setText(str(mm))
        return
    print("2.yy=", yy, "mm=", mm)
    pdcstr()


def dealstr(s, x, dd):
    today = str(dd)
    if x == 0:  # 显示该月日历的第一行
        return 0
    elif x == 1:            # 今天的日期’—-日‘是一位数
        for i in range(1, len(s)):
            print("start:"+s[i]+"end")
            if (s[i - 1] == ' ' or s[i - 1] == '\n') and s[i] == today:
                return i
    elif x == 2:            # 今天的日期’—-日‘是两位数
        for i in range(1, len(s)):
            print(s[i], end="")
            if (s[i - 1] == ' ' or s[i - 1] == '\n') and s[i] == today[0] and s[i + 1] == today[1]:
                print("i=",i)
                return i


def pdcstr():
    global yy
    global mm
    # 显示年月
    ui.lE_y.setText(str(yy))
    ui.lE_m.setText(str(mm))
    # 通过calender库获取mm月的日历
    temp = calendar.month(yy, mm)
    temp = temp.replace('\n', "\n ")
    if yy == datetime.datetime.now().year and mm == datetime.datetime.now().month:
        dd = datetime.datetime.now().day
        today = str(dd)
        if len(today) == 1:
            idxtdy = dealstr(temp, 1, dd)
            if temp[idxtdy+1] == '\n':
                ui.textBrowser.setText(temp[0:idxtdy-1]+'['+today+']'+temp[idxtdy+1:])
            else:
                ui.textBrowser.setText(temp[0:idxtdy-1]+'['+today+']'+temp[idxtdy+2:])
        if len(today) == 2:
            idxtdy = dealstr(temp, 2, dd)
            if temp[idxtdy+2] == '\n':
                ui.textBrowser.setText(temp[0:idxtdy-1]+'['+today+']'+temp[idxtdy+2:])
            elif temp[idxtdy-2] == '\n':
                ui.textBrowser.setText(temp[0:idxtdy-1]+'['+today+']'+temp[idxtdy+3:])
            else:
                ui.textBrowser.setText(temp[0:idxtdy-1]+'['+today+']'+temp[idxtdy+3:])
    else:
        ui.textBrowser.setText(temp)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = uif.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.gbtn.clicked.connect(partial(fung, ui))
    ui.lbtn.clicked.connect(funl)
    ui.nbtn.clicked.connect(funn)
    ui.nowbtn.clicked.connect(now)

    pdcstr()
    sys.exit(app.exec_())
