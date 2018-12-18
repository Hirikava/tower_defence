from Graphics.Interfaces.PygameTextureLoadInterface import load_texture_config
from Graphics.Interfaces.PygameWindowProvider import window_provider_config


def graphics_config(binder):
    load_texture_config(binder)
    window_provider_config(binder)
