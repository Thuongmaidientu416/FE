# International Plan English UI + Local Tips Tab — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** When `userPlan.plan_key === "international"`, the entire WanderHUB app renders in English and the itinerary modal gains a "Local Tips" tab with per-stop cultural guidance.

**Architecture:** A `LangContext` at the `App` root derives its value from `userPlan`. Every component calls `useT()` to get a `t(key)` translator function and an `isEn` boolean. All UI strings live in a flat `TRANSLATIONS` object at the top of `main.jsx`; no external library.

**Tech Stack:** React context, single `src/main.jsx` file, no new dependencies.

---

## Files

- Modify: `src/main.jsx` (all tasks)

---

### Task 1: TRANSLATIONS object + LangContext + useT() hook + LOCAL_TIPS tables

**Files:**
- Modify: `src/main.jsx` — add after line 336 (after `const navItems = [...]`)

- [ ] **Step 1: Add TRANSLATIONS object after `navItems` (line 336)**

Insert this block immediately after the closing `];` of `navItems`:

```js
const TRANSLATIONS = {
  vi: {
    // Navbar
    "nav.home": "Trang chủ",
    "nav.about": "Về WanderHUB",
    "nav.explore": "Khám phá",
    "nav.pricing": "Gói dịch vụ",
    "nav.reviews": "Đánh giá",
    "nav.contact": "Liên hệ",
    "nav.history": "Lịch sử",
    "nav.login": "Đăng nhập",
    "nav.logout": "Đăng xuất",
    "nav.start": "Bắt đầu lên lịch trình",
    "nav.hello": "Chào",
    // Footer
    "footer.tagline": "WanderHUB là người bạn thổ địa thông minh giúp bạn tìm hidden gems, xếp lịch trình và điều phối di chuyển trong thành phố.",
    "footer.contact": "Liên hệ",
    "footer.address": "Địa chỉ: Thủ Đức, TP.HCM",
    "footer.login": "Đăng nhập / Đăng ký",
    // Hero
    "hero.desc": "Góc nhìn WanderHUB đồng hành cùng bạn trên hành trình khám phá thành phố: lướt qua tuyến ven sông Sài Gòn, ngắm Landmark 81 phản chiếu trên mặt nước dưới ánh nắng ấm áp, nối tiếp các điểm cafe, ăn tối và check-in đúng gu của bạn.",
    "hero.cta.plan": "Lên lịch trình ngay",
    "hero.cta.explore": "Xem Trải Nghiệm Đô Thị",
    // Home sections
    "home.popular.eyebrow": "Xu hướng khám phá Sài Gòn",
    "home.popular.title": "Lịch trình được yêu thích nhất",
    "home.popular.sub": "Được đông đảo người dùng lựa chọn và xếp hạng cao. Click để trải nghiệm ngay.",
    "home.about.eyebrow": "Thương hiệu WanderHUB",
    "home.about.title": "Một góc nhìn lịch lãm về khám phá đô thị.",
    "home.how.eyebrow": "Cách hoạt động",
    "home.how.title": "Ba bước — lên đường ngay.",
    "home.how.cta": "Thử tạo lịch trình ngay",
    // Planner form
    "planner.mood.label": "Chọn vibe / Mood",
    "planner.district.label": "Quận / Khu vực",
    "planner.budget.label": "Ngân sách",
    "planner.time.label": "Khung giờ",
    "planner.interests.label": "Sở thích",
    "planner.transport.label": "Phương tiện",
    "planner.note.label": "Ghi chú / Yêu cầu đặc biệt",
    "planner.note.small": "Note cho tài xế hoặc yêu cầu riêng",
    "planner.note.placeholder": "Ví dụ: Chuẩn bị dù vì có thể mưa, cần ghế cho em bé, dị ứng hải sản...",
    "planner.btn.generate": "Lên lịch trình AI",
    "planner.generating": "Đang xử lý...",
    "planner.loading.title": "Đang tính toán...",
    "planner.result.title": "Tuyến đường AI khuyên dùng",
    "planner.export.qr": "Xuất QR",
    "planner.basic.remaining": "Gói Basic: còn {remaining}/{limit} lượt — chu kỳ {days} ngày",
    "planner.unlimited": "Gói {plan}: tạo lịch trình không giới hạn",
    "planner.limit.title": "Đã dùng lượt miễn phí trong chu kỳ này.",
    "planner.limit.reset": "Reset sau {days} ngày",
    "planner.limit.upgrade": "Hoặc nâng cấp Premium để tạo không giới hạn.",
    "planner.limit.cta": "Xem gói Premium",
    // Planner moods
    "mood.chill.hint": "Cafe, dạo phố, nhịp nhẹ",
    "mood.date.label": "Hẹn hò",
    "mood.date.hint": "Đẹp, riêng tư, ven sông",
    "mood.group.label": "Đi nhóm",
    "mood.group.hint": "Rộng rãi, vui, dễ tụ tập",
    "mood.foodie.hint": "Ăn ngon, local, must-try",
    "mood.nightlife.hint": "Bar, phố đêm, city lights",
    "mood.culture.label": "Văn hóa",
    "mood.culture.hint": "Bảo tàng, phố cũ, nghệ thuật",
    "mood.checkin.label": "Check-in",
    "mood.checkin.hint": "Ảnh đẹp, landmark, view",
    "mood.hidden_gem.hint": "Ngóc ngách ít người biết",
    "mood.healing.hint": "Yên tĩnh, xanh, hồi phục",
    "mood.premium.hint": "Rooftop, fine dining, sang",
    "mood.budget.label": "Tiết kiệm",
    "mood.budget.hint": "Vừa túi tiền, nhiều giá trị",
    "mood.solo.hint": "Tự do, dễ đi một mình",
    // Budget options
    "budget.save": "Tiết kiệm",
    "budget.mid": "Vừa đẹp",
    "budget.comfort": "Thoải mái",
    "budget.unlimited": "Không giới hạn",
    // Time slots
    "time.morning": "Sáng nhẹ",
    "time.afternoon": "Trưa chiều",
    "time.afterwork": "Sau giờ làm",
    "time.night": "Đêm Sài Gòn",
    "time.halfday": "Nửa ngày",
    "time.morning.hint": "Cafe + check-in",
    "time.afternoon.hint": "Indoor + văn hóa",
    "time.afterwork.hint": "Ăn tối + dạo phố",
    "time.night.hint": "Nightlife + ăn khuya",
    "time.halfday.hint": "4-5 điểm dừng",
    // Interests
    "interest.checkin": "Chụp hình",
    "interest.cafe": "Uống cafe",
    "interest.food": "Trải nghiệm ẩm thực",
    "interest.culture": "Văn hóa",
    "interest.nightlife": "Phố đêm",
    "interest.entertainment": "Hoạt động vui chơi",
    // Itinerary modal
    "modal.header.label": "✦ WanderHUB · Lịch trình cá nhân",
    "modal.stops": "điểm dừng",
    "modal.trip.detail": "Chi tiết hành trình",
    "modal.driver.confirmed": "Tài xế đã xác nhận",
    "modal.driver.fare": "Giá xe",
    "modal.tab.itinerary": "Lịch trình",
    "modal.tab.tips": "Local Tips",
    "modal.qr.scan": "Quét để",
    "modal.qr.open": "mở & chia sẻ",
    "modal.qr.view": "xem",
    "modal.qr.label": "lịch trình",
    "modal.qr.expand": "Phóng to QR ↗",
    // History
    "history.eyebrow": "Lịch sử hành trình",
    "history.title": "Chuyến đi đã chốt",
    "history.loading": "Đang tải lịch sử hành trình...",
    "history.error": "Không thể tải lịch sử chuyến đi.",
    "history.empty.title": "Chưa có chuyến đi nào",
    "history.empty.sub": "Bạn chưa lưu hay chốt lịch trình nào. Hãy bắt đầu chuyến đi đầu tiên nhé!",
    "history.empty.cta": "Lên lịch ngay",
    "history.detail.label": "Lịch trình chi tiết:",
    "history.btn.view": "Xem Lại Lịch Trình & Đặt Xe",
    "history.noauth.title": "Bạn chưa đăng nhập",
    "history.noauth.sub": "Đăng nhập để lưu và xem lại các lịch trình đã đi của bạn.",
    "history.noauth.cta": "Đăng nhập ngay",
    // Popular recommendations
    "popular.select_count": "lượt chọn",
    "popular.loading": "Đang tải lịch trình đề xuất...",
    "popular.btn": "Xem lịch trình",
    // Reviews
    "reviews.eyebrow": "Cộng đồng WanderHUB",
    "reviews.title": "Khách hàng nói gì?",
    // Common
    "common.loading": "Đang tải...",
    "common.book_driver": "Đặt xe ngay",
    "common.view_again": "Xem Lại",
    "common.start_plan": "Lên lịch ngay",
  },
  en: {
    // Navbar
    "nav.home": "Home",
    "nav.about": "About",
    "nav.explore": "Explore",
    "nav.pricing": "Pricing",
    "nav.reviews": "Reviews",
    "nav.contact": "Contact",
    "nav.history": "My Trips",
    "nav.login": "Sign In",
    "nav.logout": "Sign Out",
    "nav.start": "Start Planning",
    "nav.hello": "Hello",
    // Footer
    "footer.tagline": "WanderHUB is your smart local guide — uncovering hidden gems, building itineraries, and coordinating transport around the city.",
    "footer.contact": "Contact",
    "footer.address": "Address: Thu Duc, Ho Chi Minh City",
    "footer.login": "Sign In / Register",
    // Hero
    "hero.desc": "WanderHUB rides alongside you through the city: skimming the Saigon riverfront, catching Landmark 81 at golden hour, chaining cafés, dinners, and photo spots that actually match your vibe.",
    "hero.cta.plan": "Plan My Trip Now",
    "hero.cta.explore": "Explore the City",
    // Home sections
    "home.popular.eyebrow": "Trending in Saigon",
    "home.popular.title": "Most Loved Itineraries",
    "home.popular.sub": "Top-rated by our community. Click to experience them yourself.",
    "home.about.eyebrow": "The WanderHUB Story",
    "home.about.title": "A refined take on urban exploration.",
    "home.how.eyebrow": "How It Works",
    "home.how.title": "Three steps — then hit the road.",
    "home.how.cta": "Try Building an Itinerary",
    // Planner form
    "planner.mood.label": "Pick Your Vibe / Mood",
    "planner.district.label": "District / Area",
    "planner.budget.label": "Budget",
    "planner.time.label": "Time Slot",
    "planner.interests.label": "Interests",
    "planner.transport.label": "Transport",
    "planner.note.label": "Notes / Special Requests",
    "planner.note.small": "Notes for the driver or specific requirements",
    "planner.note.placeholder": "e.g. Bring umbrella — rain expected, need baby seat, seafood allergy...",
    "planner.btn.generate": "Generate AI Itinerary",
    "planner.generating": "Processing...",
    "planner.loading.title": "Calculating...",
    "planner.result.title": "AI Recommended Route",
    "planner.export.qr": "Export QR",
    "planner.basic.remaining": "Basic plan: {remaining}/{limit} uses left — {days}-day cycle",
    "planner.unlimited": "{plan} plan: unlimited itineraries",
    "planner.limit.title": "You've used all free generations this cycle.",
    "planner.limit.reset": "Resets in {days} days",
    "planner.limit.upgrade": "Or upgrade to Premium for unlimited generations.",
    "planner.limit.cta": "View Premium Plans",
    // Planner moods
    "mood.chill.hint": "Cafés, strolling, slow pace",
    "mood.date.label": "Date Night",
    "mood.date.hint": "Scenic, intimate, riverside",
    "mood.group.label": "Group Outing",
    "mood.group.hint": "Spacious, fun, easy to gather",
    "mood.foodie.hint": "Great food, local, must-try",
    "mood.nightlife.hint": "Bars, night streets, city lights",
    "mood.culture.label": "Culture",
    "mood.culture.hint": "Museums, old streets, art",
    "mood.checkin.label": "Photo Spots",
    "mood.checkin.hint": "Great shots, landmarks, views",
    "mood.hidden_gem.hint": "Off-the-beaten-path spots",
    "mood.healing.hint": "Quiet, green, restorative",
    "mood.premium.hint": "Rooftop, fine dining, luxury",
    "mood.budget.label": "Budget-Friendly",
    "mood.budget.hint": "Best value for money",
    "mood.solo.hint": "Easy to navigate solo",
    // Budget options
    "budget.save": "Budget",
    "budget.mid": "Moderate",
    "budget.comfort": "Comfortable",
    "budget.unlimited": "No Limit",
    // Time slots
    "time.morning": "Morning",
    "time.afternoon": "Afternoon",
    "time.afterwork": "After Work",
    "time.night": "Saigon Nights",
    "time.halfday": "Half Day",
    "time.morning.hint": "Café + photo spots",
    "time.afternoon.hint": "Indoor + culture",
    "time.afterwork.hint": "Dinner + evening stroll",
    "time.night.hint": "Nightlife + late bites",
    "time.halfday.hint": "4–5 stops",
    // Interests
    "interest.checkin": "Photography",
    "interest.cafe": "Café Hopping",
    "interest.food": "Food Experiences",
    "interest.culture": "Culture",
    "interest.nightlife": "Nightlife",
    "interest.entertainment": "Entertainment",
    // Itinerary modal
    "modal.header.label": "✦ WanderHUB · Personal Itinerary",
    "modal.stops": "stops",
    "modal.trip.detail": "Trip Details",
    "modal.driver.confirmed": "Driver Confirmed",
    "modal.driver.fare": "Fare",
    "modal.tab.itinerary": "Itinerary",
    "modal.tab.tips": "Local Tips",
    "modal.qr.scan": "Scan to",
    "modal.qr.open": "open & share",
    "modal.qr.view": "view",
    "modal.qr.label": "your itinerary",
    "modal.qr.expand": "Expand QR ↗",
    // History
    "history.eyebrow": "Your Journey History",
    "history.title": "Past Trips",
    "history.loading": "Loading your trip history...",
    "history.error": "Could not load trip history.",
    "history.empty.title": "No trips yet",
    "history.empty.sub": "You haven't saved or confirmed any itinerary yet. Start your first trip!",
    "history.empty.cta": "Plan a Trip",
    "history.detail.label": "Itinerary Details:",
    "history.btn.view": "View Itinerary & Book a Ride",
    "history.noauth.title": "You're not signed in",
    "history.noauth.sub": "Sign in to save and revisit your past itineraries.",
    "history.noauth.cta": "Sign In",
    // Popular recommendations
    "popular.select_count": "selected",
    "popular.loading": "Loading recommended itineraries...",
    "popular.btn": "View Itinerary",
    // Reviews
    "reviews.eyebrow": "WanderHUB Community",
    "reviews.title": "What Our Users Say",
    // Common
    "common.loading": "Loading...",
    "common.book_driver": "Book a Ride",
    "common.view_again": "View Again",
    "common.start_plan": "Plan Now",
  },
};
```

