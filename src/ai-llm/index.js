import { apiChat } from '../api';

/**
 * Orchestrator — kết nối FE chatbot với backend AI pipeline.
 * Backend chạy 4 Layer (Data → Knowledge → Recommendation → Conversation) server-side.
 * FE chỉ cần gửi message + history, backend trả lời đầy đủ.
 */
export const processUserMessage = async (userMessage, messageHistory, groqKey) => {
  try {
    const result = await apiChat(userMessage, messageHistory, groqKey);
    return result.reply;
  } catch (err) {
    // Fallback: nếu backend không available, thử gọi Groq trực tiếp (legacy)
    console.warn('[WanderBot] Backend unavailable, falling back to direct Groq:', err.message);
    
    if (!groqKey) {
      return "WanderBot đang ở chế độ offline. Vui lòng khởi động backend (python main.py) hoặc nhập Groq API Key.";
    }

    // Legacy direct call (giữ cho backward compatibility)
    try {
      const res = await fetch("https://api.groq.com/openai/v1/chat/completions", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${groqKey}`
        },
        body: JSON.stringify({
          model: "llama-3.3-70b-versatile",
          messages: [
            { role: "system", content: "Bạn là WanderBot — trợ lý AI du lịch đô thị TP.HCM. Trả lời ngắn gọn bằng tiếng Việt." },
            ...messageHistory.map(m => ({ role: m.from === "ai" ? "assistant" : "user", content: m.text })),
            { role: "user", content: userMessage }
          ],
          temperature: 0.6,
        })
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      return data.choices[0].message.content;
    } catch (fallbackErr) {
      return `Lỗi kết nối: ${fallbackErr.message}`;
    }
  }
};
