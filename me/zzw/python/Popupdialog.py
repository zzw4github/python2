from tkMessageBox import *
from tkFileDialog import *
from tkColorChooser import *

askquestion("question","is 1+1=2")
showinfo(title="info", message="this is a message")
showerror(title="error", message="there is a error")

askopenfile()

result = askcolor()
