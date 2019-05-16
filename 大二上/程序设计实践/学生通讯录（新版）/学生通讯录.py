from tkinter import *
from tkinter import messagebox

def add():
    # 下面定义增加信息文件操作
    def addData():
        if v1.get() == '' or v2.get() == '' or v3.get() == '':
            messagebox.showerror("IT Xiao Ang Zai", "信息有一个不能为空!")
        else:
            if int(v2.get()) < 0 or int(v2.get()) >= 100:
                messagebox.showinfo("IT Xiao Ang Zai", "您输入的年龄不合法!")
            else:
                messagebox.askokcancel("IT Xiao Ang Zai", "您确认增加该联系人吗?")
                if messagebox.askokcancel() is True:
                    # 下面是进行增加信息文件操作
                    with open("./record.txt", "a") as f1:
                        f1.write(v1.get())
                        f1.write(",")
                        if 0 <= int(v2.get()) < 10:
                            f1.write('0' + v2.get())
                        else:
                            f1.write(v2.get())
                        f1.write(",")
                        f1.write(v3.get())
                        f1.write("\n")
                    messagebox.showinfo("IT Xiao Ang Zai", "增加成功")

    # 下面是增加信息操作的界面化
    # 创建一个顶级容器
    top1 = Toplevel()
    top1.title("通讯录增加界面")
    # 不能使用两次Tk（）去创建窗体，因为tkinter中只能有一个主线程，
    # 当你需要再次创建一个窗体时，请使用Toplevel()。
    addPhoto = PhotoImage(file="./cc.gif")  # 创建背景图
    addZhuLabel = Label(top1, image=addPhoto)
    addZhuLabel.pack()
    addTextLabel1 = Label(top1, text="欢迎进入增加信息界面")  # 创建背景图上的文本
    addTextLabel1.place(relx=0.5, rely=0.1, anchor='center')
    addTextLabel2 = Label(top1, text="请输入下面信息")
    addTextLabel2.place(relx=0.5, rely=0.3, anchor='center')
    # 创建文本输入框
    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    Label(top1, text="人名").place(relx=0.2, rely=0.4)
    e1 = Entry(top1, textvariable=v1)
    e1.place(relx=0.3, rely=0.4, width=70)
    Label(top1, text="年龄").place(relx=0.6, rely=0.4)
    e2 = Entry(top1, textvariable=v2)
    e2.place(relx=0.7, rely=0.4, width=70)
    Label(top1, text="电话").place(relx=0.2, rely=0.6)
    e3 = Entry(top1, textvariable=v3)
    e3.place(relx=0.3, rely=0.6, width=160)
    # 创建选择按钮
    button1 = Button(top1, text='确认', width=10, height=3, bg='#00FF7F', command=addData)
    button1.place(relx=0.2, rely=0.7)
    button2 = Button(top1, text='退出', width=10, height=3, bg='#00FF7F', command=top1.withdraw)
    button2.place(relx=0.6, rely=0.7)
    mainloop()

def find():
    def findData():
        findName = vv.get()
        n = len(vv.get())
        if findName == '':
            messagebox.showerror("IT Xiao Ang Zai", "姓名不能为空!")
        else:
            temp = False
            with open("./record.txt", "r") as f2:
                text = f2.readline()
                while text:
                    if text.find(findName) == 0:
                        topp = Toplevel()
                        Label(topp, text="下面是联系人信息", pady=10).pack()
                        findName = Label(topp, text="姓名:" + text[0:len(findName)])
                        findName.pack()
                        findAge = Label(topp, text="年龄:" + text[n + 1:n + 3])
                        findAge.pack()
                        findTele = Label(topp, text="电话:" + text[n + 4:])
                        findTele.pack()
                        messagebox.showinfo("IT Xiao Ang Zai", "操作成功")
                        button1 = Button(topp, text='返回', width=7, height=2, bg='#00FF7F',
                                         command=topp.withdraw)
                        button1.pack()
                        mainloop()
                    else:
                        text = f2.readline()
            if temp == False:
                messagebox.showerror("IT Xiao Ang Zai", "没有该联系人，点击返回")

    top2 = Toplevel()
    top2.title("通讯录查找界面")
    findPhoto = PhotoImage(file="./cc.gif")  # 创建背景图
    findZhuLabel = Label(top2, image=findPhoto)
    findZhuLabel.pack()
    findTextLabel1 = Label(top2, text="欢迎进入查找信息界面", font=("", 15))  # 创建背景图上的文本
    findTextLabel1.place(relx=0.5, rely=0.1, anchor='center')
    findTextLabel2 = Label(top2, text="请确认要查找的联系人:")
    findTextLabel2.place(relx=0.5, rely=0.3, anchor='center')
    # 创建文本输入框
    vv = StringVar()
    Label(top2, text="姓名").place(relx=0.4, rely=0.5)
    e1 = Entry(top2, textvariable=vv)
    e1.place(relx=0.5, rely=0.5, width=50)
    # 创建选择按钮
    button1 = Button(top2, text='查找', width=10, height=3, bg='#00FF7F', command=findData)
    button1.place(relx=0.2, rely=0.7)
    button2 = Button(top2, text='退出', width=10, height=3, bg='#00FF7F', command=top2.withdraw)
    button2.place(relx=0.6, rely=0.7)
    mainloop()


