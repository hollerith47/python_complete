from PySide2 import QtWidgets

class App(QtWidgets.QWidget):
	def __init__(self):
		super(App, self).__init__()
		self.setWindowTitle("Main Hmak")
		self.interface()
	
	def interface(self):
		self.layout = QtWidgets.QHBoxLayout(self)
		self.combo_box = QtWidgets.QComboBox()
		self.spin = QtWidgets.QSpinBox()
		
		self.layout.addWidget(self.combo_box)
		self.layout.addWidget(self.spin)
		
		

app = QtWidgets.QApplication([])
fenetre = App()
fenetre.show()
app.exec_()