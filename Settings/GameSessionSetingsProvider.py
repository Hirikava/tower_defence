import abc
import inject

from SettingsReader import ISettingsReader


class IGameSessionSettingsProvider():
    @abc.abstractmethod
    def get_settings(self):
        raise NotImplementedError


class GameSessionSettingsProvider(IGameSessionSettingsProvider):
    def __init__(self):
        self.reader = inject.instance(ISettingsReader)()

    def get_settings(self):
        self.reader.read('game_session_settings.ini')




