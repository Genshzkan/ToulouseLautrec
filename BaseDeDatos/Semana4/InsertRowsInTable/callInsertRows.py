import sqlite3, sys
from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error
from demoInsertRowsInTable import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonInsertRow.clicked.connect(self.InsertRows)
        self.show()
    def InsertRows(self):
        sqlStatement="INSERT INTO "+self.ui.lineEditTableName.text()+"VALUES('"+self.ui.lineEditEmailAddress.text()+"','"+self.ui.lineEditPassword.text()+"')"
        try: 
            conn = sqlite3.connect(self.ui.lineEditDBName.text()+".db")
        with conn:  #error acá, muy seguro que es por algun espacio extra en el código o un paréntesis extra
            cur = conn.cursor()
            cur.execute(sqlStatement)
            self.ui.labelResponse.setText("Row successfully inserted")
        except Error as e:
            self.ui.labelResponse.setText("Error in inserting row")
        finally:
            conn.close()
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())