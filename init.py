import inject
from Graphics.config import graphics_config
from Game.config import game_session_settings_config
from Settings.config import settings_reader_config

def app_config(binder):
    game_session_settings_config(binder)
    settings_reader_config(binder)
    graphics_config(binder)

def init():
    inject.configure(app_config)