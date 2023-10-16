from PySideUI import *
from PySide2.QtWidgets import QWidget, QHBoxLayout, QApplication, QPushButton, QMessageBox
import sys


app = QApplication(sys.argv)
wd = QWidget()
lyt = QHBoxLayout()
wd.setLayout(lyt)
btn2 = SecondaryBtn('测试')
btn3 = PrimaryBtn('测试', {'color': 'red', 'background-color':'pink'}, clicked=lambda:print('hello world'))

lyt.addWidget(btn2)
lyt.addWidget(btn3)
wd.show()
sys.exit(app.exec_())



