# International Plan — English UI + Local Tips Tab

**Date:** 2026-06-30  
**Status:** Approved

---

## Goal

When a logged-in user holds the **International Tourist** plan (`plan_key === "international"`), the entire app switches to 100% English automatically. A **Local Tips** tab is added to the itinerary modal in the Planner, giving cultural context per stop in English.

---

## Architecture

### Language Context

A `LangContext` wraps the entire app at root level. The value is derived from `userPlan` and updates automatically when the user logs in or logs out.

```js
const LangContext = React.createContext("vi");

// In App root:
<LangContext.Provider value={userPlan?.plan_key === "international" ? "en" : "vi"}>
  {/* entire app */}
</LangContext.Provider>
```

### useT() Hook

```js
function useT() {
  const lang = useContext(LangContext);
  const isEn = lang === "en";
  const t = (key) => TRANSLATIONS[lang]?.[key] ?? TRANSLATIONS["vi"][key] ?? key;
  return { t, isEn, lang };
}
```

- `t("key")` returns English or Vietnamese string based on active plan
- Falls back to Vietnamese if a key is missing from the EN dictionary
- `isEn` boolean for conditional logic beyond text (e.g., showing/hiding components)

### TRANSLATIONS Object

A flat object at the top of `main.jsx` containing all UI strings in both languages. Grouped by section for readability:

```js
const TRANSLATIONS = {
  vi: { "nav.home": "Trang chủ", ... },
  en: { "nav.home": "Home", ... },
}
```

No external library. No separate file. All in `main.jsx`.

---

## Translation Coverage

### Translated
| Section | Examples |
|---|---|
| Navbar | Trang chủ → Home, Khám phá → Explore, Về WanderHUB → About, Đánh giá → Reviews, Liên hệ → Contact, Đăng nhập → Sign In, Đăng xuất → Sign Out, Bắt đầu lên lịch trình → Start Planning |
| Landing page | Hero title/subtitle, section eyebrows, CTAs, testimonial section headers, how-it-works steps |
| Planner | All labels (mood, district, transport, time), button text, status messages, driver booking flow |
| Itinerary modal | Chi tiết hành trình → Trip Details, header badges, QR label, footer actions |
| History page | Page title, empty state, card metadata labels, button |
| Pricing page | Section title, plan names (keep "International Tourist"), feature labels, CTA buttons |
| Common UI | Loading states, error messages, empty states, toast notifications |

### NOT Translated
- Proper nouns: venue names (SOBO Coffee, Araham, Hana Sinh Tố, etc.)
- Geographic names: Quận 1, Bình Thạnh, TP.HCM — kept as-is
- Currency: VNĐ format stays unchanged
- Admin panel: internal tool, Vietnamese-only is fine

---

## Local Tips Tab

### Trigger
Only renders when `isEn === true` (International plan active) AND the itinerary modal is open with stops loaded.

### Tab Bar
Added below the itinerary modal header, above the content area:

```
[ Itinerary ]  [ Local Tips ]
```

Active tab underlined with accent color. Default tab is "Itinerary".

### Local Tips Card (per stop)

Each stop renders one card with four sections:

| Section | Content | Source |
|---|---|---|
| **What it is** | 1-sentence English description of the venue type | `LOCAL_TIPS_BLURB[category_code]` lookup table |
| **Local customs** | Cultural tip relevant to the category | `LOCAL_CUSTOMS[category_code]` lookup table |
| **Must try** | Items to order/experience | `stop.must_try` array (existing data) or `stop.cuisine` |
| **Useful phrase** | 1 Vietnamese phrase + romanization + English translation | `LOCAL_PHRASES[category_code]` lookup table |

### Lookup Tables (static, defined in main.jsx)

```js
const LOCAL_TIPS_BLURB = {
  cafe: "A Vietnamese café — expect strong drip coffee, condensed milk, and a relaxed vibe.",
  restaurant: "A local eatery serving authentic Vietnamese cuisine.",
  landmark: "A historic or cultural landmark — great for photos and learning local history.",
  // ...
}

const LOCAL_CUSTOMS = {
  cafe: "Motorbikes often park on the sidewalk outside. Join them — it's normal here.",
  restaurant: "Point at the menu if unsure. Most places are used to tourists.",
  landmark: "Dress modestly if entering temples or government buildings.",
  // ...
}

const LOCAL_PHRASES = {
  cafe: { vi: "Cho tôi một ly cà phê sữa đá", roman: "Cho toy mot lee ca phe sua da", en: "One iced milk coffee, please" },
  restaurant: { vi: "Cho tôi xem thực đơn", roman: "Cho toy xem thuc don", en: "Can I see the menu?" },
  // ...
}
```

---

## Auto-Detection Logic

```
User logs in
  └── apiGetMyPlan() resolves → sets userPlan
       └── LangContext re-renders with "en" or "vi"
            └── entire app re-renders in correct language

User logs out
  └── userPlan = null → LangContext value = "vi"
       └── app reverts to Vietnamese
```

No localStorage persistence — language follows the active session plan only.

---

## Scope Boundaries

- No route changes or URL locale prefix (`/en/...`) — not needed for this use case
- No user-toggleable language switch — it's purely plan-driven
- Free and Premium users always see Vietnamese
- Local Tips tab is invisible to Free/Premium users; no dead code rendered
