pip install kivy pygame
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import pygame

class MediaPlayerApp(App):
    def build(self):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound("your_audio_file.mp3")  # Replace with your file
        
        layout = BoxLayout()
        play_button = Button(text="Play")
        pause_button = Button(text="Pause")
        stop_button = Button(text="Stop")

        play_button.bind(on_press=self.play_sound)
        pause_button.bind(on_press=self.pause_sound)
        stop_button.bind(on_press=self.stop_sound)

        layout.add_widget(play_button)
        layout.add_widget(pause_button)
        layout.add_widget(stop_button)

        return layout

    def play_sound(self, instance):
        self.sound.play()

    def pause_sound(self, instance):
        pygame.mixer.pause()

    def stop_sound(self, instance):
        self.sound.stop()

if __name__ == "__main__":
    MediaPlayerApp().run()
