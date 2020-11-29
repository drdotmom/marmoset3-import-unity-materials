class UnityTexture(object):

    def __init__(self, tex, path):

        self.path = path+'/'+tex[:-5]
        self.guid = ''
        self.name = tex[:-5]

        f = open(path+'/'+tex, 'r')
        for i in f:
            if i.find('guid: ')!=-1:
                self.guid = i[6:]
                break
        f.close