- [ ] **Step 2: Add LangContext and useT() hook immediately after TRANSLATIONS**

```js
const LangContext = React.createContext("vi");

function useT() {
  const lang = useContext(LangContext);
  const isEn = lang === "en";
  const t = (key) => TRANSLATIONS[lang]?.[key] ?? TRANSLATIONS["vi"]?.[key] ?? key;
  return { t, isEn, lang };
}
```

- [ ] **Step 3: Add LOCAL_TIPS lookup tables after `CATEGORY_BLURB` (line ~3330)**

Insert immediately after the closing `};` of `CATEGORY_BLURB`:

```js
const LOCAL_TIPS_BLURB = {
  checkin: "A popular photo spot — iconic architecture, street scenes, or viewpoints that define the Saigon aesthetic.",
  entertainment: "An entertainment venue — great for groups, high energy, and unwinding after a long day.",
  culture: "A cultural or heritage space: expect history, art, and a glimpse into Vietnamese identity.",
  nightlife: "A nightlife hotspot — drinks, music, and the electric atmosphere of Saigon after dark.",
  cafe_drink: "A Vietnamese café — expect strong drip coffee, condensed milk, and a laid-back local vibe.",
  food: "A local eatery serving authentic Vietnamese cuisine — one of the city's true pleasures.",
};

const LOCAL_CUSTOMS = {
  checkin: "Ask before photographing locals or religious spaces. A smile and a nod go a long way.",
  entertainment: "Motorbike parking on the pavement is normal. Join the flow and you'll fit right in.",
  culture: "Dress modestly (covered shoulders and knees) when entering temples or government buildings.",
  nightlife: "Cash is king at most local bars. ATMs are everywhere — withdraw before heading out.",
  cafe_drink: "It's perfectly normal to sit for hours. Order one drink and stay as long as you like.",
  food: "Point at the menu or neighbouring tables if you're unsure what to order — staff are used to it.",
};

const LOCAL_PHRASES = {
  checkin:     { vi: "Cho tôi chụp ảnh ở đây được không?", roman: "Cho toy chup anh o day duoc khong?", en: "May I take a photo here?" },
  entertainment: { vi: "Bao nhiêu tiền vào cửa?",          roman: "Bao nhieu tien vao cua?",           en: "How much is the entrance fee?" },
  culture:     { vi: "Đây là gì vậy?",                    roman: "Day la gi vay?",                    en: "What is this?" },
  nightlife:   { vi: "Cho tôi một ly bia.",               roman: "Cho toy mot ly bia.",               en: "One beer, please." },
  cafe_drink:  { vi: "Cho tôi một ly cà phê sữa đá.",    roman: "Cho toy mot lee ca phe sua da.",    en: "One iced milk coffee, please." },
  food:        { vi: "Cho tôi xem thực đơn.",             roman: "Cho toy xem thuc don.",             en: "Can I see the menu?" },
};
```

