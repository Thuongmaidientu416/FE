# WanderHUB Upgrade Design — 2026-06-06

## Scope

Four independent upgrades to the WanderHUB frontend (`src/main.jsx`) and one verification of backend KNN.

---

## 1. KNN Model Verification

**Status:** Verified — no changes needed.

`BE/ai/knn_recommender.py` uses cosine similarity between a 27-feature intent vector (built from mood/budget/food_preference) and provider vectors. Returns a 0–100 score. Logic is correct and complete.

---

## 2. Gói 7 Ngày (New Pricing Package)

**Location:** `packages` array at the top of `src/main.jsx`, and `PricingGrid` component.

**New package object:**
```js
{
  name: "Explorer 7 Ngày",
  price: "49.000 VNĐ/7 ngày",
  note: "Trải nghiệm gần như full Premium trong 7 ngày — lý tưởng cho cuối tuần hoặc du khách ngắn ngày.",
  features: [
    "Không giới hạn lịch trình AI",
    "Mở khóa 100% Hidden Gems",
    "Re-route thông minh realtime",
    "Hỗ trợ chat 24/7",
    "Bản đồ offline có sẵn",
  ],
  notIncluded: ["Ưu tiên tài xế giờ cao điểm"],
}
```

**Grid:** Change `PricingGrid` from `lg:grid-cols-2` to `lg:grid-cols-3`. Packages order: Explorer 7 Ngày → Premium (highlight) → International Tourist.

---

## 3. Commercial Suggestions — "Ngoài ra, có thể bạn quan tâm"

**Location:** `PlannerV2` component, `commercial-suggestion-panel` section (~line 3136).

**Changes:**
- Header label: `"Hidden gem / đối tác gợi ý thêm"` → `"Ngoài ra, có thể bạn quan tâm"`
- Sub-label: update to `"Được đề xuất từ đối tác mới — không nằm trong tuyến AI chính."`
- Badge: `"Partner seed"` → `"Đối tác"`
- Visual: add a subtle `✨` icon and a slightly different card background to visually separate from KNN results

---

## 4. Transport Booking Links

**Location:** `ride-confirm-btn` button (~line 3218) inside `showRideBooking` panel.

**Change:** Replace the dead `"Gửi tuyến cho đối tác vận chuyển"` button with a conditional panel:

- If `transport === "Be / Xanh SM"`:
  - Show two buttons: "Mở Be" → `https://be.com.vn` and "Mở Xanh SM" → `https://xanhsm.com` (both `target="_blank"`)
  - Brief note: "Ứng dụng sẽ nhận danh sách điểm dừng để bạn dễ nhập."
- If `transport === "Đi bộ thong thả"` or `"Tự lái xe máy"`:
  - Show a note: "Bắt đầu hành trình và theo dõi tiến độ bên dưới."

---

## 5. Theo Dõi Hành Trình (Journey Tracker — Layout A)

**Location:** Inside `showRideBooking` block in `PlannerV2`, after the booking confirmation.

**Map library:** Leaflet.js via CDN in `index.html`. OpenStreetMap tiles (no API key).

**Layout (Layout A — chosen):**
```
┌──────────────────────────────────────────────────┐
│  [Leaflet Map — 65% width]  │  [Timeline — 35%]  │
│                              │                    │
│   Pin 1 ●──────── Pin 2 ●   │  01 · Ốc Đào      │
│              ──── Pin 3 ●   │  ● Đang đến        │
│                              │  02 · Rooftop      │
│                              │  ○ Tiếp theo       │
│                              │  03 · Bến Thành    │
│                              │  ○ Chờ             │
│                              │  [Đặt xe ngay]     │
└──────────────────────────────────────────────────┘
```

**Implementation details:**
- Leaflet map initializes with `rideLegs` coordinates. If coordinates are missing (mock data), use hardcoded Ho Chi Minh City fallback coords (center: `[10.7769, 106.7009]`).
- Fallback coords per stop index for mock data:
  - Stop 1: `[10.7769, 106.7009]` (Q1 center)
  - Stop 2: `[10.7780, 106.7050]`
  - Stop 3: `[10.7720, 106.6980]`
- Draw a polyline connecting all pins.
- Each pin: numbered circle marker (orange for current, green for next, grey for waiting).
- Timeline panel: scrollable list of stops, each with status chip, estimated travel time, and cost.
- Map and timeline wrapped in `framer-motion` for smooth entrance animation.
- Leaflet CSS added to `index.html` head.

**State:** `journeyStarted: boolean` — set to `true` when user clicks "Bắt đầu hành trình". Timeline shows active stop as "Đang đến" once started.

---

## Files Changed

| File | Change |
|------|--------|
| `src/main.jsx` | packages array, PricingGrid, commercial panel, transport booking, journey tracker component |
| `index.html` | Add Leaflet CSS + JS CDN links |

## Files NOT Changed

- `BE/` — no backend changes
- `src/ai-llm/` — KNN verified, no changes
- `src/styles.css` — minimal additions only (journey tracker panel styles added inline or via Tailwind)
