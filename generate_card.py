import os, base64

# Read the logo badge image
logo_badge_path = '/Users/madhavan/.gemini/antigravity/scratch/perambalur-taisor-cabs/assets/prabhakala_logo_badge.jpg'
with open(logo_badge_path, 'rb') as f:
    b64_logo = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

# WhatsApp QR Code Link
wa_link = "https://wa.me/916385300259?text=%E0%AE%B5%E0%AE%A3%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%AE%E0%AF%8D%21%20I%20would%20like%20to%20book%20Prabhakala%20Travels%20cab%20(TN46AK1244)"
qr_img_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&margin=1&data={wa_link.replace('&', '%26')}"

card_html = f'''<!DOCTYPE html>
<html lang="ta">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prabhakala Travels — Luxury Visiting Card (A4 Sheet & PAN Card Size)</title>
  
  <!-- Google Fonts: Plus Jakarta Sans & Noto Sans Tamil -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Tamil:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <style>
    /* PAN Card ISO/IEC 7810 ID-1 standard dimensions */
    :root {{
      --card-w: 85.6mm;
      --card-h: 54.0mm;
      --card-radius: 3.2mm;
    }}

    body {{
      font-family: "Plus Jakarta Sans", "Noto Sans Tamil", sans-serif;
      -webkit-font-smoothing: antialiased;
      background-color: #f3f4f6;
    }}

    /* Standard Card Dimensions */
    .pan-card {{
      width: var(--card-w);
      height: var(--card-h);
      min-width: var(--card-w);
      min-height: var(--card-h);
      max-width: var(--card-w);
      max-height: var(--card-h);
      border-radius: var(--card-radius);
      box-sizing: border-box;
      position: relative;
      overflow: hidden;
    }}

    /* Luxury Light Cream Palette (Matching prabhakala_logo_full.jpg) */
    .light-card-front {{
      background: linear-gradient(135deg, #FFFEFD 0%, #FAF6EE 50%, #F5EEE2 100%);
      border: 1px solid #DFD5C6;
      box-shadow: inset 0 0 0 1px rgba(212, 175, 55, 0.25);
    }}

    .light-card-back {{
      background: linear-gradient(135deg, #FFFFFF 0%, #FBF8F2 60%, #F6EFE3 100%);
      border: 1px solid #DFD5C6;
      box-shadow: inset 0 0 0 1px rgba(212, 175, 55, 0.25);
    }}

    /* A4 Page Formatting for Screen and Print */
    .a4-sheet {{
      width: 210mm;
      min-height: 297mm;
      padding: 8mm 14mm;
      margin: 0 auto 20px auto;
      background: white;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
      box-sizing: border-box;
      display: grid;
      grid-template-columns: repeat(2, 85.6mm);
      gap: 3mm 8mm;
      justify-content: center;
      align-content: start;
    }}

    /* Crop / Cutting Tick Marks */
    .crop-mark-container {{
      position: relative;
      padding: 1.5mm;
    }}
    .crop-mark {{
      position: absolute;
      width: 4mm;
      height: 4mm;
      pointer-events: none;
    }}
    .crop-tl {{
      top: 0; left: 0;
      border-top: 1px dashed #cbd5e1;
      border-left: 1px dashed #cbd5e1;
    }}
    .crop-tr {{
      top: 0; right: 0;
      border-top: 1px dashed #cbd5e1;
      border-right: 1px dashed #cbd5e1;
    }}
    .crop-bl {{
      bottom: 0; left: 0;
      border-bottom: 1px dashed #cbd5e1;
      border-left: 1px dashed #cbd5e1;
    }}
    .crop-br {{
      bottom: 0; right: 0;
      border-bottom: 1px dashed #cbd5e1;
      border-right: 1px dashed #cbd5e1;
    }}

    /* Print Specific Rules */
    @page {{
      size: A4 portrait;
      margin: 6mm 10mm;
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
      .a4-sheet {{
        box-shadow: none !important;
        margin: 0 !important;
        padding: 4mm 10mm !important;
        width: 100% !important;
        min-height: auto !important;
        page-break-after: always;
      }}
      .crop-mark {{
        border-color: #94a3b8 !important;
      }}
      #previewView, #mockupView {{
        display: none !important;
      }}
    }}
  </style>
</head>
<body class="py-6 px-2 sm:px-4 flex flex-col items-center">

  <!-- ================= TOP ACTION BAR & CONTROL PANEL (Hidden on Print) ================= -->
  <header class="no-print max-w-4xl w-full bg-white rounded-2xl shadow-md border border-gray-200 p-4 sm:p-6 mb-6">
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-900 font-extrabold text-[11px] border border-amber-300">
            A4 PRINT SHEET • PAN CARD SIZE (85.6 × 54.0 mm)
          </span>
          <span class="text-xs text-gray-400">•</span>
          <span class="text-xs font-bold text-gray-700">TN 46 AK 1244</span>
        </div>
        <h1 class="text-xl sm:text-2xl font-black text-gray-950 mt-1">
          பிரபாகலா டிராவல்ஸ் — விசிட்டிங் கார்டு வடிவமைப்பு
        </h1>
        <p class="text-xs text-gray-500 font-medium mt-0.5">
          உரிமையாளர்: செல்வபாரதி (Selvabarathi) • டொயோட்டா டெய்சர் (White AC SUV) • பூலாம்பாடி & பெரம்பலூர்
        </p>
      </div>

      <!-- Quick Action Buttons -->
      <div class="flex flex-wrap items-center gap-2 shrink-0">
        <a href="index.html" class="px-3.5 py-2 rounded-xl border border-gray-300 hover:bg-gray-50 text-gray-700 text-xs font-bold transition flex items-center gap-1.5">
          <span>🌐</span>
          <span>வலைப்பக்கம் (Website)</span>
        </a>
        <a href="{wa_link}" target="_blank" class="px-3.5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold shadow-sm transition flex items-center gap-1.5">
          <span>💬</span>
          <span>WhatsApp QR டெஸ்ட்</span>
        </a>
        <button onclick="window.print()" class="px-5 py-2 rounded-xl bg-amber-400 hover:bg-amber-500 text-gray-950 text-xs font-black shadow-md transition flex items-center gap-2">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M19 8H5c-1.66 0-3 1.34-3 3v6h4v4h12v-4h4v-6c0-1.66-1.34-3-3-3zm-3 11H8v-5h8v5zm3-7c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm-1-9H6v4h12V3z"/></svg>
          <span>A4 அச்சிடுக (Print / PDF)</span>
        </button>
      </div>
    </div>

    <!-- Mode Selector Tabs -->
    <div class="mt-4 pt-4 border-t border-gray-100 flex flex-wrap items-center justify-between gap-3 text-xs">
      <div class="flex flex-wrap items-center gap-2">
        <span class="font-bold text-gray-700">பார்வை முறை (View):</span>
        <button id="btnDuplex" onclick="setViewMode('duplex')" class="view-btn px-3 py-1.5 rounded-lg font-bold bg-gray-900 text-white shadow-sm">
          📄 A4 இரட்டைப் பக்கம் (Page 1 Fronts + Page 2 Backs)
        </button>
        <button id="btnSheetPairs" onclick="setViewMode('sheet-pairs')" class="view-btn px-3 py-1.5 rounded-lg font-bold bg-gray-100 text-gray-700 hover:bg-gray-200">
          📄 A4 ஒரு தாள் (5 ஜோடி முன்பின்)
        </button>
        <button id="btnSheetFronts" onclick="setViewMode('sheet-fronts')" class="view-btn px-3 py-1.5 rounded-lg font-bold bg-gray-100 text-gray-700 hover:bg-gray-200">
          📄 A4 (10 முன்பக்கம் மட்டும்)
        </button>
        <button id="btnSheetBacks" onclick="setViewMode('sheet-backs')" class="view-btn px-3 py-1.5 rounded-lg font-bold bg-gray-100 text-gray-700 hover:bg-gray-200">
          📄 A4 (10 பின்பக்கம் மட்டும்)
        </button>
        <button id="btnPreview" onclick="setViewMode('preview')" class="view-btn px-3 py-1.5 rounded-lg font-bold bg-gray-100 text-gray-700 hover:bg-gray-200">
          ✨ கார்டு மாதிரி (Card Preview)
        </button>
        <button id="btnMockup" onclick="setViewMode('mockup')" class="view-btn px-3 py-1.5 rounded-lg font-bold bg-gray-100 text-gray-700 hover:bg-gray-200">
          📸 3D போட்டோ ரியலிஸ்டிக்
        </button>
      </div>

      <div class="text-[11px] text-gray-500 font-medium">
        💡 <strong>பிரிண்டிங் டிப்:</strong> கலர் ஜெராக்ஸ் / பிரிண்டிங் கடையில் <code class="bg-gray-100 px-1 py-0.5 rounded font-bold text-gray-800">300 GSM Matte Cardstock</code> தாளில் பிரிண்ட் எடுக்கலாம்!
      </div>
    </div>
  </header>

  <!-- ================= 3D MOCKUP SHOWCASE (Hidden by default, toggleable) ================= -->
  <div id="mockupView" class="hidden no-print max-w-4xl w-full bg-white rounded-2xl shadow-md border border-gray-200 p-6 mb-8 text-center">
    <div class="mb-4">
      <span class="px-3 py-1 rounded-full bg-amber-100 text-amber-900 text-xs font-black border border-amber-300">
        3D PHOTOREALISTIC LUXURY STATIONERY RENDER
      </span>
      <h2 class="text-xl font-black text-gray-950 mt-2">நேரடி விசிட்டிங் கார்டு 3D மாதிரிக்காட்சி</h2>
      <p class="text-xs text-gray-500">கோல்டு எட்ஜ், எம்போஸ் செய்யப்பட்ட லோகோ மற்றும் மேட் கார்டு பினிஷிங்</p>
    </div>
    <div class="rounded-2xl overflow-hidden shadow-xl border border-gray-200 max-w-3xl mx-auto">
      <img src="assets/visiting_card_light_mockup.jpg" alt="Prabhakala Travels Luxury Visiting Card Mockup" class="w-full h-auto object-cover">
    </div>
    <div class="mt-4 flex items-center justify-center gap-3">
      <button onclick="setViewMode('duplex')" class="px-4 py-2 bg-amber-400 hover:bg-amber-500 text-gray-950 text-xs font-black rounded-xl shadow transition">
        A4 அச்சுத் தாளுக்குத் திரும்பு (Back to A4 Print Sheet)
      </button>
    </div>
  </div>

  <!-- ================= INDIVIDUAL CARDS PREVIEW VIEW (Toggleable) ================= -->
  <div id="previewView" class="hidden no-print max-w-4xl w-full mb-8">
    <div class="flex flex-col md:flex-row items-center justify-center gap-8 bg-white p-8 rounded-3xl shadow-md border border-gray-200">
      <div class="flex flex-col items-center">
        <span class="text-xs font-black uppercase tracking-wider text-gray-500 mb-3">முன்பக்கம் (Front Side • PAN Card Size)</span>
        <div class="crop-mark-container">
          <div id="singleCardFront"></div>
        </div>
      </div>
      <div class="flex flex-col items-center">
        <span class="text-xs font-black uppercase tracking-wider text-gray-500 mb-3">பின்பக்கம் (Back Side • With WhatsApp QR)</span>
        <div class="crop-mark-container">
          <div id="singleCardBack"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- ================= A4 PRINT SHEET CONTAINER(S) ================= -->
  <div id="sheetWrapper" class="w-full flex flex-col items-center">
    <!-- Populated dynamically via JavaScript with exact 10 PAN cards per page -->
  </div>

  <!-- ================= INVISIBLE CARD TEMPLATES (FOR JS POPULATION) ================= -->
  <div style="display: none;">
    
    <!-- FRONT CARD TEMPLATE -->
    <div id="tplCardFront">
      <div class="pan-card light-card-front p-3.5 flex flex-col justify-between select-none relative">
        
        <!-- Subtle Top & Bottom Gold Line Trim -->
        <div class="absolute top-0 left-0 right-0 h-[2px] bg-gradient-to-r from-transparent via-[#C5A059] to-transparent"></div>
        <div class="absolute bottom-0 left-0 right-0 h-[2px] bg-gradient-to-r from-transparent via-[#C5A059] to-transparent"></div>

        <!-- Ambient Luxury Radial Sun Glow -->
        <div class="absolute -top-12 -right-12 w-32 h-32 bg-amber-200/30 rounded-full blur-2xl pointer-events-none"></div>
        <div class="absolute -bottom-12 -left-12 w-32 h-32 bg-amber-200/20 rounded-full blur-2xl pointer-events-none"></div>

        <!-- Top Auspicious & Location Header -->
        <div class="flex items-center justify-between relative z-10 leading-none">
          <span class="text-[7.5px] font-black tracking-widest text-[#B8860B]">
            ॥ ஓம் சக்தி ॥
          </span>
          <span class="text-[7px] font-black tracking-wider px-2 py-0.5 rounded-full bg-[#FAF0D7] text-[#8C620A] border border-[#E8D4A2] uppercase">
            POOLAMBADI • PERAMBALUR
          </span>
        </div>

        <!-- Center: Official Logo Badge & Typography -->
        <div class="flex items-center gap-3 my-auto relative z-10">
          <!-- Official Logo Badge -->
          <div class="w-12 h-12 rounded-xl overflow-hidden shadow-sm border border-[#DCCBB4] bg-white shrink-0 p-0.5">
            <img src="{b64_logo}" alt="Logo" class="w-full h-full object-cover rounded-lg">
          </div>

          <!-- Brand Typography -->
          <div class="flex-1 min-w-0">
            <h2 class="font-black text-[15px] tracking-tight text-[#16191E] leading-tight">
              பிரபாகலா டிராவல்ஸ்
            </h2>
            <div class="flex items-center gap-1.5 mt-0.5">
              <span class="font-black text-[10px] tracking-wider text-[#C58B24] uppercase">
                PRABHAKALA TRAVELS
              </span>
            </div>
            <p class="text-[7.5px] font-semibold text-[#5A5D64] tracking-tight mt-0.5">
              பாரதியார் நினைவில் பாதுகாப்பான பயணம்
            </p>
          </div>
        </div>

        <!-- Bottom Vehicle & Features Pill Strip -->
        <div class="pt-1.5 border-t border-[#E8DFC9] flex items-center justify-between relative z-10 leading-none">
          <div class="flex items-center gap-1 text-[7.5px] font-extrabold text-[#22242A]">
            <span class="text-[#C58B24]">🚘</span>
            <span>White Toyota Taisor (AC SUV)</span>
          </div>

          <!-- Car Number Pill -->
          <div class="px-2 py-0.5 rounded bg-amber-100/90 text-amber-950 font-black text-[8px] border border-amber-300 font-mono tracking-wider">
            TN 46 AK 1244
          </div>
        </div>

      </div>
    </div>

    <!-- BACK CARD TEMPLATE -->
    <div id="tplCardBack">
      <div class="pan-card light-card-back p-3.5 flex flex-col justify-between select-none relative">
        
        <!-- Subtle Top Gold Trim -->
        <div class="absolute top-0 left-0 right-0 h-[2px] bg-gradient-to-r from-transparent via-[#C5A059] to-transparent"></div>

        <!-- Ambient Luxury Radial Glow -->
        <div class="absolute -top-10 -right-10 w-28 h-28 bg-emerald-100/30 rounded-full blur-2xl pointer-events-none"></div>

        <!-- Top Row: Proprietor Details & Reg Number -->
        <div class="flex items-start justify-between relative z-10 leading-tight">
          <div>
            <div class="text-[6.5px] font-bold text-gray-500 uppercase tracking-wider">உரிமையாளர் / Proprietor</div>
            <div class="flex items-baseline gap-1 mt-0.5">
              <h3 class="font-black text-[13px] text-[#16191E] leading-tight">
                செல்வபாரதி
              </h3>
              <span class="text-[8.5px] font-black text-[#C58B24] uppercase">
                (SELVABARATHI)
              </span>
            </div>
          </div>

          <!-- Car Reg Pill & SUV Badge -->
          <div class="text-right">
            <span class="inline-block px-1.5 py-0.5 rounded bg-[#FAF0D7] text-[#8C620A] font-black text-[8px] border border-[#E8D4A2] font-mono tracking-wider">
              TN 46 AK 1244
            </span>
            <span class="text-[6.5px] text-gray-500 font-semibold block mt-0.5">White Toyota Taisor AC SUV</span>
          </div>
        </div>

        <!-- Middle Content: Contact Numbers + Service Locations + WhatsApp QR -->
        <div class="grid grid-cols-12 gap-1.5 my-auto items-center relative z-10 pt-0.5">
          
          <!-- Left Details (8.5 cols) -->
          <div class="col-span-8 space-y-1 text-[7.5px]">
            
            <!-- Phone / WhatsApp Direct Line -->
            <div class="flex items-center gap-1.5 bg-[#FAF7F0] p-1 rounded-lg border border-[#EBE3D3]">
              <span class="w-4 h-4 rounded-full bg-emerald-600 text-white flex items-center justify-center text-[8px] font-black shrink-0">📞</span>
              <div class="leading-none">
                <a href="tel:+916385300259" class="font-black text-[10.5px] text-[#16191E] tracking-tight hover:underline">+91 6385300259</a>
                <span class="text-[6.5px] text-emerald-800 font-bold block mt-0.5">WhatsApp & நேரடி அழைப்பு (24/7)</span>
              </div>
            </div>

            <!-- Hub & Key Routes -->
            <div class="flex items-start gap-1 leading-tight text-[#3A3D44]">
              <span class="text-[#C58B24] shrink-0 font-bold">📍</span>
              <span class="text-[7px] font-bold">
                <strong>பூலாம்பாடி & பெரம்பலூர்</strong> ⇄ திருச்சி ஏர்போர்ட், சென்னை, பெங்களூர், மதுரை, கோவை, திருப்பதி.
              </span>
            </div>

            <!-- Guarantee Note -->
            <div class="flex items-center gap-1 text-[6.8px] font-semibold text-gray-500">
              <span class="text-amber-600 font-bold">✦</span>
              <span>100% சொன்ன நேரத்தில் பிக்-அப் • குடும்பப் பயணம்</span>
            </div>

          </div>

          <!-- Right Column: WhatsApp QR Code (3.5 cols) -->
          <div class="col-span-4 flex flex-col items-center justify-center text-center">
            <a href="{wa_link}" target="_blank" title="Click to test WhatsApp chat" class="block w-[46px] h-[46px] p-0.5 bg-white border border-gray-300 rounded-lg shadow-sm hover:border-emerald-500 transition">
              <img src="{qr_img_url}" alt="WhatsApp QR" class="w-full h-full object-contain rounded">
            </a>
            <span class="text-[6px] font-black text-emerald-700 tracking-wider uppercase mt-0.5 flex items-center gap-0.5">
              <span>💬</span>
              <span>WhatsApp QR</span>
            </span>
          </div>

        </div>

        <!-- Bottom Base Town & Slogan -->
        <div class="pt-1 border-t border-[#E8DFC9] flex items-center justify-between text-[6.5px] font-bold text-gray-500 relative z-10 leading-none">
          <span>🏡 பூலாம்பாடி, பெரம்பலூர் மாவட்டம்</span>
          <span class="text-[#C58B24]">பாதுகாப்பான பயணம்</span>
        </div>

      </div>
    </div>

  </div>

  <!-- ================= JAVASCRIPT LOGIC ================= -->
  <script>
    const tplFront = document.getElementById('tplCardFront').innerHTML;
    const tplBack = document.getElementById('tplCardBack').innerHTML;

    function renderCard(type) {{
      const wrapper = document.createElement('div');
      wrapper.className = 'crop-mark-container';
      wrapper.innerHTML = `
        <div class="crop-mark crop-tl"></div>
        <div class="crop-mark crop-tr"></div>
        <div class="crop-mark crop-bl"></div>
        <div class="crop-mark crop-br"></div>
        ${{type === 'front' ? tplFront : tplBack}}
      `;
      return wrapper;
    }}

    function populateA4Sheet(mode) {{
      const wrapper = document.getElementById('sheetWrapper');
      wrapper.innerHTML = '';

      if (mode === 'duplex') {{
        // Page 1: 10 Front sides
        const sheet1 = document.createElement('div');
        sheet1.className = 'a4-sheet';
        for (let i = 0; i < 10; i++) {{
          sheet1.appendChild(renderCard('front'));
        }}
        wrapper.appendChild(sheet1);

        // Page 2: 10 Back sides
        const sheet2 = document.createElement('div');
        sheet2.className = 'a4-sheet';
        for (let i = 0; i < 10; i++) {{
          sheet2.appendChild(renderCard('back'));
        }}
        wrapper.appendChild(sheet2);
      }} else if (mode === 'sheet-pairs') {{
        // 1 sheet with 5 Fronts & 5 Backs side-by-side
        const sheet = document.createElement('div');
        sheet.className = 'a4-sheet';
        for (let i = 0; i < 5; i++) {{
          sheet.appendChild(renderCard('front'));
          sheet.appendChild(renderCard('back'));
        }}
        wrapper.appendChild(sheet);
      }} else if (mode === 'sheet-fronts') {{
        // 1 sheet with 10 Front sides
        const sheet = document.createElement('div');
        sheet.className = 'a4-sheet';
        for (let i = 0; i < 10; i++) {{
          sheet.appendChild(renderCard('front'));
        }}
        wrapper.appendChild(sheet);
      }} else if (mode === 'sheet-backs') {{
        // 1 sheet with 10 Back sides
        const sheet = document.createElement('div');
        sheet.className = 'a4-sheet';
        for (let i = 0; i < 10; i++) {{
          sheet.appendChild(renderCard('back'));
        }}
        wrapper.appendChild(sheet);
      }}
    }}

    function setViewMode(mode) {{
      // Reset button styles
      document.querySelectorAll('.view-btn').forEach(btn => {{
        btn.className = 'view-btn px-3 py-1.5 rounded-lg font-bold bg-gray-100 text-gray-700 hover:bg-gray-200 transition';
      }});

      const sheetWrapper = document.getElementById('sheetWrapper');
      const previewView = document.getElementById('previewView');
      const mockupView = document.getElementById('mockupView');

      sheetWrapper.classList.add('hidden');
      previewView.classList.add('hidden');
      mockupView.classList.add('hidden');

      if (mode === 'preview') {{
        document.getElementById('btnPreview').className = 'view-btn px-3 py-1.5 rounded-lg font-bold bg-gray-900 text-white shadow-sm';
        previewView.classList.remove('hidden');
      }} else if (mode === 'mockup') {{
        document.getElementById('btnMockup').className = 'view-btn px-3 py-1.5 rounded-lg font-bold bg-gray-900 text-white shadow-sm';
        mockupView.classList.remove('hidden');
      }} else {{
        sheetWrapper.classList.remove('hidden');
        if (mode === 'duplex') {{
          document.getElementById('btnDuplex').className = 'view-btn px-3 py-1.5 rounded-lg font-bold bg-gray-900 text-white shadow-sm';
        }} else if (mode === 'sheet-pairs') {{
          document.getElementById('btnSheetPairs').className = 'view-btn px-3 py-1.5 rounded-lg font-bold bg-gray-900 text-white shadow-sm';
        }} else if (mode === 'sheet-fronts') {{
          document.getElementById('btnSheetFronts').className = 'view-btn px-3 py-1.5 rounded-lg font-bold bg-gray-900 text-white shadow-sm';
        }} else if (mode === 'sheet-backs') {{
          document.getElementById('btnSheetBacks').className = 'view-btn px-3 py-1.5 rounded-lg font-bold bg-gray-900 text-white shadow-sm';
        }}
        populateA4Sheet(mode);
      }}
    }}

    // Init on load
    window.addEventListener('DOMContentLoaded', () => {{
      document.getElementById('singleCardFront').innerHTML = tplFront;
      document.getElementById('singleCardBack').innerHTML = tplBack;
      setViewMode('duplex');
    }});
  </script>

</body>
</html>
'''

visiting_card_file = '/Users/madhavan/.gemini/antigravity/scratch/perambalur-taisor-cabs/visiting-card.html'
with open(visiting_card_file, 'w', encoding='utf-8') as f:
    f.write(card_html)

print("Regenerated visiting-card.html with Duplex mode and A4 sheets successfully!")
