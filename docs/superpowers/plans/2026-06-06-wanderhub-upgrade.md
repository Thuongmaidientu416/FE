# WanderHUB Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Thêm gói 7 ngày vào Pricing, đổi nhãn commercial suggestions, thêm booking links cho Be/Xanh SM, và xây tính năng Theo dõi hành trình với bản đồ Leaflet tương tác.

**Architecture:** Tất cả thay đổi nằm trong `src/main.jsx` (React, Vite). Leaflet được load qua CDN trong `index.html` và truy cập qua `window.L` bên trong một `useEffect`. Không có backend thay đổi.

**Tech Stack:** React 18, Framer Motion, Tailwind CSS, Leaflet.js (CDN), OpenStreetMap tiles (no API key)

---

## File Map

| File | Thay đổi |
|------|----------|
| `index.html` | Thêm Leaflet CSS + JS CDN trong `<head>` |
| `src/main.jsx` | (1) `packages` array, (2) `PricingGrid`, (3) commercial suggestion labels, (4) transport booking panel, (5) journey tracker component |
| `src/styles.css` | Thêm styles cho `.journey-tracker-panel`, `.journey-tracker-map`, `.journey-tracker-timeline` |

---

## Task 1: Leaflet CDN vào index.html

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Thêm Leaflet CSS và JS vào `<head>` của `index.html`**

Thay thế nội dung `<head>`:

```html
<!doctype html>
<html lang="vi">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>WanderHUB - AI Urban Itinerary Platform</title>
    <meta
      name="description"
      content="WanderHUB thiết kế và điều phối lịch trình giải trí đô thị cá nhân hóa bằng AI."
    />
    <link
      rel="stylesheet"
      href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
      integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
      crossorigin=""
    />
    <script
      src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
      integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV/XN/WLs="
      crossorigin=""
    ></script>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

- [ ] **Step 2: Kiểm tra Leaflet load được**

Chạy `npm run dev`, mở browser, mở DevTools Console và gõ `window.L`. Phải thấy object Leaflet, không phải `undefined`.

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add Leaflet CDN for journey tracker map"
```

---

## Task 2: Thêm gói Explorer 7 Ngày vào Pricing

**Files:**
- Modify: `src/main.jsx` (lines 54–84 — `packages` array; lines 1853–1883 — `PricingGrid`)

- [ ] **Step 1: Thêm package object vào `packages` array**

Tìm dòng `const packages = [` (~line 54). Thêm object mới vào **đầu mảng** (trước Premium):

```js
const packages = [
  {
    name: "Explorer 7 Ngày",
    price: "49.000 VNĐ/7 ngày",
    note: "Trải nghiệm gần như full Premium trong 7 ngày — lý tưởng cho cuối tuần hoặc du khách ngắn ngày.",
    features: [
      "Không giới hạn lịch trình AI",
      "Mở khóa 100% Hidden Gems",
      "Re-route thông minh realtime",
      "Hỗ trợ chat 24/7",
      "Bản đồ theo dõi hành trình",
    ],
    notIncluded: ["Ưu tiên tài xế giờ cao điểm"],
  },
  {
    name: "Premium",
    // ... giữ nguyên phần còn lại
```

- [ ] **Step 2: Cập nhật `PricingGrid` sang 3 cột**

Tìm hàm `PricingGrid` (~line 1853). Thay `lg:grid-cols-2` thành `lg:grid-cols-3`:

```jsx
function PricingGrid({ preview = false, user = null }) {
  return (
    <div className="grid gap-8 lg:grid-cols-3 max-w-7xl mx-auto">
      {packages.map((plan) => (
```

- [ ] **Step 3: Kiểm tra trực quan**

Mở `/pricing` trong browser. Phải thấy 3 card: Explorer 7 Ngày → Premium (có badge "Best vibe") → International Tourist. Trên mobile (< lg) phải stack thành 1 cột.

- [ ] **Step 4: Commit**

```bash
git add src/main.jsx
git commit -m "feat: add Explorer 7-day pricing package"
```

---

## Task 3: Đổi nhãn Commercial Suggestions

**Files:**
- Modify: `src/main.jsx` (~lines 3138–3143)

- [ ] **Step 1: Thay text trong `commercial-suggestion-panel`**

Tìm đoạn:
```jsx
<strong>Hidden gem / đối tác gợi ý thêm</strong>
<small>Nằm ngoài 6 điểm AI chính, khách có thể chọn thêm nếu muốn trải nghiệm dịch vụ mới.</small>
```
và badge `<span>Partner seed</span>`.

