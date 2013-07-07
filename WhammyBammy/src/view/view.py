from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QGraphicsView, QPixmap, QGraphicsPixmapItem, QMainWindow, QActionGroup, QGraphicsScene, \
                        QDesktopWidget, QMatrix, QAction, QIcon, qApp, QGraphicsSimpleTextItem
from PyQt4.QtCore import Qt, QTimer
from os.path import join
from functools import partial 

class Instruction(object): pass
    
class View(QtGui.QGraphicsView):
    
    #change the scene =  on change, renger the next events 
    
    def __init__(self):
        QtGui.QGraphicsView.__init__(self)
        self.resize(1024, 768) 
        self.qtscene = None
        self.references = []
        self.items = {}
        
    def show_scene(self, scene):
        self.references = []
        self.qtscene = QtGui.QGraphicsScene(self)
        self.qtscene.setSceneRect(QtCore.QRectF(0, 0, 1000, 750))
        self.setScene(self.qtscene)
        for stage_direction in scene.stage_directions:
            self.schedule_stage_direction(stage_direction)
        
    
    def schedule_stage_direction(self, stage_direction):
        QTimer.singleShot(stage_direction.start, partial(self.render_stage_direction, stage_direction))
    
    def render_stage_direction(self, stage_direction):
        item = self.add_item(stage_direction.character)
        tl = QtCore.QTimeLine(stage_direction.duration)
        a = QtGui.QGraphicsItemAnimation()
        a.setItem(item)
        a.setTimeLine(tl)
        for movement in stage_direction.movements:
            a.setPosAt(movement.step, QtCore.QPointF(movement.coordinate.x, movement.coordinate.y))
            if movement.rotation is not None:
                a.setRotationAt(movement.step, movement.rotation)
            if movement.xscale is not None:
                a.setScaleAt(movement.step, movement.xscale, movement.yscale)
        tl.start()
        self.add_reference(tl, a)
    
    def add_reference(self, *a):
        self.references.extend(a)
    
    def add_item(self, character):
        item = self.items.get(character)
        if item:
            return item
        pmap = QPixmap(join("..", "images", "protagonist.jpg"))
#         pmap.scaled(100, 50, QtCore.Qt.KeepAspectRatio)
        item = QGraphicsPixmapItem(pmap)
        item.setZValue(1)
        self.qtscene.addItem(item)
        self.add_reference(pmap)
        self.items[character] = item
        return item
        
