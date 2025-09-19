import bpy

# 현재 선택된 객체가 Armature인지 확인
arm = bpy.context.object
if arm and arm.type == 'ARMATURE':
    for bone in arm.data.bones:
        if bone.name.startswith("mixamorig:"):
            bone.name = bone.name.replace("mixamorig:", "", 1)

print("mixamorig: 접두사가 제거되었습니다.")
