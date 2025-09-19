# Hitbox-Maker
유니티와 블렌더를 사용하여 Skeleton에 Hitbox를 생성하고, 이를 유니티에서 사용하는 코드.

## Blender
- 언어: **Python**

| 파일 | 설명 |
|------|------|
| HitboxMaker | 스켈레톤을 기반으로 히트박스 메시를 생성합니다. 남여 차이가 존재하며 원한다면 내부 수치를 조절하여 사용할 수 있습니다. |
| NameChange | 뼈의 이름을 변경합니다. 접두사/접미사등 뼈의 이름에 부수적인 것들이 들어가면 이를 지우고 뼈의 이름을 단순화 합니다. |
| SetOriginLocation | 만일 Edit 모드에서 Scale 작업 이후에 전반적인 위치가 맞지 않는다면 뼈의 위치를 재조정합니다. |
| TreeMaker | 블렌더에서 Armature의 Tree 구조를 표시합니다. |


## Unity
- 언어: **C#**

| 파일 | 설명 |
|------|------|
| AddHitbox | Bone 구조를 검사하고, 이를 기반으로 Hitbox, 충돌 감지 Capsule를 생성합니다. Mesh Renderer 관련 컴포넌트를 지우고, 콜라이더를 부착합니다. 태그도 설정합니다. |
| AddLayer | 특정 Layer가 존재하지 않는다면 새로 생성합니다. |
| AddTag | 특정 Tag가 존재하지 않는다면 새로 생성합니다. |
| CheckGround | 땅에 붙어있는지 아닌지 검사합니다. |
| DrawBoneGizmo | 유니티 에디터 상에서 뼈 구조를 시각적으로 표현합니다. |
| DrawCollider | 유니티 에디터 상에서 Collider를 시각적으로 표현합니다. |
