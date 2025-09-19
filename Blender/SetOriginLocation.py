import bpy
import mathutils

def sol(sex = "female"):
    
    if sex == "female" or sex == "male":
        obj = bpy.context.active_object

        if obj and obj.type == 'ARMATURE':
            
            bpy.ops.object.mode_set(mode='EDIT')
            
            armature_data = obj.data
            
            bpy.ops.armature.select_all(action='DESELECT')
            
            bone_name = 'LeftToe_End'
            if bone_name in armature_data.edit_bones:
                bone = armature_data.edit_bones[bone_name]
                
                z_value = (obj.matrix_world @ bone.tail).z

                bpy.ops.armature.select_all(action='SELECT')
                
                move_amount = 0.1
                
                if z_value == 0 :
                    print("Z 값이 0이므로 이동하지 않습니다.")
                else:
                    bpy.ops.transform.translate(value=(0, 0, -z_value))
                
                if sex == 'male':
                    bpy.ops.transform.translate(value=(0,0,0.02053220011293888))
                
            else:
                print(f"'{bone_name}' 본을 찾을 수 없습니다. 본 이름을 확인해 주세요.")

            bpy.ops.object.mode_set(mode='OBJECT')
            
        else:
            print("아마추어 객체를 선택해 주세요.")
    else:
        print("정확한 성별을 선택하세요.")

def main():
    sol()

if __name__ == '__main__':
    main()