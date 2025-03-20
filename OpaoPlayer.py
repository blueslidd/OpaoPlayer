from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.clock import Clock
import os

class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 加载音频文件
        self.sound = SoundLoader.load('opao.mp3')
        if self.sound:
            self.sound.loop = True  # 循环播放
            self.sound.volume = 1.0  # 最大音量
            self.sound.play()
        
        # 设置定时器，确保音频持续播放
        Clock.schedule_interval(self.ensure_playing, 1)
        
        # 禁用返回键
        Window.bind(on_keyboard=self.on_keyboard)

    def on_keyboard(self, window, key, *args):
        # 禁用所有键盘事件
        return True

    def ensure_playing(self, dt):
        # 确保音频始终在播放
        if self.sound and not self.sound.state == 'play':
            self.sound.play()
            self.sound.volume = 1.0

class MainApp(App):
    def build(self):
        # 禁用关闭按钮
        Window.borderless = True
        return MainWidget()

    def on_pause(self):
        # 防止应用暂停
        return False

    def on_stop(self):
        # 尝试阻止应用停止
        return False

if __name__ == '__main__':
    MainApp().run()
