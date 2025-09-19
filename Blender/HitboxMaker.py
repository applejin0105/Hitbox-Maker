import bpy
import os
import mathutils

FEMALE_RADIUS_ARM_SCALE_VALUE = 2.0
MALE_RADIUS_ARM_SCALE_VALUE = 2.5

COMMON_RADIUS_FOREARM_SCALE_VALUE = 0.85

FEMALE_LENGTH_HIP_SCALE_VALUE = 2.0
MALE_LENGTH_HIP_SCALE_VALUE = 1.1

FEMALE_RADIUS_UPLEG_SCALE_VALUE = 3
MALE_RADIUS_UPLEG_SCALE_VALUE = 2

FEMALE_RADIUS_LEG_SCALE_VALUE = 0.85
MALE_RADIUS_LEG_SCALE_VALUE = 0.95

FEMALE_DEPTH_HAND_SCALE_VALUE = 0.5
MALE_DEPTH_HAND_SCALE_VALUE = 0.65

FEMALE_WIDTH_FEET_SCALE_VALUE = 0.32
MALE_WIDTH_FEET_SCALE_VALUE = 0.42

def global_bones():
    global ARMATURE_NAME, HEAD_BONE_NAME, HEAD_TOPEND_BONE_NAME, NECK_BONE_NAME
    global LEFT_SHOULDER_BONE_NAME, RIGHT_SHOULDER_BONE_NAME
    global LEFT_ARM_BONE_NAME, RIGHT_ARM_BONE_NAME
    global LEFT_FOREARM_BONE_NAME, RIGHT_FOREARM_BONE_NAME
    global LEFT_HAND_BONE_NAME, RIGHT_HAND_BONE_NAME
    global LEFT_HAND_MIDDLE4_BONE_NAME, RIGHT_HAND_MIDDLE4_BONE_NAME
    global LEFT_HAND_THUMB1_BONE_NAME, LEFT_HAND_PINKY1_BONE_NAME
    global LEFT_UPLEG_BONE_NAME, RIGHT_UPLEG_BONE_NAME
    global LEFT_LEG_BONE_NAME, RIGHT_LEG_BONE_NAME
    global LEFT_FOOT_BONE_NAME, RIGHT_FOOT_BONE_NAME
    global LEFT_TOEBASE_BONE_NAME, RIGHT_TOEBASE_BONE_NAME
    global HIPS_BONE_NAME
    
    ARMATURE_NAME = "Armature"

    HEAD_BONE_NAME = "Head"
    HEAD_TOPEND_BONE_NAME = "HeadTop_End"

    NECK_BONE_NAME = "Neck"

    LEFT_SHOULDER_BONE_NAME = "LeftShoulder"
    RIGHT_SHOULDER_BONE_NAME = "RightShoulder"

    LEFT_ARM_BONE_NAME = "LeftArm"
    RIGHT_ARM_BONE_NAME = "RightArm"

    LEFT_FOREARM_BONE_NAME = "LeftForeArm"
    RIGHT_FOREARM_BONE_NAME = "RightForeArm"

    LEFT_HAND_BONE_NAME = "LeftHand"
    RIGHT_HAND_BONE_NAME = "RightHand"

    LEFT_HAND_MIDDLE4_BONE_NAME = "LeftHandMiddle4"
    RIGHT_HAND_MIDDLE4_BONE_NAME = "RightHandMiddle4"
    
    LEFT_HAND_THUMB1_BONE_NAME = "LeftHandThumb1"
    LEFT_HAND_PINKY1_BONE_NAME = "LeftHandPinky1"

    LEFT_UPLEG_BONE_NAME = "LeftUpLeg"
    RIGHT_UPLEG_BONE_NAME = "RightUpLeg"

    LEFT_LEG_BONE_NAME = "LeftLeg"
    RIGHT_LEG_BONE_NAME = "RightLeg"

    LEFT_FOOT_BONE_NAME = "LeftFoot"
    RIGHT_FOOT_BONE_NAME = "RightFoot"

    LEFT_TOEBASE_BONE_NAME = "LeftToeBase"
    RIGHT_TOEBASE_BONE_NAME = "RightToeBase"

    HIPS_BONE_NAME = "Hips"
    
