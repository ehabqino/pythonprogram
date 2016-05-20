import sys
from PyQt4.Qt import *
app=QApplication(sys.argv)

button=QPushButton("Hello World",None)
button.show()
app.exec_()