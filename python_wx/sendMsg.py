# !/usr/bin/python
import itchat
import _thread
import os
import time

name = ""
doc = []
inp = ""


def printDoc():
    os.system("cls")
    global inp
    global doc
    print("\n=====聊天界面======================")
    for i in doc:
        print(i)
    print("=====================================")
    time.sleep(2)
    inp = input("")


def sendMsg():
    global name
    global doc
    while True:
        print("======= 进入主界面 ======")
        name = input("choose your friend:")
        if name == "exit":  # 用户退出
            break
        if name == "filehelper":  # 如果是发送给自己的文件助手
            name = "filehelper"

        else:
            user = itchat.search_friends(name=name)
            if len(user) == 0:
                print("找不到用户:", name, "\n")
                continue
            else:
                name = user.userName
        print("===进入和 [", name, "]的聊天界面====")
        while True:
            printDoc()

            if inp == "exit":
                break
            else:
                itchat.send_msg(inp, toUserName=name)
                s = "me => " + inp
                doc.append(s)



@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def text_reply(msg):
    global on
    global name
    if msg.toUserName == name:
        s = "\t\t\t" + msg.text + " <= " + msg.toUserName
        doc.append(s)
        printDoc()
    return


_thread.start_new_thread(sendMsg, ())
# itchat.auto_login(enableCmdQR=1, hotReload=True) # 如果是在window上或者有可视化界面的ubuntu系统上，可以用这个
itchat.auto_login(enableCmdQR=0, hotReload=True)  # enableCmdQR=1是在控制台输出微信登录二维码
itchat.run()