def validChecker():
    isValid = False
    
    global gender
    
    blend_path = bpy.data.filepath
    project_name = os.path.splitext(os.path.basename(blend_path))[0]
    
    if "Female" in project_name:
        print("Sex: Female")
        gender = "Female"
    elif "Male" in project_name:
        print("Sex: Male")
        gender = "Male"
    else:
        print("파일 이름에 성별(Male/Female)이 추가되어야 합니다.")
        return isValid
        
    global arm
    arm = bpy.data.objects.get(ARMATURE_NAME)
    
    if arm is None:
        printError(ARMATURE_NAME)
        
    global armature
    armature = arm.data

    bones_to_check = [
        ("head_bone", HEAD_BONE_NAME),
        ("head_topend_bone", HEAD_TOPEND_BONE_NAME),
        ("neck_bone", NECK_BONE_NAME),
        ("left_shoulder_bone", LEFT_SHOULDER_BONE_NAME),
        ("right_shoulder_bone", RIGHT_SHOULDER_BONE_NAME),
        ("left_arm_bone", LEFT_ARM_BONE_NAME),
        ("right_arm_bone", RIGHT_ARM_BONE_NAME),
        ("left_forearm_bone", LEFT_FOREARM_BONE_NAME),
        ("right_forearm_bone", RIGHT_FOREARM_BONE_NAME),
        ("left_hand_bone", LEFT_HAND_BONE_NAME),
        ("right_hand_bone", RIGHT_HAND_BONE_NAME),
        ("left_upleg_bone", LEFT_UPLEG_BONE_NAME),
        ("left_hand_middle4_bone", LEFT_HAND_MIDDLE4_BONE_NAME),
        ("right_hand_middle4_bone", RIGHT_HAND_MIDDLE4_BONE_NAME),
        ("left_hand_thumb1_bone", LEFT_HAND_THUMB1_BONE_NAME),
        ("left_hand_pinky1_bone", LEFT_HAND_PINKY1_BONE_NAME),
        ("right_upleg_bone", RIGHT_UPLEG_BONE_NAME),
        ("left_leg_bone", LEFT_LEG_BONE_NAME),
        ("right_leg_bone", RIGHT_LEG_BONE_NAME),
        ("left_foot_bone", LEFT_FOOT_BONE_NAME),
        ("right_foot_bone", RIGHT_FOOT_BONE_NAME),
        ("left_toebase_bone", LEFT_TOEBASE_BONE_NAME),
        ("right_toebase_bone", RIGHT_TOEBASE_BONE_NAME),
        ("hips_bone", HIPS_BONE_NAME)
    ]
    
    for var_name, bone_name in bones_to_check:
        globals()[var_name] = armature.bones.get(bone_name)
        if globals()[var_name] is None:
            printError(bone_name)
    
    bpy.ops.object.select_all(action='DESELECT')
    
    global arm_obj
    arm_obj = arm
    
    if arm_obj is not None:
        arm_obj.select_set(True)
        bpy.context.view_layer.objects.active = arm_obj
        
    print("Armature와 Bone이 정상적으로 존재합니다. 작업을 시작합니다.")
    return True

def delete_hitbox(keywords):
    found_and_deleted = False
    
    for obj in list(bpy.data.objects):
        for keyword in keywords:
            if keyword in obj.name:
                obj_name = obj.name
                bpy.data.objects.remove(obj, do_unlink=True)
                print(f"'{obj_name}' 오브젝트가 삭제되었습니다.")
                found_and_deleted = True
                break
    
    if not found_and_deleted:
        print(f"삭제할 오브젝트가 존재하지 않습니다.")   
         
def worldLocation(BONE, ISHEAD):
    if ISHEAD == True:
        return arm_obj.matrix_world @ BONE.head_local
    else:
        return arm_obj.matrix_world @ BONE.tail_local
    
