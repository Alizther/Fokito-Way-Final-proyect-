from pathlib import Path
from typing import Any
import xml.etree.ElementTree as ET

from src.Tilemap import Tilemap

class TmxSceneLoader:
    FILE_EXT = "tmx"

    def __init__(self) -> None:
        self.height = None
        self.width = None
        self.tilewidth = None
        self.tileheight = None
        self.first_ids = {}

    def load(self, scene: any, scene_path: Path) -> None:
        tree = ET.parse(f"{scene_path}.{self.FILE_EXT}")
        root = tree.getroot()

        self.width = int(root.attrib["width"])
        self.height = int(root.attrib["height"])
        self.tilewidth = int(root.attrib["tilewidth"])
        self.tileheight = int(root.attrib["tileheight"])

        for child in root.findall("tileset"):
            name = Path(child.attrib["source"]).stem
            self.first_ids[name] = int(child.attrib["firstgid"])

        self.load_tilemap(scene, root)

        #for child in root.findall("group"):
        #    group_name = child.attrib["name"]
        #    getattr(self, f"load_{group_name}")(scene, child)

    def load_tilemap(self, scene: any, group: ET.Element) -> None:
        tilemap = Tilemap(self.height, self.width, self.tilewidth, self.tileheight)
        #scene.tilemap.update({"rows": self.height, "cols": self.width, "layers": []})

        for layer in group.findall("layer"):
            tilemap.create_layer()
            #l = [[None for _ in range(self.width)] for _ in range(self.height)]
            data = [
                line for line in layer.find("data").text.splitlines() if len(line) > 0
            ]
            for i in range(self.height):
                line = [s for s in data[i].split(",") if len(s) > 0]
                for j in range(self.width):
                    #value = int(line[j]) - self.first_ids["tiles"]
                    #if value is 0:
                    #    frame_index = 4
                    #frame_index = value
                    frame_index = int(line[j]) - self.first_ids["tiles"]
                    tilemap.set_new_tile(i, j, frame_index)
                    #l[i][j] = {
                    #    "position": (j * self.tilewidth, i * self.tileheight),
                    #    "frame_index": frame_index,
                    #}
            #scene.tilemap["layers"].append(l)
        scene.tilemap = tilemap
   
    def load_items(self, scene: any, group: ET.Element) -> None:
        pass
