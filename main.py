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


'''
    now()
    函数功能：获取当前年月
    函数参数：无
    函数输出：无
'''
def now():
    global yy
    global mm
    yy = datetime.datetime.now().year
    mm = datetime.datetime.now().month
    dd = datetime.datetime.now().day
    pdcstr()


'''
    funl(),“lastmonth”上一月按钮触发函数
    函数功能：计算上一月的年月，并修改全局变量的值
    函数参数：无
    函数输出：无
'''
def funl():
    global mm
    global yy
    if mm != 1:
        mm = mm - 1
    else:
        mm = 12
        yy = yy - 1
    pdcstr()


'''
    funn(),“nextmonth”下一月按钮触发函数
    函数功能：计算下一月的年月，并修改全局变量的值
    函数参数：无
    函数输出：无
'''
def funn():
    global mm
    global yy
    if mm != 12:
        mm += 1
    else:
        mm = 1
        yy += 1
    pdcstr()

'''
    fung(),“Go”按钮触发函数
    函数功能：获取当前输入的年月，及其所对应的当月日历
    函数参数：ui
    函数输出：无
'''
def fung(ui):
    global mm
    global yy
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
    pdcstr()

'''
    dealstr(s, x, dd),
    函数功能：检索获取的字符串，获取今天所对应日期再字符串中的标号
    函数参数：s(string)待检索字符串,x(int)天的位数,dd(int)日期（--日）
    函数输出：i 序号
'''
def dealstr(s, x, dd):
    today = str(dd)
    if x == 0:  # 显示该月日历的第一行
        return 0
    elif x == 1:            # 今天的日期’—-日‘是一位数
        for i in range(1, len(s)):
            if (s[i - 1] == ' ' or s[i - 1] == '\n') and s[i] == today:
                return i
    elif x == 2:            # 今天的日期’—-日‘是两位数
        for i in range(1, len(s)):
            if (s[i - 1] == ' ' or s[i - 1] == '\n') and s[i] == today[0] and s[i + 1] == today[1]:
                return i

'''
    pdcstr()
    函数功能：生成字符串
    函数参数：s(string)待检索字符串,x(int)天的位数,dd(int)日期（--日）
    函数输出：i 序号
'''
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
            else:
                ui.textBrowser.setText(temp[0:idxtdy-1]+'['+today+']'+temp[idxtdy+3:])
    else:
        ui.textBrowser.setText(temp)



if __name__ == '__main__':
    # 初始化
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = uif.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # 连接按钮gbtn与函数fung，并传参数ui
    ui.gbtn.clicked.connect(partial(fung, ui))
    # 连接按钮lbtn与函数funl
    ui.lbtn.clicked.connect(funl)
    # 连接按钮nbtn与函数funn
    ui.nbtn.clicked.connect(funn)
    # 连接按钮nowbtn与函数now
    ui.nowbtn.clicked.connect(now)
    #显示当月日历
    pdcstr()
    # 退出程序
    sys.exit(app.exec_())
