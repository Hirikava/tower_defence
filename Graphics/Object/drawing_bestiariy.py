from Graphics.Manager.TextureManager import TextureManager

bestiariy = {"skeleton" : "Assets\\monster.png",
             "archery": "Assets\\tower.png",
             "arrow" : "Assets\\arrow.png"}

def get_drawing_instance(name):
    return TextureManager().load_texture(bestiariy[name])