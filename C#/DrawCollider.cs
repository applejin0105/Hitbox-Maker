using UnityEngine;

#if UNITY_EDITOR
using UnityEditor;
#endif

[ExecuteAlways]
public class DrawCollider : MonoBehaviour
{
    [Header("계층별 색상")]
    public Color firstLevelColor = Color.red;    // 메인 직계
    public Color secondLevelColor = Color.cyan;  // 손자
    public Color deeperLevelColor = Color.green; // 그 이하

#if UNITY_EDITOR
    private void OnDrawGizmos()
    {
        // if (EditorApplication.isPlayingOrWillChangePlaymode) return;
        if (transform == null) return;

        // 메인 오브젝트 직계부터 시작
        foreach (Transform child in transform)
        {
            if (child == null) continue;
            DrawCollidersRecursive(child, 0);
        }
    }

    private void DrawCollidersRecursive(Transform obj, int depth)
    {
        if (obj == null) return;

        Collider[] colliders = obj.GetComponents<Collider>();
        if (colliders == null) return;

        foreach (var col in colliders)
        {
            if (col == null) continue;

            // 색상 결정
            Gizmos.color = GetColorByDepth(depth);
            
            // Collider 종류별 그리기
            if (col is BoxCollider box)
            {
                if (box == null) continue;
                Gizmos.matrix = box.transform.localToWorldMatrix;
                Gizmos.DrawWireCube(box.center, box.size);
            }
            else if (col is SphereCollider sphere)
            {
                if (sphere == null) continue;
                Gizmos.matrix = sphere.transform.localToWorldMatrix;
                Gizmos.DrawWireSphere(sphere.center, sphere.radius);
            }
            else if (col is CapsuleCollider capsule)
            {
                if (capsule == null) continue;
                Gizmos.matrix = capsule.transform.localToWorldMatrix;
                DrawCapsuleWireframe(capsule);
            }
            else if (col is MeshCollider mesh)
            {
                if (mesh == null || mesh.sharedMesh == null) continue;
                Gizmos.matrix = mesh.transform.localToWorldMatrix;
                Gizmos.DrawWireMesh(mesh.sharedMesh);
            }
        }

        // 하위 재귀 호출
        foreach (Transform child in obj)
        {
            if (child == null) continue;
            DrawCollidersRecursive(child, depth + 1);
        }
    }

    private Color GetColorByDepth(int depth)
    {
        // 기준 HSV 값 (원하는 시작 색상)
        float baseHue = 0.0f; // 빨강에서 시작 (0~1)
        float saturation = 0.8f;
        float value = 0.9f;

        // depth가 깊어질수록 hue를 조금씩 회전
        float hueStep = 0.07f; // 단계당 hue 변화량
        float hue = (baseHue + depth * hueStep) % 1f;

        return Color.HSVToRGB(hue, saturation, value);
    }
    
    // CapsuleCollider 실제 형태에 가까운 Wireframe
    private void DrawCapsuleWireframe(CapsuleCollider capsule)
    {
        Vector3 axis = Vector3.up;
        switch (capsule.direction)
        {
            case 0: axis = Vector3.right; break;
            case 1: axis = Vector3.up; break;
            case 2: axis = Vector3.forward; break;
        }

        float radius = capsule.radius;
        float height = Mathf.Max(capsule.height, radius * 2);
        Vector3 center = capsule.center;

        // 직교 벡터
        Vector3 ortho1 = Vector3.zero, ortho2 = Vector3.zero;
        if (axis == Vector3.up) { ortho1 = Vector3.forward; ortho2 = Vector3.right; }
        else if (axis == Vector3.right) { ortho1 = Vector3.up; ortho2 = Vector3.forward; }
        else if (axis == Vector3.forward) { ortho1 = Vector3.up; ortho2 = Vector3.right; }

        // 상하 구형
        Vector3 top = center + axis * (height / 2 - radius);
        Vector3 bottom = center - axis * (height / 2 - radius);
        Gizmos.DrawWireSphere(top, radius);
        Gizmos.DrawWireSphere(bottom, radius);

        // 상하 구형 연결 선
        DrawCapsuleConnectingLines(top, bottom, ortho1, ortho2, radius);
    }

    private void DrawCapsuleConnectingLines(Vector3 top, Vector3 bottom, Vector3 ortho1, Vector3 ortho2, float radius)
    {
        Gizmos.DrawLine(top + ortho1 * radius, bottom + ortho1 * radius);
        Gizmos.DrawLine(top - ortho1 * radius, bottom - ortho1 * radius);
        Gizmos.DrawLine(top + ortho2 * radius, bottom + ortho2 * radius);
        Gizmos.DrawLine(top - ortho2 * radius, bottom - ortho2 * radius);
    }
#endif
}