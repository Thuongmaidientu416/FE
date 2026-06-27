"""
WanderHUB AI — Layer 4: Conversation Layer
Builds prompts with real data and calls the LLM (Groq API) server-side.
"""

from __future__ import annotations
import json
import httpx

from config import GROQ_API_KEY, GROQ_API_URL, GROQ_MODEL


SYSTEM_PROMPT_TEMPLATE = """Bạn là WanderBot — trợ lý AI thông minh hỗ trợ khách hàng của WanderHUB, nền tảng gợi ý trải nghiệm đô thị tại TP.HCM.

VAI TRÒ CỦA BẠN (Layer 4 — AI Conversation Layer):
- Giải đáp thắc mắc và hỗ trợ khách hàng về các vấn đề phát sinh (chính sách, dịch vụ, CSKH).
- Cung cấp thông tin chi tiết và hữu ích về các địa điểm (giới thiệu địa điểm, món ăn, khoảng giá, địa chỉ) từ dữ liệu hệ thống dựa trên nhu cầu tìm kiếm của người dùng.
- KHÔNG gợi ý hoặc tự tạo lịch trình/tuyến đường mẫu (itinerary/route). Nếu người dùng muốn lên lịch trình, hãy hướng dẫn họ sử dụng tính năng "Lên lịch trình" chính trên website WanderHUB.
- Trả lời hội thoại theo phong cách Gen Z Sài Gòn: trẻ trung, gần gũi nhưng chuyên nghiệp.

QUY TẮC BẮT BUỘC:
- CHỈ sử dụng dữ liệu địa điểm được cung cấp bởi hệ thống backend.
- KHÔNG bịa giá, giờ mở cửa, thông tin địa điểm hoặc sáng tác khuyến mãi không có trong data.
- KHÔNG tạo tuyến đường/lịch trình mẫu cho người dùng.
- Giữ câu trả lời ngắn gọn, hữu ích, tập trung đúng trọng tâm câu hỏi.
- Luôn trả lời bằng tiếng Việt.
- Khi giới thiệu địa điểm, nêu rõ tên, quận/khu vực, khoảng giá và lý do phù hợp.
- CHỈ giới thiệu địa điểm khi người dùng chủ động hỏi/tìm kiếm địa điểm vui chơi, ăn uống, giải trí. Tuyệt đối KHÔNG tự động đính kèm các gợi ý địa điểm ăn uống/vui chơi khi người dùng đang hỏi về các vấn đề CSKH, hỗ trợ kỹ thuật, tài khoản, đặt xe hoặc gói dịch vụ.

HƯỚNG DẪN XỬ LÝ CÁC TÌNH HUỐNG CSKH (CUSTOMER SERVICE GUIDELINES):
- Gói dịch vụ & Hoàn tiền:
  + Gói Basic (Cơ bản): Miễn phí. Giới hạn tạo 1 lịch trình mỗi 20 ngày.
  + Gói Premium (Cao cấp): Tạo lịch trình không giới hạn, mở khóa mọi tính năng cao cấp.
  + Gói International (Quốc tế): Dành cho khách du lịch quốc tế và đối tác, tạo lịch trình không giới hạn, hỗ trợ dịch thuật nâng cao.
  + Hủy gói: Thực hiện tại mục Cài đặt tài khoản. Quyền lợi duy trì đến hết chu kỳ thanh toán.
  + Hoàn tiền: Hoàn tiền 100% trong vòng 7 ngày kể từ ngày đăng ký nếu chưa dùng quá 3 lượt tạo lịch trình. Liên hệ hotline 1900-0905 hoặc support@wanderhub.vn để được hỗ trợ.
- Lỗi kỹ thuật / Sự cố hệ thống:
  + Khuyên người dùng tải lại trang (Ctrl + F5), xóa cache trình duyệt hoặc thử đăng nhập lại. Nếu lỗi vẫn tiếp diễn, báo cáo lỗi tại mục "Liên hệ" hoặc gửi email tới support@wanderhub.vn kèm ảnh chụp màn hình để bộ phận kỹ thuật kiểm tra.
- Sự cố đặt xe (Vehicle Booking):
  + Liên hệ trực tiếp số điện thoại tài xế trong trang chi tiết đặt xe. Nếu không liên hệ được tài xế hoặc xe gặp sự cố dọc đường, liên hệ hotline WanderHUB 1900-0905 để được hỗ trợ điều phối xe khác thay thế khẩn cấp.
- Tài khoản & Bảo mật:
  + Đổi mật khẩu/Cập nhật thông tin: Thực hiện trong phần "Trang cá nhân" (Profile). Quên mật khẩu: Nhấn "Quên mật khẩu" ở màn hình đăng nhập hoặc gửi mail hỗ trợ xác minh tài khoản.
- Hợp tác đối tác (Local Partners):
  + Các cơ sở kinh doanh muốn hợp tác gửi yêu cầu tại trang "Đối tác" hoặc gửi email tới partner@wanderhub.vn để được bộ phận kinh doanh liên hệ hỗ trợ.

DỮ LIỆU TỪ HỆ THỐNG BACKEND:
{system_data}"""