Thay bằng:
```jsx
<strong>✨ Ngoài ra, có thể bạn quan tâm</strong>
<small>Được đề xuất từ đối tác mới — không nằm trong tuyến AI chính.</small>
```
và badge:
```jsx
<span>Đối tác</span>
```

- [ ] **Step 2: Kiểm tra trực quan**

Vào `/planner`, generate lịch trình. Panel đối tác phía dưới các AI cards phải hiện nhãn mới "✨ Ngoài ra, có thể bạn quan tâm" và badge "Đối tác".

- [ ] **Step 3: Commit**

```bash
git add src/main.jsx
git commit -m "feat: rename commercial suggestions panel to 'Ngoài ra, có thể bạn quan tâm'"
```

---

## Task 4: Transport Booking Links + Journey Tracker

Đây là task lớn nhất. Thay toàn bộ `showRideBooking` block (~lines 3188–3223) bằng `JourneyTracker` component.

**Files:**
- Modify: `src/main.jsx` (~lines 3188–3223)
- Modify: `src/styles.css` (append styles ở cuối)

### Step 4a: Thêm CSS styles

- [ ] **Step 4a.1: Append vào cuối `src/styles.css`**

```css
/* ===== Journey Tracker (Layout A) ===== */

.journey-tracker-panel {
  grid-column: 1 / -1;
  border: 1px solid rgba(45, 90, 61, 0.15);
  border-radius: 20px;
  overflow: hidden;
  background: #fdf8f3;
}

.journey-tracker-inner {
  display: grid;
  grid-template-columns: 1fr 320px;
  min-height: 420px;
}

.journey-tracker-map-wrap {
  position: relative;
  background: #e8f0ea;
  min-height: 420px;
}

.journey-tracker-map-wrap > div {
  height: 100%;
  min-height: 420px;
}

.journey-tracker-timeline {
  display: flex;
  flex-direction: column;
  padding: 20px 16px;
  background: #fff;
  border-left: 1px solid rgba(45, 90, 61, 0.1);
  overflow-y: auto;
  max-height: 520px;
}

.journey-tracker-timeline-head {
  margin-bottom: 14px;
}

.journey-tracker-timeline-head strong {
  display: block;
  font-size: 15px;
  font-weight: 900;
  color: #1e4230;
}

.journey-tracker-timeline-head small {
  display: block;
  margin-top: 3px;
  font-size: 12px;
  color: rgba(30, 66, 48, 0.55);
}

.journey-tracker-leg {
  display: flex;
  gap: 10px;
  align-items: flex-start;
  position: relative;
  padding-bottom: 16px;
}

.journey-tracker-leg::before {
  content: '';
  position: absolute;
  left: 13px;
  top: 28px;
  bottom: 0;
  width: 2px;
  background: rgba(45, 90, 61, 0.15);
}

.journey-tracker-leg:last-child::before {
  display: none;
}

.journey-tracker-pin {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 900;
  flex-shrink: 0;
  position: relative;
  z-index: 1;
}

.journey-tracker-pin.is-current {
  background: #c96420;
  color: #fff;
  box-shadow: 0 0 0 4px rgba(201, 100, 32, 0.18);
}

.journey-tracker-pin.is-next {
  background: #2d5a3d;
  color: #fff;
}

.journey-tracker-pin.is-waiting {
  background: #e5e7eb;
  color: #9ca3af;
}

.journey-tracker-leg-info {
  flex: 1;
  min-width: 0;
}

.journey-tracker-leg-info b {
  display: block;
  font-size: 13px;
  font-weight: 800;
  color: #1e4230;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.journey-tracker-leg-info small {
  display: block;
  font-size: 11px;
  color: rgba(30, 66, 48, 0.55);
  margin-top: 2px;
}

.journey-tracker-status {
  font-size: 10px;
  font-weight: 800;
  padding: 2px 8px;
  border-radius: 999px;
  white-space: nowrap;
}

.journey-tracker-status.current {
  background: rgba(201, 100, 32, 0.12);
  color: #c96420;
}

.journey-tracker-status.next {
  background: rgba(45, 90, 61, 0.1);
  color: #2d5a3d;
}

.journey-tracker-status.waiting {
  background: #f3f4f6;
  color: #9ca3af;
}

.journey-tracker-booking {
  margin-top: auto;
  padding-top: 14px;
  border-top: 1px solid rgba(45, 90, 61, 0.1);
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.journey-tracker-booking-note {
  font-size: 11px;
  color: rgba(30, 66, 48, 0.55);
  line-height: 1.5;
}

.journey-tracker-btn-be {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: #f59e0b;
  color: #1c1917;
  font-size: 13px;
  font-weight: 900;
  border-radius: 12px;
  padding: 10px 14px;
  text-decoration: none;
  transition: opacity 0.15s;
}

.journey-tracker-btn-be:hover { opacity: 0.88; }

.journey-tracker-btn-xanh {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: #16a34a;
  color: #fff;
  font-size: 13px;
  font-weight: 900;
  border-radius: 12px;
  padding: 10px 14px;
  text-decoration: none;
  transition: opacity 0.15s;
}

.journey-tracker-btn-xanh:hover { opacity: 0.88; }

.journey-tracker-walk-note {
  background: rgba(45, 90, 61, 0.07);
  border-radius: 12px;
  padding: 10px 12px;
  font-size: 12px;
  color: #2d5a3d;
  font-weight: 600;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .journey-tracker-inner {
    grid-template-columns: 1fr;
  }
  .journey-tracker-map-wrap {
    min-height: 240px;
  }
  .journey-tracker-map-wrap > div {
    min-height: 240px;
  }
  .journey-tracker-timeline {
    border-left: none;
    border-top: 1px solid rgba(45, 90, 61, 0.1);
    max-height: none;
  }
}
```

