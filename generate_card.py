import os, base64

# Read the logo badge image
logo_badge_path = '/Users/madhavan/.gemini/antigravity/scratch/perambalur-taisor-cabs/assets/prabhakala_logo_badge.jpg'
with open(logo_badge_path, 'rb') as f:
    b64_logo = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

# Read the car image
car_path = '/Users/madhavan/.gemini/antigravity/scratch/perambalur-taisor-cabs/assets/toyota_taisor_hero.jpg'
with open(car_path, 'rb') as f:
    b64_car = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

card_html = f'''<!DOCTYPE html>
<html lang="ta">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prabhakala Travels — Visiting Card (Selvabarathi)</title>
  
  <!-- Google Fonts: Plus Jakarta Sans & Noto Sans Tamil -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Tamil:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>

  <style>
    @page {{
      size: 3.5in 2in;
      margin: 0;
    }}
    body {{
      font-family: "Plus Jakarta Sans", "Noto Sans Tamil", sans-serif;
      -webkit-font-smoothing: antialiased;
    }}
    .card-dimension {{
      width: 3.5in;
      height: 2in;
      min-width: 3.5in;
      min-height: 2in;
    }}
    @media print {{
      body {{
        background: transparent;
        padding: 0;
      }}
      .no-print {{
        display: none !important;
      }}
      .print-card {{
        page-break-after: always;
        box-shadow: none !important;
        border: none !important;
      }}
    }}
  </style>
</head>
<body class="bg-gray-100 min-h-screen py-10 px-4 flex flex-col items-center justify-center">

  <!-- TOP ACTION BAR (Hidden on print) -->
  <div class="no-print max-w-2xl w-full flex items-center justify-between mb-8 bg-white p-4 rounded-2xl shadow-sm border border-gray-200">
    <div>
      <h1 class="font-black text-lg text-gray-900">Visiting Card Design • பிரபாகலா டிராவல்ஸ்</h1>
      <p class="text-xs text-gray-500 font-medium">Standard 3.5" × 2" Print Size • Front & Back Design</p>
    </div>
    <div class="flex items-center gap-3">
      <button onclick="window.print()" class="px-5 py-2.5 rounded-xl bg-amber-400 hover:bg-amber-500 text-gray-950 font-black text-xs shadow-md transition-all flex items-center gap-2">
        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M19 8H5c-1.66 0-3 1.34-3 3v6h4v4h12v-4h4v-6c0-1.66-1.34-3-3-3zm-3 11H8v-5h8v5zm3-7c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm-1-9H6v4h12V3z"/></svg>
        <span>Print / Save PDF (அச்சிடுக)</span>
      </button>
    </div>
  </div>

  <div class="flex flex-col md:flex-row items-center justify-center gap-8">

    <!-- ================= FRONT SIDE (LUXURY GOLD & ONYX BLACK) ================= -->
    <div class="flex flex-col items-center">
      <span class="no-print text-xs font-black uppercase tracking-widest text-gray-400 mb-2">Front Side (முன்பக்கம்)</span>
      
      <div class="card-dimension print-card bg-gradient-to-br from-[#121316] via-[#1a1c22] to-[#0a0a0c] text-white rounded-2xl p-5 shadow-2xl relative overflow-hidden flex flex-col justify-between border border-gray-800">
        
        <!-- Subtle Gold Geometric Ambient Glow -->
        <div class="absolute -top-10 -right-10 w-36 h-36 bg-[#FFC802]/15 rounded-full blur-3xl pointer-events-none"></div>
        <div class="absolute -bottom-10 -left-10 w-36 h-36 bg-[#FFC802]/10 rounded-full blur-3xl pointer-events-none"></div>
        
        <!-- Gold Accent Line -->
        <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-transparent via-[#FFC802] to-transparent"></div>

        <!-- Top Header: Auspicious Om / Pill Tag -->
        <div class="flex items-center justify-between relative z-10">
          <span class="text-[9px] font-bold tracking-widest text-[#FFC802] uppercase">॥ ஓம் சக்தி ॥</span>
          <span class="text-[8px] font-black tracking-widest px-2 py-0.5 rounded-full bg-[#FFC802]/20 text-[#FFC802] border border-[#FFC802]/40 uppercase">
            POOLAMBADI • PERAMBALUR
          </span>
        </div>

        <!-- Center: Official Logo & Brand Name -->
        <div class="flex items-center gap-3.5 my-auto relative z-10">
          <!-- Logo Badge -->
          <div class="w-14 h-14 rounded-2xl overflow-hidden shadow-lg border border-amber-400/50 bg-[#121316] shrink-0 p-0.5">
            <img src="{b64_logo}" alt="Logo" class="w-full h-full object-cover rounded-xl">
          </div>
          
          <!-- Typography -->
          <div>
            <h2 class="font-black text-xl tracking-tight text-white leading-tight">
              பிரபாகலா டிராவல்ஸ்
            </h2>
            <h3 class="font-black text-xs tracking-widest text-[#FFC802] uppercase mt-0.5">
              PRABHAKALA TRAVELS
            </h3>
            <p class="text-[8px] font-medium text-gray-400 tracking-wider mt-1">
              பாரதியார் நினைவில் பாதுகாப்பான பயணம்
            </p>
          </div>
        </div>

        <!-- Bottom Feature Bar -->
        <div class="pt-2 border-t border-gray-800 flex items-center justify-between text-[8px] font-bold text-gray-300 relative z-10">
          <span class="flex items-center gap-1"><span class="text-[#FFC802]">✦</span> White Toyota Taisor (AC SUV)</span>
          <span class="flex items-center gap-1"><span class="text-[#FFC802]">✦</span> 24/7 Service</span>
          <span class="flex items-center gap-1 text-[#25D366]">● 6385300259</span>
        </div>

      </div>
    </div>

    <!-- ================= BACK SIDE (CONTACT & DETAILS) ================= -->
    <div class="flex flex-col items-center">
      <span class="no-print text-xs font-black uppercase tracking-widest text-gray-400 mb-2">Back Side (பின்பக்கம்)</span>
      
      <div class="card-dimension print-card bg-white text-gray-900 rounded-2xl p-5 shadow-2xl relative overflow-hidden flex flex-col justify-between border border-gray-200">
        
        <!-- Top Left Corner Gold Accent -->
        <div class="absolute top-0 right-0 w-24 h-24 bg-gradient-to-bl from-amber-100/60 to-transparent rounded-bl-full pointer-events-none"></div>

        <!-- Top Row: Person Name & Vehicle Tag -->
        <div class="flex items-start justify-between relative z-10">
          <div>
            <div class="text-[9px] font-bold text-gray-400 uppercase tracking-wider">உரிமையாளர் / Proprietor</div>
            <h3 class="font-black text-lg text-gray-950 leading-tight mt-0.5">
              செல்வபாரதி
            </h3>
            <span class="font-extrabold text-[10px] text-amber-600 block">
              SELVABARATHI
            </span>
          </div>

          <!-- Car Icon/Tag -->
          <div class="text-right">
            <span class="inline-flex items-center gap-1 text-[8px] font-black px-2 py-0.5 rounded-full bg-amber-50 text-amber-900 border border-amber-200">
              🚘 Toyota Taisor SUV
            </span>
            <span class="text-[8px] text-gray-400 font-medium block mt-0.5">குளிர் ஏசி • 190mm மேடு</span>
          </div>
        </div>

        <!-- Middle: Contact Numbers & Routes -->
        <div class="grid grid-cols-12 gap-2 my-auto items-center relative z-10 pt-1">
          
          <!-- Left Details (8 cols) -->
          <div class="col-span-8 space-y-1.5 text-[9px]">
            <!-- Phone / WhatsApp -->
            <div class="flex items-center gap-2">
              <span class="w-5 h-5 rounded-lg bg-emerald-500 text-white flex items-center justify-center text-[10px] shrink-0 font-bold">📞</span>
              <div>
                <a href="tel:+916385300259" class="font-black text-xs text-gray-950 hover:underline">+91 6385300259</a>
                <span class="text-[8px] text-gray-500 block">WhatsApp & நேரடி அழைப்பு</span>
              </div>
            </div>

            <!-- Services -->
            <div class="flex items-start gap-2 pt-0.5">
              <span class="w-5 h-5 rounded-lg bg-amber-400 text-gray-950 flex items-center justify-center text-[10px] shrink-0 font-bold">📍</span>
              <div class="text-[8px] leading-tight text-gray-700 font-semibold">
                சென்னை, திருச்சி ஏர்போர்ட், பெங்களூர், மதுரை, கோவை, திருப்பதி & அனைத்து ஊர்களுக்கும்.
              </div>
            </div>
          </div>

          <!-- Right: WhatsApp QR Code (4 cols) -->
          <div class="col-span-4 flex flex-col items-center justify-center text-center">
            <div class="w-14 h-14 p-1 bg-white border border-gray-200 rounded-xl shadow-sm flex items-center justify-center">
              <img src="https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=https%3A%2F%2Fwa.me%2F916385300259" alt="Scan to WhatsApp" class="w-full h-full object-contain">
            </div>
            <span class="text-[7px] font-bold text-gray-400 tracking-wider uppercase mt-1">Scan to Book</span>
          </div>

        </div>

        <!-- Bottom: Base Address & Trust Assurance -->
        <div class="pt-1.5 border-t border-gray-100 flex items-center justify-between text-[8px] font-semibold text-gray-500 relative z-10">
          <span>🏡 பூலாம்பாடி & பெரம்பலூர்</span>
          <span class="text-amber-600 font-black">100% சொன்ன நேரத்தில் உறுதி</span>
        </div>

      </div>
    </div>

  </div>

  <!-- HELPFUL PRINT TIP (Hidden on print) -->
  <div class="no-print mt-8 text-center text-xs text-gray-500 max-w-md">
    💡 <strong>அச்சிடும் குறிப்பு:</strong> இந்த பக்கத்தை <kbd class="px-1.5 py-0.5 bg-gray-200 rounded text-gray-800 font-mono text-[11px]">Cmd + P</kbd> செய்து "Save as PDF" தேர்வு செய்யவும். எந்தவொரு விசிட்டிங் கார்டு பிரிண்டிங் பிரஸ்ஸிலும் கொடுத்து உடனே அச்சிடலாம்!
  </div>

</body>
</html>
'''

visiting_card_file = '/Users/madhavan/.gemini/antigravity/scratch/perambalur-taisor-cabs/visiting-card.html'
with open(visiting_card_file, 'w', encoding='utf-8') as f:
    f.write(card_html)

print("Created visiting-card.html successfully!")
