from math import atan2, degrees
from kivy.base import runTouchApp

from kivy.animation import Animation
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ListProperty, ReferenceListProperty


Builder.load_string('''                                                                                                                                        
<PlayerImage>:                                                                                                                                                 
    canvas.before:                                                                                                                                             
        PushMatrix                                                                                                                                             
        Rotate:                                                                                                                                                
            angle: self.angle                                                                                                                                  
            axis: (0, 0, 1)                                                                                                                                    
            origin: self.center                                                                                                                                
    canvas.after:                                                                                                                                              
        PopMatrix                                                                                                                                              
''')


class PlayerImage(Image):
    angle = NumericProperty(0)

    def on_touch_down(self, touch):
        Animation.cancel_all(self)
        angle = degrees(atan2(touch.y - self.center_y,
                              touch.x - self.center_x))

        Animation(center=touch.pos, angle=angle).start(self)


root = Builder.load_string('''                                                                                                                                 
Widget:                                                                                                                                                        
    PlayerImage:                                                                                                                                               
        source: 'boy.png'                                                                                                                                  
        allow_stretch: True                                                                                                                                    
        keep_ratio: False                                                                                                                                      
''')

runTouchApp(root)