### Step 4b: Thêm JourneyTracker component vào main.jsx

- [ ] **Step 4b.1: Định nghĩa `JourneyTracker` component**

Thêm component này **ngay trước** hàm `PlannerV2` (~line 2601):

```jsx
const HCM_FALLBACK_COORDS = [
  [10.7769, 106.7009],
  [10.7800, 106.7050],
  [10.7720, 106.6980],
  [10.7740, 106.7030],
  [10.7760, 106.7070],
];

function JourneyTracker({ rideLegs, transport, totalRideMinutes }) {
  const mapContainerRef = useRef(null);
  const leafletInstanceRef = useRef(null);
  const [activeIndex, setActiveIndex] = useState(0);

  const getCoords = (leg, index) => {
    if (leg.latitude && leg.longitude) return [leg.latitude, leg.longitude];
    return HCM_FALLBACK_COORDS[index % HCM_FALLBACK_COORDS.length];
  };

  useEffect(() => {
    const L = window.L;
    if (!L || !mapContainerRef.current || leafletInstanceRef.current) return;

    const coords = rideLegs.map((leg, i) => getCoords(leg, i));
    const center = coords[0] || [10.7769, 106.7009];

    const map = L.map(mapContainerRef.current, { zoomControl: true, scrollWheelZoom: false }).setView(center, 14);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: "© OpenStreetMap",
      maxZoom: 18,
    }).addTo(map);

    if (coords.length > 1) {
      L.polyline(coords, { color: "#2d5a3d", weight: 3, dashArray: "6 4", opacity: 0.8 }).addTo(map);
    }

    coords.forEach((coord, index) => {
      const isFirst = index === 0;
      const icon = L.divIcon({
        className: "",
        html: `<div style="
          width:28px;height:28px;border-radius:50%;
          background:${isFirst ? "#c96420" : "#2d5a3d"};
          color:#fff;display:flex;align-items:center;justify-content:center;
          font-size:12px;font-weight:900;
          box-shadow:0 2px 8px rgba(0,0,0,0.25);
          border:2px solid #fff;
        ">${index + 1}</div>`,
        iconSize: [28, 28],
        iconAnchor: [14, 14],
      });
      L.marker(coord, { icon })
        .addTo(map)
        .bindPopup(`<b>${rideLegs[index].title}</b><br><small>${rideLegs[index].time || ""}</small>`);
    });

    if (coords.length > 1) {
      const bounds = L.latLngBounds(coords);
      map.fitBounds(bounds, { padding: [40, 40] });
    }

    leafletInstanceRef.current = map;
    return () => {
      map.remove();
      leafletInstanceRef.current = null;
    };
  }, []);

  const isRide = transport === "Be / Xanh SM";

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: "easeOut" }}
      className="journey-tracker-panel"
    >
      <div className="journey-tracker-inner">
        <div className="journey-tracker-map-wrap">
          <div ref={mapContainerRef} />
        </div>

        <div className="journey-tracker-timeline">
          <div className="journey-tracker-timeline-head">
            <strong>Theo dõi hành trình</strong>
            <small>{rideLegs.length} điểm · {totalRideMinutes} phút di chuyển</small>
          </div>

          {rideLegs.map((leg, index) => {
            const status = index < activeIndex ? "done" : index === activeIndex ? "current" : index === activeIndex + 1 ? "next" : "waiting";
            return (
              <div key={`tracker-${leg.provider_id || leg.title}-${index}`} className="journey-tracker-leg">
                <div className={`journey-tracker-pin ${status === "current" ? "is-current" : status === "next" ? "is-next" : "is-waiting"}`}>
                  {index + 1}
                </div>
                <div className="journey-tracker-leg-info">
                  <b>{leg.title}</b>
                  <small>{leg.time || leg.rideLabel} {index > 0 && leg.travelFromPrevious ? `· ${leg.travelFromPrevious} phút từ điểm trước` : ""}</small>
                </div>
                {status !== "done" && (
                  <span className={`journey-tracker-status ${status}`}>
                    {status === "current" ? "Đang đến" : status === "next" ? "Tiếp theo" : "Chờ"}
                  </span>
                )}
              </div>
            );
          })}

          <div className="journey-tracker-booking">
            {isRide ? (
              <>
                <p className="journey-tracker-booking-note">
                  Ứng dụng sẽ nhận danh sách điểm dừng — copy tên điểm để nhập nhanh vào app.
                </p>
                <a
                  href="https://be.com.vn"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="journey-tracker-btn-be"
                >
                  <Car size={15} /> Mở Be
                </a>
                <a
                  href="https://xanhsm.com"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="journey-tracker-btn-xanh"
                >
                  <Car size={15} /> Mở Xanh SM
                </a>
              </>
            ) : (
              <div className="journey-tracker-walk-note">
                {transport === "Đi bộ thong thả"
                  ? "Bắt đầu đi bộ và theo dõi tiến độ từng điểm trên bản đồ."
                  : "Khởi động xe và theo dõi hành trình trên bản đồ."}
              </div>
            )}
          </div>
        </div>
      </div>
    </motion.div>
  );
}
```

- [ ] **Step 4b.2: Thay thế `showRideBooking` block trong `PlannerV2`**

Tìm đoạn từ `{showRideBooking ? (` (~line 3188) đến `): null}` (~line 3223). Thay toàn bộ bằng:

```jsx
{showRideBooking ? (
  <JourneyTracker
    rideLegs={rideLegs}
    transport={transport}
    totalRideMinutes={totalRideMinutes}
  />
) : null}
```

- [ ] **Step 4b.3: Xóa `map-strip` dư thừa**

Tìm và xóa dòng (~line 3225):
```jsx
<div className="map-strip flex items-center gap-3 justify-center mt-2"><RouteIcon /> Sẵn sàng kết nối Xanh SM di chuyển</div>
```
(Thông tin này đã được tích hợp vào JourneyTracker)

- [ ] **Step 4b.4: Kiểm tra trực quan**

1. Vào `/planner`, generate lịch trình.
2. Tick chọn ít nhất 1 stop → click "Tiếp tục đặt xe".
3. Panel **Theo dõi hành trình** phải hiện ra với:
   - Bản đồ Leaflet thực, có pins đánh số và route line xanh lá nét đứt.
   - Timeline bên phải với trạng thái "Đang đến / Tiếp theo / Chờ".
4. Nếu transport là "Be / Xanh SM": thấy 2 nút "Mở Be" (vàng) và "Mở Xanh SM" (xanh lá).
5. Nếu transport là "Đi bộ" hoặc "Tự lái": thấy note text thay vì nút booking.

- [ ] **Step 4b.5: Commit**

```bash
git add src/main.jsx src/styles.css
git commit -m "feat: add JourneyTracker with Leaflet map and transport booking links"
```

---

## Self-Review Checklist

- [x] **Task 1** — Leaflet CDN: `index.html` head cập nhật đủ CSS + JS, integrity hash đúng với v1.9.4.
- [x] **Task 2** — Gói 7 ngày: package object đầy đủ features + notIncluded, grid chuyển sang 3 cột.
- [x] **Task 3** — Label: 2 string thay thế rõ ràng, không còn "Partner seed" hay "Hidden gem / đối tác gợi ý thêm".
- [x] **Task 4** — JourneyTracker: `HCM_FALLBACK_COORDS` fallback khi stop không có lat/lon; `leafletInstanceRef` cleanup đúng trong return của useEffect; `transport` prop truyền đúng; `rideLegs` và `totalRideMinutes` là giá trị tính sẵn từ `PlannerV2` (không cần tính lại).
- [x] **Type consistency** — `rideLegs` shape là `{ title, time, rideLabel, travelFromPrevious, latitude, longitude, provider_id }` — khớp với `rideLegs` useMemo trong PlannerV2.
- [x] **No placeholders** — mọi bước đều có code đầy đủ.
