# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.config import Config
# from kivy.uix.floatlayout import FloatLayout

# Config.set('graphics', 'resizable', '0')
# Config.set('graphics', 'width', '640')
# Config.set('graphics', 'height', '480')




# class MyApp(App):
#     def build(self):

#         fl = FloatLayout(size = (300, 300))
#         fl.add_widget(Button(text='first button',\
#             font_size = 30,
#             on_press = self.btn_press,
#             background_color = [0, 1, 0.063, 1],
#             background_normal = '',
#             size_hint = (.5, .25),
#             pos = (640/2-(640/2/2), 480/2-(480*.25/2))))

#         return fl
    
#     def btn_press(self, instance):
#         print(f'Кнопка {instance.text} нажата')
#         instance.text = "I'm presed"

# if __name__ == '__main__':
#     MyApp().run()

# from kivy.app import App
# from kivy.uix.button import Button

# from kivy.uix.boxlayout import BoxLayout

# class BoxApp(App):
#     def build(self):
#         bl = BoxLayout(orientation='vertical', padding=[50, 25], spacing=100)

#         bl.add_widget( Button(text='1') )
#         bl.add_widget( Button(text='2') )
#         bl.add_widget( Button(text='3') )

#         return bl

# if __name__ == '__main__':
#     BoxApp().run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.core.window import Window
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
from random import random

class PainterWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def on_touch_down(self, touch):
        with self.canvas:
            Color(random(), random(), random(), 1)
            rad = 10
            Ellipse(pos = (touch.x-rad/2, touch.y-rad/2), size=(rad, rad))
            touch.ud['line'] = Line(points = (touch.x, touch.y), width=5)
    
    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)
            

class PointApp(App):
    def build(self):
        parent = Widget()
        self.painter = PainterWidget()
        parent.add_widget(self.painter)
        parent.add_widget(Button(text='Clear', on_press = self.clear_canvas, size=(100, 50)))
        parent.add_widget(Button(text='Save', on_press = self.save, size=(100, 50), pos=(100,0)))


        return parent
    
    def clear_canvas(self, i):
        self.painter.canvas.clear()

    def save(self, i):
        self.painter.size = (Window.size[0], Window.size[1])
        self.painter.export_to_png('image.png')



if __name__ == '__main__':
    PointApp().run()