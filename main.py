import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

kivy.require('2.1.0')


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def click_button(self):
        app = App.get_running_app()
        sm = app.root.ids.sm
        sm.current = 'second_screen'


class SecondScreen(Screen):
    pass


class MyApp(App):
    def build(self):
        self.title = 'Screen with Header and Footer'
        return Builder.load_file('gui.kv')


if __name__ == '__main__':
    MyApp().run()
