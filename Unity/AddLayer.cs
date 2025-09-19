#if UNITY_EDITOR
using UnityEngine;
using UnityEditorInternal;
using UnityEditor;

public class AddLayer : MonoBehaviour
{
    public static void AddLayerIfNotExist(string layerName)
    {
        if (string.IsNullOrEmpty(layerName))
        {
            Debug.LogError("레이어 이름이 비어 있습니다.");
            return;
        }
        
        SerializedObject tagManager = new SerializedObject(
            AssetDatabase.LoadAllAssetsAtPath("ProjectSettings/TagManager.asset")[0]
        );

        SerializedProperty layersProp = tagManager.FindProperty("layers");
        
        for (int i = 0; i < layersProp.arraySize; i++)
        {
            SerializedProperty layerSP = layersProp.GetArrayElementAtIndex(i);
            if (layerSP.stringValue == layerName)
            {
                Debug.Log($"레이어 '{layerName}' 이미 존재합니다.");
                return;
            }
        }

        // 기본 레이어 0~7는 예약되어 있으므로 8~31에 추가
        for (int i = 8; i < layersProp.arraySize; i++)
        {
            SerializedProperty layerSP = layersProp.GetArrayElementAtIndex(i);
            if (string.IsNullOrEmpty(layerSP.stringValue))
            {
                layerSP.stringValue = layerName;
                tagManager.ApplyModifiedProperties();
                Debug.Log($"레이어 '{layerName}' 추가 완료 (인덱스 {i})");
                return;
            }
        }

        Debug.LogError("빈 레이어 슬롯이 없습니다. 31개 레이어 제한을 확인하세요.");
    }
}
#endif