from importer import CACHE
from utils import marmoset_materials_utils as mmu
import mset
import os


global u_mats
u_mats = []

window = mset.UIWindow("Import Unity Materials")
window.width = 400
window.height = 800

drawer = mset.UIDrawer(name="Settings")
drawer_window = mset.UIWindow(name="", register=False)
drawer.containedControl = drawer_window

scrollbox = mset.UIScrollBox()
scrollbox_window = mset.UIWindow(name="", register=False)
scrollbox.containedControl = scrollbox_window


global checks_list
checks_list=[]


def sunc_scene_materials():
    for mat in mset.getAllMaterials():
        for check in checks_list:
            if mat.name == check.label:
                check.value = True


def import_materials():

    def apply_material(unity_material):

        def setField(mmat, Sub, Field, Value):
            if Value != None:
                mmat.getSubroutine(Sub).setField(Field, Value)

        inScene = False
        for mat in mset.getAllMaterials():
            if mat.name == unity_material.name:
                inScene = True

        if inScene==False:
            mmat = mset.Material(unity_material.name)
        else:
            mmat = mset.findMaterial(unity_material.name)

        mmu.setFields(mmat)
        setField(mmat, "albedo", 'Color', unity_material._Color.store.rgb)
        setField(mmat, "albedo", 'Albedo Map', unity_material._MainTex.store.path)
        setField(mmat, "surface", 'Normal Map', unity_material._BumpMap.store.path)
        setField(mmat, "microsurface", 'Gloss Map', unity_material._MetallicGlossMap.store.path)
        setField(mmat, "reflectivity", 'Metalness Map', unity_material._MetallicGlossMap.store.path)
        setField(mmat, "occlusion", 'Occlusion Map', unity_material._OcclusionMap.store.path)
        setField(mmat, "emissive", 'Color', unity_material._EmissionColor.store.rgb)
        setField(mmat, "emissive", 'Emissive Map', unity_material._EmissionMap.store.path)

    for i in checks_list:
        if i.value == True:
            for mat in u_mats:
                if mat.name == i.label:
                    apply_material(mat)

    mset.shutdownPlugin()


def select_all():
    for i in checks_list:
        i.value = True


def deselcet_all():
    for i in checks_list:
        i.value = False


def cancel():
    mset.shutdownPlugin()


def refrash_materials_list():
    global u_mats
    global checks_list

    scrollbox_window.clearElements()
    checks_list.clear()
    u_mats.clear()

    cache = CACHE.cache(folder_line.value)
    u_mats = cache.materials

    for i in u_mats:
        checkbox = mset.UICheckBox()
        checkbox.label = i.name
        checks_list.append(checkbox)
        scrollbox_window.addReturn()
        scrollbox_window.addElement(checkbox)


def select_folder():
    folder_line.value = mset.showOpenFolderDialog()


folder_line = mset.UITextField()
folder_line.value = ''

folder_button = mset.UIButton()
folder_button.onClick = select_folder
folder_button.setIcon(os.path.abspath(os.path.join(os.curdir, "data/gui/control/materialgroupnew.tga")))

button_all = mset.UIButton()
button_all.onClick = select_all
button_all.text = 'All'

button_none = mset.UIButton()
button_none.onClick = deselcet_all
button_none.text = 'None'

button_scene = mset.UIButton()
button_scene.onClick = sunc_scene_materials
button_scene.text = 'Scene'

refresh_button = mset.UIButton()
refresh_button.onClick = refrash_materials_list
refresh_button.text = 'Refresh'

button_cancel = mset.UIButton()
button_cancel.onClick = cancel
button_cancel.text = 'Close'

button_import = mset.UIButton()
button_import.onClick = import_materials
button_import.text = 'Import'


window.addElement(folder_line)
window.addElement(folder_button)
window.addReturn()
window.addElement(button_all)
window.addElement(button_none)
window.addElement(button_scene)
window.addStretchSpace()
window.addElement(refresh_button)
window.addReturn()
window.addElement(scrollbox)
window.addReturn()
window.addStretchSpace()
window.addElement(button_cancel)
window.addElement(button_import)