def bone_location():
    global head_bone_head_location, head_bone_tail_location
    global head_topend_bone_head_location
    global neck_bone_head_location
    
    global left_shoulder_bone_head_location, left_shoulder_bone_tail_location
    global right_shoulder_bone_head_location, right_shoulder_bone_tail_location
    
    global left_arm_bone_head_location, left_arm_bone_tail_location
    global right_arm_bone_head_location, right_arm_bone_tail_location
    
    global left_forearm_bone_head_location, left_forearm_bone_tail_location
    global right_forearm_bone_head_location, right_forearm_bone_tail_location
    
    global left_hand_bone_head_location
    global right_hand_bone_head_location
    
    global left_hand_middle4_bone_tail_location
    global right_hand_middle4_bone_tail_location
    
    global left_hand_thumb1_bone_tail_location
    
    global left_hand_pinky1_bone_tail_location
    
    global left_upleg_bone_head_location, left_upleg_bone_tail_location
    global right_upleg_bone_head_location, right_upleg_bone_tail_location
    
    global left_leg_bone_head_location, left_leg_bone_tail_location
    global right_leg_bone_head_location, right_leg_bone_tail_location
    
    global left_foot_bone_head_location, left_foot_bone_tail_location
    global right_foot_bone_head_location, right_foot_bone_tail_location
    
    global left_toebase_bone_head_location, left_toebase_bone_tail_location
    global right_toebase_bone_head_location
    
    head_bone_head_location = worldLocation(head_bone, True)
    head_bone_tail_location = worldLocation(head_bone, False)
    
    head_topend_bone_head_location = worldLocation(head_topend_bone, True)
    
    neck_bone_head_location = worldLocation(neck_bone, True)
    
    left_shoulder_bone_head_location = worldLocation(left_shoulder_bone, True)
    left_shoulder_bone_tail_location = worldLocation(left_shoulder_bone, False)
    
    right_shoulder_bone_head_location = worldLocation(right_shoulder_bone, True)
    right_shoulder_bone_tail_location = worldLocation(right_shoulder_bone, False)
    
    left_arm_bone_head_location = worldLocation(left_arm_bone, True)
    left_arm_bone_tail_location = worldLocation(left_arm_bone, False)
    
    right_arm_bone_head_location = worldLocation(right_arm_bone, True)
    right_arm_bone_tail_location = worldLocation(right_arm_bone, False)

    left_forearm_bone_head_location = worldLocation(left_forearm_bone, True)
    left_forearm_bone_tail_location = worldLocation(left_forearm_bone, False)
    
    right_forearm_bone_head_location = worldLocation(right_forearm_bone, True)
    right_forearm_bone_tail_location = worldLocation(right_forearm_bone, False)
    
    left_hand_bone_head_location = worldLocation(left_hand_bone, True)
    right_hand_bone_head_location = worldLocation(right_hand_bone, True)
    
    left_hand_middle4_bone_tail_location = worldLocation(left_hand_middle4_bone, False)
    right_hand_middle4_bone_tail_location = worldLocation(right_hand_middle4_bone, False)
    
    left_hand_thumb1_bone_tail_location = worldLocation(left_hand_thumb1_bone, False)
    left_hand_pinky1_bone_tail_location = worldLocation(left_hand_pinky1_bone, False)
        
    left_upleg_bone_head_location = worldLocation(left_upleg_bone, True)
    left_upleg_bone_tail_location = worldLocation(left_upleg_bone, False)
    
    right_upleg_bone_head_location = worldLocation(right_upleg_bone, True)
    right_upleg_bone_tail_location = worldLocation(right_upleg_bone, False)
    
    left_leg_bone_head_location = worldLocation(left_leg_bone, True)
    left_leg_bone_tail_location = worldLocation(left_leg_bone, False)
    
    right_leg_bone_head_location = worldLocation(right_leg_bone, True)
    right_leg_bone_tail_location = worldLocation(right_leg_bone, False)
    
    left_foot_bone_head_location = worldLocation(left_foot_bone, True)
    left_foot_bone_tail_location = worldLocation(left_foot_bone, False)
    
    right_foot_bone_head_location = worldLocation(right_foot_bone, True)
    right_foot_bone_tail_location = worldLocation(right_foot_bone, False)
    
    left_toebase_bone_head_location = worldLocation(left_toebase_bone, True)
    left_toebase_bone_tail_location = worldLocation(left_toebase_bone, False)
    
    right_toebase_bone_head_location = worldLocation(right_toebase_bone, True)
    
def printError(NAME):
    raise ValueError({NAME} + "이(가) 올바르지 않습니다. Armature에" + {NAME} + "이(가) 포함되어 있는지, 이름이 올바른지 확인하십시오.")
    
