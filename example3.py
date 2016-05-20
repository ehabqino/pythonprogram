import sys
from PyQt4.Qt import *
app=QApplication(sys.argv)

w=QWidget()
w.resize(320,240)
w.setWindowTitle("Hello World !")


button=QPushButton("Hello",w)
button.setToolTip("Click To Exit")
button.clicked.connect(exit)
button.resize(button.sizeHint())
button.move(100,80)

w.show()

sys.exit(app.exec_())