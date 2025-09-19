#if UNITY_EDITOR
using UnityEngine;
using UnityEditorInternal;
using UnityEditor;

public class AddTag : MonoBehaviour
{
    public static void InitTag(string tag)
    {
        if (!IsTagExists(tag))
        {
            SerializedObject tagManager = new SerializedObject(AssetDatabase.LoadAllAssetsAtPath("ProjectSettings/TagManager.asset")[0]);
            
            SerializedProperty tagsProp = tagManager.FindProperty("tags");
            
            tagsProp.InsertArrayElementAtIndex(tagsProp.arraySize);
            SerializedProperty newTag = tagsProp.GetArrayElementAtIndex(tagsProp.arraySize - 1);
            newTag.stringValue = tag;
            
            tagManager.ApplyModifiedProperties();
        }
    }
    private static bool IsTagExists(string tag)
    {
        foreach (var t in InternalEditorUtility.tags)
        {
            if (t.Equals(tag)) return true;
        }
        return false;
    }
}
#endif