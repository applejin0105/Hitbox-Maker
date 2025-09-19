using System;
using UnityEngine;

public class CheckGround : MonoBehaviour
{
    [Header("Ground Check Settings")]
    public Transform groundCheckPointR;
    public Transform groundCheckPointL;
    public float groundCheckRadius;
    public LayerMask groundLayer;
    public float rayDistance;

    [HideInInspector] public bool isOnGrounded;
    [HideInInspector] public bool isOnGroundedL;
    [HideInInspector] public bool isOnGroundedR;
    [HideInInspector] public bool isOnGroundedB;

    [HideInInspector] public float slopeL;
    [HideInInspector] public float slopeR;
    
    private bool rayHitR;
    private bool rayHitL;

    void Awake()
    {
        isOnGrounded = false;
        isOnGroundedL = false;
        isOnGroundedR = false;
        isOnGroundedB = false;
        rayHitR = false;
        rayHitL = false;
    }
    void FixedUpdate()
    {
        CheckingGround();
    }
    void CheckingGround()
    {
        bool sphereTouchL = Physics.CheckSphere(groundCheckPointL.position, groundCheckRadius, groundLayer);
        bool sphereTouchR = Physics.CheckSphere(groundCheckPointR.position, groundCheckRadius, groundLayer);
    
        if (sphereTouchL)
        {
            RaycastHit hitL;
    
            bool physicRaycastL = Physics.Raycast(groundCheckPointL.position + Vector3.up * 0.1f, Vector3.down, out hitL,
                rayDistance, groundLayer);
            
            if (physicRaycastL)
            {
                rayHitL = true;
                slopeL = Vector3.Angle(hitL.normal, Vector3.up);
            }
        }

        if (sphereTouchR)
        {
            RaycastHit hitR;
            
            bool physicRaycastR = Physics.Raycast(groundCheckPointR.position + Vector3.up * 0.1f, Vector3.down, out hitR,
                rayDistance, groundLayer);
            
            if (physicRaycastR)
            {
                rayHitR = true;
                slopeR = Vector3.Angle(hitR.normal, Vector3.up);
            }
        }
        
        bool isRayHit = (rayHitR || rayHitL);
        bool isSphereHit = (sphereTouchL || sphereTouchR);
        isOnGroundedB = (rayHitR || rayHitL || sphereTouchL || sphereTouchR);
        
        isOnGrounded = (isRayHit && isSphereHit);
    }
    private void OnDrawGizmos()
    {
        if (groundCheckPointR == null || groundCheckPointL == null) return;

        Gizmos.color = Color.white;
        Gizmos.DrawWireSphere(groundCheckPointR.position, groundCheckRadius);
        Gizmos.DrawWireSphere(groundCheckPointL.position, groundCheckRadius);
        Gizmos.DrawLine(groundCheckPointR.position + Vector3.up * 0.1f,
            groundCheckPointR.position + Vector3.up * 0.1f + Vector3.down * rayDistance);
        Gizmos.DrawLine(groundCheckPointL.position + Vector3.up * 0.1f,
            groundCheckPointL.position + Vector3.up * 0.1f + Vector3.down * rayDistance);
    }
}