import os

from ..logging import LOGGER


def dirr():
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
        elif file.endswith(".jpeg"):
            os.remove(file)
        elif file.endswith(".png"):
            os.remove(file)

    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")

    LOGGER(__name__).info("𝐃𝐢𝐫𝐞𝐜𝐭𝐨𝐫𝐢𝐞𝐬 𝐔𝐩𝐝𝐚𝐭𝐞𝐝.")
