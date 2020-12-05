import mset

for marmoset_material in mset.getAllMaterials():
    try:
        marmoset_material.getSubroutine("albedo").setField("Color", [255.0, 255.0, 255.0])
    except:
        pass

    try:
        marmoset_material.getSubroutine("emissive").setField("Color", [0.0, 0.0, 0.0])
    except:
        pass