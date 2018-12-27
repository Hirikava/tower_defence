from UserInterface.Actions.Explosion import ButtonExplousion

instance = {"explousion" : ButtonExplousion}

def get_button(name):
    return instance[name]