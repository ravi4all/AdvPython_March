from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymysql

connection = pymysql.connect(host='localhost',user='root',
                             database='emp_db',port=3306,
                             autocommit = True
                             )
cursor = connection.cursor()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1260, 796)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 30, 761, 81))
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 250, 391, 71))
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(660, 250, 471, 71))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 370, 391, 71))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setGeometry(QtCore.QRect(660, 360, 471, 71))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 490, 251, 71))
        self.pushButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 620, 411, 81))
        self.pushButton_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1261, 761))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(420, 50, 431, 71))
        self.label_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(80, 190, 371, 61))
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(80, 270, 371, 61))
        self.label_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(80, 350, 371, 61))
        self.label_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(80, 430, 371, 61))
        self.label_8.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(80, 510, 371, 61))
        self.label_9.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(570, 190, 321, 61))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(570, 270, 321, 61))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(570, 350, 321, 61))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(570, 430, 321, 61))
        self.comboBox.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(570, 510, 321, 61))
        self.comboBox_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        # self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        # self.lineEdit_6.setGeometry(QtCore.QRect(570, 430, 321, 61))
        # self.lineEdit_6.setObjectName("lineEdit_6")
        # self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        # self.lineEdit_7.setGeometry(QtCore.QRect(570, 510, 321, 61))
        # self.lineEdit_7.setObjectName("lineEdit_7")

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 640, 381, 61))
        self.pushButton_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1261, 751))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(350, 20, 421, 71))
        self.label_10.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(80, 170, 1091, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        # self.tableWidget.setRowCount(1)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1260, 31))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuEmpSearch = QtWidgets.QMenu(self.menubar)
        self.menuEmpSearch.setObjectName("menuEmpSearch")
        self.menuDeleteEmp = QtWidgets.QMenu(self.menubar)
        self.menuDeleteEmp.setObjectName("menuDeleteEmp")
        self.menuUpdateEmp = QtWidgets.QMenu(self.menubar)
        self.menuUpdateEmp.setObjectName("menuUpdateEmp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionRegister = QtWidgets.QAction(MainWindow)
        self.actionRegister.setObjectName("actionRegister")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuOptions.addAction(self.actionLogin)
        self.menuOptions.addAction(self.actionRegister)
        self.menuOptions.addAction(self.actionQuit)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuEmpSearch.menuAction())
        self.menubar.addAction(self.menuDeleteEmp.menuAction())
        self.menubar.addAction(self.menuUpdateEmp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Employee Management System"))
        self.label_2.setText(_translate("MainWindow", "Enter Emp Id"))
        self.label_3.setText(_translate("MainWindow", "Enter Emp Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Register Now"))
        self.label_4.setText(_translate("MainWindow", "Register Employee"))
        self.label_5.setText(_translate("MainWindow", "Enter Emp ID"))
        self.label_6.setText(_translate("MainWindow", "Enter Emp Name"))
        self.label_7.setText(_translate("MainWindow", "Enter Emp Password"))
        self.label_8.setText(_translate("MainWindow", "Enter Emp Dept"))
        self.label_9.setText(_translate("MainWindow", "Enter Emp City"))
        self.pushButton_3.setText(_translate("MainWindow", "Register"))
        self.label_10.setText(_translate("MainWindow", "Employee Dashboard"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Emp_Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Emp_Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Emp_Department"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Emp_City"))

        # __sortingEnabled = self.tableWidget.isSortingEnabled()
        # self.tableWidget.setSortingEnabled(False)
        # item = self.tableWidget.item(0, 0)
        # item.setText(_translate("MainWindow", "0"))
        # item = self.tableWidget.item(0, 1)
        # item.setText(_translate("MainWindow", "admin"))
        # item = self.tableWidget.item(0, 2)
        # item.setText(_translate("MainWindow", "admin"))
        # item = self.tableWidget.item(0, 3)
        # item.setText(_translate("MainWindow", "Pune"))
        # self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuEmpSearch.setTitle(_translate("MainWindow", "EmpSearch"))
        self.menuDeleteEmp.setTitle(_translate("MainWindow", "DeleteEmp"))
        self.menuUpdateEmp.setTitle(_translate("MainWindow", "UpdateEmp"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionRegister.setText(_translate("MainWindow", "Register"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

        self.comboBox.setItemText(0, _translate("MainWindow", "IT"))
        self.comboBox.setItemText(1, _translate("MainWindow", "HR"))
        self.comboBox.setItemText(2, _translate("MainWindow", "BPO"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Tech Support"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Delhi"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Pune"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Chennai"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Mumbai"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Noida"))

        self.frame.hide()

        self.actionLogin.triggered.connect(self.showHome)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.showRegister)
        self.pushButton_3.clicked.connect(self.registerUser)

    def showHome(self):
        self.frame.hide()

    def showRegister(self):
        self.frame.show()
        self.frame_2.hide()

    def registerUser(self):
        emp_id = self.lineEdit_3.text()
        emp_name = self.lineEdit_4.text()
        emp_pwd = self.lineEdit_5.text()
        emp_dept = self.comboBox.currentText()
        emp_city = self.comboBox_2.currentText()
        query = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (emp_id, emp_name, emp_pwd, emp_dept, emp_city))

        QMessageBox.about(self, "Success", "Data Inserted Successfully...")

        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")

    def login(self):
        emp_id = self.lineEdit.text()
        emp_pwd = self.lineEdit_2.text()
        query = "SELECT * FROM employees WHERE emp_id = %s AND emp_pwd = %s"
        cursor.execute(query, (emp_id, emp_pwd))
        data = cursor.fetchall()
        # print(data)
        if len(data) > 0:
            self.showDashboard()
        else:
            QMessageBox.about(self, "Success", "User Don't Exist...")
    def showDashboard(self):
        self.frame.show()
        self.frame_2.show()

        query = "SELECT emp_id, emp_name, emp_dept, emp_city FROM employees"
        cursor.execute(query)
        data = cursor.fetchall()
        row_count = cursor.rowcount
        print(row_count)
        self.tableWidget.setRowCount(row_count)
        # for row in range(row_count):
        #     for col in range(len(data[0])):
        #         print(row, col)
        try:
            for row in range(row_count):
                for col in range(len(data[0])):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(row, col, item)
                    item = self.tableWidget.item(row, col)
                    item.setText(str(data[row][col]))
        except BaseException as ex:
            print(ex)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