def printCreated(MESH_NAME):
    print(f"{MESH_NAME}가 생성되었고, 부모 연결이 완료되었습니다.")
    
def setToObject():
    for obj in bpy.data.objects:
        obj.select_set(False)
    
    if bpy.context.object is not None and bpy.context.object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
        
    obj = bpy.data.objects.get(ARMATURE_NAME)
    
    if obj is not None:
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        
def setToEdit():
    setToObject()
    if bpy.context.object is not None and bpy.context.object.mode != 'EDIT':
        bpy.ops.object.mode_set(mode='EDIT')  
        
def setToPose():
    setToObject()
    if bpy.context.object is not None and bpy.context.object.mode != 'POSE':
        bpy.ops.object.mode_set(mode='POSE')
        
def makeParentBone(PARENT_BONE_NAME, MESH_NAME):
    mesh = bpy.data.objects.get(MESH_NAME)
    if mesh is None : printError(MESH_NAME)
    
    setToPose()
    
    for b in arm.pose.bones:
        b.bone.select = False
    bone = arm.pose.bones.get(PARENT_BONE_NAME)
    
    if not bone: printError(PARENT_BONE_NAME)
    
    bone.bone.select = True
    armature.bones.active = bone.bone
    
    mesh.select_set(True)
    arm.select_set(True)
    
    bpy.context.view_layer.objects.active = arm
    
    try:
        bpy.ops.object.parent_set(type='BONE', keep_transform=True)
        print(f"'{MESH_NAME}'를 '{PARENT_BONE_NAME}'에 부착하였습니다.")
    except RuntimeError as e:
        print(f"'{MESH_NAME}'를 '{PARENT_BONE_NAME}'에 부착하지 못했습니다.")
        
    setToObject()
    
def makePlayerCapsule():
    bottom_mid_location = (left_toebase_bone_head_location + right_toebase_bone_head_location) / 2.0
    
    height = (head_bone_tail_location.z - bottom_mid_location.z) / 1.0
    rad1 = (left_shoulder_bone_tail_location.x - right_shoulder_bone_tail_location.x) / 2.0
    rad2 = (left_shoulder_bone_tail_location.x - left_shoulder_bone_head_location.x)
    rad = rad1 + rad2
    mid_point = (head_bone_tail_location + bottom_mid_location) / 2.0
    
    bpy.ops.mesh.primitive_cylinder_add(
        radius=rad,
        depth=height,
        enter_editmode=False,
        align='WORLD',
        location=mid_point
    )
    
    cylinder = bpy.context.active_object
    cylinder.name = f"PlayerCapsule"
    
    makeParentBone(HIPS_BONE_NAME, cylinder.name)
    
def makeHead():
    mid_point = (head_topend_bone_head_location + head_bone_head_location) / 2.0
    distance = (head_topend_bone_head_location - head_bone_head_location).length
    
    rad = distance / 2.0
    
    rad = rad * 1.2
    
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=rad,
        enter_editmode=False,
        align='WORLD',
        location=mid_point
    )
    
    sphere = bpy.context.active_object
    sphere.name = f"Hitbox_Head"
    
    makeParentBone(HEAD_BONE_NAME, sphere.name)
    
    printCreated(sphere.name)
    
def makeTorso():
    rad = (left_shoulder_bone_tail_location.x - right_shoulder_bone_tail_location.x) / 2.0
    
    head_location_world = neck_bone_head_location
    tail_location_world = (left_upleg_bone_head_location + right_upleg_bone_head_location) / 2.0
    
    length = (neck_bone_head_location.z - tail_location_world.z)
    mid_point = (head_location_world + tail_location_world) / 2.0
    direction_vector = (tail_location_world - head_location_world).normalized()
    
    bpy.ops.mesh.primitive_cylinder_add(
        radius=rad,
        depth=length,
        enter_editmode=False,
        align='WORLD',
        location=mid_point
    )
    
    cylinder = bpy.context.active_object
    cylinder.name = f"Hitbox_Torso"
    
    makeParentBone(HIPS_BONE_NAME, cylinder.name)
    printCreated(cylinder.name)
    
