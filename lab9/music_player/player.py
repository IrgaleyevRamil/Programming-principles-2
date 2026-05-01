import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        self.music_folder = music_folder
        self.playlist = []
        self.current_index = 0
        self.is_playing = False
        self.load_playlist()

    def load_playlist(self):
        for file in os.listdir(self.music_folder):
            if file.endswith(".wav") or file.endswith(".mp3"):
                self.playlist.append(file)

    def play(self):
        if not self.playlist:
            return

        track_path = os.path.join(self.music_folder, self.playlist[self.current_index])
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if not self.playlist:
            return

        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def previous_track(self):
        if not self.playlist:
            return

        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def get_current_track(self):
        if not self.playlist:
            return "No tracks found"
        return self.playlist[self.current_index]