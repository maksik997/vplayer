from typing import Final

from vlc import Instance, EventType, Event


class Player:
    SETTINGS : Final = ("--intf", "dummy",
                       "--no-video", "--quiet")

    def __init__(self, playlist : tuple[str, ...]):
        self.instance = Instance(*Player.SETTINGS)
        self.player = self.instance.media_player_new()
        self.media = None
        self.event_manager = self.player.event_manager()
        self.event_manager.event_attach(EventType.MediaPlayerEndReached, self.on_end)
        self.playlist = playlist
        self.current_track = 0
        self.running = True

    def play_track(self, index : int):
        if 0 <= index < len(self.playlist):
            self.media = self.instance.media_new(self.playlist[index])
            self.player.set_media(self.media)
            self.player.play()

    def start(self):
        self.play_track(0)

    def stop(self):
        self.player.stop()

    def is_running(self) -> bool:
        return self.running

    def on_end(self, event : Event):
        self.current_track += 1
        if self.current_track >= len(self.playlist):
            self.running = False
        else:
            self.play_track(self.current_track)

