import imageio
from os import listdir, fsdecode

class Img2gif():

    def __init__(self):

        self.name = input("GIF name (without .gif): ")
        self.speed = input("GIF speed (example: 0.1s): ")

    def to_gif(self):
        
        filenames = []

        for file in listdir():
            filename = fsdecode(file)
            if filename.endswith( ('.jpeg', '.png', '.gif') ):
                filenames.append(filename)

        filenames.sort()
            
        images = list(map(lambda filename: imageio.imread(filename), filenames))

        imageio.mimsave(self.name + ".gif", images, duration = self.speed)

Img2gif().to_gif()
