from . import types


class UnityMaterial(object):

    def __init__(self, name, matfile, tex_cache):

        self.name = name[:-4]
        self._Color = types.EmptyStore()
        self._MainTex = types.EmptyStore()
        self._MetallicGlossMap = types.EmptyStore()
        self._Metallic = types.EmptyStore()
        self._MetallicGlossMap = types.EmptyStore()
        self._Glossiness = types.EmptyStore()
        self._BumpMap = types.EmptyStore()
        self._BumpScale = types.EmptyStore()
        self._OcclusionMap = types.EmptyStore()
        self._OcclusionStrength = types.EmptyStore()
        self._EmissionMap = types.EmptyStore()
        self._EmissionColor = types.EmptyStore()
        self.shader = types.EmptyStore()


        def get_property(mat_data, i, field, tex_cache):

            if field.type == 'TEX':
                try:
                    tex = mat_data[i+1].split(' guid: ')[1].split(',')[0]
                    find = False
                    for c_tex in tex_cache:
                        if c_tex.guid[:-1] == tex:
                            find = True
                            f.store = c_tex
                            return f
                            break
                    if find == False:
                        f.store = types.EmptyStore()
                        return f
                except:
                    f.store = types.EmptyStore()
                    return f
                
            if field.type == 'VAL':
                try:
                    val = mat_data[i].split(field.name+': ')[1]
                    f.store = float(val)
                    return f
                except:
                    f.store = types.EmptyStore()
                    return f
                
            if field.type == 'COL':
                try:
                    lst = mat_data[i].split(field.name+': ')[1][:-1].split(',')
                    col = [float(i[4:]) for i in lst]
                    f.store = types.RGBA(col)
                    return f
                except:
                    f.store = types.EmptyStore()
                    return f


        fields = [
            types.FIELD(['_BumpMap', 'TEX', types.EmptyStore()]),
            types.FIELD(['_EmissionMap', 'TEX', types.EmptyStore()]),
            types.FIELD(['_MainTex', 'TEX', types.EmptyStore()]),
            types.FIELD(['_MetallicGlossMap', 'TEX', types.EmptyStore()]),
            types.FIELD(['_OcclusionMap', 'TEX', types.EmptyStore()]),
            types.FIELD(['_ParallaxMap', 'TEX', types.EmptyStore()]),
            types.FIELD(['_BumpScale', 'VAL', types.EmptyStore()]),
            types.FIELD(['_Glossiness', 'VAL', types.EmptyStore()]),
            types.FIELD(['_Metallic', 'VAL', types.EmptyStore()]),
            types.FIELD(['_OcclusionStrength', 'VAL', types.EmptyStore()]),
            types.FIELD(['_Color', 'COL', types.EmptyStore()]),
            types.FIELD(['_EmissionColor', 'COL', types.EmptyStore()])]

        props = []
        matf = open(matfile, 'r')
        mat_data = matf.read().split('\n')

        for i, line in enumerate(mat_data):
            if line.startswith('    - '):
                for f in fields:
                    if line.startswith('    - '+f.name):
                        prop = get_property(mat_data, i, f, tex_cache)
                        props.append(prop)

        for uf in props:
            for cf in self.__dict__:
                if uf.name == cf:
                    self.__dict__[cf] = uf

        matf.close()