# coding=utf-8
from Tkinter import *


import ttk


import pymssql


class MSSQL:
    """
    对pymssql的简单封装
    pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

    用法：

    """

    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

class Glis:

    def __init__(self, master):

        frame = Frame(master,width=2000,height=1000)
        frame.grid(row=0, column=0, rowspan=5,columnspan=8)

        default_ip = StringVar()
        default_ip.set('192.168.0.222')

        default_usr = StringVar()
        default_usr.set('sa')

        default_pwd = StringVar()
        default_pwd.set('S60INFO2000')

        default_database = StringVar()
        default_database.set('glis7')

        default_sql = StringVar()
        default_sql.set('select * from dzxxb bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')

        self.lbl1 = Label(frame, text="IP")
        self.entry1 = Entry(frame, textvariable=default_ip)

        self.lbl2 = Label(frame, text="用户名")
        self.entry2 = Entry(frame, textvariable=default_usr)
        self.lbl3 = Label(frame, text="密码")
        self.entry3 = Entry(frame, textvariable=default_pwd)

        self.lbl4 = Label(frame, text="数据库")
        self.entry4 = Entry(frame, textvariable=default_database)

        self.connect = Button(frame, text="连接", command=self.getconn)
        self.execute = Button(frame, text="执行sql", command=self.getconn)

        self.sqlstr = Text(frame, width=200, height=20)

        self.lbl5 = Label(frame, text="导出")
        self.entry5 = Entry(frame, textvariable=default_database)

        self.results = ttk.Notebook(frame, height=100, width=1400)

        self.panedwindow = ttk.PanedWindow(frame, height=100,width=1400)

        left = Label(self.panedwindow, text="left pane")
        self.panedwindow.add(left)

        panedwindow2 = PanedWindow(self.panedwindow, orient=VERTICAL)
        self.panedwindow.add(panedwindow2)

        top = Label(panedwindow2, text="top pane")
        panedwindow2.add(top)

        bottom = Label(panedwindow2, text="bottom pane")
        panedwindow2.add(bottom)

        self.lbl1.grid( row=2, column=0)
        self.entry1.grid( row=2, column=1)
        self.lbl2.grid( row=2, column=2)
        self.entry2.grid(row=2, column=3)
        self.lbl3.grid(row=2, column=4)
        self.entry3.grid(row=2, column=5)
        self.lbl4.grid(row=2, column=6)
        self.entry4.grid(row=2, column=7)
        self.connect.grid(row=2, column=8)
        self.execute.grid(row=2, column=9)
        # self.sqlstr.pack()

        self.sqlstr.grid(sticky=NW, row=3, column=0, rowspan=1, columnspan=10)

        self.lbl5.grid(row=4, column=0)
        self.entry5.grid(row=4, column=1)

        self.results.grid(row=5, column=0, rowspan=2, columnspan=10)

        self.panedwindow.grid(row=7, column=0, rowspan=2, columnspan=10)
        # self.panedwindow.pack(fill=BOTH, expand=1)

    def getconn(self):
        self.conn = MSSQL(host=self.entry1.get(),user=self.entry1.get(),pwd=self.entry1.get(),db=self.entry1.get())
        print self.conn


root = Tk()
glis = Glis(root)

root.mainloop()


