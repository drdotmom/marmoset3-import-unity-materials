import os
from . import formats
from . import unity_texture as TEX
from . import unity_material as MAT


class cache(object):

    def __init__(self, path):

        self.materials = []
        self.textures = []
        self.project_path = path

        materials = []
        textures = []
        for dirs, folders, files in os.walk(self.project_path):

            for f in files:
                if f.endswith('.mat'):
                    materials.append([f, dirs])
                for i in formats.image_formats:
                    if f.lower().endswith(i):
                        textures.append([f, dirs])

        for tex in textures:
            self.textures.append(TEX.UnityTexture(tex[0], tex[1]))

        for mat in materials:
            matfile = mat[1]+'/'+mat[0]
            self.materials.append(MAT.UnityMaterial(mat[0], matfile,
                                                    self.textures))