- [ ] **Step 4: Wire LangContext.Provider in App root**

Find the `return (` in `function App()` (line ~5736). Wrap the fragment:

```jsx
// Before:
return (
  <>
    <Navbar user={user} userPlan={userPlan} onLogout={handleLogout} />
    ...

// After:
const lang = userPlan?.plan_key === "international" ? "en" : "vi";
return (
  <LangContext.Provider value={lang}>
    <>
      <Navbar user={user} userPlan={userPlan} onLogout={handleLogout} />
      ...
    </>
  </LangContext.Provider>
);
```

- [ ] **Step 5: Commit**

```bash
git add src/main.jsx
git commit -m "feat: add TRANSLATIONS, LangContext, useT() hook, LOCAL_TIPS tables, wire App root"
```

---

### Task 2: Translate Navbar + Footer

**Files:**
- Modify: `src/main.jsx` — `Navbar` (~line 675), `Footer` (~line 777)

- [ ] **Step 1: Update navItems to use translation keys**

Replace the static `navItems` array:

```js
// Remove this:
const navItems = [
  ["Trang chủ", "/"],
  ["Về WanderHUB", "/about"],
  ["Khám phá", "/explore"],
  ["Gói dịch vụ", "/pricing"],
  ["Đánh giá", "/reviews"],
  ["Liên hệ", "/contact"],
];

// Replace with keys — Navbar will resolve labels using useT()
const NAV_ITEMS = [
  { key: "nav.home",    href: "/" },
  { key: "nav.about",   href: "/about" },
  { key: "nav.explore", href: "/explore" },
  { key: "nav.pricing", href: "/pricing" },
  { key: "nav.reviews", href: "/reviews" },
  { key: "nav.contact", href: "/contact" },
];
```

