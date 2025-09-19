using UnityEngine;

[ExecuteInEditMode]
public class DrawBoneGizmo : MonoBehaviour
{
    public float size = 0.02f;
    public Color color = Color.green;

    // OnDrawGizmos는 시작점 역할만 합니다.
    private void OnDrawGizmos()
    {
        // 이 스크립트가 붙어있는 Transform부터 재귀적으로 그리기 시작합니다.
        DrawGizmosRecursive(transform);
    }

    // 재귀적으로 자식들을 탐색하며 기즈모를 그리는 함수
    private void DrawGizmosRecursive(Transform currentTransform)
    {
        // 현재 노드가 HitBox라면 이 노드 및 하위 노드 전부 무시
        if (currentTransform.tag.StartsWith("HitBox"))
            return;

        Gizmos.color = color;

        // 현재 위치 구체 표시
        Gizmos.DrawSphere(currentTransform.position, size);

        foreach (Transform child in currentTransform)
        {
            // child가 HitBox라면 무시하고 재귀 안 들어감
            if (child.tag.StartsWith("HitBox"))
                continue;

            // 자식 위치에 구체 그리기
            Gizmos.DrawSphere(child.position, size);

            // 부모 -> 자식 연결선
            Gizmos.DrawLine(currentTransform.position, child.position);

            // 재귀 호출
            DrawGizmosRecursive(child);
        }
    }
}