def change():
    def changeData():
        myChooose = 1

        def writeFile():
            if v1.get() == '' or v2.get() == '' or v3.get() == '':
                messagebox.showerror("IT Xiao Ang Zai", "信息有一个不能为空!")
            else:
                if int(v2.get()) < 0 or int(v2.get()) >= 100:
                    messagebox.showinfo("IT Xiao Ang Zai", "您输入的年龄不合法!")
                else:
                    file_data = ""
                    with open("./record.txt", "r") as f:
                        for line in f:
                            if findName in line:
                                line = line.replace(text[0:len(findName)], v1.get())
                                if 0 <= int(v2.get()) < 10:
                                    line = line.replace(text[len(findName) + 1:len(findName) + 3], '0' + v2.get())
                                else:
                                    line = line.replace(text[len(findName) + 1:len(findName) + 3], v2.get())
                                line = line.replace(text[len(findName) + 4:], v3.get() + "\n")
                            file_data += line
                    with open("./record.txt", "w") as f2:
                        f2.write(file_data)
                    messagebox.showinfo("IT Xiao Ang Zai", "修改成功,点击退出")
                    topp.withdraw()
                    if messagebox.showinfo == 'ok':
                        exit()

        changeName = vv.get()
        if changeName == '':
            messagebox.showerror("IT Xiao Ang Zai", "姓名不能为空!")
        else:
            findName = vv.get()
            temp = False
            with open("./record.txt", "r") as f2:
                text = f2.readline()
                while text:
                    if text.find(findName) == 0:
                        messagebox.askokcancel("IT Xiao Ang Zai", "您确认修改该联系人吗?")
                        if messagebox.askokcancel() is True:
                            topp = Toplevel()
                            Label(topp, text="姓名").grid(row=0)
                            Label(topp, text="年龄").grid(row=1)
                            Label(topp, text="电话").grid(row=2)
                            v1 = StringVar()
                            v2 = StringVar()
                            v3 = StringVar()
                            Entry(topp, textvariable=v1).grid(row=0, column=1)
                            Entry(topp, textvariable=v2).grid(row=1, column=1)
                            Entry(topp, textvariable=v3).grid(row=2, column=1)
                            button1 = Button(topp, text='确认', width=6, height=2, bg='#00FF7F',
                                             command=writeFile)
                            button1.grid(row=3, columnspan=3, pady=5)
                            mainloop()
                        else:
                            myChooose = 2
                            break
                    else:
                        text = f2.readline()
            if temp == False:
                if myChooose == 1:
                    messagebox.showerror("IT Xiao Ang Zai", "没有该联系人，点击返回")
                else:
                    messagebox.showinfo("IT Xiao Ang Zai", "您决定不修改联系人信息!")

    top3 = Toplevel()
    top3.title("通讯录修改界面")
    deletePhoto = PhotoImage(file="./cc.gif")  # 创建背景图
    deleteZhuLabel = Label(top3, image=deletePhoto)
    deleteZhuLabel.pack()
    deleteTextLabel1 = Label(top3, text="欢迎进入修改信息界面", font=("", 15))  # 创建背景图上的文本
    deleteTextLabel1.place(relx=0.5, rely=0.1, anchor='center')
    deleteTextLabel2 = Label(top3, text="请确认要修改的联系人:")
    deleteTextLabel2.place(relx=0.5, rely=0.3, anchor='center')
    # 创建文本输入框
    vv = StringVar()
    Label(top3, text="姓名").place(relx=0.4, rely=0.5)
    e1 = Entry(top3, textvariable=vv)
    e1.place(relx=0.5, rely=0.5, width=50)
    # 创建选择按钮
    button1 = Button(top3, text='确认', width=10, height=3, bg='#00FF7F', command=changeData)
    button1.place(relx=0.2, rely=0.7)
    button2 = Button(top3, text='返回', width=10, height=3, bg='#00FF7F', command=top3.withdraw)
    button2.place(relx=0.6, rely=0.7)
    mainloop()