- [ ] **Step 2: Update Navbar component**

```jsx
function Navbar({ user, userPlan, onLogout }) {
  const { t, isEn } = useT();
  const [open, setOpen] = useState(false);

  const displayedNavItems = user
    ? [...NAV_ITEMS, { key: "nav.history", href: "/history" }]
    : NAV_ITEMS.filter(({ href }) => href !== "/pricing");

  return (
    <header className="site-nav fixed left-4 right-4 top-4 z-50">
      <div className="nav-glass mx-auto flex h-20 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        <Logo />
        <nav className="hidden items-center gap-7 lg:flex">
          {displayedNavItems.map(({ key, href }) => (
            <NavLink
              id={`nav-link-${href.replace("/", "") || "home"}`}
              key={href}
              to={href}
              className={({ isActive }) =>
                `text-sm font-medium transition ${isActive ? "text-cyan" : "text-[#5a7a60] hover:text-[#1e4230]"}`
              }
            >
              {t(key)}
            </NavLink>
          ))}
        </nav>
        <div className="hidden items-center gap-3 lg:flex">
          {user ? (
            <>
              {user.role === "admin" && (
                <NavLink id="nav-btn-admin" to="/admin" className="mr-2 text-xs font-semibold px-2.5 py-1 rounded-full border border-[#c96420]/30 bg-[#c96420]/5 text-[#c96420] hover:bg-[#c96420]/10 transition">
                  🛡️ Admin Panel
                </NavLink>
              )}
              <span className="text-sm font-semibold text-[#1e4230]">{t("nav.hello")}, {user.name}!</span>
              {userPlan && (
                <span className={`text-xs font-semibold px-2.5 py-1 rounded-full ${PLAN_BADGE_STYLES[userPlan.plan_key] || PLAN_BADGE_STYLES.basic}`}>
                  {userPlan.plan_name}
                </span>
              )}
              <button onClick={onLogout} className="btn btn-ghost">{t("nav.logout")}</button>
            </>
          ) : (
            <>
              <NavLink to="/auth" className="btn btn-ghost">{t("nav.login")}</NavLink>
              <NavLink to="/auth" className="btn btn-primary">{t("nav.start")}</NavLink>
            </>
          )}
        </div>
      </div>
    </header>
  );
}
```

