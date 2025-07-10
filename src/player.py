from typing import Final, Sequence

from vlc import Instance, MediaList


class Player:
    SETTINGS : Final = ("--intf", "dummy",
                       "--no-video", "--quiet")

    def __init__(self, playlist : Sequence[str]):
        self.instance = Instance(*Player.SETTINGS)
        self.player = self.instance.media_list_player_new()
        self.media_list = self.__create_media_list(playlist)
        self.player.set_media_list(self.media_list)
        self.playlist = playlist
        self.running = True

    def start(self):
        self.player.play()

    def stop(self):
        self.player.stop()

    def is_running(self) -> bool:
        return self.player.is_playing()

    def __create_media_list(self, playlist : Sequence[str]) -> MediaList:
        ml = self.instance.media_list_new()
        for t in playlist:
            ml.add_media(self.instance.media_new(t))
        return ml

