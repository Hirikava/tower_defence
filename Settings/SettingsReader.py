
def settings_reader_config(binder):
    binder.bind(ISettingsReader,SettingsReader)

class ISettingsReader():
    def read_settings(self,filename):
        raise NotImplementedError


class SettingsReader(ISettingsReader):
    def __init__(self):
        self.settings_dict = dict()
    def read_settings(self,filename):
        with open(filename,'r',encoding='utf-8') as file:
            for line in file:
                tokens = line.split("=")
                self.settings_dict[tokens[0]] = tokens[1]
        return self.settings_dict
