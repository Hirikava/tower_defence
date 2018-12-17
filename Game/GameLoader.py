class GameLoader():
    def load(self,filename):
        res = dict()
        with open(filename,'r',encoding='utf-8') as file:
            res["life_counter"] = int(file.readline())
            spawner_tokens = file.readline().split(",")
            res["spawner_pos"] = (int(spawner_tokens[0]),int(spawner_tokens[1]))
            res["track"] = list()
            for point in file.readline().split(" "):
                point = point.split(",")
                res["track"].append((int(point[0]),int(point[1])))
            res["spawn_monsters"] = list()
            token = file.readline()
            while token:
                tokens = token.split(":")
                res["spawn_monsters"].append((int(tokens[0]),tokens[1].replace("\n","")))
                token = file.readline()
        return res
