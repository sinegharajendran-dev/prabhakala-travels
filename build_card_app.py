import os, base64

# Read base64 assets
logo_badge_path = '/Users/madhavan/.gemini/antigravity/scratch/perambalur-taisor-cabs/assets/prabhakala_logo_badge.jpg'
with open(logo_badge_path, 'rb') as f:
    b64_logo = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

os.makedirs('/Users/madhavan/.gemini/antigravity/scratch/perambalur-taisor-cabs/card', exist_ok=True)

def get_card_html(relative_prefix=""):
    return f'''<!DOCTYPE html>
<html lang="ta">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prabhakala Travels — Visiting Card Studio (Selvabarathi)</title>
  
  <!-- Google Fonts: Plus Jakarta Sans & Noto Sans Tamil -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Tamil:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <style>
    /* Exact PAN Card (ISO/IEC 7810 ID-1) Dimensions: 85.6mm x 54.0mm (3.37" x 2.125") */
    :root {{
      --card-w: 85.6mm;
      --card-h: 54.0mm;
      --card-radius: 3.2mm;
    }}

    body {{
      font-family: "Plus Jakarta Sans", "Noto Sans Tamil", sans-serif;
      -webkit-font-smoothing: antialiased;
      background-color: #F8F9FA;
    }}

    /* Screen display: scaled slightly for crisp readability (1.35x visual scale on screen, exact mm on print) */
    .pan-card-screen {{
      width: 440px;
      height: 277px;
      max-width: 100%;
      border-radius: 16px;
      box-sizing: border-box;
      position: relative;
      overflow: hidden;
      box-shadow: 0 15px 35px -5px rgba(0, 0, 0, 0.08), 0 5px 15px -3px rgba(0, 0, 0, 0.04);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .pan-card-screen:hover {{
      transform: translateY(-2px);
      box-shadow: 0 20px 40px -5px rgba(0, 0, 0, 0.12);
    }}

    /* Luxury Light Cream Palette (Matching prabhakala_logo_full.jpg) */
    .light-card-front {{
      background: linear-gradient(135deg, #FFFEFD 0%, #FAF6EE 50%, #F5EEE2 100%);
      border: 1.5px solid #DFD5C6;
    }}

    .light-card-back {{
      background: linear-gradient(135deg, #FFFFFF 0%, #FBF8F2 60%, #F6EFE3 100%);
      border: 1.5px solid #DFD5C6;
    }}

    /* Print Specific Rules (Exact PAN card print) */
    @page {{
      size: auto;
      margin: 15mm;
    }}

    @media print {{
      body {{
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
      }}
      .no-print {{
        display: none !important;
      }}
      .print-container {{
        display: flex !important;
        flex-direction: column !important;
        gap: 15mm !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 10mm !important;
      }}
      .pan-card-screen {{
        width: 85.6mm !important;
        height: 54.0mm !important;
        min-width: 85.6mm !important;
        min-height: 54.0mm !important;
        border-radius: 3.2mm !important;
        box-shadow: none !important;
        border: 1px solid #D5C7B2 !important;
        page-break-inside: avoid !important;
      }}
    }}
  </style>
</head>
<body class="py-6 px-3 sm:px-6 flex flex-col items-center min-h-screen">

  <!-- ================= TOP ACTION BAR & CONTROL PANEL (Hidden on Print) ================= -->
  <header class="no-print max-w-5xl w-full bg-white rounded-3xl shadow-sm border border-gray-200 p-4 sm:p-6 mb-6">
    
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <div class="flex items-center gap-2 flex-wrap">
          <span class="px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-950 font-extrabold text-[11px] border border-amber-300">
            PAN CARD SIZE (85.6 × 54.0 mm)
          </span>
          <span class="text-xs text-gray-400">•</span>
          <span id="headerRegBadge" class="text-xs font-mono font-black text-amber-900 bg-amber-50 px-2 py-0.5 rounded border border-amber-200">
            TN 46 AK 1244
          </span>
          <span class="text-xs text-gray-400">•</span>
          <span class="text-xs font-bold text-emerald-700 flex items-center gap-1">
            <span>💾</span> <span>Auto-Saved Locally</span>
          </span>
        </div>
        <h1 class="text-xl sm:text-2xl font-black text-gray-950 mt-1">
          பிரபாகலா டிராவல்ஸ் — விசிட்டிங் கார்டு
        </h1>
        <p class="text-xs text-gray-500 font-medium mt-0.5">
          உரிமையாளர்: <strong id="headerOwnerName" class="text-gray-800">செல்வபாரதி (Selvabarathi)</strong> • White Toyota Taisor SUV
        </p>
      </div>

      <!-- Quick Action Buttons -->
      <div class="flex flex-wrap items-center gap-2 shrink-0">
        <!-- Home Link -->
        <a href="{relative_prefix}index.html" class="px-3.5 py-2 rounded-xl border border-gray-300 hover:bg-gray-50 text-gray-700 text-xs font-bold transition flex items-center gap-1.5">
          <span>🏠</span>
          <span>Home (முகப்பு)</span>
        </a>

        <!-- Open Live Text Editor Button -->
        <button id="btnToggleEditor" onclick="toggleEditor()" class="px-3.5 py-2 rounded-xl bg-indigo-50 hover:bg-indigo-100 text-indigo-950 border border-indigo-200 text-xs font-black shadow-sm transition flex items-center gap-1.5">
          <span>✏️</span>
          <span>எழுத்துக்களை மாற்று (Edit Text)</span>
        </button>

        <!-- 3D Mockup View Toggle -->
        <button onclick="toggleMockupView()" class="px-3.5 py-2 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-950 border border-amber-200 text-xs font-bold transition flex items-center gap-1.5">
          <span>📸</span>
          <span>3D Mockup</span>
        </button>

        <!-- Print PDF Button -->
        <button onclick="window.print()" class="px-4 py-2 rounded-xl bg-amber-400 hover:bg-amber-500 text-gray-950 text-xs font-black shadow-md transition flex items-center gap-2">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M19 8H5c-1.66 0-3 1.34-3 3v6h4v4h12v-4h4v-6c0-1.66-1.34-3-3-3zm-3 11H8v-5h8v5zm3-7c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm-1-9H6v4h12V3z"/></svg>
          <span>அச்சிடுக (Print / PDF)</span>
        </button>
      </div>
    </div>

    <!-- Language Selector Toolbar -->
    <div class="mt-4 pt-3.5 border-t border-gray-100 flex flex-wrap items-center justify-between gap-3 text-xs">
      <div class="flex items-center gap-2 flex-wrap">
        <span class="font-extrabold text-gray-700">கார்டின் மொழி (Language):</span>
        <button id="langTaBtn" onclick="setCardLanguage('ta')" class="card-lang-btn px-3 py-1.5 rounded-xl font-black bg-gray-950 text-white shadow-sm transition">
          தமிழ் (Tamil)
        </button>
        <button id="langEnBtn" onclick="setCardLanguage('en')" class="card-lang-btn px-3 py-1.5 rounded-xl font-bold bg-gray-100 text-gray-700 hover:bg-gray-200 transition">
          English
        </button>
        <button id="langBiBtn" onclick="setCardLanguage('bilingual')" class="card-lang-btn px-3 py-1.5 rounded-xl font-bold bg-gray-100 text-gray-700 hover:bg-gray-200 transition">
          இருமொழி (Bilingual)
        </button>
      </div>

      <div class="text-[11px] text-gray-500 font-medium">
        💡 கீழேயுள்ள கார்டுகளுக்கு அடியில் <strong>SVG, PNG, JPG</strong> பதிவிறக்க பொத்தான்கள் உள்ளன.
      </div>
    </div>
  </header>

  <!-- ================= LIVE TEXT EDITOR DRAWER (Toggleable) ================= -->
  <div id="editorDrawer" class="hidden no-print max-w-5xl w-full bg-white rounded-3xl shadow-xl border-2 border-indigo-200 p-5 sm:p-7 mb-6 transition-all">
    <div class="flex items-center justify-between pb-3 border-b border-gray-200 mb-4">
      <div>
        <h2 class="font-black text-lg sm:text-xl text-gray-900 flex items-center gap-2">
          <span>✏️ கார்டின் விவரங்களைத் திருத்துங்கள் (Live Text Editor)</span>
        </h2>
        <p class="text-xs text-gray-500 font-medium">
          நீங்கள் மாற்றும் விவரங்கள் உடனே கார்டில் தெரியும். உங்கள் பிரவுசரில் தானாகவே சேமிக்கப்படும் (LocalStorage).
        </p>
      </div>
      <div class="flex items-center gap-2">
        <button onclick="resetCardDataToDefault()" class="px-3 py-1.5 rounded-xl border border-rose-300 bg-rose-50 hover:bg-rose-100 text-rose-800 text-xs font-bold transition">
          🔄 அசல் நிலைக்கு மீட்டமை (Reset)
        </button>
        <button onclick="toggleEditor()" class="w-8 h-8 rounded-full bg-gray-100 hover:bg-gray-200 text-gray-600 font-bold flex items-center justify-center">
          ✕
        </button>
      </div>
    </div>

    <!-- Editor Fields Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 text-xs">
      
      <!-- Brand Name Tamil -->
      <div class="bg-gray-50 p-2.5 rounded-2xl border border-gray-200">
        <label class="font-black text-gray-700 block mb-1">பிராண்ட் பெயர் (தமிழ்):</label>
        <input type="text" id="inputBrandTa" oninput="onFieldChange('brandTa', this.value)" class="w-full p-2 rounded-xl border border-gray-300 font-bold text-gray-900 bg-white focus:outline-none focus:border-amber-400">
      </div>

      <!-- Brand Name English -->
      <div class="bg-gray-50 p-2.5 rounded-2xl border border-gray-200">
        <label class="font-black text-gray-700 block mb-1">Brand Name (English):</label>
        <input type="text" id="inputBrandEn" oninput="onFieldChange('brandEn', this.value)" class="w-full p-2 rounded-xl border border-gray-300 font-bold text-gray-900 bg-white focus:outline-none focus:border-amber-400">
      </div>

      <!-- Top Auspicious Blessing -->
      <div class="bg-gray-50 p-2.5 rounded-2xl border border-gray-200">
        <label class="font-black text-gray-700 block mb-1">மேல் வரி (Blessing / Om Shakti):</label>
        <input type="text" id="inputOmShakti" oninput="onFieldChange('omShakti', this.value)" class="w-full p-2 rounded-xl border border-gray-300 font-bold text-gray-900 bg-white focus:outline-none focus:border-amber-400">
      </div>

      <!-- Owner Name Tamil -->
      <div class="bg-gray-50 p-2.5 rounded-2xl border border-gray-200">
        <label class="font-black text-gray-700 block mb-1">உரிமையாளர் பெயர் (தமிழ்):</label>
        <input type="text" id="inputOwnerTa" oninput="onFieldChange('ownerTa', this.value)" class="w-full p-2 rounded-xl border border-gray-300 font-bold text-gray-900 bg-white focus:outline-none focus:border-amber-400">
      </div>

      <!-- Owner Name English -->
      <div class="bg-gray-50 p-2.5 rounded-2xl border border-gray-200">
        <label class="font-black text-gray-700 block mb-1">Owner Name (English):</label>
        <input type="text" id="inputOwnerEn" oninput="onFieldChange('ownerEn', this.value)" class="w-full p-2 rounded-xl border border-gray-300 font-bold text-gray-900 bg-white focus:outline-none focus:border-amber-400">
      </div>

      <!-- Car Registration Number -->
      <div class="bg-gray-50 p-2.5 rounded-2xl border border-gray-200">
        <label class="font-black text-amber-900 block mb-1">காரின் பதிவு எண் (Car Reg):</label>
        <input type="text" id="inputCarReg" oninput="onFieldChange('carReg', this.value)" class="w-full p-2 rounded-xl border border-amber-300 font-mono font-black text-gray-950 bg-amber-50 focus:outline-none focus:border-amber-500">
      </div>

      <!-- Phone / WhatsApp Number -->
      <div class="bg-gray-50 p-2.5 rounded-2xl border border-gray-200">
        <label class="font-black text-emerald-900 block mb-1">போன் & WhatsApp எண்:</label>
        <input type="text" id="inputPhone" oninput="onFieldChange('phone', this.value)" class="w-full p-2 rounded-xl border border-emerald-300 font-bold text-gray-950 bg-white focus:outline-none focus:border-emerald-500">
      </div>

      <!-- Car Model -->
      <div class="bg-gray-50 p-2.5 rounded-2xl border border-gray-200">
        <label class="font-black text-gray-700 block mb-1">வாகனம் (Car Model):</label>
        <input type="text" id="inputCarModel" oninput="onFieldChange('carModel', this.value)" class="w-full p-2 rounded-xl border border-gray-300 font-bold text-gray-900 bg-white focus:outline-none focus:border-amber-400">
      </div>

      <!-- Base Hub -->
      <div class="bg-gray-50 p-2.5 rounded-2xl border border-gray-200">
        <label class="font-black text-gray-700 block mb-1">இருப்பிடம் (Base Town):</label>
        <input type="text" id="inputBaseTown" oninput="onFieldChange('baseTown', this.value)" class="w-full p-2 rounded-xl border border-gray-300 font-bold text-gray-900 bg-white focus:outline-none focus:border-amber-400">
      </div>

      <!-- Popular Routes (Col Span 2) -->
      <div class="bg-gray-50 p-2.5 rounded-2xl border border-gray-200 md:col-span-2">
        <label class="font-black text-gray-700 block mb-1">முக்கிய வழித்தடங்கள் (Popular Routes):</label>
        <input type="text" id="inputRoutes" oninput="onFieldChange('routes', this.value)" class="w-full p-2 rounded-xl border border-gray-300 font-bold text-gray-900 bg-white focus:outline-none focus:border-amber-400">
      </div>

      <!-- Slogan -->
      <div class="bg-gray-50 p-2.5 rounded-2xl border border-gray-200">
        <label class="font-black text-gray-700 block mb-1">முழக்க வரி (Slogan / Motto):</label>
        <input type="text" id="inputSlogan" oninput="onFieldChange('slogan', this.value)" class="w-full p-2 rounded-xl border border-gray-300 font-bold text-gray-900 bg-white focus:outline-none focus:border-amber-400">
      </div>

    </div>

    <div class="mt-4 pt-3 border-t border-gray-200 flex items-center justify-between">
      <span class="text-xs text-emerald-700 font-bold flex items-center gap-1.5">
        <span>✅</span>
        <span>விவரங்கள் உங்கள் பிரவுசரில் பாதுகாப்பாக சேமிக்கப்பட்டுவிட்டன!</span>
      </span>
      <button onclick="toggleEditor()" class="px-5 py-2 rounded-xl bg-gray-900 hover:bg-black text-white text-xs font-black shadow-md transition">
        முடிந்தது (Close Editor)
      </button>
    </div>
  </div>

  <!-- ================= 3D MOCKUP MODAL (Hidden by default, toggleable) ================= -->
  <div id="mockupModal" class="hidden no-print max-w-4xl w-full bg-white rounded-3xl shadow-xl border border-gray-200 p-6 mb-6 text-center">
    <div class="flex items-center justify-between pb-3 border-b border-gray-100 mb-4">
      <div>
        <span class="px-3 py-1 rounded-full bg-amber-100 text-amber-900 text-xs font-black border border-amber-300">
          3D PHOTOREALISTIC LUXURY STATIONERY RENDER
        </span>
        <h2 class="text-xl font-black text-gray-950 mt-1">நேரடி விசிட்டிங் கார்டு 3D மாதிரிக்காட்சி</h2>
      </div>
      <button onclick="toggleMockupView()" class="w-8 h-8 rounded-full bg-gray-100 hover:bg-gray-200 text-gray-600 font-bold flex items-center justify-center">
        ✕
      </button>
    </div>
    <div class="rounded-2xl overflow-hidden shadow-xl border border-gray-200 max-w-3xl mx-auto">
      <img src="{relative_prefix}assets/visiting_card_light_mockup.jpg" alt="Prabhakala Travels Luxury Visiting Card Mockup" class="w-full h-auto object-cover">
    </div>
  </div>

  <!-- ================= MAIN VISITING CARDS SHOWCASE (FRONT & BACK) ================= -->
  <main class="print-container max-w-5xl w-full flex flex-col lg:flex-row items-center justify-center gap-8 my-auto">
    
    <!-- FRONT CARD WRAPPER -->
    <div class="flex flex-col items-center w-full max-w-[440px]">
      <div class="no-print flex items-center justify-between w-full mb-2.5 px-1">
        <span class="text-xs font-black text-gray-500 uppercase tracking-wider flex items-center gap-1.5">
          <span>💳</span> <span>முன்பக்கம் (Front Side)</span>
        </span>
        <span class="text-[11px] font-bold text-amber-800 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200">
          85.6 × 54.0 mm
        </span>
      </div>

      <!-- Front Card Element -->
      <div id="cardFrontContainer" class="pan-card-screen light-card-front p-5 sm:p-6 flex flex-col justify-between select-none">
        <!-- Rendered dynamically by JS -->
      </div>

      <!-- Front Card Download Toolbar -->
      <div class="no-print w-full mt-3 bg-white p-3 rounded-2xl border border-gray-200 shadow-sm flex items-center justify-between gap-2">
        <span class="text-[11px] font-bold text-gray-600">Front:</span>
        <div class="flex items-center gap-1.5 flex-1 justify-end">
          <button onclick="downloadCard('front', 'svg')" class="px-2.5 py-1.5 rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-800 font-black text-[11px] transition shadow-xs">
            ⬇️ SVG
          </button>
          <button onclick="downloadCard('front', 'png')" class="px-2.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-black text-[11px] transition shadow-xs">
            ⬇️ PNG (300 DPI)
          </button>
          <button onclick="downloadCard('front', 'jpg')" class="px-2.5 py-1.5 rounded-lg bg-amber-400 hover:bg-amber-500 text-gray-950 font-black text-[11px] transition shadow-xs">
            ⬇️ JPG
          </button>
        </div>
      </div>
    </div>

    <!-- BACK CARD WRAPPER -->
    <div class="flex flex-col items-center w-full max-w-[440px]">
      <div class="no-print flex items-center justify-between w-full mb-2.5 px-1">
        <span class="text-xs font-black text-gray-500 uppercase tracking-wider flex items-center gap-1.5">
          <span>💬</span> <span>பின்பக்கம் (Back Side • With QR)</span>
        </span>
        <span class="text-[11px] font-bold text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">
          WhatsApp Scannable
        </span>
      </div>

      <!-- Back Card Element -->
      <div id="cardBackContainer" class="pan-card-screen light-card-back p-5 sm:p-6 flex flex-col justify-between select-none">
        <!-- Rendered dynamically by JS -->
      </div>

      <!-- Back Card Download Toolbar -->
      <div class="no-print w-full mt-3 bg-white p-3 rounded-2xl border border-gray-200 shadow-sm flex items-center justify-between gap-2">
        <span class="text-[11px] font-bold text-gray-600">Back:</span>
        <div class="flex items-center gap-1.5 flex-1 justify-end">
          <button onclick="downloadCard('back', 'svg')" class="px-2.5 py-1.5 rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-800 font-black text-[11px] transition shadow-xs">
            ⬇️ SVG
          </button>
          <button onclick="downloadCard('back', 'png')" class="px-2.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-black text-[11px] transition shadow-xs">
            ⬇️ PNG (300 DPI)
          </button>
          <button onclick="downloadCard('back', 'jpg')" class="px-2.5 py-1.5 rounded-lg bg-amber-400 hover:bg-amber-500 text-gray-950 font-black text-[11px] transition shadow-xs">
            ⬇️ JPG
          </button>
        </div>
      </div>
    </div>

  </main>

  <!-- Combined Pair Download Footer (No-Print) -->
  <div class="no-print max-w-5xl w-full mt-8 bg-white p-4 sm:p-5 rounded-3xl border border-gray-200 shadow-sm flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left">
    <div>
      <span class="font-black text-sm text-gray-900 block">முன்பக்கம் + பின்பக்கம் இரண்டும் ஒரே படத்தில் (Combined Pair)</span>
      <span class="text-xs text-gray-500">வாட்ஸ்அப் நிலை (Status), சமூக வலைத்தளங்களில் பகிர மிகச் சிறந்தது.</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="downloadCombined('png')" class="px-4 py-2 rounded-xl bg-gray-900 hover:bg-black text-white font-black text-xs shadow transition">
        ⬇️ இரண்டும் சேர்ந்த படம் (PNG)
      </button>
      <button onclick="downloadCombined('jpg')" class="px-4 py-2 rounded-xl bg-amber-400 hover:bg-amber-500 text-gray-950 font-black text-xs shadow transition">
        ⬇️ இரண்டும் சேர்ந்த படம் (JPG)
      </button>
    </div>
  </div>

  <!-- Hidden Canvas for Vector to PNG/JPG rasterization -->
  <canvas id="exportCanvas" style="display: none;"></canvas>

  <!-- ================= JAVASCRIPT STUDIO ENGINE ================= -->
  <script>
    const LOGO_BASE64 = "{b64_logo}";

    // Default Card Settings Data
    const DEFAULT_CARD_DATA = {{
      brandTa: "பிரபாகலா டிராவல்ஸ்",
      brandEn: "PRABHAKALA TRAVELS",
      omShakti: "॥ ஓம் சக்தி ॥",
      ownerTa: "செல்வபாரதி",
      ownerEn: "SELVABARATHI",
      carReg: "TN 46 AK 1244",
      phone: "+91 6385300259",
      carModel: "White Toyota Urban Cruiser Taisor (AC SUV)",
      baseTown: "பூலாம்பாடி & பெரம்பலூர்",
      routes: "திருச்சி ஏர்போர்ட், சென்னை, பெங்களூர், மதுரை, கோவை, திருப்பதி",
      slogan: "பாரதியார் நினைவில் பாதுகாப்பான பயணம்"
    }};

    // Active State Store (Loaded from LocalStorage)
    let cardData = Object.assign({{}}, DEFAULT_CARD_DATA);
    let cardLang = 'ta'; // 'ta', 'en', 'bilingual'

    // Load from LocalStorage on Startup
    function loadSavedCardData() {{
      try {{
        const saved = localStorage.getItem('prabhakala_card_data');
        if (saved) {{
          const parsed = JSON.parse(saved);
          cardData = Object.assign({{}}, DEFAULT_CARD_DATA, parsed);
        }}
        const savedLang = localStorage.getItem('prabhakala_card_lang');
        if (savedLang) {{
          cardLang = savedLang;
        }}
      }} catch (e) {{
        console.warn('LocalStorage error:', e);
      }}
      syncInputsWithData();
    }}

    // Save to LocalStorage
    function persistCardData() {{
      try {{
        localStorage.setItem('prabhakala_card_data', JSON.stringify(cardData));
        localStorage.setItem('prabhakala_card_lang', cardLang);
      }} catch (e) {{
        console.warn('LocalStorage save error:', e);
      }}
    }}

    // Sync input fields with active state
    function syncInputsWithData() {{
      document.getElementById('inputBrandTa').value = cardData.brandTa;
      document.getElementById('inputBrandEn').value = cardData.brandEn;
      document.getElementById('inputOmShakti').value = cardData.omShakti;
      document.getElementById('inputOwnerTa').value = cardData.ownerTa;
      document.getElementById('inputOwnerEn').value = cardData.ownerEn;
      document.getElementById('inputCarReg').value = cardData.carReg;
      document.getElementById('inputPhone').value = cardData.phone;
      document.getElementById('inputCarModel').value = cardData.carModel;
      document.getElementById('inputBaseTown').value = cardData.baseTown;
      document.getElementById('inputRoutes').value = cardData.routes;
      document.getElementById('inputSlogan').value = cardData.slogan;

      document.getElementById('headerRegBadge').textContent = cardData.carReg;
      document.getElementById('headerOwnerName').textContent = `${{cardData.ownerTa}} (${{cardData.ownerEn}})`;
    }}

    // Input field change handler
    function onFieldChange(key, value) {{
      cardData[key] = value;
      persistCardData();
      document.getElementById('headerRegBadge').textContent = cardData.carReg;
      document.getElementById('headerOwnerName').textContent = `${{cardData.ownerTa}} (${{cardData.ownerEn}})`;
      refreshCardRenders();
    }}

    // Reset to default
    function resetCardDataToDefault() {{
      if (confirm('அனைத்து விவரங்களையும் அசல் நிலைக்கு மீட்டமைக்க வேண்டுமா? (Reset all to defaults?)')) {{
        cardData = Object.assign({{}}, DEFAULT_CARD_DATA);
        persistCardData();
        syncInputsWithData();
        refreshCardRenders();
      }}
    }}

    // Toggle Editor Drawer
    function toggleEditor() {{
      const drawer = document.getElementById('editorDrawer');
      drawer.classList.toggle('hidden');
      if (!drawer.classList.contains('hidden')) {{
        drawer.scrollIntoView({{ behavior: 'smooth' }});
      }}
    }}

    // Toggle 3D Mockup
    function toggleMockupView() {{
      const modal = document.getElementById('mockupModal');
      modal.classList.toggle('hidden');
      if (!modal.classList.contains('hidden')) {{
        modal.scrollIntoView({{ behavior: 'smooth' }});
      }}
    }}

    // Language Toggle
    function setCardLanguage(lang) {{
      cardLang = lang;
      persistCardData();

      document.querySelectorAll('.card-lang-btn').forEach(b => {{
        b.className = 'card-lang-btn px-3 py-1.5 rounded-xl font-bold bg-gray-100 text-gray-700 hover:bg-gray-200 transition';
      }});

      if (lang === 'ta') {{
        document.getElementById('langTaBtn').className = 'card-lang-btn px-3 py-1.5 rounded-xl font-black bg-gray-950 text-white shadow-sm transition';
      }} else if (lang === 'en') {{
        document.getElementById('langEnBtn').className = 'card-lang-btn px-3 py-1.5 rounded-xl font-black bg-gray-950 text-white shadow-sm transition';
      }} else {{
        document.getElementById('langBiBtn').className = 'card-lang-btn px-3 py-1.5 rounded-xl font-black bg-gray-950 text-white shadow-sm transition';
      }}

      refreshCardRenders();
    }}

    // Generate Card Front HTML String based on Language & Data
    function renderCardFront() {{
      const d = cardData;
      let brandHTML = '';
      let sloganHTML = '';
      let carTag = '';
      let topLocation = '';

      if (cardLang === 'en') {{
        brandHTML = `
          <h2 class="font-black text-xl sm:text-2xl tracking-wider text-[#C58B24] uppercase leading-tight">
            ${{d.brandEn}}
          </h2>
          <span class="text-[11px] font-black text-gray-500 uppercase tracking-wider block mt-0.5">LUXURY CAB & TOURS</span>
        `;
        sloganHTML = `<p class="text-[11px] font-semibold text-[#5A5D64] tracking-tight mt-1">Safe Journey in Memory of Bharathiyar</p>`;
        carTag = `White Toyota Taisor (AC SUV)`;
        topLocation = `POOLAMBADI &bull; PERAMBALUR`;
      }} else if (cardLang === 'bilingual') {{
        brandHTML = `
          <h2 class="font-black text-xl sm:text-2xl tracking-tight text-[#16191E] leading-tight">
            ${{d.brandTa}}
          </h2>
          <span class="font-black text-xs sm:text-sm tracking-wider text-[#C58B24] uppercase block mt-0.5">
            ${{d.brandEn}}
          </span>
        `;
        sloganHTML = `<p class="text-[10px] sm:text-[11px] font-semibold text-[#5A5D64] tracking-tight mt-1">${{d.slogan}}</p>`;
        carTag = `White Toyota Taisor (AC SUV)`;
        topLocation = `POOLAMBADI &bull; PERAMBALUR`;
      }} else {{
        // Tamil default
        brandHTML = `
          <h2 class="font-black text-xl sm:text-2xl tracking-tight text-[#16191E] leading-tight">
            ${{d.brandTa}}
          </h2>
          <span class="font-black text-xs sm:text-sm tracking-wider text-[#C58B24] uppercase block mt-0.5">
            ${{d.brandEn}}
          </span>
        `;
        sloganHTML = `<p class="text-[10px] sm:text-[11px] font-semibold text-[#5A5D64] tracking-tight mt-1">${{d.slogan}}</p>`;
        carTag = `ஒயிட் டொயோட்டா டெய்சர் (AC SUV)`;
        topLocation = `பூலாம்பாடி &bull; பெரம்பலூர்`;
      }}

      return `
        <!-- Subtle Top & Bottom Gold Line Trim -->
        <div class="absolute top-0 left-0 right-0 h-[2.5px] bg-gradient-to-r from-transparent via-[#C5A059] to-transparent"></div>
        <div class="absolute bottom-0 left-0 right-0 h-[2.5px] bg-gradient-to-r from-transparent via-[#C5A059] to-transparent"></div>

        <!-- Ambient Luxury Radial Sun Glow -->
        <div class="absolute -top-12 -right-12 w-36 h-36 bg-amber-200/30 rounded-full blur-2xl pointer-events-none"></div>
        <div class="absolute -bottom-12 -left-12 w-36 h-36 bg-amber-200/20 rounded-full blur-2xl pointer-events-none"></div>

        <!-- Top Auspicious & Location Header -->
        <div class="flex items-center justify-between relative z-10 leading-none">
          <span class="text-[10.5px] font-black tracking-widest text-[#B8860B]">
            ${{d.omShakti}}
          </span>
          <span class="text-[9.5px] font-black tracking-wider px-2.5 py-1 rounded-full bg-[#FAF0D7] text-[#8C620A] border border-[#E8D4A2] uppercase">
            ${{topLocation}}
          </span>
        </div>

        <!-- Center: Official Logo Badge & Typography -->
        <div class="flex items-center gap-3.5 my-auto relative z-10">
          <div class="w-14 h-14 sm:w-16 sm:h-16 rounded-2xl overflow-hidden shadow-sm border border-[#DCCBB4] bg-white shrink-0 p-0.5">
            <img src="${{LOGO_BASE64}}" alt="Logo" class="w-full h-full object-cover rounded-xl">
          </div>

          <div class="flex-1 min-w-0">
            ${{brandHTML}}
            ${{sloganHTML}}
          </div>
        </div>

        <!-- Bottom Vehicle & Features Pill Strip -->
        <div class="pt-2 border-t border-[#E8DFC9] flex items-center justify-between relative z-10 leading-none">
          <div class="flex items-center gap-1.5 text-[10px] sm:text-[11px] font-extrabold text-[#22242A]">
            <span class="text-[#C58B24]">🚘</span>
            <span>${{carTag}}</span>
          </div>

          <div class="px-2.5 py-1 rounded bg-amber-100/90 text-amber-950 font-black text-[11px] border border-amber-300 font-mono tracking-wider shadow-xs">
            ${{d.carReg}}
          </div>
        </div>
      `;
    }}

    // Generate Card Back HTML String based on Language & Data
    function renderCardBack() {{
      const d = cardData;
      const cleanPhone = d.phone.replace(/[^0-9]/g, '');
      const waLink = `https://wa.me/${{cleanPhone}}?text=%E0%AE%B5%E0%AE%A3%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%AE%E0%AF%8D!%20I%20would%20like%20to%20book%20Prabhakala%20Travels%20cab%20(${{encodeURIComponent(d.carReg)}})`;
      const qrImgUrl = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&margin=1&data=${{encodeURIComponent(waLink)}}`;

      let ownerTitle = '';
      let ownerNameHTML = '';
      let callSubtitle = '';
      let routesLabel = '';
      let guaranteeText = '';
      let footerLeft = '';
      let footerRight = '';
      let qrLabel = '';

      if (cardLang === 'en') {{
        ownerTitle = 'Proprietor & Chauffeur';
        ownerNameHTML = `<h3 class="font-black text-lg sm:text-xl text-[#16191E] leading-tight mt-0.5">${{d.ownerEn}}</h3>`;
        callSubtitle = 'Direct Call & WhatsApp (24/7)';
        routesLabel = `<strong>${{d.baseTown}}</strong> &bull; ${{d.routes}}`;
        guaranteeText = '✦ 100% Punctual Doorstep Pickup &bull; Family Safe';
        footerLeft = `🏡 ${{d.baseTown}}, Tamil Nadu`;
        footerRight = 'Safe & Comfortable Journey';
        qrLabel = 'Scan to Chat';
      }} else if (cardLang === 'bilingual') {{
        ownerTitle = 'உரிமையாளர் / Proprietor';
        ownerNameHTML = `
          <div class="flex items-baseline gap-1.5 mt-0.5">
            <h3 class="font-black text-lg sm:text-xl text-[#16191E] leading-tight">${{d.ownerTa}}</h3>
            <span class="text-xs font-black text-[#C58B24] uppercase">(${{d.ownerEn}})</span>
          </div>
        `;
        callSubtitle = 'WhatsApp & Direct Call (24/7)';
        routesLabel = `<strong>${{d.baseTown}}</strong> &bull; ${{d.routes}}`;
        guaranteeText = '✦ 100% சொன்ன நேரத்தில் பிக்-அப் &bull; குடும்பப் பயணம்';
        footerLeft = `🏡 ${{d.baseTown}}`;
        footerRight = 'பாதுகாப்பான பயணம்';
        qrLabel = 'Scan WhatsApp';
      }} else {{
        // Tamil default
        ownerTitle = 'உரிமையாளர் & ஓட்டுநர்';
        ownerNameHTML = `
          <div class="flex items-baseline gap-1.5 mt-0.5">
            <h3 class="font-black text-lg sm:text-xl text-[#16191E] leading-tight">${{d.ownerTa}}</h3>
            <span class="text-xs font-black text-[#C58B24] uppercase">(${{d.ownerEn}})</span>
          </div>
        `;
        callSubtitle = 'நேரடி அழைப்பு & WhatsApp (24/7)';
        routesLabel = `<strong>${{d.baseTown}}</strong> &bull; ${{d.routes}}`;
        guaranteeText = '✦ 100% சொன்ன நேரத்தில் பிக்-அப் &bull; குடும்பப் பயணம்';
        footerLeft = `🏡 ${{d.baseTown}}, பெரம்பலூர் மாவட்டம்`;
        footerRight = 'பாதுகாப்பான பயணம்';
        qrLabel = 'ஸ்கேன் செய்க';
      }}

      return `
        <!-- Subtle Top Gold Trim -->
        <div class="absolute top-0 left-0 right-0 h-[2.5px] bg-gradient-to-r from-transparent via-[#C5A059] to-transparent"></div>

        <!-- Ambient Luxury Radial Glow -->
        <div class="absolute -top-10 -right-10 w-32 h-32 bg-emerald-100/30 rounded-full blur-2xl pointer-events-none"></div>

        <!-- Top Row: Proprietor Details & Reg Number -->
        <div class="flex items-start justify-between relative z-10 leading-tight">
          <div>
            <div class="text-[9px] font-bold text-gray-500 uppercase tracking-wider">${{ownerTitle}}</div>
            ${{ownerNameHTML}}
          </div>

          <div class="text-right">
            <span class="inline-block px-2 py-0.5 rounded bg-[#FAF0D7] text-[#8C620A] font-black text-[10.5px] border border-[#E8D4A2] font-mono tracking-wider shadow-xs">
              ${{d.carReg}}
            </span>
            <span class="text-[9px] text-gray-500 font-semibold block mt-0.5">White Toyota Taisor SUV</span>
          </div>
        </div>

        <!-- Middle Content: Contact Numbers + Service Locations + WhatsApp QR -->
        <div class="grid grid-cols-12 gap-2 my-auto items-center relative z-10 pt-1">
          
          <!-- Left Details (8 cols) -->
          <div class="col-span-8 space-y-1.5 text-[10px] sm:text-[10.5px]">
            
            <!-- Phone / WhatsApp Direct Line -->
            <div class="flex items-center gap-2 bg-[#FAF7F0] p-1.5 rounded-xl border border-[#EBE3D3]">
              <span class="w-5 h-5 rounded-full bg-emerald-600 text-white flex items-center justify-center text-[10px] font-black shrink-0">📞</span>
              <div class="leading-none">
                <a href="tel:${{d.phone}}" class="font-black text-sm sm:text-base text-[#16191E] tracking-tight hover:underline">${{d.phone}}</a>
                <span class="text-[8.5px] text-emerald-800 font-bold block mt-0.5">${{callSubtitle}}</span>
              </div>
            </div>

            <!-- Hub & Key Routes -->
            <div class="flex items-start gap-1.5 leading-tight text-[#3A3D44]">
              <span class="text-[#C58B24] shrink-0 font-bold text-xs">📍</span>
              <span class="text-[9.5px] font-bold leading-snug">
                ${{routesLabel}}
              </span>
            </div>

            <!-- Guarantee Note -->
            <div class="flex items-center gap-1.5 text-[9px] font-semibold text-gray-500">
              <span class="text-amber-600 font-bold">✦</span>
              <span>${{guaranteeText}}</span>
            </div>

          </div>

          <!-- Right Column: WhatsApp QR Code (4 cols) -->
          <div class="col-span-4 flex flex-col items-center justify-center text-center">
            <a href="${{waLink}}" target="_blank" title="Click to test WhatsApp chat" class="block w-[60px] h-[60px] p-0.5 bg-white border border-gray-300 rounded-xl shadow-sm hover:border-emerald-500 transition">
              <img src="${{qrImgUrl}}" alt="WhatsApp QR" class="w-full h-full object-contain rounded-lg">
            </a>
            <span class="text-[8px] font-black text-emerald-700 tracking-wider uppercase mt-1 flex items-center gap-0.5">
              <span>💬</span>
              <span>${{qrLabel}}</span>
            </span>
          </div>

        </div>

        <!-- Bottom Base Town & Slogan -->
        <div class="pt-1.5 border-t border-[#E8DFC9] flex items-center justify-between text-[9px] font-bold text-gray-500 relative z-10 leading-none">
          <span>${{footerLeft}}</span>
          <span class="text-[#C58B24] font-semibold">${{footerRight}}</span>
        </div>
      `;
    }}

    // Refresh all rendered cards on screen
    function refreshCardRenders() {{
      document.getElementById('cardFrontContainer').innerHTML = renderCardFront();
      document.getElementById('cardBackContainer').innerHTML = renderCardBack();
    }}

    // ================= HIGH-RESOLUTION SVG / PNG / JPG EXPORTER =================
    function getCardSVG(type) {{
      const d = cardData;
      const cleanPhone = d.phone.replace(/[^0-9]/g, '');
      const waLink = `https://wa.me/${{cleanPhone}}?text=%E0%AE%B5%E0%AE%A3%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%AE%E0%AF%8D!%20Prabhakala%20Travels%20(${{encodeURIComponent(d.carReg)}})`;
      const qrImgUrl = `https://api.qrserver.com/v1/create-qr-code/?size=240x240&margin=1&data=${{encodeURIComponent(waLink)}}`;

      if (type === 'front') {{
        return `<?xml version="1.0" encoding="UTF-8"?>
<svg width="1012" height="638" viewBox="0 0 1012 638" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFEFD"/>
      <stop offset="50%" stop-color="#FAF6EE"/>
      <stop offset="100%" stop-color="#F5EEE2"/>
    </linearGradient>
    <linearGradient id="goldBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="transparent"/>
      <stop offset="50%" stop-color="#C5A059"/>
      <stop offset="100%" stop-color="transparent"/>
    </linearGradient>
  </defs>
  
  <!-- Base Background -->
  <rect x="0" y="0" width="1012" height="638" rx="38" ry="38" fill="url(#bgGrad)" stroke="#DFD5C6" stroke-width="3"/>
  <rect x="8" y="8" width="996" height="622" rx="30" ry="30" fill="none" stroke="rgba(212,175,55,0.3)" stroke-width="2"/>
  
  <!-- Gold Trims -->
  <rect x="0" y="0" width="1012" height="6" fill="url(#goldBar)"/>
  <rect x="0" y="632" width="1012" height="6" fill="url(#goldBar)"/>

  <!-- Top Auspicious & Location Header -->
  <text x="45" y="55" font-family="'Noto Sans Tamil', 'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="18" fill="#B8860B" letter-spacing="4">${{d.omShakti}}</text>
  
  <rect x="670" y="32" width="295" height="32" rx="16" ry="16" fill="#FAF0D7" stroke="#E8D4A2" stroke-width="1.5"/>
  <text x="817" y="53" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="13" fill="#8C620A" text-anchor="middle" letter-spacing="2">POOLAMBADI • PERAMBALUR</text>

  <!-- Official Logo Badge -->
  <image href="${{LOGO_BASE64}}" x="55" y="150" width="190" height="190" rx="30" />
  
  <!-- Brand Typography -->
  <text x="275" y="220" font-family="'Noto Sans Tamil', sans-serif" font-weight="900" font-size="52" fill="#16191E" letter-spacing="-1">${{d.brandTa}}</text>
  <text x="275" y="265" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="28" fill="#C58B24" letter-spacing="3">${{d.brandEn}}</text>
  <text x="275" y="310" font-family="'Noto Sans Tamil', sans-serif" font-weight="600" font-size="21" fill="#5A5D64">${{d.slogan}}</text>

  <!-- Bottom Divider Line -->
  <line x1="45" y1="520" x2="967" y2="520" stroke="#E8DFC9" stroke-width="2"/>

  <!-- Vehicle Tag -->
  <text x="45" y="575" font-family="'Plus Jakarta Sans', 'Noto Sans Tamil', sans-serif" font-weight="900" font-size="22" fill="#22242A">🚘 ${{d.carModel}}</text>

  <!-- Car Reg Number Pill -->
  <rect x="735" y="540" width="230" height="48" rx="12" ry="12" fill="#FEF3C7" stroke="#FCD34D" stroke-width="2"/>
  <text x="850" y="573" font-family="'Plus Jakarta Sans', monospace" font-weight="900" font-size="24" fill="#78350F" text-anchor="middle" letter-spacing="3">${{d.carReg}}</text>
</svg>`;
      }} else {{
        return `<?xml version="1.0" encoding="UTF-8"?>
<svg width="1012" height="638" viewBox="0 0 1012 638" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradBack" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="60%" stop-color="#FBF8F2"/>
      <stop offset="100%" stop-color="#F6EFE3"/>
    </linearGradient>
    <linearGradient id="goldBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="transparent"/>
      <stop offset="50%" stop-color="#C5A059"/>
      <stop offset="100%" stop-color="transparent"/>
    </linearGradient>
  </defs>

  <!-- Base Background -->
  <rect x="0" y="0" width="1012" height="638" rx="38" ry="38" fill="url(#bgGradBack)" stroke="#DFD5C6" stroke-width="3"/>
  <rect x="8" y="8" width="996" height="622" rx="30" ry="30" fill="none" stroke="rgba(212,175,55,0.3)" stroke-width="2"/>
  <rect x="0" y="0" width="1012" height="6" fill="url(#goldBar)"/>

  <!-- Top Row: Proprietor Details -->
  <text x="45" y="50" font-family="'Noto Sans Tamil', 'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="16" fill="#6B7280" letter-spacing="1">உரிமையாளர் / PROPRIETOR</text>
  <text x="45" y="105" font-family="'Noto Sans Tamil', sans-serif" font-weight="900" font-size="44" fill="#16191E">${{d.ownerTa}}</text>
  <text x="310" y="98" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="24" fill="#C58B24" letter-spacing="2">(${{d.ownerEn}})</text>

  <!-- Top Right Car Reg Pill -->
  <rect x="735" y="35" width="230" height="42" rx="10" ry="10" fill="#FAF0D7" stroke="#E8D4A2" stroke-width="1.5"/>
  <text x="850" y="64" font-family="'Plus Jakarta Sans', monospace" font-weight="900" font-size="22" fill="#8C620A" text-anchor="middle" letter-spacing="2">${{d.carReg}}</text>
  <text x="850" y="98" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="15" fill="#6B7280" text-anchor="middle">White Toyota Taisor SUV</text>

  <!-- Middle Contact Pill -->
  <rect x="45" y="160" width="570" height="85" rx="20" ry="20" fill="#FAF7F0" stroke="#EBE3D3" stroke-width="2"/>
  <circle cx="95" cy="202" r="26" fill="#059669"/>
  <text x="95" y="210" font-size="24" text-anchor="middle" fill="#FFFFFF">📞</text>
  <text x="140" y="196" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="34" fill="#16191E">${{d.phone}}</text>
  <text x="142" y="226" font-family="'Noto Sans Tamil', sans-serif" font-weight="700" font-size="17" fill="#065F46">WhatsApp &amp; நேரடி அழைப்பு (24/7)</text>

  <!-- Routes & Hub -->
  <text x="45" y="295" font-family="'Noto Sans Tamil', sans-serif" font-weight="900" font-size="20" fill="#C58B24">📍</text>
  <text x="75" y="295" font-family="'Noto Sans Tamil', sans-serif" font-weight="800" font-size="19" fill="#1F2937">பூலாம்பாடி &amp; பெரம்பலூர் ⇄ ${{d.routes}}</text>
  
  <text x="45" y="340" font-family="'Noto Sans Tamil', sans-serif" font-weight="700" font-size="17" fill="#6B7280">✦ 100% சொன்ன நேரத்தில் பிக்-அப் • குடும்பப் பயணம்</text>

  <!-- WhatsApp QR Code Box -->
  <rect x="680" y="150" width="285" height="340" rx="24" ry="24" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="2"/>
  <image href="${{qrImgUrl}}" x="712" y="175" width="220" height="220" />
  <text x="822" y="440" font-family="'Noto Sans Tamil', sans-serif" font-weight="900" font-size="18" fill="#047857" text-anchor="middle">💬 ஸ்கேன் செய்க (WhatsApp)</text>
  <text x="822" y="468" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="14" fill="#9CA3AF" text-anchor="middle">Scan to Chat with Owner</text>

  <!-- Bottom Divider Line -->
  <line x1="45" y1="520" x2="967" y2="520" stroke="#E8DFC9" stroke-width="2"/>

  <!-- Footer -->
  <text x="45" y="575" font-family="'Noto Sans Tamil', sans-serif" font-weight="700" font-size="18" fill="#6B7280">🏡 ${{d.baseTown}}, பெரம்பலூர் மாவட்டம்</text>
  <text x="967" y="575" font-family="'Noto Sans Tamil', sans-serif" font-weight="800" font-size="18" fill="#C58B24" text-anchor="end">பாதுகாப்பான பயணம் • நியாயமான கட்டணம்</text>
</svg>`;
      }}
    }}

    // Direct SVG, PNG, JPG Exporter
    function downloadCard(type, format) {{
      const svgString = getCardSVG(type);
      const filename = `prabhakala_travels_card_${{type}}_${{cardLang}}`;

      if (format === 'svg') {{
        const blob = new Blob([svgString], {{ type: 'image/svg+xml;charset=utf-8' }});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.download = `${{filename}}.svg`;
        a.href = url;
        a.click();
        URL.revokeObjectURL(url);
      }} else {{
        const canvas = document.getElementById('exportCanvas');
        canvas.width = 1012;
        canvas.height = 638;
        const ctx = canvas.getContext('2d');

        const img = new Image();
        img.crossOrigin = 'anonymous';
        img.onload = () => {{
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          if (format === 'jpg') {{
            ctx.fillStyle = '#FAF6EE';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
          }}
          ctx.drawImage(img, 0, 0);

          const mime = format === 'png' ? 'image/png' : 'image/jpeg';
          const a = document.createElement('a');
          a.download = `${{filename}}.${{format}}`;
          a.href = canvas.toDataURL(mime, 0.98);
          a.click();
        }};
        img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgString);
      }}
    }}

    // Download Both Cards Combined (Side-by-Side)
    function downloadCombined(format) {{
      const svgFront = getCardSVG('front');
      const svgBack = getCardSVG('back');
      const filename = `prabhakala_travels_visiting_cards_pair_${{cardLang}}`;

      const canvas = document.getElementById('exportCanvas');
      canvas.width = 2084;
      canvas.height = 718;
      const ctx = canvas.getContext('2d');

      ctx.fillStyle = '#F4F5F7';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      let loadedCount = 0;
      const imgF = new Image();
      const imgB = new Image();

      function onBothLoaded() {{
        ctx.drawImage(imgF, 30, 40);
        ctx.drawImage(imgB, 1072, 40);
        const mime = format === 'png' ? 'image/png' : 'image/jpeg';
        const a = document.createElement('a');
        a.download = `${{filename}}.${{format}}`;
        a.href = canvas.toDataURL(mime, 0.98);
        a.click();
      }}

      imgF.onload = () => {{ loadedCount++; if (loadedCount === 2) onBothLoaded(); }};
      imgB.onload = () => {{ loadedCount++; if (loadedCount === 2) onBothLoaded(); }};

      imgF.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgFront);
      imgB.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgBack);
    }}

    // Init on Load
    window.addEventListener('DOMContentLoaded', () => {{
      loadSavedCardData();
      refreshCardRenders();
    }});
  </script>

</body>
</html>
'''

# Write to visiting-card.html
with open('/Users/madhavan/.gemini/antigravity/scratch/perambalur-taisor-cabs/visiting-card.html', 'w', encoding='utf-8') as f:
    f.write(get_card_html(relative_prefix=""))

# Write to card.html
with open('/Users/madhavan/.gemini/antigravity/scratch/perambalur-taisor-cabs/card.html', 'w', encoding='utf-8') as f:
    f.write(get_card_html(relative_prefix=""))

# Write to card/index.html
with open('/Users/madhavan/.gemini/antigravity/scratch/perambalur-taisor-cabs/card/index.html', 'w', encoding='utf-8') as f:
    f.write(get_card_html(relative_prefix="../"))

print("Clean Visiting Card Studio created without A4 options!")