def makeNeck():
    rad = (left_shoulder_bone_head_location.x - right_shoulder_bone_head_location.x) / 2.0
    
    length = (head_bone_head_location - neck_bone_head_location).length
    mid_point = (head_bone_head_location + neck_bone_head_location) / 2.0
    direction_vector = (head_bone_head_location - neck_bone_head_location).normalized()
    
    bpy.ops.mesh.primitive_cylinder_add(
        radius=rad,
        depth=length,
        enter_editmode=False,
        align='WORLD',
        location=mid_point
    )
    
    cylinder = bpy.context.active_object
    cylinder.name = f"Hitbox_Neck"
    
    initial_vector = mathutils.Vector((0, 0, 1))
    rotation_quat = initial_vector.rotation_difference(direction_vector)
    
    cylinder.rotation_mode = 'QUATERNION'
    cylinder.rotation_quaternion = rotation_quat
    
    makeParentBone(NECK_BONE_NAME, cylinder.name)
    printCreated(cylinder.name)
    
def makeLimbs(HEAD, TAIL, RADIUS, BONE_NAME):
    length = (TAIL - HEAD).length
    mid_point = (TAIL + HEAD) / 2.0
    direction_vector = (TAIL - HEAD).normalized()
    
    bpy.ops.mesh.primitive_cylinder_add(
        radius=RADIUS,
        depth=length,
        enter_editmode=False,
        align='WORLD',
        location=mid_point
    )
    
    cylinder = bpy.context.active_object
    cylinder.name = f"Hitbox_{BONE_NAME}"

    initial_vector = mathutils.Vector((0, 0, 1))
    rotation_quat = initial_vector.rotation_difference(direction_vector)
            
    cylinder.rotation_mode = 'QUATERNION'
    cylinder.rotation_quaternion = rotation_quat
    
    makeParentBone(BONE_NAME, cylinder.name)
    printCreated(cylinder.name)
    
def makeHand(HEAD, TAIL, LENGTH, WIDTH, DEPTH, BONE_NAME):
    mid_point = (HEAD + TAIL) / 2.0
    
    bpy.ops.mesh.primitive_cube_add(
        size = 2.0,
        enter_editmode=False,
        align='WORLD',
        location=mid_point
    )
    
    cube = bpy.context.active_object
    cube.scale = (LENGTH / 2.0 , WIDTH / 2.0, DEPTH / 2.0)
    cube.name = f"Hitbox_{BONE_NAME}"
    
    makeParentBone(BONE_NAME, cube.name)
    printCreated(cube.name)
    
def makeFeet(MID_POINT, WIDTH, LENGTH, DEPTH, BONE_NAME):
    bpy.ops.mesh.primitive_cube_add(
        size = 2.0,
        enter_editmode=False,
        align='WORLD',
        location=MID_POINT
    )
    
    cube = bpy.context.active_object
    cube.scale = (WIDTH / 2.0 , LENGTH / 2.0, DEPTH / 2.0)
    cube.name = f"Hitbox_{BONE_NAME}"
    
    makeParentBone(BONE_NAME, cube.name)
    printCreated(cube.name)
    
