from Settings.GameSessionSetingsProvider import IGameSessionSettingsProvider, GameSessionSettingsProvider


def game_session_settings_config(binder):
    binder.bind(IGameSessionSettingsProvider,GameSessionSettingsProvider)