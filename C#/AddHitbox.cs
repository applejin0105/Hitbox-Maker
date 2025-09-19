#if UNITY_EDITOR
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using System.Linq;

[ExecuteInEditMode]
[RequireComponent(typeof(DrawBoneGizmo))]
[RequireComponent(typeof(DrawCollider))]
[RequireComponent(typeof(AddTag))]
[RequireComponent(typeof(AddLayer))]
public class AddHitbox : MonoBehaviour
{
    private static GameObject _target;
    private static string _hitbox = "Hitbox";
    private static string _playerCapsule = "PlayerCapsule";

    enum ColliderType
    {
        Sphere,
        Capsule,
        Box
    }

    enum HitboxType
    {
        Head,
        Torso,
        Arm,
        Leg
    }
    
    static List<string> BoneStructure = new List<string>() { "Hips", "Hitbox_Torso", "LeftUpLeg", "Hitbox_LeftUpLeg", "LeftLeg", "Hitbox_LeftLeg", "LeftFoot", "Hitbox_LeftFoot", "LeftToeBase", "LeftToe_End", "PlayerCapsule", "RightUpLeg", "Hitbox_RightUpLeg", "RightLeg", "Hitbox_RightLeg", "RightFoot", "Hitbox_RightFoot", "RightToeBase", "RightToe_End", "Spine", "Spine1", "Spine2", "LeftShoulder", "LeftArm", "Hitbox_LeftArm", "LeftForeArm", "Hitbox_LeftForeArm", "LeftHand", "Hitbox_LeftHand", "LeftHandIndex1", "LeftHandIndex2", "LeftHandIndex3", "LeftHandIndex4", "LeftHandMiddle1", "LeftHandMiddle2", "LeftHandMiddle3", "LeftHandMiddle4", "LeftHandPinky1", "LeftHandPinky2", "LeftHandPinky3", "LeftHandPinky4", "LeftHandRing1", "LeftHandRing2", "LeftHandRing3", "LeftHandRing4", "LeftHandThumb1", "LeftHandThumb2", "LeftHandThumb3", "LeftHandThumb4", "Neck", "Head", "HeadTop_End", "Hitbox_Head", "Hitbox_Neck", "RightShoulder", "RightArm", "Hitbox_RightArm", "RightForeArm", "Hitbox_RightForeArm", "RightHand", "Hitbox_RightHand", "RightHandIndex1", "RightHandIndex2", "RightHandIndex3", "RightHandIndex4", "RightHandMiddle1", "RightHandMiddle2", "RightHandMiddle3", "RightHandMiddle4", "RightHandPinky1", "RightHandPinky2", "RightHandPinky3", "RightHandPinky4", "RightHandRing1", "RightHandRing2", "RightHandRing3", "RightHandRing4", "RightHandThumb1", "RightHandThumb2", "RightHandThumb3", "RightHandThumb4" };
    
