import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

