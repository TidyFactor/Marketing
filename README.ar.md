<div align="center" dir="rtl">

# 🚀 محرك تايدي فاكتور للتسويق المباشر والنمو `TidyFactor Marketing v1.3.0`
### هندسة التسويق المباشر، طبقة القرارات السياقية (CDL)، ونظام كتابة المحتوى عالي التحويل

**الأساس التسويقي الرسمي لمنظومة تايدي فاكتور (TidyFactor Ecosystem) والشريك الاستراتيجي وكالة الوكالة (Alwkala).**

[![npm version](https://img.shields.io/npm/v/@tidyfactor/marketing.svg?style=for-the-badge&color=4F46E5&logo=npm)](https://www.npmjs.com/package/@tidyfactor/marketing)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=for-the-badge)](LICENSE)
[![Ecosystem](https://img.shields.io/badge/TidyFactor-Skills--LAB-purple.svg?style=for-the-badge)](https://github.com/TidyFactor)
[![Compatibility](https://img.shields.io/badge/Agents-Antigravity%20|%20Claude%20|%20Cursor%20|%20Codex-orange.svg?style=for-the-badge)](SKILL.md)
[![CDL Layer](https://img.shields.io/badge/CDL-طبقة%20القرارات%20السياقية-purple.svg?style=for-the-badge)](#-طبقة-القرارات-السياقية-cdl)
[![RTL Ready](https://img.shields.io/badge/RTL-Native%20Arabic-emerald.svg?style=for-the-badge)](README.ar.md)
[![Architect Score](https://img.shields.io/badge/Architect%20Score-13%2F13%20Pass%20(100%25)-green.svg?style=for-the-badge)](#-معايير-الحوكمة-والجودة)
[![AI Agents Compatible](https://img.shields.io/badge/AI%20Agents-Universal%20Compatibility-4285F4.svg?style=for-the-badge)](SKILL.md)

[ English ](README.md) • [ العربية ](README.ar.md) • [ فارسی ](README.fa.md) • [ Español ](README.es.md) • [ Português ](README.pt.md) • [ 简体中文 ](README.zh.md) • [ Deutsch ](README.de.md) • [ Français ](README.fr.md)

<br/><br/>

<p align="center">
  <img src="assets/hero-banner.png" alt="TidyFactor Marketing Hero Banner" width="100%" />
</p>

</div>

---

> [!NOTE]
> **TidyFactor Marketing** هو المحرك الرسمي للاستجابة المباشرة وهندسة النمو ضمن **TidyFactor Ecosystem**. يُزوّد وكلاء الذكاء الاصطناعي البرمجيين (Google Antigravity, Claude Code, Cursor, Windsurf) ومديري النمو والمسوقين بأدلة عمل تنفيذية مبنية على البيانات والأرقام عبر كافة مراحل الاستحواذ، والاحتفاظ، والتسعير.

---

<div dir="rtl">

## 🌟 نظرة عامة والقيمة المضافة

| لمؤسسي المشاريع والمسوقين | لقادة المنتجات والنمو | لوكلاء الذكاء الاصطناعي (AI Agents) |
|---|---|---|
| **خالٍ من العبارات الإنشائية**: حظر النصائح العامة ("انشر محتوى مميز"). كل مخرج يمنحك أرقاماً، زوايا نفسية، وخطط تنفيذ زمنية دقيقة. | **حماية هوامش الربح والتسعير**: حاسبات مدمجة لحماية الهوامش ومنع الخصومات المدمرة، وهندسة باقات (Good/Better/Best). | **توجيه موفر للتوكنز (Token-Efficient)**: استدعاء ملف مسار العمل والذاكرة المطلوب فقط (~400 توكن) لكل مهمة عبر Slash Commands. |
| **لغة عربية تسويقية أصيلة**: نصوص مباشرة بالفصحى المعاصرة الرنانة متوافقة ثقافياً مع الأسواق الخليجية والعربية والعالمية. | **تغطية شاملة للقمع التسويقي**: من خطط إطلاق المنتجات ($T-30$)، والإعلانات، وسيو المقالات، واستعادة السلات، وسلاسل الـ Win-Back. | **قوائم تحقق إلزامية**: إنهاء كل مسار عمل بقائمة فحص جودة صارمة تضمن مخرجات عملية وقابلة للقياس فوراً. |
| **إتقان أسواق الشرق الأوسط**: مصفوفة ترتيب المنصات لكل دولة وتأثير بوابات الدفع (مدى، تمارا، تابى، إنستاباي) على رفع المبيعات. | **تجارب نمو علمية**: ترتيب أولويات التجارب باستخدام معادلة **ICE Scoring** الفرضية ($\text{Impact} \times \text{Confidence} \times \text{Ease}$). | **مخرجات حتمية ومنضبطة**: امتثال كامل بنسبة 100% لمعايير الحوكمة عبر 7 أوامر و7 مسارات عمل و7 ملفات ذاكرة تشغيلية. |

---

## 🏛️ المعمارية الهيكلية للمنظومة

```
tidyfactor-marketing/
├── .tidyfactor                        ← بيان تكامل المنظومة (Ecosystem JSON Manifest)
├── brand.json                         ← رموز الهوية ونبرة الصوت (Schema v2)
├── AGENTS.md                          ← قواعد بيئة العمل وتوجيه الوكلاء
├── SKILL.md                           ← الموجه المركزي لجميع الأوامر (28 قدرة)
├── SKILL-REGISTRY.md                  ← سجل الهوية الموحدة وأوامر الـ CLI
├── VISION.md                          ← الرؤية العامة المرتبطة بـ TidyFactor
├── CHANGELOG.md                       ← سجل التحديثات والإصدارات الدلالي (v1.2.0)
├── requirements.txt                   ← مكتبات بايثون لتحليل الكلمات والبيانات
├── package.json                       ← إعدادات حزمة NPM (@tidyfactor/marketing)
├── README.md & README.ar.md           ← التوثيق المزدوج (عربي وإنجليزي)
├── bin/                               ← أدوات سطر الأوامر (create-kit.js, add-skill.js)
├── references/
│   ├── commands/                      ← 7 ملفات توجيه أوامر دقيقة
│   ├── workflows/                     ← 7 مسارات عمل مع قوائم تحقق إلزامية
│   └── memory/                        ← 7 ملفات ذاكرة تشغيلية (أرقام، قوالب، معادلات)
├── .claude-skill/                     ← غلاف Claude Code و Cursor
└── .agents/skills/tidyfactor-marketing/ ← غلاف Google Antigravity و Windsurf
```

---

## 🧠 طبقة القرارات السياقية (CDL v1.0) وأمر `/brief`

لمنع توليد حملات تسويقية عشوائية أو غير متطابقة مع نبرة العلامة وسياق السوق، تطبق المهارة **طبقة القرارات السياقية**:

1. **حوار الاستكشاف القبلي (`/brief`)**: إدارة حوار استكشافي من 3 أسئلة مركّزة وتخزين اختيارات المشروع في `.tidyfactor/marketing-brief.md`.
2. **شروط التخطي المنطقية الحتمية**: التخطي الفوري للأسئلة في حال توفر الـ Brief مسبقاً، أو تحديد المعايير في الطلب، أو الاستدعاء المباشر للأوامر.
3. **التجميع الأحادي وتراتبية الأولويات**: حصر الأسئلة المتبقية في جولة واحدة بحد أقصى 3 أسئلة وفق الأولوية:
   $$\mathbf{M1 \text{ (السوق/المنطقة)}} > \mathbf{M2 \text{ (نبرة الصوت)}} > \mathbf{M3 \text{ (مرحلة القمع)}} > \mathbf{M4 \text{ (العرض)}} > \mathbf{M5 \text{ (العمق)}}$$
4. **النقد الذاتي القبلي سباعي المحاور (`P/H/E/S/R/V/D`)**:
   `/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */`
   - **P (تحديد الألم بدقة)**: معالجة مشكلة حقيقية دون حشو إنشائي (1-5).
   - **H (قوة الهوك الافتتاحي)**: خطاف جاذب بصرياً ولفظياً في أول 3 ثوانٍ (1-5).
   - **E (اكتمال التنفيذ)**: تسليم نصوص كاملة مع أزرار الإجراء ومحفزات الثقة (1-5).
   - **S (ملاءمة السوق والمرحلة)**: التوافق مع درجات الوعي واللهجة الإقليمية (1-5).
   - **R (حماية الهوامش والعلامة)**: حماية هوامش الربح من الخصم العشوائي (1-5).
   - **V (أصالة الصوت ومنع الكليشيهات)**: خلو تام من عبارات الذكاء الاصطناعي المبتذلة (1-5).
   - **D (مطابقة قرارات الـ Brief)**: التزام صارم بالخيارات المعتمدة (1-5).

---

## ⚡ سجل الأوامر والركائز التسويقية الـ 8 والـ 28 قدرة

| الركيزة | القدرة التسويقية | أمر الاستدعاء | الكلمات المفتاحية المحفزة | ما يتم تحميله | المخرج النهائي |
|---|---|---|---|---|---|
| **1. الاستراتيجية** | **صوت وتموضع العلامة** | `/marketing strategy` | "brand voice", "positioning", "هوية العلامة" | `campaign-launch.md` + `frameworks.md` | معادلة التموضع الصارمة، ركائز الصوت عبر التضاد، مرونة النبرة، والميزة التنافسية |
| **1. الاستراتيجية** | **استراتيجية الحملات** | `/marketing strategy` | "campaign strategy", "marketing plan", "خطة تسويق" | `campaign-launch.md` + `metrics-benchmarks.md` | خطة تسويقية متعددة القنوات، تقسيم الجماهير، توزيع الميزانيات، ومؤشرات الأداء |
| **1. الاستراتيجية** | **خطة إطلاق المنتجات** | `/marketing strategy` | "product launch", "launch plan", "إطلاق منتج" | `campaign-launch.md` + `frameworks.md` | جدول زمني مرحلي (الإحماء $T-30$، الإطلاق $T-0$، والاستدامة $T+14$) وقمع قائمة الانتظار |
| **2. المحتوى والسيو** | **منشورات السوشيال ميديا** | `/marketing content` | "social media content", "write posts", "محتوى سوشيال" | `content-engine.md` + `platform-specs.md` | 10+ منشورات تفاعلية بخطافات الثواني الثلاث الأولى وإيقاع بصري ودعوات CTA واضحة |
| **2. المحتوى والسيو** | **استراتيجية السيو (Pillar)** | `/marketing content` | "seo strategy", "keyword clustering", "استراتيجية السيو" | `content-engine.md` + `frameworks.md` | خريطة نية البحث الثلاثية، هيكل الدليل الرئيسي (3000 كلمة)، وخطة 5 مقالات عنقودية |
| **2. المحتوى والسيو** | **جدول النشر الشهري** | `/marketing content` | "content calendar", "publishing schedule", "جدول نشر" | `content-engine.md` + `platform-specs.md` | جدول 30 يوماً متوازن بين الأعمدة الأربعة وتنسيقات الفيديو والتصاميم |
| **2. المحتوى والسيو** | **النشرات البريدية** | `/marketing content` | "newsletter strategy", "email newsletter", "نشرة بريدية" | `content-engine.md` + `frameworks.md` | هيكل نشرة بريدية عالية الفتح مع 3 عناوين للاختبار وصياغة Hook-Story-Offer |
| **3. السوشيال ولينكد إن** | **تسويق B2B ولينكد إن** | `/marketing social` | "linkedin b2b", "founder personal brand", "لينكد إن" | `social-growth.md` + `platform-specs.md` | استراتيجية الحساب الشخصي للمؤسس، أعمدة المحتوى الـ 4، وآداب رسائل InMail الثلاثية |
| **3. السوشيال ولينكد إن** | **استراتيجية إنستغرام** | `/marketing social` | "instagram strategy", "reels hooks", "إنستغرام" | `social-growth.md` + `platform-specs.md` | صياغة البايو التحويلي، الهايلايت الثلاثية، 5 سيناريوهات ريلز، وتسلسل الستوري |
| **3. السوشيال ولينكد إن** | **خطافات تيك توك** | `/marketing social` | "tiktok strategy", "short form video", "تيك توك" | `social-growth.md` + `platform-specs.md` | 5 سيناريوهات فيديو قصير مع توجيهات الخطاف البصري والكلامي (0-3 ثوانٍ) |
| **3. السوشيال ولينكد إن** | **تدقيق الحسابات** | `/marketing social` | "social media audit", "profile teardown", "تدقيق حساب" | `social-growth.md` + `metrics-benchmarks.md` | تشخيص شامل للبروفايل، احتساب معدل التفاعل، اكتشاف تسرب المتابعين، وخطة معالجة |
| **3. السوشيال ولينكد إن** | **أول 1,000 متابع** | `/marketing social` | "first 1000 followers", "grow from zero", "أول 1000 متابع" | `social-growth.md` + `platform-specs.md` | استراتيجية التفاعل اليومي ($1.80)، التعاون المشترك مع الأقران، وتنسيقات الانتشار |
| **3. السوشيال ولينكد إن** | **استراتيجية الهاشتاجات** | `/marketing social` | "hashtag strategy", "hashtags", "هاشتاجات" | `social-growth.md` + `platform-specs.md` | كتلة الهاشتاج الثلاثية (2 عامة + 4 تخصصية + 2 براند) وقواعد خوارزميات البحث |
| **4. البريد الإلكتروني** | **تنمية القائمة البريدية** | `/marketing email` | "grow email list", "lead magnet", "قائمة بريدية" | `email-lifecycle.md` + `frameworks.md` | هندسة مغناطيس العملاء السريع (< 10 دقائق)، نصوص نماذج الاشتراك، ونوافذ الخروج |
| **4. البريد الإلكتروني** | **السلسلة الترحيبية** | `/marketing email` | "welcome sequence", "onboarding drip", "رسائل ترحيبية" | `email-lifecycle.md` + `lifecycle-flows.md` | سلسلة من 5 رسائل (التسليم، قصة المؤسس، كسر الخرافات، دراسة الحالة، والعرض الحاسم) |
| **4. البريد الإلكتروني** | **استعادة السلات المتروكة** | `/marketing email` | "abandoned cart", "recover carts", "سلات متروكة" | `email-lifecycle.md` + `lifecycle-flows.md` | مسار من 3 مراحل (ساعة: دعم ومساعدة، 24 ساعة: آراء وضمانات، 48 ساعة: خصم ينتهي) |
| **4. البريد الإلكتروني** | **سلاسل الاستعادة (Win-Back)**| `/marketing email` | "win-back flow", "re-engagement", "استعادة العملاء" | `email-lifecycle.md` + `lifecycle-flows.md` | رسائل محددة زمنياً (30 يوماً: تحديثات، 60 يوماً: رصيد 20$، 90 يوماً: إذن إنهاء الحساب) |
| **5. الإعلانات والـ CRO** | **كتابة الإعلانات المباشرة** | `/marketing ads` | "write ad copy", "meta ad copy", "كتابة إعلانات" | `paid-acquisition.md` + `ad-copy-templates.md` | 3 زوايا نفسية متباينة (تجنب الخسارة، المنطق/العائد، المكانة)، و15 عنواناً لإعلانات جوجل |
| **5. الإعلانات والـ CRO** | **صفحات الهبوط وتدقيق CRO** | `/marketing ads` | "landing page strategy", "cro audit", "صفحة هبوط" | `paid-acquisition.md` + `metrics-benchmarks.md` | هيكل أقسام الصفحة الـ 8، اختبار وضوح القيمة في 5 ثوانٍ، وأزرار الدفع السريع بالجوال |
| **5. الإعلانات والـ CRO** | **حملات إعلانات Meta** | `/marketing ads` | "facebook ads", "meta ads plan", "إعلانات فيسبوك" | `paid-acquisition.md` + `metrics-benchmarks.md` | هيكلية Advantage+ مقابل ABO، ميزانية اختبار الإبداعات (20-50$/يوم)، وقواعد التوسع |
| **5. الإعلانات والـ CRO** | **خطة إعلانات جوجل** | `/marketing ads` | "google ads plan", "search ads", "إعلانات جوجل" | `paid-acquisition.md` + `ad-copy-templates.md` | مصفوفة 15 عنواناً و 4 أوصاف لإعلانات RSA، ومطابقة نية البحث، والكلمات السلبية |
| **5. الإعلانات والـ CRO** | **أول حملة إعلانية تجريبية** | `/marketing ads` | "first ad campaign", "test budget", "أول حملة إعلانية" | `paid-acquisition.md` + `metrics-benchmarks.md` | إطلاق منخفض المخاطر (10-20$/يوم)، التحقق من البكسل و CAPI، وضوابط وقف الخسارة |
| **6. العروض والتسعير** | **العروض الخاطفة (Flash Sale)**| `/marketing promo` | "plan a sale", "flash sale", "عروض وتخفيضات" | `promo-conversion.md` + `promotions-math.md` | جدول زمني لـ 72 ساعة (إطلاق VIP مبكر، إثبات اجتماعي، وإغلاق حاسم مع مؤقت تنازلي) |
| **6. العروض والتسعير** | **المسابقات الفيروسية** | `/marketing promo` | "giveaway", "contest", "مسابقة" | `promo-conversion.md` + `promotions-math.md` | شروط الجائزة المخصصة للجمهور المثالي، نقاط الإحالة الفيروسية، وقسيمة الترضية |
| **6. العروض والتسعير** | **هندسة التسعير والخيار الطعم**| `/marketing promo` | "pricing strategy", "pricing tiers", "تسعير وباقات" | `promo-conversion.md` + `frameworks.md` | جدول باقات (Good/Better/Best)، تثبيت الباقة المستهدفة بالـ Decoy Effect، والخصم السنوي |
| **6. العروض والتسعير** | **حماية هوامش الربح** | `/marketing promo` | "coupon strategy", "discount math", "كوبونات خصم" | `promo-conversion.md` + `promotions-math.md` | احتساب زيادة المبيعات المطلوبة لتعويض الخصم، عتبات رفع السلة ("أنفق 100$ واحصل على 15$") |
| **7. الاستبقاء والنمو** | **تشخيص الارتداد والاحتفاظ** | `/marketing growth` | "customer retention", "reduce churn", "تقليل الارتداد" | `viral-retention.md` + `lifecycle-flows.md` | تشخيص نقاط التسرب (تأهيل الـ SaaS، أو الشراء الثاني بالمتجر)، ورسائل الاطمئنان الذكية |
| **7. الاستبقاء والنمو** | **تصميم برامج الولاء** | `/marketing growth` | "loyalty program", "rewards program", "برنامج ولاء" | `viral-retention.md` + `metrics-benchmarks.md` | اختيار النموذج (نقاط للتجزئة، مستويات للـ VIP، امتيازات للـ SaaS)، ومتابعة المشاركة |
| **7. الاستبقاء والنمو** | **برامج الإحالة ذات الاتجاهين** | `/marketing growth` | "referral program", "viral loop", "برنامج إحالة" | `viral-retention.md` + `metrics-benchmarks.md` | حوافز (امنح X واحصل على Y)، نقاط تحفيز ما بعد الشراء والـ NPS، وتدرج المكافآت |
| **7. الاستبقاء والنمو** | **التسويق عبر المؤثرين** | `/marketing growth` | "influencer outreach", "influencers", "تسويق المؤثرين" | `viral-retention.md` + `metrics-benchmarks.md` | بطاقة فحص الحسابات (تفاعل > 3%)، رسائل التواصل المباشرة، وتتبع روابط الـ UTM |
| **7. الاستبقاء والنمو** | **محرك الانتشار وبناء الوعي**| `/marketing growth` | "brand awareness", "pr outreach", "انتشار العلامة" | `viral-retention.md` + `frameworks.md` | زوايا الظهور في البودكاست، الشراكات الترويجية المتبادلة، وإعادة تدوير المحتوى (1 إلى 9) |

---

## 🧠 النماذج العقلية النفسية الـ 12 في الإقناع

تُطبق منظومة TidyFactor Marketing العلوم السلوكية في كل صياغة إعلانية أو هيكل تسعير:

| # | النموذج العقلي | الآلية السلوكية | التطبيق العملي في المنظومة |
|---|---|---|---|
| **1** | **الإرساء السعري (Anchoring)** | اتخاذ القرارات بناءً على أول رقم تراه العين. | إظهار السعر الأصلي مشطوباً قبل عرض السعر الفعلي للباقة. |
| **2** | **تأثير الخيار الطعم (Decoy Effect)** | إضافة خيار ثالث غير متوازن يجعل الباقة المستهدفة تبدو الأفضل. | تصميم باقة Pro في المنتصف بفارق بسيط عن الباقة الأساسية لتوجيه 80% من المبيعات لها. |
| **3** | **تجنب الخسارة (Loss Aversion)** | ألم خسارة 100$ يعادل ضعف متعة كسب 100$. | التركيز على تكلفة عدم اتخاذ القرار، وإهدار الميزانية الإعلانية، ونهاية العرض. |
| **4** | **تكديس الإثبات الاجتماعي (Social Proof)** | ميل البشر لتقليد سلوك الأقران قبل الدفع. | دمج أعداد العملاء ("10,000+ فريق") مع تقييمات المنصات ودراسات الحالة بالفيديو. |
| **5** | **تأثير زايجارنيك (Zeigarnik Effect)** | العقل يتذكر المهام غير المكتملة ويسعى لإنهائها. | وضع شريط تقدم يبدأ من 50% في نماذج التسجيل والشراء متعددة الخطوات. |
| **6** | **تسارع الاقتراب من الهدف (Goal Gradient)** | تضاعف الحماس كلما شعر العميل بقربه من خط النهاية. | صياغة عبارات: "أنت على بعد خطوة واحدة فقط من تقرير تدقيقك المخصص". |
| **7** | **مفارقة كثرة الخيارات (Paradox of Choice)**| الخيارات الزائدة تسبب شللاً في القرار وانعدام الشراء. | إلزام الصفحة بـ CTA رئيسي واحد في الجزء العلوي، و 3 باقات تسعير واضحة كحد أقصى. |
| **8** | **تأثير التأطير (Framing Effect)** | طريقة عرض المعلومة تحدد قيمتها في ذهن العميل. | إعادة تأطير العرض: "وفّر 1,200$ سنوياً" تحقق تحويلاً أعلى من "خصم 100$/شهرياً". |
| **9** | **الندرة والإلحاح (Scarcity & Urgency)** | ارتفاع القيمة النفسية للشيء عند قلة توفره أو ضيق وقته. | استخدام مؤقتات عد تنازلي لـ 72 ساعة، ومقاعد محدودة فعلياً، وحجز السلة المؤقت. |
| **10** | **فخ التكلفة الغارقة (Sunk Cost Fallacy)** | زيادة التزام العميل بعد بذل مجهود أولي صغير. | استخدام حاسبات واختبارات تفاعلية قبل طلب البريد أو وسيلة الدفع. |
| **11** | **تأثير الهالة (Halo Effect)** | الانطباع الإيجابي في جانب ينعكس على المنظومة ككل. | إبراز الظهور الإعلامي في الصحف المرموقة وشهادات الأمان والاعتماد في واجهة الصفحة. |
| **12** | **تأثير التملك النفسي (Endowment Effect)**| تقدير العميل للمنتج يتضاعف بمجرد شعوره بتجربته. | إتاحة النسخ التجريبية التفاعلية الفورية (Sandboxes) أو تجربة مجانية لـ 14 يوماً. |

---

## 🌍 ذكاء أسواق الشرق الأوسط وبوابات الدفع الإقليمية

معايير تشغيلية مدمجة مخصصة لدول الخليج وشمال أفريقيا:

```
├── 🇸🇦 المملكة العربية السعودية (KSA) ── الأولوية: سناب شات → X → تيك توك → إنستغرام → يوتيوب
│     ├── بوابات الدفع الحيوية: مدى (رفع التحويل بنسبة +35-50%)، تمارا، تابى (+25-40% لمتوسط السلة)، أبل باي
│     └── المحددات الثقافية: قوة شرائية عالية، محتوى مرئي سريع بالجوال، احترام اللهجة المحلية والفصحى المعاصرة
│
├── 🇦🇪 الإمارات العربية المتحدة (UAE) ── الأولوية: إنستغرام → لينكد إن (B2B) → تيك توك → يوتيوب
│     ├── بوابات الدفع: أبل باي، سترايب، تابى، تمارا
│     └── المحددات: تنوع عالمي للمقيمين والمواطنين، إلزامية الازدواج اللغوي (عربي / إنجليزي) بأعلى جودة
│
├── 🇪🇬 جمهورية مصر العربية ── الأولوية: فيسبوك (المسيطر على B2C و B2B) → واتساب → يوتيوب → تيك توك
│     ├── بوابات الدفع: إنستاباي (InstaPay)، فوري (استعادة +40% من السلات)، ميزة، فودافون كاش، فاليو
│     └── المحددات: ثقافة الإغلاق عبر الواتساب، حساسية عالية للعائد على الاستثمار، طلب براهين سنوات الخبرة
│
├── 🇰🇼 دولة الكويت ── الأولوية: إنستغرام → سناب شات → تيك توك → واتساب
│     ├── بوابات الدفع: كي نت (KNET - ضرورة مطلقة)، أبل باي، تمارا، تابى
│     └── المحددات: أعلى متوسط قيمة سلة (AOV)، وتفضيل خدمة العملاء الراقية والخاصة
│
└── 🇶🇦 قطر، 🇯🇴 الأردن، 🇲🇦 المغرب ── مصفوفات دفع مخصصة وبراهين ثقة محلية
```

---

## 🛡️ ميثاق منع الكليشيهات وضبط الجودة

تلتزم المنظومة بـ **قاعدة استبدال الصفة بالآلية (Mechanism Replacement Rule)**:
> *إذا كانت الجملة التسويقية تحتوي على صفة تفضيلية عامة لا تحمل رقماً، أو آلية تقنية، أو دليلاً قابلاً للإثبات، فيتم حظرها واستبدالها فوراً.*

### جدول العبارات المحظورة والبدائل الإلزامية:

| العبارة المحظورة (بالعربية) | البديل الإلزامي بالآلية والأرقام |
|---|---|
| ❌ *"نسعى دائماً لتقديم الأفضل / نحرص على التميز"* | ✅ اذكر الإجراء الفعلي: `"نختبر سرعة التحميل وتوافق الجوال قبل إطلاق أي صفحة"` |
| ❌ *"فريق من الخبراء المتخصصين"* | ✅ اذكر سابقة الأعمال بالأرقام: `"أكثر من 8 سنوات من إدارة حملات الـ B2B في الخليج"` |
| ❌ *"حلول متكاملة ومبتكرة"* | ✅ اذكر الميزة التقنية: `"منظومة ربط إلكتروني متكاملة مع بوابات مدى وتمارا"` |
| ❌ *"في عالمنا الرقمي المتسارع"* | ✅ احذف المقدمة الإنشائية وابدأ فوراً بالمشكلة والحل المباشر |
| ❌ *"الجودة هي شعارنا"* | ✅ اذكر الضمان الصريح: `"ضمان استرداد كامل للأموال خلال 30 يوماً بدون أي شروط"` |

---

## 🚀 التثبيت والبدء السريع

اختر طريقة التثبيت المناسبة لمشروعك:

### الخيار (أ): عبر TidyFactor CLI الرسمي (الموصى به)
التثبيت الفوري دون الحاجة لتثبيت الأداة عالمياً في بيئة عملك النشطة:
```bash
npx @tidyfactor/cli add marketing
```
*أو في حال كانت الأداة مثبتة لديك عالمياً (`npm i -g @tidyfactor/cli`):*
```bash
tidyfactor add marketing
```

### الخيار (ب): عبر معيار مهارات الوكلاء المفتوح (skills.sh)
التثبيت العالمي المتوافق مع كافة بيئات الوكلاء ومحررات الذكاء الاصطناعي (Antigravity, Cursor, Claude Code, Windsurf, Codex):
```bash
npx skills add tidyfactor/marketing
```

### الخيار (ج): التثبيت المباشر الفردي عبر NPM
تشغيل مثبت المهارة المستقل مباشرة مع تجاوز الذاكرة المخبأة وضمان أحدث إصدار:
```bash
npx @tidyfactor/marketing@latest
```

### الخيار 3: أوامر Slash للوكلاء الأذكياء (Claude, Antigravity, Cursor)
استدعِ مسارات العمل التسويقية مباشرة داخل محادثة الوكيل:
```markdown
/marketing strategy  "خطط لإطلاق مرحلي لمنظومة SaaS جديدة في السوق السعودي"
/marketing ads       "اكتب 3 زوايا إعلانية متباينة لإعلانات Meta لمنتج مكتبي مريح"
/marketing email     "اكتب سلسلة رسائل ترحيبية من 5 رسائل لنشرتنا البريدية للمطورين"
/marketing promo     "صمم عرضاً خاطفاً لـ 72 ساعة مع حماية هوامش الربح وتقسيط تمارا"
/marketing growth    "شخص أسباب ارتداد العملاء وصمم برنامج إحالة فيروسي للعملاء"
```

---

## 📜 المعمارية والحوكمة

- **منهجية TidyFactor Skill Architect**: امتثال كامل للقواعد الهيكلية (اجتياز 6/6 قواعد بنسبة 100%).
- **أدوات التدقيق الآلي**: شغّل `python scratch/deep_audit_marketing_skill.py` للتأكد من سلامة كافة المسارات بنسبة 100%.
- **الترخيص**: مرخصة بموجب رخصة **[MIT مفتوحة المصدر](LICENSE)** من **TidyFactor و [الوكالة للبرمجيات (Alwkala)](https://alwkala.com)**.

</div>


---

## 🏛️ معمارية منظومة TidyFactor

**منظومة TidyFactor** هي بيئة معمارية برمجية مفتوحة وحزم مهارات لوكلاء الذكاء الاصطناعي قائمة على الفصل التام للمسؤوليات عبر دورة حياة المنتجات:

```text
منظمة TidyFactor الرسمية (github.com/TidyFactor)
│
├── مهارات التصميم (Design Skills)
│   ├── Cinematic    ← تجربة الإبهار البصري / Experience ("Wow")     (صفحات سينمائية تفاعلية)
│   ├── Design       ← بناء النماذج الأولية / Prototype ("Build")   (محرك تصميم كودي وبديل Figma)
│   └── Styler       ← الجاهزية للإنتاج والتنسيق / Production ("Ship")  (محرك التنسيق ودعم RTL)
│
├── مهارات التطوير البرمجي (Development Skills)
│   ├── HTML         ← المواقع الثابتة وسيو المحتوى / Static & SEO   (هياكل خفيفة وسريعة)
│   ├── HTMX         ← الواجهات التفاعلية الخفيفة / Hypermedia        (تفاعلات بدون جافاسكريبت معقدة)
│   ├── JS           ← تطبيقات الصفحة الواحدة بدون أطر / Vanilla SPA  (نماذج تفاعلية بـ ES Modules)
│   ├── PHP          ← المنظومات المخدمية الحديثة / Server-Rendered  (مكونات حديثة وتطبيقات PHP 8)
│   └── Next         ← منصات الساس متعددة المستأجرين / Multi-Tenant (Next.js 16 + Postgres RLS)
│
└── مهارات النمو والتسويق (Growth Skills)
    └── Marketing    ← استراتيجيات النمو والمبيعات / Growth & SEO    (تسويق الاستجابة المباشرة)
```

### 💎 ثلاثي الواجهات الأمامية والتجربة (Frontend Triad)

```text
                TidyFactor
                    │
          ┌─────────┼─────────┐
          │         │         │
      Cinematic   Design    Styler
          │         │         │
       Experience Prototype Production
          │         │         │
       "Wow"      "Build"   "Ship"
```

### 📦 مصفوفة التكامل الشامل للمجتمع (GitHub • Skill • NPM)

| المسار البرمجي | الفئة | مستودع GitHub | مهارة الوكيل | حزمة NPM |
| :--- | :--- | :--- | :--- | :--- |
| **Cinematic** | التصميم | [`TidyFactor/Cinematic`](https://github.com/TidyFactor/Cinematic) | `tidyfactor-cinematic` | [`@tidyfactor/cinematic`](https://www.npmjs.com/package/@tidyfactor/cinematic) |
| **Design** | التصميم | [`TidyFactor/Design`](https://github.com/TidyFactor/Design) | `tidyfactor-design` | [`@tidyfactor/design`](https://www.npmjs.com/package/@tidyfactor/design) |
| **Styler** | التصميم | [`TidyFactor/Styler`](https://github.com/TidyFactor/Styler) | `tidyfactor-styler` | [`@tidyfactor/styler`](https://www.npmjs.com/package/@tidyfactor/styler) |
| **Next** | التطوير | [`TidyFactor/Next`](https://github.com/TidyFactor/Next) | `tidyfactor-next` | [`@tidyfactor/next`](https://www.npmjs.com/package/@tidyfactor/next) |
| **HTML** | التطوير | [`TidyFactor/HTML`](https://github.com/TidyFactor/HTML) | `tidyfactor-html` | [`@tidyfactor/html`](https://www.npmjs.com/package/@tidyfactor/html) |
| **HTMX** | التطوير | [`TidyFactor/HTMX`](https://github.com/TidyFactor/HTMX) | `tidyfactor-htmx` | [`@tidyfactor/htmx`](https://www.npmjs.com/package/@tidyfactor/htmx) |
| **JS** | التطوير | [`TidyFactor/JS`](https://github.com/TidyFactor/JS) | `tidyfactor-js` | [`@tidyfactor/js`](https://www.npmjs.com/package/@tidyfactor/js) |
| **PHP** | التطوير | [`TidyFactor/PHP`](https://github.com/TidyFactor/PHP) | `tidyfactor-php` | [`@tidyfactor/php`](https://www.npmjs.com/package/@tidyfactor/php) |
| **Marketing** | النمو | [`TidyFactor/Marketing`](https://github.com/TidyFactor/Marketing) | `tidyfactor-marketing` | [`@tidyfactor/marketing`](https://www.npmjs.com/package/@tidyfactor/marketing) |

---

## 👨‍💻 المنظمة والتواصل والدعم

- 🌐 **الموقع الرسمي للمنظومة:** [https://tidyfactor.com/](https://tidyfactor.com/)
- 📚 **التوثيق الرسمي المعتمد:** [https://tidyfactor.com/documentation](https://tidyfactor.com/documentation)
- 🤝 **الشريك التقني الرسمي:** [الوكالة الرقمية Alwkala](https://alwkala.com/)
- 🐙 **منظمة GitHub الرسمية:** [github.com/TidyFactor](https://github.com/TidyFactor)
- 📧 **استفسارات الأعمال والشركات:** [hello@tidyfactor.com](mailto:hello@tidyfactor.com)
- 📱 **واتساب:** [+20 101 665 6899](https://wa.me/201016656899)
- 📞 **الهاتف:** +20 101 665 6899
- 📍 **المقر:** القاهرة، جمهورية مصر العربية

---

## 📜 الترخيص والمجتمع

مرخصة تحت رخصة **Apache License 2.0**. حقوق النشر محفوظة (c) 2026 لصالح [منظومة TidyFactor](https://tidyfactor.com) و[الوكالة الرقمية Alwkala](https://alwkala.com).
