#gui面向对象编程
from tkinter import *
from tkinter import messagebox
class Application(Frame):
    """一个经典gui程序写法"""

    def __init__(self,master=None):#构造器
        super().__init__(master)  #super代表父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):#再次创建组件
        self.label01 = Label(self,text='用户名')
        self.label01.pack()
        #stringvar变量绑定到指定组件
        #stringvar变量的值发生变化，组件内容也变化
        #组件内容变化，stringvar值也变化
        v1 = StringVar()
        self.entry01 = Entry(self,textvariable = v1)
        self.entry01.pack()
        v1.set("admin")
        print(v1.get());print(self.entry01.get())
        #创建密码
        self.label02 = Label(self, text='密码')
        self.label02.pack()

        v2 = StringVar()#密码
        self.entry02 = Entry(self, textvariable=v2,show = "*")
        self.entry02.pack()

        self.btn01 = Button(self,text='登录',command = self.login)
        self.btn01.pack()

    def login(self):
        username = self.entry01.get()
        pwd = self.entry02.get()
        print("用户名："+username)
        print("密码：" + pwd)
        if username=="admin" and pwd =="12345":
            messagebox.showinfo("学习系统", "登陆成功！开始学习！")
        else:
            messagebox.showinfo("学习系统", "登录错误")




if  __name__=='__main__':
    root = Tk()
    root.geometry("400x340+200+300")
    root.title("学习系统")
    app = Application(master=root)

    root.mainloop()