def makeArmLeg():    
    length_Shoulder = (left_shoulder_bone_head_location.x - right_shoulder_bone_head_location.x)
    
    if gender == "Female" :
        radius_Arm = (length_Shoulder / FEMALE_RADIUS_ARM_SCALE_VALUE)
    elif gender == "Male":
        radius_Arm = (length_Shoulder / MALE_RADIUS_ARM_SCALE_VALUE)
    
    if gender == "Female" :
        length_hip = (length_Shoulder * FEMALE_LENGTH_HIP_SCALE_VALUE)
        radius_Upleg = (length_hip / FEMALE_RADIUS_UPLEG_SCALE_VALUE)
    elif gender == "Male":
        length_hip = (length_Shoulder * MALE_LENGTH_HIP_SCALE_VALUE)
        radius_Upleg = (length_hip / MALE_RADIUS_UPLEG_SCALE_VALUE)
        
    makeLimbs(left_arm_bone_head_location, left_arm_bone_tail_location, radius_Arm, LEFT_ARM_BONE_NAME)
    makeLimbs(right_arm_bone_head_location, right_arm_bone_tail_location, radius_Arm, RIGHT_ARM_BONE_NAME)
    
    makeLimbs(left_upleg_bone_head_location, left_upleg_bone_tail_location, radius_Upleg, LEFT_UPLEG_BONE_NAME)
    makeLimbs(right_upleg_bone_head_location, right_upleg_bone_tail_location, radius_Upleg, RIGHT_UPLEG_BONE_NAME)
    
    if gender == "Female" :
        radius_leg = radius_Upleg * FEMALE_RADIUS_LEG_SCALE_VALUE
    elif gender == "Male":
        radius_leg = radius_Upleg * MALE_RADIUS_LEG_SCALE_VALUE
    
    radius_ForeArm = (radius_Arm * COMMON_RADIUS_FOREARM_SCALE_VALUE)
    makeLimbs(left_forearm_bone_head_location, left_forearm_bone_tail_location, radius_ForeArm, LEFT_FOREARM_BONE_NAME)
    makeLimbs(right_forearm_bone_head_location, right_forearm_bone_tail_location, radius_ForeArm, RIGHT_FOREARM_BONE_NAME)
    
    makeLimbs(left_leg_bone_head_location, left_leg_bone_tail_location, radius_leg, LEFT_LEG_BONE_NAME)
    makeLimbs(right_leg_bone_head_location, right_leg_bone_tail_location, radius_leg, RIGHT_LEG_BONE_NAME)
    
    if left_hand_middle4_bone_tail_location.x > left_hand_bone_head_location.x:
        length_Hand = left_hand_middle4_bone_tail_location.x - left_hand_bone_head_location.x
    else:
        length_Hand = left_hand_middle4_bone_tail_location.x - left_hand_bone_head_location.x
    
    width_Hand = (left_hand_pinky1_bone_tail_location.y - left_hand_thumb1_bone_tail_location.y)
    
    if gender == "Female" :
        depth_Hand = radius_Arm * FEMALE_DEPTH_HAND_SCALE_VALUE
    elif gender == "Male":
        depth_Hand = radius_Arm * MALE_DEPTH_HAND_SCALE_VALUE
    
    makeHand(left_hand_middle4_bone_tail_location, left_hand_bone_head_location, length_Hand, width_Hand, depth_Hand, LEFT_HAND_BONE_NAME)
    makeHand(right_hand_middle4_bone_tail_location, right_hand_bone_head_location, length_Hand, width_Hand, depth_Hand, RIGHT_HAND_BONE_NAME)

    length_Feet = left_toebase_bone_tail_location.y - left_foot_bone_head_location.y
    depth_Feet = left_foot_bone_head_location.z - left_toebase_bone_tail_location.z
    
    if gender == "Female" :
        width_Feet = length_Feet * FEMALE_WIDTH_FEET_SCALE_VALUE
    elif gender == "Male":
        width_Feet = length_Feet * MALE_WIDTH_FEET_SCALE_VALUE  

    left_mid_point = (left_foot_bone_head_location + left_foot_bone_tail_location) / 2.0
    right_mid_point = (right_foot_bone_head_location + right_foot_bone_tail_location) / 2.0

    makeFeet(left_mid_point, width_Feet, length_Feet, depth_Feet, LEFT_FOOT_BONE_NAME)
    makeFeet(right_mid_point, width_Feet, length_Feet, depth_Feet, RIGHT_FOOT_BONE_NAME)
    
    makeGroundChecker(left_mid_point, right_mid_point, depth_Feet)
    
def makeGroundChecker(left_mid_point, right_mid_point, RADIUS):
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=RADIUS,
        enter_editmode=False,
        align='WORLD',
        location=left_mid_point
    )
    
    sphere = bpy.context.active_object
    sphere.name = f"GroundChecker_L"
    
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=RADIUS,
        enter_editmode=False,
        align='WORLD',
        location=right_mid_point
    )
    
    sphere = bpy.context.active_object
    sphere.name = f"GroundChecker_R"
    
    printCreated(sphere.name)
    
def hbm():
    makePlayerCapsule()
    makeHead()
    makeTorso()
    makeNeck()
    makeArmLeg()

def main():
    print("Hitbox 생성을 시작합니다.")
    delete_hitbox(["Hitbox", "PlayerCapsule", "GroundChecker"])
    global_bones()
    print("뼈 확인 작업을 완료하였습니다.")
    
    if validChecker() == True:
        bone_location()
        hbm()
        print("Hitbox 생성이 완료되었습니다.")
    
if __name__ == '__main__':
    main()
