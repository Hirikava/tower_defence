from Graphics.Manager.TextureManager import TextureManager

bestiariy = {"skeleton" : "Assets/skeleton.png",
             "armored_skeleton" : "Assets/armored_skeleton.png",
             "archery": "Assets/archery.png",
             "archery*": "Assets/archery1.png",
             "archery**": "Assets/archery2.png",
             "arrow" : "Assets/arrow.png",
             "yadro" : "Assets/yadro.png",
             "canon" : "Assets/canon.png",
             "canon*" : "Assets/canon1.png",
             "canon**" : "Assets/canon2.png",
             "grass1" : "Assets/Grass1.png",
             "skeleton_king" : "Assets/skeleton_king.png",
             "explousion" : "Assets/explousion.png",
             "bird" : "Assets/bird.png"}

def get_drawing_instance(name):
    return TextureManager().load_texture(bestiariy[name])