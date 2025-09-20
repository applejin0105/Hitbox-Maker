import bpy

ARMATURE_NAME = "Armature"

arm = bpy.data.objects.get(ARMATURE_NAME)



def set3DCursor(ORIGIN):
    bpy.context.scene.cursor.location = ORIGIN

def select_bone_and_children(root_bone_name):
    if not arm or arm.type != 'ARMATURE':
        print(f"Armature '{ARMATURE_NAME}' not found")
        return

    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='EDIT')
    ebones = arm.data.edit_bones

    if root_bone_name not in ebones:
        print(f"Bone '{root_bone_name}' not found")
        return

    bpy.ops.armature.select_all(action='DESELECT')

    def select_recursive(bone):
        bone.select = True
        bone.select_head = True
        bone.select_tail = True
        for child in bone.children:
            select_recursive(child)

    root_bone = ebones[root_bone_name]
    select_recursive(root_bone)

    ebones.active = root_bone
    
def scale_value(value):
    bpy.ops.transform.resize(value=(value, value, value), center_override=bpy.context.scene.cursor.location)

def main():
    SACLE_VALUE_BODY = 1.0
    SACLE_VALUE_HEAD = 1.0
    SACLE_VALUE_ARM = 1.0
    SACLE_VALUE_LEG = 1.0
    
    ALL_ORIGIN = (0.0, 0.0, 0.0)
    set3DCursor(ALL_ORIGIN)
    select_bone_and_children("Hips")
    scale_value(SACLE_VALUE_BODY)
    
    Neck_Bone = arm.data.bones.get("Neck")
    Neck_Tail_Loc = arm.matrix_world @ Neck_Bone.tail_local
    HEAD_ORIGIN = Neck_Tail_Loc
    set3DCursor(HEAD_ORIGIN)
    select_bone_and_children("Head")
    scale_value(SACLE_VALUE_HEAD)
    
    Spine2_Bone = arm.data.bones.get("Spine2")
    Spine2_Tail_Loc = arm.matrix_world @ Spine2_Bone.tail_local
    ARM_ORIGIN = Spine2_Tail_Loc
    set3DCursor(ARM_ORIGIN)
    root_bones_to_select = ["LeftShoulder", "RightShoulder"]
    for bone_name in root_bones_to_select:
        select_bone_and_children(bone_name)
    scale_value(SACLE_VALUE_ARM)
    
    Hips_Bone = arm.data.bones.get("Hips")
    Hips_Tail_Loc = arm.matrix_world @ Hips_Bone.tail_local
    LEG_ORIGIN = Hips_Tail_Loc 
    set3DCursor(LEG_ORIGIN)
    root_bones_to_select = ["LeftUpLeg", "RightUpLeg"]
    for bone_name in root_bones_to_select:
        select_bone_and_children(bone_name)
    scale_value(SACLE_VALUE_LEG)
    
    set3DCursor(ALL_ORIGIN)

    
if __name__ == '__main__':
    main()