# ── Fallback mock responses ──────────────────────────────────────
MOCK_RESPONSES = {
    "chill": "Với mood chill, mình gợi ý bạn ghé thử một số quán cafe hoặc không gian thoáng đãng tại Quận 1 có điểm đánh giá cao của hệ thống. Bạn có muốn mình giới thiệu các địa điểm chill cụ thể không? 🌿",
    "date": "Để đi hẹn hò, mình gợi ý bạn chọn một số quán ăn lãng mạn hoặc quán nước rooftop view đẹp. Bạn thích tìm quán ở khu vực nào để mình giới thiệu cụ thể nhé? 💫",
    "food": "Đi ăn uống tại Sài Gòn thì tuyệt vời! Hệ thống của mình có rất nhiều quán ăn ngon từ bình dân đến cao cấp. Bạn đang thèm ăn món gì hoặc muốn tìm quán ở quận mấy? 🍜",
    "default": "Cảm ơn bạn đã liên hệ WanderBot! Mình có thể hỗ trợ giải đáp thông tin dịch vụ, giải quyết các vấn đề phát sinh hoặc giới thiệu các địa điểm ăn chơi phù hợp với nhu cầu của bạn. Bạn cần hỗ trợ gì hôm nay? 🗺️",
}


async def generate_response(
    user_message: str,
    message_history: list[dict],
    system_data: dict,
    groq_key: str | None = None,
) -> tuple[str, str]:
    """
    Layer 4 — Generate AI response using LLM.

    Args:
        user_message: Current user message
        message_history: Previous messages [{"from": "user"|"ai", "text": "..."}]
        system_data: Backend data to inject into prompt (user context, rules, recommendations)
        groq_key: Optional override key (from user) or falls back to server env key

    Returns:
        (reply_text, source) where source is "ai", "mock", or "error"
    """
    api_key = groq_key or GROQ_API_KEY

    if not api_key:
        # No API key — use mock fallback
        reply = _mock_reply(user_message)
        return reply, "mock"

    # Build system prompt with real data
    system_content = SYSTEM_PROMPT_TEMPLATE.format(
        system_data=json.dumps(system_data, ensure_ascii=False, indent=2)
    )

    # Build message list
    messages = [{"role": "system", "content": system_content}]
    for msg in message_history[-20:]:  # Keep last 20 messages for context
        role = "assistant" if msg.get("from") == "ai" else "user"
        messages.append({"role": role, "content": msg.get("text", "")})
    messages.append({"role": "user", "content": user_message})

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                GROQ_API_URL,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}",
                },
                json={
                    "model": GROQ_MODEL,
                    "messages": messages,
                    "temperature": 0.6,
                    "max_tokens": 1024,
                },
            )

        if response.status_code != 200:
            error_data = response.json() if response.headers.get("content-type", "").startswith("application/json") else {}
            error_msg = error_data.get("error", {}).get("message", f"HTTP {response.status_code}")
            return f"Lỗi kết nối AI: {error_msg}", "error"

        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        return reply, "ai"

    except httpx.TimeoutException:
        return "Hệ thống AI đang bận, vui lòng thử lại sau ít giây. ⏳", "error"
    except Exception as exc:
        return f"Lỗi hệ thống: {str(exc)}", "error"


def _mock_reply(message: str) -> str:
    """Generate a mock reply based on keyword matching."""
    lower = message.lower()

    if any(kw in lower for kw in ["chill", "thư giãn", "relax"]):
        return MOCK_RESPONSES["chill"]
    if any(kw in lower for kw in ["date", "hẹn hò", "lãng mạn"]):
        return MOCK_RESPONSES["date"]
    if any(kw in lower for kw in ["ăn", "food", "quán", "ốc", "bún"]):
        return MOCK_RESPONSES["food"]

    return MOCK_RESPONSES["default"]


def build_chat_system_data(
    conn,
    user_message: str,
    moods: list[str],
    district: str = "Quận 1",
) -> dict:
    """Build system data for chat context by querying relevant providers."""
    import sqlite3

    # Fetch a few top providers matching detected mood
    mood_placeholders = ",".join("?" for _ in moods)
    query = f"""
        SELECT DISTINCT
            v.provider_name,
            v.district_name,
            v.category_name,
            v.role_name,
            v.price_min_vnd,
            v.price_max_vnd,
            v.wanderhub_score,
            v.description,
            v.ai_base_score
        FROM v_recommendation_base v
        LEFT JOIN provider_moods pm ON pm.provider_id = v.provider_id
        LEFT JOIN moods m ON m.id = pm.mood_id
        WHERE m.code IN ({mood_placeholders})
        ORDER BY v.ai_base_score DESC
        LIMIT 8
    """
    rows = conn.execute(query, moods).fetchall()
    relevant_providers = [dict(r) for r in rows]

    # Fetch district stats
    district_stats = dict(conn.execute(
        "SELECT * FROM v_district_summary WHERE district_name = ?",
        (district,),
    ).fetchone() or {})

    return {
        "current_district": district,
        "detected_moods": moods,
        "relevant_providers": relevant_providers,
        "district_stats": district_stats,
        "total_providers": conn.execute("SELECT COUNT(*) FROM providers").fetchone()[0],
    }
