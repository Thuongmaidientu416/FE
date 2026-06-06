"""
WanderHUB Backend — Plans Router (Select / Get current plan)
"""

from __future__ import annotations
import sqlite3
from fastapi import APIRouter, Depends, HTTPException

from database import get_db_dependency
from models.schemas import PlanSelectRequest, PlanResponse
from routers.auth import require_auth

router = APIRouter(prefix="/api/plans", tags=["plans"])

PLAN_LIMITS: dict[str, int | None] = {
    "basic": 2,
    "premium": None,
    "international": None,
}


def _usage_this_month(conn: sqlite3.Connection, user_id: int) -> int:
    row = conn.execute(
        """
        SELECT COUNT(*) AS cnt FROM itineraries
        WHERE user_id = ?
          AND strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')
        """,
        (user_id,),
    ).fetchone()
    return row["cnt"] if row else 0


@router.post("/select", response_model=PlanResponse)
def select_plan(
    body: PlanSelectRequest,
    user_id: int = Depends(require_auth),
    conn: sqlite3.Connection = Depends(get_db_dependency),
):
    if body.plan_key not in PLAN_LIMITS:
        raise HTTPException(status_code=400, detail="Gói dịch vụ không hợp lệ.")

    conn.execute(
        """
        INSERT INTO user_plans (user_id, plan_name, plan_key)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            plan_name = excluded.plan_name,
            plan_key  = excluded.plan_key,
            selected_at = CURRENT_TIMESTAMP
        """,
        (user_id, body.plan_name, body.plan_key),
    )
    conn.commit()

    row = conn.execute(
        "SELECT plan_name, plan_key, selected_at FROM user_plans WHERE user_id = ?",
        (user_id,),
    ).fetchone()

    return PlanResponse(
        plan_name=row["plan_name"],
        plan_key=row["plan_key"],
        selected_at=row["selected_at"],
        usage_this_month=_usage_this_month(conn, user_id),
        monthly_limit=PLAN_LIMITS.get(row["plan_key"]),
    )


@router.get("/me", response_model=PlanResponse)
def get_my_plan(
    user_id: int = Depends(require_auth),
    conn: sqlite3.Connection = Depends(get_db_dependency),
):
    row = conn.execute(
        "SELECT plan_name, plan_key, selected_at FROM user_plans WHERE user_id = ?",
        (user_id,),
    ).fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Chưa chọn gói dịch vụ.")

    return PlanResponse(
        plan_name=row["plan_name"],
        plan_key=row["plan_key"],
        selected_at=row["selected_at"],
        usage_this_month=_usage_this_month(conn, user_id),
        monthly_limit=PLAN_LIMITS.get(row["plan_key"]),
    )
