import abc
import inject

from Settings.SettingsReader import ISettingsReader

def game_session_settings_config(binder):
    binder.bind(IGameSessionSettingsProvider,GameSessionSettingsProvider)

class IGameSessionSettingsProvider():
    @abc.abstractmethod
    def get_settings(self):
        raise NotImplementedError


class GameSessionSettingsProvider(IGameSessionSettingsProvider):
    def __init__(self):
        self.reader = inject.instance(ISettingsReader)()

    def get_settings(self):
        return self.reader.read('game_session_settings.ini')