- [ ] **Step 3: Update Footer component**

```jsx
function Footer({ user }) {
  const { t } = useT();
  return (
    <footer className="border-t border-[#2d5a3d]/10 bg-[#f5f0e8]">
      <div className="mx-auto grid max-w-7xl gap-8 px-4 py-10 sm:px-6 md:grid-cols-[1.4fr_1fr_1fr] lg:px-8">
        <div>
          <Logo />
          <p className="mt-4 max-w-md text-sm leading-6 text-[#3d2b1a]/65">{t("footer.tagline")}</p>
        </div>
        <div className="text-sm text-[#3d2b1a]/65">
          <div className="mb-3 font-semibold text-[#1e4230]">{t("footer.contact")}</div>
          <p>{t("footer.address")}</p>
          <p>Hotline: 1900-0905</p>
          <p>Email: <a href="mailto:wanderhub.team.sg@gmail.com" className="hover:underline">wanderhub.team.sg@gmail.com</a></p>
          <p>Facebook: <a href="https://www.facebook.com/wanderhub.team.sg" target="_blank" rel="noopener noreferrer" className="hover:underline">WanderHUB Team</a></p>
        </div>
        <div className="grid gap-2 text-sm">
          <NavLink to="/faq" className="text-[#3d2b1a]/62 hover:text-cyan">FAQ</NavLink>
          <NavLink to="/terms" className="text-[#3d2b1a]/62 hover:text-cyan">Terms & Policies</NavLink>
          <NavLink to="/auth" className="text-[#3d2b1a]/62 hover:text-cyan">{t("footer.login")}</NavLink>
          <NavLink to={!user ? "/auth" : hasPlan() ? "/planner" : "/pricing"} className="text-[#3d2b1a]/62 hover:text-cyan">AI Trip Planner</NavLink>
        </div>
      </div>
    </footer>
  );
}
```

- [ ] **Step 4: Commit**

```bash
git add src/main.jsx
git commit -m "feat: translate Navbar and Footer via useT()"
```

---

### Task 3: Translate Landing Page (Home + HeroCyclingText)

**Files:**
- Modify: `src/main.jsx` — `heroMessages` (~line 837), `HeroCyclingText` (~line 843), `Home` (~line 1825), `PopularRecommendations` (~line 5008)

- [ ] **Step 1: Replace heroMessages with bilingual versions**

```js
// Remove:
const heroMessages = [
  { sub: "Landmark 81 → Nguyễn Huệ → Ốc Đào", main: ["Đi qua ánh đèn", "ven sông Sài Gòn."] },
  { sub: "AI itinerary engine", main: ["Designed For Your Vibe,", "Built For Your Route."] },
  { sub: "Bưu Điện → Secret Garden → Bến Thành", main: ["Khám phá Sài Gòn", "theo cách của bạn."] },
];

// Replace with:
const heroMessages = {
  vi: [
    { sub: "Landmark 81 → Nguyễn Huệ → Ốc Đào", main: ["Đi qua ánh đèn", "ven sông Sài Gòn."] },
    { sub: "AI itinerary engine", main: ["Designed For Your Vibe,", "Built For Your Route."] },
    { sub: "Bưu Điện → Secret Garden → Bến Thành", main: ["Khám phá Sài Gòn", "theo cách của bạn."] },
  ],
  en: [
    { sub: "Landmark 81 → Nguyễn Huệ → Ốc Đào", main: ["Through the lights", "along the Saigon River."] },
    { sub: "AI itinerary engine", main: ["Designed For Your Vibe,", "Built For Your Route."] },
    { sub: "Bưu Điện → Secret Garden → Bến Thành", main: ["Discover Saigon", "your way."] },
  ],
};
```

- [ ] **Step 2: Update HeroCyclingText to use lang**

```jsx
function HeroCyclingText() {
  const { lang } = useT();
  const messages = heroMessages[lang] ?? heroMessages.vi;
  const [idx, setIdx] = useState(0);
  useEffect(() => {
    const id = setInterval(() => setIdx((i) => (i + 1) % messages.length), 3600);
    return () => clearInterval(id);
  }, [messages.length]);
  const { sub, main } = messages[idx];
  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={`${lang}-${idx}`}
        initial={{ opacity: 0, y: 44 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -30 }}
        transition={{ duration: 0.72, ease: "easeOut" }}
        className="hero-cycling-slide"
      >
        <p className="eyebrow">{sub}</p>
        <h1 className="hero-title">{main[0]}<br />{main[1]}</h1>
      </motion.div>
    </AnimatePresence>
  );
}
```

- [ ] **Step 3: Update Home component hero section**

In `function Home({ user })`, add `const { t } = useT();` at the top, then replace:

```jsx
// hero description paragraph:
<p className="hero-city-description">{t("hero.desc")}</p>

// CTA buttons:
<NavLink to={!user ? "/auth" : hasPlan() ? "/planner" : "/pricing"} className="btn btn-primary hero-main-cta">
  {t("hero.cta.plan")} <ArrowRight size={18} />
</NavLink>
<button
  onClick={() => document.getElementById("experience-section")?.scrollIntoView({ behavior: "smooth" })}
  className="btn btn-glass hero-main-cta"
>
  {t("hero.cta.explore")}
</button>
```