def delete():
    def deleteData():
        myChoose = 1
        deleteName = vv.get()
        if deleteName == '':
            messagebox.showerror("IT Xiao Ang Zai", "姓名不能为空!")
        else:
            temp = False
            with open("./record.txt", "r") as f5:
                text = f5.readline()
                while text:
                    if text.find(deleteName) == 0:
                        messagebox.askokcancel("IT Xiao Ang Zai", "您确认删除该联系人吗?")
                        if messagebox.askokcancel() is True:
                            file_data = ""
                            with open("./record.txt", "r") as f:
                                for line in f:
                                    if deleteName in line:
                                        line = line.replace(text[0:len(text)], "")
                                    file_data += line
                            with open("./record.txt", "w") as f:
                                f.write(file_data)
                            myChoose = 2
                            break
                        else:
                            myChoose = 3
                            break
                    else:
                        text = f5.readline()
            if temp == False:
                if myChoose == 1:
                    messagebox.showerror("IT Xiao Ang Zai", "没有该联系人，点击返回")
                elif myChoose == 2:
                    messagebox.showinfo("IT Xiao Ang Zai", "删除成功,点击退出")
                else:
                    messagebox.showinfo("IT Xiao Ang Zai", "您决定不删除联系人信息!")

    top4 = Toplevel()
    top4.title("通讯录删除界面")
    deletePhoto = PhotoImage(file="./cc.gif")  # 创建背景图
    deleteZhuLabel = Label(top4, image=deletePhoto)
    deleteZhuLabel.pack()
    deleteTextLabel1 = Label(top4, text="欢迎进入删除信息界面", font=("", 15))  # 创建背景图上的文本
    deleteTextLabel1.place(relx=0.5, rely=0.1, anchor='center')
    deleteTextLabel2 = Label(top4, text="请确认要删除的联系人:")
    deleteTextLabel2.place(relx=0.5, rely=0.3, anchor='center')
    # 创建文本输入框
    vv = StringVar()
    Label(top4, text="姓名").place(relx=0.4, rely=0.5)
    e1 = Entry(top4, textvariable=vv)
    e1.place(relx=0.5, rely=0.5, width=50)
    # 创建选择按钮
    button1 = Button(top4, text='确认', width=10, height=3, bg='#00FF7F', command=deleteData)
    button1.place(relx=0.2, rely=0.7)
    button2 = Button(top4, text='返回', width=10, height=3, bg='#00FF7F', command=top4.withdraw)
    button2.place(relx=0.6, rely=0.7)
    mainloop()


def main():
    def secondJieMian():
        # 为单选按钮进行不同选择
        getChoose = v.get()
        if getChoose == 1:
            add()
        elif getChoose == 2:
            find()
        elif getChoose == 3:
            change()
        elif getChoose == 4:
            delete()
        else:
            exit()

    # 创建主窗口
    root = Tk()
    root.title("学生通讯录")
    # 创建背景图片
    photo = PhotoImage(file="./cc.gif")
    zhuLabel = Label(root, image=photo)
    zhuLabel.pack()
    # 创建背景图上的文本
    textLabel1 = Label(root, text="欢迎进入通讯录系统")
    textLabel1.place(relx=0.5, rely=0.1, anchor='center')
    textLabel2 = Label(root, text="请选择", font=("", 40), fg='#7CFC00', anchor='center')
    textLabel2.place(relx=0.5, rely=0.3, anchor='center')
    # 创建单选按钮
    choose = [("1.添加联系人", 1), ("2.查询联系人", 2), ("3.修改联系人", 3), ("4.删除联系人", 4),
              ("0.退出", 0)]
    v = IntVar()
    v.set(1)
    for lang, num in choose:
        a = Radiobutton(root, text=lang, variable=v, value=num)
        a.pack()
    # 创建选择按钮
    Button(root, text='确认', width=10, height=3, bg='#00FF7F', command=secondJieMian).pack(side='left')
    Button(root, text='退出', width=10, height=3, bg='#00FF7F', command=exit).pack(side='right')
    mainloop()


if __name__ == '__main__':
    main()

