from PyQt4.QtGui import QGraphicsView, QPixmap, QGraphicsPixmapItem, QGraphicsScene, QGraphicsSimpleTextItem, QGraphicsItemAnimation, qApp, QBrush, QColor, QFont
from PyQt4.QtCore import QTimer, QRectF, QTimeLine, QPointF, Qt
from os.path import join
from functools import partial 

class Instruction(object): pass
    
class View(QGraphicsView):
    
    def __init__(self):
        QGraphicsView.__init__(self)
        self.resize(1024, 768) 
        self.qtscene = None
        self.references = []
        self.items = {}
        self.timelines = []
        self.max_time = 0
        
    def init_scene(self, scene):
        #TODO: background, sound
        self.references = []
        self.items = {}
        self.qtscene = QGraphicsScene(self)
        self.qtscene.setSceneRect(QRectF(0, 0, 1000, 750))
        brush = QBrush(QColor(80,90,130))
        self.qtscene.setBackgroundBrush(brush)
        
        self.setScene(self.qtscene)
        
    def load_directions(self, stage_directions):
        self.max_time = 0
        for character, item in self.items.items():
            if character.text:
                item.hide() 
        for stage_direction in stage_directions:
            self.schedule_stage_direction(stage_direction)
            self.max_time = max(self.max_time, stage_direction.end)
        QTimer.singleShot(self.max_time, self.on_directions_finished)
        
    
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
        self.timelines.append(tl)
        self.add_reference(a)
    
    def add_reference(self, *a):
        """ Some PyQT stuff requires you to hold onto it otherwise it gets GC'ed """
        self.references.extend(a)
    
    def add_item(self, character):
        item = self.items.get(character)
        if item:
            return item
        if character.text:
            item =  QGraphicsSimpleTextItem(character.text)
            item.setBrush(QBrush(QColor(199,0,3)))
            item.setFont(QFont("Times", 30, QFont.Bold)) 
        else:
            pmap = QPixmap(join("..", "images", character.image))
            item = QGraphicsPixmapItem(pmap)
            item.show()
            self.add_reference(pmap)
        item.setX(-1000) #Do not want it on the screen, 
        
        self.qtscene.addItem(item)
        self.items[character] = item
        return item
    
    def keyPressEvent(self, ev):
        if ev.key() == Qt.Key_Escape:
            self.quit()
        self.on_key_event(ev.key())
        
    def quit(self):
        qApp.quit() 
        