- [ ] **Step 4: Update Home section eyebrows and titles**

Find and replace each hardcoded section header in `Home`:

```jsx
// Popular section (already conditional on user):
{user && <PopularRecommendations />}

// About section eyebrow/title:
<span className="section-eyebrow">{t("home.about.eyebrow")}</span>
<h2 className="section-title-large">{t("home.about.title")}</h2>

// How it works:
<span className="section-eyebrow">{t("home.how.eyebrow")}</span>
<h2 className="section-title-large">{t("home.how.title")}</h2>

// How it works CTA:
<NavLink to={!user ? "/auth" : hasPlan() ? "/planner" : "/pricing"} className="btn btn-primary inline-flex items-center gap-2">
  {t("home.how.cta")} <ArrowRight size={16} />
</NavLink>
```

- [ ] **Step 5: Update PopularRecommendations**

```jsx
function PopularRecommendations() {
  const { t } = useT();
  // ... existing state/effects ...

  if (loading) {
    return (
      <div className="py-16 text-center">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-cyan mx-auto"></div>
        <p className="text-sm text-stone-500 mt-2">{t("popular.loading")}</p>
      </div>
    );
  }

  // In the section header:
  <span className="section-eyebrow">{t("home.popular.eyebrow")}</span>
  <h2 className="section-title-large">{t("home.popular.title")}</h2>
  <p className="text-stone-600">{t("home.popular.sub")}</p>

  // select_count badge:
  🔥 {itinerary.select_count} {t("popular.select_count")}
```

- [ ] **Step 6: Commit**

```bash
git add src/main.jsx
git commit -m "feat: translate landing page hero, section headers, popular recommendations"
```

---

### Task 4: Translate Planner Form + Result Area

**Files:**
- Modify: `src/main.jsx` — `PlannerV2` (~line 3903)

- [ ] **Step 1: Add useT() + translate moodOptions**

At top of `PlannerV2`, add `const { t, isEn } = useT();`

Then replace the `moodOptions` array with translated labels/hints:

```js
const moodOptions = [
  { code: "chill",      label: "Chill",            hint: t("mood.chill.hint"),   icon: Coffee },
  { code: "date",       label: t("mood.date.label"),   hint: t("mood.date.hint"),    icon: Sparkles },
  { code: "group",      label: t("mood.group.label"),  hint: t("mood.group.hint"),   icon: Headphones },
  { code: "foodie",     label: "Foodie",           hint: t("mood.foodie.hint"),  icon: Utensils },
  { code: "nightlife",  label: "Nightlife",        hint: t("mood.nightlife.hint"), icon: Star },
  { code: "culture",    label: t("mood.culture.label"), hint: t("mood.culture.hint"), icon: BadgeCheck },
  { code: "checkin",    label: t("mood.checkin.label"), hint: t("mood.checkin.hint"), icon: Camera },
  { code: "hidden_gem", label: "Hidden Gem",       hint: t("mood.hidden_gem.hint"), icon: Gem },
  { code: "healing",    label: "Healing",          hint: t("mood.healing.hint"), icon: Compass },
  { code: "premium",    label: "Premium",          hint: t("mood.premium.hint"), icon: ShieldCheck },
  { code: "budget",     label: t("mood.budget.label"), hint: t("mood.budget.hint"), icon: Wallet },
  { code: "solo",       label: "Solo",             hint: t("mood.solo.hint"),    icon: Navigation },
];
```

- [ ] **Step 2: Translate budgetOptions, timeOptions, interestOptions**

```js
const budgetOptions = [
  { label: t("budget.save"),      value: 200000,  display: "150K - 200K" },
  { label: t("budget.mid"),       value: 500000,  display: "300K - 500K" },
  { label: t("budget.comfort"),   value: 800000,  display: "500K - 800K" },
  { label: t("budget.unlimited"), value: 1200000, display: "Premium" },
];

const timeOptions = [
  { label: t("time.morning"),   start: "08:30", end: "11:30", hint: t("time.morning.hint") },
  { label: t("time.afternoon"), start: "13:30", end: "17:30", hint: t("time.afternoon.hint") },
  { label: t("time.afterwork"), start: "18:30", end: "22:00", hint: t("time.afterwork.hint") },
  { label: t("time.night"),     start: "20:00", end: "23:30", hint: t("time.night.hint") },
  { label: t("time.halfday"),   start: "15:00", end: "22:00", hint: t("time.halfday.hint") },
];

const interestOptions = [
  { code: "checkin",       label: t("interest.checkin"),       icon: Camera },
  { code: "cafe_drink",    label: t("interest.cafe"),          icon: Coffee },
  { code: "food",          label: t("interest.food"),          icon: Utensils },
  { code: "culture",       label: t("interest.culture"),       icon: BadgeCheck },
  { code: "nightlife",     label: t("interest.nightlife"),     icon: Star },
  { code: "entertainment", label: t("interest.entertainment"), icon: Sparkles },
];
```

- [ ] **Step 3: Translate Planner form labels and the generate button**

Find each hardcoded label in the Planner form JSX and replace:

```jsx
// Field labels:
<span>{t("planner.mood.label")}</span>
<span>{t("planner.district.label")}</span>
<span>{t("planner.budget.label")}</span>
<span>{t("planner.time.label")}</span>
<span>{t("planner.interests.label")}</span>
<span>{t("planner.transport.label")}</span>

// Note field:
<span>{t("planner.note.label")}</span>
<small>{t("planner.note.small")}</small>
<textarea placeholder={t("planner.note.placeholder")} ... />

// Generate button:
{isGenerating ? t("planner.generating") : t("planner.btn.generate")}

// Basic plan remaining:
{t("planner.basic.remaining")
  .replace("{remaining}", monthlyLimit - freeUsageCount)
  .replace("{limit}", monthlyLimit)
  .replace("{days}", FREE_PERIOD_DAYS)}

// Premium plan unlimited:
{t("planner.unlimited").replace("{plan}", userPlan?.plan_name)}
```

- [ ] **Step 4: Translate limit-reached block and generating/result states**

```jsx
// Generating state:
<h4 className="font-bold text-[#1e4230] text-lg">{t("planner.loading.title")}</h4>

// Result title:
<h2 className="serif-h text-2xl text-[#1e4230]">{t("planner.result.title")}</h2>

// QR button:
<button ...>{t("planner.export.qr")}</button>

// Limit reached block:
<p className="font-semibold text-amber-700">{t("planner.limit.title")}</p>
<p className="text-amber-600 mt-1">
  {t("planner.limit.reset").replace("{days}", Math.max(1, Math.ceil((new Date(userPlan.period_reset_at) - Date.now()) / 86400000)))}
</p>
<p className="text-amber-500 text-xs mt-1">{t("planner.limit.upgrade")}</p>
<NavLink to="/pricing" className="btn btn-primary mt-3 w-full justify-center text-sm">
  {t("planner.limit.cta")} <ChevronRight size={14} />
</NavLink>
```

- [ ] **Step 5: Commit**

```bash
git add src/main.jsx
git commit -m "feat: translate Planner form options, labels, generating states"
```

---

### Task 5: Translate Itinerary Modal Header + QR Labels

**Files:**
- Modify: `src/main.jsx` — `JourneyTracker` itinerary modal (~line 3555)

- [ ] **Step 1: Add useT() to JourneyTracker**

At top of `function JourneyTracker(...)`, add:

```js
const { t } = useT();
```

- [ ] **Step 2: Replace hardcoded strings in modal header and body**

```jsx
// Header label:
<div style={{ fontSize: "9px", ... }}>{t("modal.header.label")}</div>

// Stop count line:
<div>{selectedStops.length} {t("modal.stops")} · {routeDuration} · {transport}</div>

// Driver banner:
<div>{t("modal.driver.confirmed")}</div>
<div>{t("modal.driver.fare")}</div>

// Trip detail label:
<div style={{ ... }}>{t("modal.trip.detail")}</div>

// QR labels:
<div>📱 {t("modal.qr.scan")} {itineraryId ? t("modal.qr.open") : t("modal.qr.view")}<br/>{t("modal.qr.label")}</div>
{itineraryId && (
  <button onClick={() => setShowQrCode(true)} ...>{t("modal.qr.expand")}</button>
)}
```

- [ ] **Step 3: Commit**

```bash
git add src/main.jsx
git commit -m "feat: translate itinerary modal header, driver banner, QR labels"
```

---

### Task 6: Add Local Tips Tab to Itinerary Modal

**Files:**
- Modify: `src/main.jsx` — itinerary modal in `JourneyTracker` (~line 3555)

- [ ] **Step 1: Add activeTab state to JourneyTracker**

```js
const [activeTab, setActiveTab] = useState("itinerary"); // "itinerary" | "tips"
```

- [ ] **Step 2: Add tab bar below the modal header (after the badge row)**

Insert after the closing `</div>` of the header badges row (~line 3582):

```jsx
{isEn && (
  <div style={{ display: "flex", borderBottom: "1px solid rgba(255,255,255,0.1)", marginTop: "8px" }}>
    {["itinerary", "tips"].map((tab) => (
      <button
        key={tab}
        onClick={() => setActiveTab(tab)}
        style={{
          flex: 1,
          padding: "10px 0",
          fontSize: "13px",
          fontWeight: "700",
          color: activeTab === tab ? "white" : "rgba(255,255,255,0.45)",
          background: "none",
          border: "none",
          borderBottom: activeTab === tab ? "2px solid #c96420" : "2px solid transparent",
          cursor: "pointer",
          transition: "all 0.2s",
          letterSpacing: "0.3px",
        }}
      >
        {tab === "itinerary" ? t("modal.tab.itinerary") : t("modal.tab.tips")}
      </button>
    ))}
  </div>
)}
```

Note: `isEn` must be destructured from `useT()` in Step 1 of Task 5.

- [ ] **Step 3: Wrap the stop list grid in a tab condition**

Find the `{/* Stop list — card grid */}` div (Task 5 result). Wrap it:

```jsx
{(!isEn || activeTab === "itinerary") && (
  <div style={{ padding: "22px" }}>
    {/* existing card grid */}
  </div>
)}
```

- [ ] **Step 4: Add the Local Tips tab panel below the stop list**

Insert after the stop list closing div:

```jsx
{isEn && activeTab === "tips" && (
  <div style={{ padding: "22px", display: "flex", flexDirection: "column", gap: "16px" }}>
    {selectedStops.map((stop, idx) => {
      const catCode = stop.category_code || "food";
      const phrase = LOCAL_PHRASES[catCode];
      return (
        <div key={stop.provider_id || idx} style={{ background: "white", borderRadius: "20px", overflow: "hidden", border: "1px solid #e8f0eb", boxShadow: "0 2px 10px rgba(30,66,48,0.06)" }}>
          {/* Stop header */}
          <div style={{ background: "linear-gradient(135deg, #1e4230, #2d5a3d)", padding: "14px 18px", display: "flex", alignItems: "center", gap: "10px" }}>
            <div style={{ width: "26px", height: "26px", borderRadius: "50%", background: "rgba(255,255,255,0.15)", color: "white", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: "800", fontSize: "12px", flexShrink: 0 }}>{idx + 1}</div>
            <div style={{ fontWeight: "800", fontSize: "15px", color: "white" }}>{stop.title}</div>
            {stop.category && (
              <div style={{ marginLeft: "auto", background: "rgba(255,255,255,0.15)", borderRadius: "12px", padding: "2px 10px", fontSize: "10px", fontWeight: "700", color: "rgba(255,255,255,0.85)", textTransform: "uppercase" }}>{stop.category}</div>
            )}
          </div>

          <div style={{ padding: "16px 18px", display: "flex", flexDirection: "column", gap: "12px" }}>
            {/* What it is */}
            {LOCAL_TIPS_BLURB[catCode] && (
              <div>
                <div style={{ fontSize: "10px", fontWeight: "700", color: "#c96420", textTransform: "uppercase", letterSpacing: "1px", marginBottom: "4px" }}>What it is</div>
                <div style={{ fontSize: "13px", color: "#4a6552", lineHeight: 1.6 }}>{LOCAL_TIPS_BLURB[catCode]}</div>
              </div>
            )}

            {/* Local customs */}
            {LOCAL_CUSTOMS[catCode] && (
              <div>
                <div style={{ fontSize: "10px", fontWeight: "700", color: "#2d5a3d", textTransform: "uppercase", letterSpacing: "1px", marginBottom: "4px" }}>Local Customs</div>
                <div style={{ fontSize: "13px", color: "#4a6552", lineHeight: 1.6 }}>💡 {LOCAL_CUSTOMS[catCode]}</div>
              </div>
            )}

            {/* Must try */}
            {(stop.must_try?.length > 0 || stop.cuisine) && (
              <div>
                <div style={{ fontSize: "10px", fontWeight: "700", color: "#7c3aed", textTransform: "uppercase", letterSpacing: "1px", marginBottom: "4px" }}>Must Try</div>
                <div style={{ fontSize: "13px", color: "#4a6552", lineHeight: 1.6 }}>
                  {stop.cuisine && <span>🍽️ {stop.cuisine}</span>}
                  {stop.must_try?.length > 0 && <span> · {stop.must_try.join(", ")}</span>}
                </div>
              </div>
            )}

            {/* Useful phrase */}
            {phrase && (
              <div style={{ background: "#f0f7f2", borderRadius: "12px", padding: "12px 14px" }}>
                <div style={{ fontSize: "10px", fontWeight: "700", color: "#2d5a3d", textTransform: "uppercase", letterSpacing: "1px", marginBottom: "8px" }}>Useful Phrase</div>
                <div style={{ fontSize: "14px", fontWeight: "700", color: "#1e4230", marginBottom: "2px" }}>"{phrase.vi}"</div>
                <div style={{ fontSize: "12px", color: "#7aaa8e", fontStyle: "italic", marginBottom: "4px" }}>/{phrase.roman}/</div>
                <div style={{ fontSize: "12px", color: "#555", fontWeight: "600" }}>{phrase.en}</div>
              </div>
            )}
          </div>
        </div>
      );
    })}
  </div>
)}
```

- [ ] **Step 5: Commit**

```bash
git add src/main.jsx
git commit -m "feat: add Local Tips tab to itinerary modal for International plan users"
```

---

### Task 7: Translate HistoryPage

**Files:**
- Modify: `src/main.jsx` — `HistoryPage` (~line 5117)

- [ ] **Step 1: Add useT() and replace all strings**

At top of `function HistoryPage({ user })`, add `const { t } = useT();`

Then replace:

```jsx
// Page shell:
<PageShell eyebrow={t("history.eyebrow")} title={t("history.title")}>

// Loading:
<p className="text-stone-500 mt-4">{t("history.loading")}</p>

// Error:
<div className="text-center py-20 text-red-500">{t("history.error")}</div>

// Empty state:
<h3 className="text-xl font-semibold text-[#1e4230] mb-2">{t("history.empty.title")}</h3>
<p className="text-stone-500 mb-6">{t("history.empty.sub")}</p>
<NavLink to="/planner" className="btn btn-primary">{t("history.empty.cta")}</NavLink>

// Detail label:
<h4 className="text-xs font-bold text-[#1e4230] uppercase tracking-wider mb-3">{t("history.detail.label")}</h4>

// View button:
<MapPin size={16} /> {t("history.btn.view")}

// Not logged in:
<h3 className="text-xl font-semibold text-[#1e4230] mb-2">{t("history.noauth.title")}</h3>
<p className="text-stone-500 mb-6">{t("history.noauth.sub")}</p>
<NavLink to="/auth" className="btn btn-primary">{t("history.noauth.cta")}</NavLink>
```

- [ ] **Step 2: Commit**

```bash
git add src/main.jsx
git commit -m "feat: translate HistoryPage via useT()"
```

---

### Task 8: Push to GitHub

- [ ] **Step 1: Push all commits**

```bash
git push fe main
```

Expected output:
```
To https://github.com/Thuongmaidientu416/FE.git
   <hash>..<hash>  main -> main
```
