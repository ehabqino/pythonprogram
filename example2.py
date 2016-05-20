import sys
from PyQt4.Qt import *
app=QApplication(sys.argv)

w=QWidget()
w.resize(320,240)
w.setWindowTitle("Hello World !")
w.show()

sys.exit(app.exec_())