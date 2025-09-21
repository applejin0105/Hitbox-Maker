import bpy

ARMATURE_NAME = "Armature"
arm = bpy.data.objects.get(ARMATURE_NAME)

if not arm or arm.type != 'ARMATURE':
    print(f"Armature '{ARMATURE_NAME}' not found or is not an armature.")
else:
    Neck_Bone = arm.data.bones.get("Neck")
    Spine2_Bone = arm.data.bones.get("Spine2")
    Hips_Bone = arm.data.bones.get("Hips")
    
    def check_bone(bone_name):
        if not arm.data.bones.get(bone_name):
            print(f"Bone '{bone_name}' not found.")
            return False
        return True

def set3DCursor(ORIGIN):
    bpy.context.scene.cursor.location = ORIGIN

# 'root_bone_names' 파라미터를 리스트로 변경합니다.
def select_bone_and_children(root_bone_names):
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='EDIT')
    ebones = arm.data.edit_bones

    bpy.ops.armature.select_all(action='DESELECT')

    def select_recursive(bone):
        bone.select = True
        bone.select_head = True
        bone.select_tail = True
        for child in bone.children:
            select_recursive(child)

    # 리스트를 순회하며 각 뼈대를 선택합니다.
    for root_bone_name in root_bone_names:
        if root_bone_name not in ebones:
            print(f"Bone '{root_bone_name}' not found.")
            continue
        
        root_bone = ebones[root_bone_name]
        select_recursive(root_bone)
        ebones.active = root_bone

def scale_value(value):
    bpy.ops.transform.resize(value=(value, value, value), center_override=bpy.context.scene.cursor.location)

def main():
    SCALE_VALUE_BODY = 1.0
    SCALE_VALUE_HEAD = 1.0
    SCALE_VALUE_ARM = 1.0
    SCALE_VALUE_LEG = 1.0
    
    # 힙본 스케일링
    if check_bone("Hips"):
        set3DCursor((0.0, 0.0, 0.0))
        select_bone_and_children(["Hips"])
        scale_value(SCALE_VALUE_BODY)

    # 머리 스케일링
    if check_bone("Head"):
        Neck_Tail_Loc = arm.matrix_world @ Neck_Bone.tail_local
        set3DCursor(Neck_Tail_Loc)
        select_bone_and_children(["Head"])
        scale_value(SCALE_VALUE_HEAD)
    
    # 팔 스케일링
    if check_bone("LeftShoulder") and check_bone("RightShoulder"):
        Spine2_Tail_Loc = arm.matrix_world @ Spine2_Bone.tail_local
        set3DCursor(Spine2_Tail_Loc)
        # 리스트로 뼈대 이름을 전달합니다.
        select_bone_and_children(["LeftShoulder", "RightShoulder"])
        scale_value(SCALE_VALUE_ARM)
        
    # 다리 스케일링
    if check_bone("LeftUpLeg") and check_bone("RightUpLeg"):
        Hips_Tail_Loc = arm.matrix_world @ Hips_Bone.tail_local
        set3DCursor(Hips_Tail_Loc)
        # 리스트로 뼈대 이름을 전달합니다.
        select_bone_and_children(["LeftUpLeg", "RightUpLeg"])
        scale_value(SCALE_VALUE_LEG)
    
    set3DCursor((0.0, 0.0, 0.0))
    bpy.ops.wm.redraw_all()
    
if __name__ == '__main__':
    main()
