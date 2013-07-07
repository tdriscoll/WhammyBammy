from PyQt4.QtGui import QApplication
import sys
from production.presenter import Presenter
from view.view import View

#TODO: images sort of jump around at the start, try inserting at the right location?
#TODO: set backround color
#

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Whammy Bammy!")
    view = View()
    presenter = Presenter(view)
    presenter.initialize()
    view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()