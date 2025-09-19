import bpy

# 기준 뼈 이름 리스트 (순서가 중요)
target_bone_names = [
    "Hips", "Spine", "Spine1", "Spine2", "Neck", "Head", "HeadTop_End",
    "RightShoulder", "RightArm", "RightForeArm", "RightHand",
    "RightHandThumb1", "RightHandThumb2", "RightHandThumb3", "RightHandThumb4",
    "RightHandIndex1", "RightHandIndex2", "RightHandIndex3", "RightHandIndex4",
    "RightHandMiddle1", "RightHandMiddle2", "RightHandMiddle3", "RightHandMiddle4",
    "RightHandRing1", "RightHandRing2", "RightHandRing3", "RightHandRing4",
    "RightHandPinky1", "RightHandPinky2", "RightHandPinky3", "RightHandPinky4",
    "LeftShoulder", "LeftArm", "LeftForeArm", "LeftHand",
    "LeftHandThumb1", "LeftHandThumb2", "LeftHandThumb3", "LeftHandThumb4",
    "LeftHandIndex1", "LeftHandIndex2", "LeftHandIndex3", "LeftHandIndex4",
    "LeftHandMiddle1", "LeftHandMiddle2", "LeftHandMiddle3", "LeftHandMiddle4",
    "LeftHandRing1", "LeftHandRing2", "LeftHandRing3", "LeftHandRing4",
    "LeftHandPinky1", "LeftHandPinky2", "LeftHandPinky3", "LeftHandPinky4",
    "RightUpLeg", "RightLeg", "RightFoot", "RightToeBase", "RightToe_End",
    "LeftUpLeg", "LeftLeg", "LeftFoot", "LeftToeBase", "LeftToe_End"
]

# 현재 Armature 선택
arm = bpy.context.object
if arm and arm.type == 'ARMATURE':
    bones = arm.data.bones
    
    if len(bones) != len(target_bone_names):
        print(f"뼈 개수가 맞지 않습니다. Armature가 {len(bones)} 개의 뼈를 가지고 있습니다만, 리스트에는 {len(target_bone_names)}개가 있습니다.")
    else:
        for i, bone in enumerate(bones):
            old_name = bone.name
            new_name = target_bone_names[i]
            bone.name = new_name
            print(f"{i+1}. {old_name} -> {new_name}")
