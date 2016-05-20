import  sys
from PyQt4.QtGui import *
a=QApplication(sys.argv)

w=QWidget()

result=QMessageBox.question(w,'Message',"Do You Like Python ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
if result == QMessageBox.Yes:
    print("Yes")
else:
    print ("No")

w.show()
sys.exit(a.exec_())