from . import lists


def setFields(marmoset_material):

    for field in lists.u2m_fields:
        marmoset_material.setSubroutine(field[0], field[1])
    for channel in lists.u2m_channels:
        marmoset_material.getSubroutine(channel[0]).setField(channel[1], channel[2])


def cleanFields(marmoset_material):
    marmoset_material.getSubroutine("albedo").setField("Color", [255.0, 255.0, 255.0])
    marmoset_material.getSubroutine("emissive").setField("Color", [255.0, 255.0, 255.0])


def swapOcclusion(marmoset_material):
    marmoset_material.setSubroutine("occlusion", "Occlusion")

    albedo = marmoset_material.getSubroutine("albedo").getField("Albedo Map")
    occlusion = marmoset_material.getSubroutine("occlusion").getField("Occlusion Map")

    if albedo != None or occlusion != None:
        marmoset_material.getSubroutine("albedo").setField("Albedo Map", occlusion)
        marmoset_material.getSubroutine("occlusion").setField("Occlusion Map", albedo)