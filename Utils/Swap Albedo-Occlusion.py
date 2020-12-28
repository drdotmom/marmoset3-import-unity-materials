import mset


for marmoset_material in mset.getAllMaterials():

    marmoset_material.setSubroutine("occlusion", "Occlusion")

    albedo = marmoset_material.getSubroutine("albedo").getField("Albedo Map")
    occlusion = marmoset_material.getSubroutine("occlusion").getField("Occlusion Map")

    if albedo is not None or occlusion is not None:
        marmoset_material.getSubroutine("albedo").setField("Albedo Map", occlusion)
        marmoset_material.getSubroutine("occlusion").setField("Occlusion Map", albedo)
