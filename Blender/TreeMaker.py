import bpy

def print_bone_tree(armature, indent=""):
    for bone in armature.bones:
        if not bone.parent:  # 루트 뼈부터 시작
            print_branch(bone, indent)

def print_branch(bone, indent):
    print(indent + "├─ " + bone.name)
    children = bone.children
    for i, child in enumerate(children):
        if i == len(children)-1:
            print_branch(child, indent + "   ")
        else:
            print_branch(child, indent + "│  ")

# Armature 이름 지정
arm_obj = bpy.data.objects.get("Armature")
if arm_obj and arm_obj.type == 'ARMATURE':
    print("Armature:", arm_obj.name)
    print_bone_tree(arm_obj.data)
else:
    print("Armature not found")
