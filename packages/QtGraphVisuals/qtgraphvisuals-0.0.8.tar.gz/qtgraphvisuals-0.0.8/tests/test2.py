import sys
import networkx as nx
from PySide6.QtWidgets import QApplication
from QtGraphVisuals import QGraphViewer

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setApplicationName("QtGraphVisuals Demo")

    viewer = QGraphViewer({'graph1': nx.path_graph([1,2,3], create_using=nx.DiGraph)})
    viewer.resize(800,600)
    viewer.show()

    sys.exit(app.exec())
