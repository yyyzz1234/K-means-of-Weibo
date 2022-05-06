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
        self.label01 = Label(self,text='测试label',width=10,height=2,bg = 'black',fg = 'white')
        self.label01.pack()
        self.label02 = Label(self, text='测试label222', width=20, height=2, bg='black', fg='white',font=('SimHei.ttf',30))
        self.label02.pack()
        #显示图像
        global photo #把图片声明成全局变量，不然笨方法执行完毕后，图片销毁，无法显示
        photo = PhotoImage(file = "photo1.gif")
        self.label03 = Label(self,image = photo)
        self.label03.pack()
        #显示多行文本
        self.label04 = Label(self,text="12345\n上山大老鼠\n帅且高",borderwidth=1,relief="solid",justify="right")
        #relief边界效果
        self.label04.pack()


if  __name__=='__main__':
    root = Tk()
    root.geometry("400x640+200+300")
    root.title("测试label")
    app = Application(master=root)

    root.mainloop()