    [MenuItem("Custom/HitBox/Create Hit Box")]
    private static void Init()
    {
        if (Selection.activeTransform == null)
        {
            Debug.LogWarning("Root GameObjet를 선택하십시오.");
            return;
        }
        
        AddLayer.AddLayerIfNotExist("Ground");
        List<string> tags = new List<string>() { "CharacterSkeleton", "Hitbox_Head", "Hitbox_Torso", "Hitbox_Arm", "Hitbox_Leg" };
        foreach (var t in tags)
        {
            AddTag.InitTag(t);
        }
        _target = Selection.activeTransform.gameObject;
    }
    private static void ClickCreateHitBox()
    {
        if (CheckBoneStructure())
        {
            Debug.Log("Root GameObject가 선택되었고, Hitbox를 생성합니다!");
            CreateAllHitBoxes();
            GameObject obj = GameObject.Find("PlayerCapsule");
            GameObject grCPL = GameObject.Find("GroundCheckerL");
            GameObject grCPR = GameObject.Find("GroundCheckerR");
            EndSetting(obj, grCPL, grCPR);
        }
    }
    private static bool CheckBoneStructure()
    {
        Transform hips = _target.transform.Find("Hips");
        if (hips == null)
        {
            Debug.LogError($"선택한 '{_target.name}' 아래에 'Hips' 본이 존재하지 않습니다!");
            return false;
        }
        
        List<string> actualHierarchy = new List<string>();
        
        List<string> actual = new List<string>();
        CollectHierarchy(hips, actual);
        
        var missing = BoneStructure.Except(actual).ToList();
        var extra   = actual.Except(BoneStructure).ToList();

        Debug.Log("Bone 확인이 끝났습니다.");
        
        if (missing.Count > 0)
        {
            Debug.LogWarning("Bone이 없습니다: " + string.Join(", ", missing));
        }

        if (extra.Count > 0)
        {
            Debug.LogWarning("추가적인 Bone이 존재합니다: " + string.Join(", ", extra));
        }

        if (missing.Count == 0 && extra.Count == 0)
        {
            Debug.Log("Bone이 완벽하게 일치합니다.");
            return true;
        }
        
        return false;
    }
    private static void CollectHierarchy(Transform node, List<string> list)
    {
        list.Add(node.name);

        foreach (Transform child in node)
        {
            CollectHierarchy(child, list);
        }
    }
    private static void CreateAllHitBoxes()
    {
        Transform[] allChildren = _target.GetComponentsInChildren<Transform>();

        List<string> capsuleObjects = new List<string>() {"Arm", "Leg", "Torso", "Capsule", "Neck"};
        List<string> sphereObjects = new List<string>() {"Head", "GroundChecker_L", "GroundChecker_R"};
        List<string> boxObjects = new List<string>() {"Foot", "Hand"};
        
        List<string> torsoObjects = new List<string>() {"Hitbox_Torso", "Hitbox_Neck"};
        List<string> armObjects = new List<string>() {"Hitbox_LeftArm", "Hitbox_LeftForeArm", "Hitbox_LeftHand", "Hitbox_RightArm", "Hitbox_RightForeArm", "Hitbox_RightHand"};
        List<string> legObjects = new List<string>() {"Hitbox_LeftLeg", "Hitbox_LeftUpLeg", "Hitbox_LeftFoot", "Hitbox_RightLeg", "Hitbox_RightUpLeg", "Hitbox_RightFoot"};
        List<string> headObjects = new List<string>() {"Hitbox_Head"};
        
        List<string> groundChecker = new List<string>() {"GroundChecker_L", "GroundChecker_R"};
        
        foreach (var child in allChildren)
        {
            if (child.name == _target.name)
            {
                if(child.GetComponent<DrawBoneGizmo>() == null)
                    child.gameObject.AddComponent<DrawBoneGizmo>();
                if(child.GetComponent<DrawCollider>() == null)
                    child.gameObject.AddComponent<DrawCollider>();
                child.tag = "CharacterSkeleton";
                continue;
            }
            
            if (child.gameObject.name.Contains(_hitbox) || child.gameObject.name.Contains(_playerCapsule))
            {
                foreach (var col in capsuleObjects)
                {
                    if (child.gameObject.name.Contains(col))
                    {
                        CreateCollider(child.gameObject, ColliderType.Capsule);
                    }
                }
                
                foreach (var sph in sphereObjects)
                {
                    if (child.gameObject.name.Contains(sph))
                    {
                        CreateCollider(child.gameObject, ColliderType.Sphere);
                    }
                }
                
                foreach (var box in boxObjects)
                {
                    if (child.gameObject.name.Contains(box))
                    {
                        CreateCollider(child.gameObject, ColliderType.Box);
                    }
                }
            }
        }
        
        foreach (var torso in torsoObjects)
        { 
            ChangeHitboxTag(torso, HitboxType.Torso);
        }
                
        foreach (var arm in armObjects)
        { 
            ChangeHitboxTag(arm, HitboxType.Arm);
        }
                
        foreach (var leg in legObjects)
        {
            ChangeHitboxTag(leg, HitboxType.Leg);
        }
                
        foreach (var head in headObjects)
        {
            ChangeHitboxTag(head, HitboxType.Head);
        }
        
        Debug.Log("완료되었습니다!");
    }
    private static void CreateCollider(GameObject obj, ColliderType colliderType)
    {
        switch (colliderType)
        {
            case ColliderType.Capsule:
                if (obj.GetComponent<CapsuleCollider>() == null)
                {
                    obj.AddComponent<CapsuleCollider>();
                    obj.GetComponent<CapsuleCollider>().isTrigger = false;
                }
                break;
            case ColliderType.Sphere:
                if (obj.GetComponent<SphereCollider>() == null)
                {
                    obj.AddComponent<SphereCollider>();
                    obj.GetComponent<SphereCollider>().isTrigger = false;
                }
                break;
            case ColliderType.Box:
                if (obj.GetComponent<BoxCollider>() == null)
                {
                    obj.AddComponent<BoxCollider>();
                    obj.GetComponent<BoxCollider>().isTrigger = false;
                }
                break;
        }
        DestroyMesh(obj);
    }
    private static void ChangeHitboxTag(string objName, HitboxType hitboxType)
    {
        GameObject tagObject = GameObject.Find(objName);
        
        if (tagObject != null)
        {
            switch (hitboxType)
            {
                case HitboxType.Torso:
                    tagObject.tag = "Hitbox_Torso";
                    break;
                case HitboxType.Arm:
                    tagObject.tag = "Hitbox_Arm";
                    break;
                case HitboxType.Leg:
                    tagObject.tag = "Hitbox_Leg";
                    break;
                case HitboxType.Head:
                    tagObject.tag = "Hitbox_Head";
                    break;
            }
        }
    }
    private static void DestroyMesh(GameObject obj)
    {
        if (obj.GetComponent<MeshRenderer>() != null)
            DestroyImmediate(obj.GetComponent<MeshRenderer>());
        if (obj.GetComponent<MeshFilter>() != null)
            DestroyImmediate(obj.GetComponent<MeshFilter>());
    }
    private static void EndSetting(GameObject obj, GameObject groundCheckerL, GameObject groundCheckerR)
    {
        obj.GetComponent<BoxCollider>().isTrigger = true;
        obj.AddComponent<Rigidbody>();
        obj.GetComponent<Rigidbody>().automaticCenterOfMass = true;
        obj.GetComponent<Rigidbody>().automaticInertiaTensor = true;
        obj.GetComponent<Rigidbody>().isKinematic = false;
        obj.GetComponent<Rigidbody>().useGravity = true;
        obj.GetComponent<Rigidbody>().interpolation = RigidbodyInterpolation.Interpolate;
        obj.GetComponent<Rigidbody>().collisionDetectionMode = CollisionDetectionMode.Discrete;
        obj.GetComponent<Rigidbody>().constraints = RigidbodyConstraints.FreezeRotation;
        obj.AddComponent<CheckGround>();
        obj.GetComponent<CheckGround>().groundLayer = LayerMask.GetMask("Ground");
        obj.GetComponent<CheckGround>().groundCheckPointL = groundCheckerL.transform;
        obj.GetComponent<CheckGround>().groundCheckPointL = groundCheckerR.transform;
        groundCheckerL.GetComponent<SphereCollider>().isTrigger = true;
        groundCheckerR.GetComponent<SphereCollider>().isTrigger = true;
    }
}
#endif