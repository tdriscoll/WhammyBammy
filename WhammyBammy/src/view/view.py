from PyQt4.QtGui import QGraphicsView, QPixmap, QGraphicsPixmapItem, QMainWindow, QActionGroup, QGraphicsScene, \
                        QDesktopWidget, QMatrix, QAction, QIcon, qApp, QGraphicsSimpleTextItem, QGraphicsItemAnimation
from PyQt4.QtCore import Qt, QTimer, QRectF, QTimeLine, QPointF
from os.path import join
from functools import partial 

class Instruction(object): pass
    
class View(QGraphicsView):
    
    # change the scene =  on change, renger the next events 
    
    def __init__(self):
        QGraphicsView.__init__(self)
        self.resize(1024, 768) 
        self.qtscene = None
        self.references = []
        self.items = {}
        
    def show_scene(self, scene):
        self.references = []
        self.qtscene = QGraphicsScene(self)
        self.qtscene.setSceneRect(QRectF(0, 0, 1000, 750))
        self.setScene(self.qtscene)
        for stage_direction in scene.stage_directions:
            self.schedule_stage_direction(stage_direction)
    
    def schedule_stage_direction(self, stage_direction):
        QTimer.singleShot(stage_direction.start, partial(self.render_stage_direction, stage_direction))
    
    def render_stage_direction(self, stage_direction):
        item = self.add_item(stage_direction.character)
        tl = QTimeLine(stage_direction.duration)
        a = QGraphicsItemAnimation()
        a.setItem(item)
        a.setTimeLine(tl)
        for movement in stage_direction.movements:
            a.setPosAt(movement.step, QPointF(movement.coordinate.x, movement.coordinate.y))
            if movement.rotation is not None:
                a.setRotationAt(movement.step, movement.rotation)
            if movement.xscale is not None:
                a.setScaleAt(movement.step, movement.xscale, movement.yscale)
        tl.start()
        self.add_reference(tl, a)
    
    def add_reference(self, *a):
        """ Some PyQT stuff requires you to hold onto it otherwise it gets GCed """
        self.references.extend(a)
    
    def add_item(self, character):
        item = self.items.get(character)
        if item:
            return item
        pmap = QPixmap(join("..", "images", character.image))
        item = QGraphicsPixmapItem(pmap)
        item.setZValue(1)
        self.qtscene.addItem(item)
        self.add_reference(pmap)
        self.items[character] = item
        return item
        
