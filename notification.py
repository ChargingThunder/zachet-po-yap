from PyQt6 import QtCore, QtGui, QtWidgets

centralwidget = QtWidgets.QWidget()
font = QtGui.QFont()
font.setPointSize(12)
centralwidget.setFont(font)
centralwidget.setObjectName("centralwidget")
MainLabel = QtWidgets.QLabel(parent=centralwidget)
MainLabel.setGeometry(QtCore.QRect(150, 40, 391, 41))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(20)
font.setBold(True)
font.setWeight(75)
MainLabel.setFont(font)
MainLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
MainLabel.setObjectName("MainLabel")
SecondLabel = QtWidgets.QLabel(parent=centralwidget)
SecondLabel.setGeometry(QtCore.QRect(10, 90, 811, 61))
font = QtGui.QFont()
font.setFamily("Times New Roman")
SecondLabel.setFont(font)
SecondLabel.setObjectName("SecondLabel")
AdminKeyEdit = QtWidgets.QLineEdit(parent=centralwidget)
AdminKeyEdit.setGeometry(QtCore.QRect(40, 170, 241, 41))
font = QtGui.QFont()
font.setFamily("Times New Roman")
AdminKeyEdit.setFont(font)
AdminKeyEdit.setObjectName("AdminKeyEdit")
AdminKEyLAbel = QtWidgets.QLabel(parent=centralwidget)
AdminKEyLAbel.setGeometry(QtCore.QRect(50, 150, 201, 16))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(11)
AdminKEyLAbel.setFont(font)
AdminKEyLAbel.setObjectName("AdminKEyLAbel")
Submit = QtWidgets.QPushButton(parent=centralwidget)
Submit.setGeometry(QtCore.QRect(290, 170, 111, 41))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(14)
font.setBold(True)
font.setWeight(75)
Submit.setFont(font)
Submit.setObjectName("Submit")

MainLabel.setText("Добро пожаловать!")
SecondLabel.setText("Срок действия вашего гостевого пропуска истёк. Пожалйста позовите администратора.")
AdminKEyLAbel.setText("Ключ администратора:")
Submit.setText("Ввод")