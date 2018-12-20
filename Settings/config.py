from Settings.SettingsReader import SettingsReader, ISettingsReader


def settings_reader_config(binder):
    binder.bind(ISettingsReader,SettingsReader)