import os, base64

# Read base64 assets
logo_badge_path = '/Users/madhavan/.gemini/antigravity/scratch/perambalur-taisor-cabs/assets/prabhakala_logo_badge.jpg'
with open(logo_badge_path, 'rb') as f:
    b64_logo_badge = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

car_hero_path = '/Users/madhavan/.gemini/antigravity/scratch/perambalur-taisor-cabs/assets/toyota_taisor_hero.jpg'
with open(car_hero_path, 'rb') as f:
    b64_car_hero = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="ta" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>PKS Travels — Premier Cab Service | White Toyota Taisor SUV (TN 46 AK 1244)</title>
  <meta name="description" content="Official cab service by Selvabarathi. Clean White Toyota Urban Cruiser Taisor AC SUV (TN46AK1244). Doorstep pickup from Perambalur district to Chennai, Trichy, Bangalore, Coimbatore, Madurai & all destinations.">
  
  <!-- Google Fonts: Plus Jakarta Sans & Noto Sans Tamil -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Tamil:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- Tailwind Config -->
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              yellow: '#FFC802',
              yellowHover: '#E5B400',
              yellowLight: '#FFF9E5',
              dark: '#121316',
              grayLight: '#F4F5F7',
              whatsapp: '#25D366',
              whatsappDark: '#1EBE5D'
            }}
          }},
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', '"Noto Sans Tamil"', 'system-ui', 'sans-serif'],
            tamil: ['"Noto Sans Tamil"', '"Plus Jakarta Sans"', 'sans-serif']
          }},
          boxShadow: {{
            'bento': '0 10px 30px -5px rgba(0, 0, 0, 0.05), 0 4px 12px -2px rgba(0, 0, 0, 0.025)',
            'wa': '0 8px 24px -4px rgba(37, 211, 102, 0.35)'
          }}
        }}
      }}
    }}
  </script>

  <style>
    /* Strict Mobile Viewport Safety - Prevents ANY horizontal scroll blowout */
    html, body {{
      overflow-x: hidden;
      max-width: 100vw;
      width: 100%;
    }}
    * {{
      box-sizing: border-box;
    }}
    body {{
      font-family: "Plus Jakarta Sans", "Noto Sans Tamil", sans-serif;
      -webkit-font-smoothing: antialiased;
      line-height: 1.5;
      word-break: normal;
      overflow-wrap: break-word;
    }}
    .no-scrollbar::-webkit-scrollbar {{
      display: none;
    }}
    .no-scrollbar {{
      -ms-overflow-style: none;
      scrollbar-width: none;
    }}
    .glow-pedestal {{
      box-shadow: 0 0 60px 10px rgba(255, 200, 2, 0.35);
    }}
    .tactile-btn:active {{
      transform: scale(0.97);
    }}
  </style>
</head>
<body class="bg-[#F8F9FA] text-brand-dark min-h-screen flex flex-col antialiased selection:bg-brand-yellow selection:text-brand-dark pb-20 md:pb-8">

  <!-- ================= TOP NOTIFICATION / TRUST BAR ================= -->
  <div class="bg-brand-dark text-white text-[11px] sm:text-xs py-2 px-3 sm:px-4 text-center font-medium w-full overflow-hidden">
    <div class="max-w-7xl mx-auto flex items-center justify-center gap-1.5 sm:gap-2 flex-wrap leading-relaxed">
      <span class="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-ping shrink-0"></span>
      <span class="lang-text" data-ta="பெரம்பலூர் மாவட்டத்தின் பிரத்யேக கார் சேவை" data-en="Exclusive Cab Service in Perambalur District">
        பெரம்பலூர் மாவட்டத்தின் பிரத்யேக கார் சேவை
      </span>
      <span class="text-gray-400 hidden xs:inline">•</span>
      <span class="text-brand-yellow font-bold lang-text" data-ta="100% சொன்ன நேரத்தில் புறப்பாடு • TN 46 AK 1244" data-en="100% Punctual Doorstep Pickup • TN 46 AK 1244">
        100% சொன்ன நேரத்தில் புறப்பாடு • TN 46 AK 1244
      </span>
    </div>
  </div>

  <!-- ================= RESPONSIVE NAVIGATION ================= -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-gray-100 shadow-sm py-2.5 sm:py-3.5">
    <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8 flex items-center justify-between gap-2">
      
      <!-- Brand Logo & Title: Clean, never-truncated on mobile -->
      <a href="#" class="flex items-center gap-2.5 sm:gap-3 group min-w-0 flex-1">
        <!-- Logo Badge -->
        <div class="w-10 h-10 sm:w-12 sm:h-12 rounded-xl sm:rounded-2xl overflow-hidden shadow-sm border border-amber-300 bg-amber-50 shrink-0">
          <img src="{b64_logo_badge}" alt="PKS Travels Logo" class="w-full h-full object-cover">
        </div>
        
        <!-- Text Group (Flexible, legible, never wraps messily) -->
        <div class="min-w-0 flex-1">
          <div class="flex items-center gap-1.5">
            <span class="font-black text-base sm:text-xl md:text-2xl tracking-tight text-brand-dark leading-tight whitespace-nowrap lang-text" data-ta="PKS டிராவல்ஸ்" data-en="PKS TRAVELS">
              PKS டிராவல்ஸ்
            </span>
            <span class="hidden sm:inline-block text-[10px] font-black tracking-wider px-2 py-0.5 rounded-md bg-brand-yellow text-brand-dark shrink-0 lang-text" data-ta="பெரம்பலூர் மாவட்டம்" data-en="Perambalur District">
              பெரம்பலூர் மாவட்டம்
            </span>
          </div>
          <p class="text-[11px] sm:text-xs text-gray-500 font-semibold leading-tight mt-0.5 truncate lang-text" data-ta="பெரம்பலூர் மாவட்டம் • TN 46 AK 1244" data-en="Perambalur District • TN 46 AK 1244">
            பெரம்பலூர் மாவட்டம் • TN 46 AK 1244
          </p>
        </div>
      </a>

      <!-- Quick Action Buttons -->
      <div class="flex items-center gap-1.5 sm:gap-3 shrink-0">
        <!-- Language Switcher: Big, accessible pill -->
        <button id="langToggleBtn" onclick="toggleLanguage()" class="px-3 sm:px-4 py-1.5 sm:py-2 rounded-full border-2 border-brand-yellow/60 text-xs font-black text-brand-dark bg-brand-yellowLight hover:bg-brand-yellow flex items-center gap-1.5 tactile-btn shadow-sm transition-colors cursor-pointer">
          <span>🌐</span>
          <span id="langText" class="text-xs font-black">English</span>
        </button>

        <!-- Call Button (Desktop / Tablet) -->
        <a href="tel:+916385300259" class="hidden md:flex items-center gap-2 px-3.5 py-2 rounded-full bg-brand-grayLight hover:bg-gray-200 text-brand-dark font-bold text-xs tactile-btn border border-gray-200">
          <svg class="w-3.5 h-3.5 text-brand-dark" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24 11.72 11.72 0 003.68.59 1 1 0 011 1v3.5a1 1 0 01-1 1A16 16 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.72 11.72 0 00.59 3.68 1 1 0 01-.24 1.02l-2.23 2.09z"/></svg>
          <span>6385300259</span>
        </a>

        <!-- WhatsApp Quick Link (Desktop & Tablet only, hidden on mobile) -->
        <a href="https://api.whatsapp.com/send?phone=916385300259&text=%E0%AE%B5%E0%AE%A3%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%AE%E0%AF%8D!%20I%20want%20to%20enquire%20about%20booking%20a%20cab%20with%20PKS%20Travels." target="_blank" class="hidden sm:flex px-3.5 py-2 rounded-full bg-brand-whatsapp hover:bg-brand-whatsappDark text-white font-bold text-xs shadow-wa tactile-btn items-center gap-1.5">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.007c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86.174.086.275.072.376-.043.101-.116.433-.506.549-.68.116-.173.231-.145.39-.086s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.099.824zm-3.423-14.416c-6.627 0-12 5.373-12 12 0 2.159.57 4.184 1.564 5.938l-1.564 5.714 5.86-1.537c1.704.931 3.659 1.473 5.74 1.473 6.627 0 12-5.373 12-12s-5.373-12-12-12z"/></svg>
          <span>WhatsApp</span>
        </a>
      </div>

    </div>
  </header>

  <!-- ================= HERO & MAIN CONTENT ================= -->
  <main class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 pt-5 md:pt-10 w-full min-w-0">

    <!-- Top Headline Banner -->
    <div class="text-center max-w-3xl mx-auto mb-6 sm:mb-8">
      
      <!-- Sleek Hero Pill Tag -->
      <div class="inline-flex items-center justify-center gap-1.5 px-4 py-1.5 rounded-full bg-brand-yellowLight border border-brand-yellow/50 text-brand-dark text-xs sm:text-sm font-bold mb-3 shadow-sm text-center">
        <span>✨</span>
        <span class="lang-text" data-ta="பிரீமியர் கார் சேவை" data-en="Premier Cab Service">
          பிரீமியர் கார் சேவை
        </span>
      </div>
      
      <!-- Main Headline with generous line-height for Tamil characters -->
      <h1 class="text-2xl sm:text-4xl md:text-5xl font-black text-brand-dark tracking-tight leading-[1.3] sm:leading-tight px-1 break-words">
        <span class="lang-text" data-ta="உங்கள் சொந்த கார் போல ஒரு நிம்மதியான பயணம்!" data-en="Comfortable & Safe Rides Like Your Own Family Car!">
          உங்கள் சொந்த கார் போல ஒரு நிம்மதியான பயணம்!
        </span>
      </h1>
      
      <!-- Subtitle -->
      <p class="mt-2.5 sm:mt-3 text-xs sm:text-base text-gray-600 font-medium max-w-2xl mx-auto leading-relaxed px-2 break-words">
        <span class="lang-text" 
          data-ta="பெரம்பலூர் மாவட்டத்திலிருந்து சென்னை, திருச்சி, பெங்களூர், கோவை, மதுரை & அனைத்து ஊர்களுக்கும் 100% சொன்ன நேரத்தில் புறப்படும் நம்பகமான ஏசி கார்." 
          data-en="Doorstep pickup from Perambalur district to Chennai, Trichy, Bangalore, Coimbatore, Madurai & all destinations with 100% on-time guarantee.">
          பெரம்பலூர் மாவட்டத்திலிருந்து சென்னை, திருச்சி, பெங்களூர், கோவை, மதுரை & அனைத்து ஊர்களுக்கும் 100% சொன்ன நேரத்தில் புறப்படும் நம்பகமான ஏசி கார்.
        </span>
      </p>
    </div>

    <!-- MAIN GRID: Left (Interactive IndiGo-Style Booking Engine) | Right (Toyota Taisor 3D Showcase & Bento Stats) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-8 items-start w-full min-w-0">

      <!-- ================= LEFT: INDIGO-STYLE BOOKING WIDGET (7 COLS) ================= -->
      <div class="lg:col-span-7 bg-white rounded-3xl p-4 sm:p-7 shadow-bento border border-gray-100 min-w-0 w-full overflow-hidden lg:sticky lg:top-24 self-start">
        
        <!-- Booking Card Header -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-gray-100 mb-5">
          
          <div class="flex items-center gap-2.5 min-w-0">
            <span class="w-9 h-9 rounded-xl bg-brand-yellow flex items-center justify-center font-bold text-base shrink-0">✈️</span>
            <div class="min-w-0">
              <h2 class="font-black text-base sm:text-xl text-brand-dark leading-tight lang-text" data-ta="எளிதான முன்பதிவு" data-en="Instant Cab Booking">
                எளிதான முன்பதிவு
              </h2>
              <p class="text-[11px] sm:text-xs text-gray-500 font-medium truncate lang-text" data-ta="விவரங்களை தேர்வு செய்து வாட்ஸ்அப்பில் புக் செய்க" data-en="Select details & confirm via WhatsApp">
                விவரங்களை தேர்வு செய்து வாட்ஸ்அப்பில் புக் செய்க
              </p>
            </div>
          </div>
          
          <!-- Route Type Pill Toggles -->
          <div class="inline-flex p-1 rounded-2xl bg-gray-100 border border-gray-200 self-start sm:self-auto w-full sm:w-auto">
            <button type="button" id="tripOneWay" onclick="setTripType('oneway')" class="flex-1 sm:flex-initial px-4 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all bg-brand-yellow text-brand-dark shadow-sm text-center cursor-pointer">
              <span class="lang-text" data-ta="ஒரு வழி" data-en="One-Way">ஒரு வழி</span>
            </button>
            <button type="button" id="tripRound" onclick="setTripType('round')" class="flex-1 sm:flex-initial px-4 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all text-gray-600 hover:text-brand-dark text-center cursor-pointer">
              <span class="lang-text" data-ta="இரு வழி" data-en="Round-Trip">இரு வழி</span>
            </button>
          </div>

        </div>

        <!-- Interactive Form Fields -->
        <form id="bookingForm" onsubmit="handleBookingSubmit(event)" class="space-y-5">

          <!-- STEP 1: PICKUP & DROP CITIES -->
          <div class="space-y-2.5 sm:space-y-3">
            
            <div class="flex items-center justify-between gap-2 flex-wrap">
              <label class="text-[11px] sm:text-xs font-black uppercase tracking-wider text-gray-500 flex items-center gap-1.5">
                <span class="lang-text" data-ta="📍 வழித்தடம் விவரங்கள்" data-en="📍 Route Details">📍 வழித்தடம் விவரங்கள்</span>
                <span class="text-gray-400 font-normal">/ Pickup & Drop</span>
              </label>
              
              <span id="routeDistanceBadge" class="inline-flex items-center gap-1 text-[11px] sm:text-xs font-black px-2.5 py-1 rounded-full bg-amber-50 text-amber-900 border border-amber-200 shrink-0">
                🛣️ <span id="distKMText">~270 KM</span>
              </span>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 sm:gap-3">
              <!-- FROM (Default Perambalur / Poolambadi) -->
              <div class="relative bg-brand-grayLight/80 hover:bg-brand-grayLight p-3 sm:p-3.5 rounded-2xl border border-gray-200 focus-within:border-brand-yellow focus-within:bg-white transition-all min-w-0">
                <span class="text-[10px] font-black uppercase text-gray-400 tracking-wider block lang-text" data-ta="புறப்படும் இடம் (From)" data-en="Pickup Location (From)">
                  புறப்படும் இடம் (From)
                </span>
                <div class="flex items-center gap-2 mt-1 min-w-0">
                  <span class="text-emerald-500 font-bold text-base sm:text-lg shrink-0">🟢</span>
                  <select id="pickupCity" onchange="calculateRoute()" class="w-full max-w-full bg-transparent font-bold text-sm sm:text-base text-brand-dark focus:outline-none cursor-pointer truncate">
                    <!-- Populated dynamically via JS -->
                  </select>
                </div>
              </div>

              <!-- TO (Destination) -->
              <div class="relative bg-brand-grayLight/80 hover:bg-brand-grayLight p-3 sm:p-3.5 rounded-2xl border border-gray-200 focus-within:border-brand-yellow focus-within:bg-white transition-all min-w-0">
                <span class="text-[10px] font-black uppercase text-gray-400 tracking-wider block lang-text" data-ta="செல்லும் இடம் (Destination)" data-en="Drop Location (To)">
                  செல்லும் இடம் (Destination)
                </span>
                <div class="flex items-center gap-2 mt-1 min-w-0">
                  <span class="text-rose-500 font-bold text-base sm:text-lg shrink-0">🏁</span>
                  <select id="dropCity" onchange="calculateRoute()" class="w-full max-w-full bg-transparent font-bold text-sm sm:text-base text-brand-dark focus:outline-none cursor-pointer truncate">
                    <!-- Populated dynamically via JS -->
                  </select>
                </div>
              </div>
            </div>

            <!-- Custom Pickup Text Input (Reveals when Custom is selected) -->
            <div id="customPickupContainer" class="hidden mt-2">
              <input type="text" id="customPickupInput" oninput="calculateRoute()" placeholder="புறப்படும் ஊர் அல்லது முகவரி உள்ளிடவும் (e.g. தெரு / லேண்ட்மார்க்)..." class="w-full p-3 rounded-2xl border border-gray-200 text-xs sm:text-sm font-semibold focus:outline-none focus:border-brand-yellow bg-gray-50 focus:bg-white transition-all shadow-inner">
            </div>

            <!-- Custom Destination Text Input (Reveals when Custom is selected) -->
            <div id="customDropContainer" class="hidden mt-2">
              <input type="text" id="customDropInput" oninput="calculateRoute()" placeholder="செல்லும் ஊரின் பெயரை உள்ளிடவும் (Enter Destination City / Town)..." class="w-full p-3 rounded-2xl border border-gray-200 text-xs sm:text-sm font-semibold focus:outline-none focus:border-brand-yellow bg-gray-50 focus:bg-white transition-all shadow-inner">
            </div>

            <!-- Quick Route Preset Chips -->
            <div class="pt-1">
              <span class="text-[11px] font-bold text-gray-400 block mb-1.5 lang-text" data-ta="அடிக்கடி செல்லும் வழித்தடங்கள் / Quick Routes:" data-en="Popular Quick Routes:">
                அடிக்கடி செல்லும் வழித்தடங்கள் / Quick Routes:
              </span>
              <div class="flex items-center gap-1.5 overflow-x-auto pb-1 no-scrollbar -mx-1 px-1">
                <button type="button" onclick="quickSelectRoute('Perambalur', 'Chennai')" class="shrink-0 px-3 py-1 rounded-full text-xs font-bold bg-gray-100 hover:bg-brand-yellow hover:text-brand-dark transition-colors cursor-pointer border border-gray-200">
                  📍 <span class="lang-text" data-ta="சென்னை (270 km)" data-en="Chennai (270 km)">சென்னை (270 km)</span>
                </button>
                <button type="button" onclick="quickSelectRoute('Perambalur', 'Trichy Airport')" class="shrink-0 px-3 py-1 rounded-full text-xs font-bold bg-gray-100 hover:bg-brand-yellow hover:text-brand-dark transition-colors cursor-pointer border border-gray-200">
                  ✈️ <span class="lang-text" data-ta="திருச்சி ஏர்போர்ட் (55 km)" data-en="Trichy Airport (55 km)">திருச்சி ஏர்போர்ட் (55 km)</span>
                </button>
                <button type="button" onclick="quickSelectRoute('Perambalur', 'Bangalore')" class="shrink-0 px-3 py-1 rounded-full text-xs font-bold bg-gray-100 hover:bg-brand-yellow hover:text-brand-dark transition-colors cursor-pointer border border-gray-200">
                  📍 <span class="lang-text" data-ta="பெங்களூர் (340 km)" data-en="Bangalore (340 km)">பெங்களூர் (340 km)</span>
                </button>
                <button type="button" onclick="quickSelectRoute('Poolambadi', 'Chennai')" class="shrink-0 px-3 py-1 rounded-full text-xs font-bold bg-gray-100 hover:bg-brand-yellow hover:text-brand-dark transition-colors cursor-pointer border border-gray-200">
                  📍 <span class="lang-text" data-ta="பூலாம்பாடி → சென்னை" data-en="Poolambadi → Chennai">பூலாம்பாடி → சென்னை</span>
                </button>
                <button type="button" onclick="quickSelectRoute('Perambalur', 'Salem')" class="shrink-0 px-3 py-1 rounded-full text-xs font-bold bg-gray-100 hover:bg-brand-yellow hover:text-brand-dark transition-colors cursor-pointer border border-gray-200">
                  📍 <span class="lang-text" data-ta="சேலம் (140 km)" data-en="Salem (140 km)">சேலம் (140 km)</span>
                </button>
                <button type="button" onclick="quickSelectRoute('Perambalur', 'Tirupati')" class="shrink-0 px-3 py-1 rounded-full text-xs font-bold bg-gray-100 hover:bg-brand-yellow hover:text-brand-dark transition-colors cursor-pointer border border-gray-200">
                  🛕 <span class="lang-text" data-ta="திருப்பதி (340 km)" data-en="Tirupati (340 km)">திருப்பதி (340 km)</span>
                </button>
              </div>
            </div>
          </div>

          <!-- STREAMLINED ACTION: CONTINUE TO DATE, TIME & DETAILS -->
          <div class="pt-2 min-w-0">
            <button type="button" onclick="openStep1Modal()" class="w-full py-4 px-6 rounded-2xl bg-brand-yellow hover:bg-brand-yellowHover text-brand-dark font-black text-base sm:text-lg shadow-wa flex items-center justify-center gap-2 sm:gap-3 tactile-btn group cursor-pointer transition-all border border-brand-yellowHover">
              <span class="lang-text" data-ta="தொடரவும்" data-en="Continue">
                தொடரவும்
              </span>
              <span class="text-lg sm:text-xl group-hover:translate-x-1.5 transition-transform">➔</span>
            </button>
            <p class="text-center text-[10px] sm:text-xs text-gray-500 font-medium pt-2 lang-text" data-ta="⚡ பயண நாள், நேரம் & பயணிகளை தேர்வு செய்து வாட்ஸ்அப்பில் புக் செய்யலாம்." data-en="⚡ Select travel date, time & passengers to confirm on WhatsApp.">
              ⚡ பயண நாள், நேரம் & பயணிகளை தேர்வு செய்து வாட்ஸ்அப்பில் புக் செய்யலாம்.
            </p>
          </div>
        </form>

      </div>

      <!-- ================= RIGHT: TOYOTA TAISOR 3D SHOWCASE & BENTO TRUST (5 COLS) ================= -->
      <div class="lg:col-span-5 space-y-5 sm:space-y-6 min-w-0 w-full overflow-hidden">

        <!-- 3D CAR SPOTLIGHT CARD -->
        <div class="bg-white rounded-3xl p-5 sm:p-6 shadow-bento border border-gray-100 relative overflow-hidden text-center min-w-0">
          
          <!-- Badge -->
          <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-brand-yellow/20 text-brand-dark text-xs font-black mb-2">
            <span>✨</span>
            <span class="lang-text" data-ta="அதிநவீன டொயோட்டா டெய்சர் SUV" data-en="Brand New Toyota Taisor SUV">
              அதிநவீன டொயோட்டா டெய்சர் SUV
            </span>
          </div>

          <h3 class="font-black text-xl sm:text-2xl text-brand-dark tracking-tight leading-tight">
            White Toyota Taisor
          </h3>
          <p class="text-xs text-gray-500 font-medium lang-text" data-ta="பதிவு எண்: TN 46 AK 1244 • பெரம்பலூர் மாவட்டம்" data-en="Registration: TN 46 AK 1244 • Perambalur District">
            பதிவு எண்: TN 46 AK 1244 • பெரம்பலூர் மாவட்டம்
          </p>

          <!-- The Rendered 3D Isometric Toyota Taisor Image -->
          <div class="relative my-3 sm:my-4 group cursor-pointer">
            <div class="absolute inset-0 bg-brand-yellow/15 rounded-full blur-2xl glow-pedestal"></div>
            <img 
              src="{b64_car_hero}" 
              alt="White Toyota Urban Cruiser Taisor - PKS Travels (TN 46 AK 1244)"
              class="relative z-10 w-full h-auto max-h-[220px] sm:max-h-[260px] object-contain mx-auto drop-shadow-2xl group-hover:scale-105 transition-transform duration-300"
            >
          </div>

          <!-- Feature Badges Bento Strip (3 Clean Spacious Pills) -->
          <div class="grid grid-cols-3 gap-2.5 pt-2 border-t border-gray-100 text-center">
            <div class="p-2.5 rounded-2xl bg-gray-50 border border-gray-100">
              <span class="block text-lg">❄️</span>
              <span class="text-[11px] font-bold text-gray-800 block mt-0.5 lang-text" data-ta="குளிர் ஏசி" data-en="Chilled AC">குளிர் ஏசி</span>
            </div>
            <div class="p-2.5 rounded-2xl bg-gray-50 border border-gray-100">
              <span class="block text-lg">⛰️</span>
              <span class="text-[11px] font-bold text-gray-800 block mt-0.5 lang-text" data-ta="190mm மேடு" data-en="190mm Clearance">190mm மேடு</span>
            </div>
            <div class="p-2.5 rounded-2xl bg-gray-50 border border-gray-100">
              <span class="block text-lg">👥</span>
              <span class="text-[11px] font-bold text-gray-800 block mt-0.5 lang-text" data-ta="4 பயணிகள்" data-en="4 Passengers">4 பயணிகள்</span>
            </div>
          </div>

        </div>

        <!-- BENTO CARD: WHY CHOOSE PKS TRAVELS OVER OLA / UBER? -->
        <div class="bg-brand-dark text-white rounded-3xl p-5 sm:p-6 shadow-bento relative overflow-hidden min-w-0">
          <div class="flex items-center gap-2 mb-4">
            <span class="w-8 h-8 rounded-xl bg-brand-yellow text-brand-dark flex items-center justify-center font-bold text-sm shrink-0">★</span>
            <div>
              <h4 class="font-black text-sm sm:text-base text-white lang-text" data-ta="ஓலா / ஊபரை விட PKS டிராவல்ஸ் ஏன் சிறந்தது?" data-en="Why Choose PKS Travels Over Ola / Uber?">
                ஓலா / ஊபரை விட PKS டிராவல்ஸ் ஏன் சிறந்தது?
              </h4>
              <p class="text-[11px] text-gray-400 font-medium lang-text" data-ta="சொந்த கார் • குடும்பப் பயணம் • நியாயமான கட்டணம்" data-en="Owner Driven • Safe Family Ride • Transparent Fares">
                சொந்த கார் • குடும்பப் பயணம் • நியாயமான கட்டணம்
              </p>
            </div>
          </div>

          <ul class="space-y-3 text-xs sm:text-sm">
            <li class="flex items-start gap-2.5">
              <span class="w-5 h-5 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">✓</span>
              <div class="min-w-0 break-words">
                <strong class="text-brand-yellow block leading-tight lang-text" data-ta="டிரைவர் கேன்சல் செய்யும் தொல்லை இல்லை" data-en="Zero Booking Cancellations">
                  டிரைவர் கேன்சல் செய்யும் தொல்லை இல்லை
                </strong>
                <span class="text-gray-300 text-[11px] sm:text-xs lang-text" data-ta="சொன்ன நேரத்திற்கு 10 நிமிடம் முன்பே உங்கள் வீட்டு வாசலில் கார் நிற்கும்." data-en="No driver cancellations. Cab arrives at your doorstep 10 mins early.">
                  சொன்ன நேரத்திற்கு 10 நிமிடம் முன்பே உங்கள் வீட்டு வாசலில் கார் நிற்கும்.
                </span>
              </div>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="w-5 h-5 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">✓</span>
              <div class="min-w-0 break-words">
                <strong class="text-brand-yellow block leading-tight lang-text" data-ta="குடும்பங்களுக்கு 100% பாதுகாப்பான பயணம்" data-en="100% Safe For Families & Elders">
                  குடும்பங்களுக்கு 100% பாதுகாப்பான பயணம்
                </strong>
                <span class="text-gray-300 text-[11px] sm:text-xs lang-text" data-ta="நிதானமான மற்றும் கண்ணியமான டிரைவிங். பெண்களுக்கும் குழந்தைகளுக்கும் நிம்மதி." data-en="Disciplined, courteous chauffeur. Highly recommended for families & seniors.">
                  நிதானமான மற்றும் கண்ணியமான டிரைவிங். பெண்களுக்கும் குழந்தைகளுக்கும் நிம்மதி.
                </span>
              </div>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="w-5 h-5 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">✓</span>
              <div class="min-w-0 break-words">
                <strong class="text-brand-yellow block leading-tight lang-text" data-ta="தெளிவான வெளிப்படையான கட்டணம்" data-en="Transparent & Fair Kilometre Rates">
                  தெளிவான வெளிப்படையான கட்டணம்
                </strong>
                <span class="text-gray-300 text-[11px] sm:text-xs lang-text" data-ta="மழைக்கால சர்ஜ் கட்டணங்கள் இல்லை. மறைமுக கட்டணங்கள் ஏதும் இல்லை." data-en="No surge pricing or hidden commissions. Direct, honest rates.">
                  மழைக்கால சர்ஜ் கட்டணங்கள் இல்லை. மறைமுக கட்டணங்கள் ஏதும் இல்லை.
                </span>
              </div>
            </li>
          </ul>

          <!-- Call Chauffeur Button -->
          <div class="mt-4 pt-4 border-t border-gray-800 flex items-center justify-between">
            <div>
              <div class="text-[10px] uppercase font-bold text-gray-400 lang-text" data-ta="நேரடி தொடர்பு (செல்வபாரதி)" data-en="Direct Contact (Selvabarathi)">
                நேரடி தொடர்பு (செல்வபாரதி)
              </div>
              <a href="tel:+916385300259" class="font-black text-sm sm:text-base text-brand-yellow hover:underline">+91 6385300259</a>
            </div>
            <a href="tel:+916385300259" class="px-3.5 py-1.5 rounded-xl bg-white text-brand-dark font-black text-xs tactile-btn hover:bg-brand-yellow cursor-pointer">
              <span class="lang-text" data-ta="📞 அழைக்கவும்" data-en="📞 Call Now">📞 அழைக்கவும்</span>
            </a>
          </div>
        </div>

        <!-- POPULAR DESTINATIONS FROM PERAMBALUR DISTRICT -->
        <div class="bg-white rounded-3xl p-5 sm:p-6 shadow-bento border border-gray-100 min-w-0">
          <h4 class="font-black text-sm sm:text-base text-brand-dark mb-3 flex items-center gap-2">
            <span>🗺️</span>
            <span class="lang-text" data-ta="பெரம்பலூர் மாவட்டத்திலிருந்து முக்கிய ஊர்கள் (KM)" data-en="Popular Destinations from Perambalur District">
              பெரம்பலூர் மாவட்டத்திலிருந்து முக்கிய ஊர்கள் (KM)
            </span>
          </h4>

          <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-gray-50 border border-gray-100 flex justify-between items-center">
              <span class="font-bold text-gray-700 lang-text" data-ta="சென்னை" data-en="Chennai">சென்னை</span>
              <span class="font-black text-brand-dark">270 KM</span>
            </div>
            <div class="p-2.5 rounded-xl bg-gray-50 border border-gray-100 flex justify-between items-center">
              <span class="font-bold text-gray-700 lang-text" data-ta="திருச்சி ஏர்போர்ட்" data-en="Trichy Airport">திருச்சி ஏர்போர்ட்</span>
              <span class="font-black text-brand-dark">55 KM</span>
            </div>
            <div class="p-2.5 rounded-xl bg-gray-50 border border-gray-100 flex justify-between items-center">
              <span class="font-bold text-gray-700 lang-text" data-ta="பெங்களூர்" data-en="Bangalore">பெங்களூர்</span>
              <span class="font-black text-brand-dark">340 KM</span>
            </div>
            <div class="p-2.5 rounded-xl bg-gray-50 border border-gray-100 flex justify-between items-center">
              <span class="font-bold text-gray-700 lang-text" data-ta="பூலாம்பாடி" data-en="Poolambadi">பூலாம்பாடி</span>
              <span class="font-black text-brand-dark">28 KM</span>
            </div>
            <div class="p-2.5 rounded-xl bg-gray-50 border border-gray-100 flex justify-between items-center">
              <span class="font-bold text-gray-700 lang-text" data-ta="சேலம் / ஆத்தூர்" data-en="Salem / Attur">சேலம் / ஆத்தூர்</span>
              <span class="font-black text-brand-dark">140 KM</span>
            </div>
            <div class="p-2.5 rounded-xl bg-gray-50 border border-gray-100 flex justify-between items-center">
              <span class="font-bold text-gray-700 lang-text" data-ta="திருப்பதி" data-en="Tirupati">திருப்பதி</span>
              <span class="font-black text-brand-dark">340 KM</span>
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- ================= CUSTOMER TRUST & REVIEWS SECTION ================= -->
    <section class="mt-10 sm:mt-14 mb-8 min-w-0">
      <div class="text-center mb-6 sm:mb-8">
        <h3 class="text-xl sm:text-2xl font-black text-brand-dark lang-text" data-ta="மக்களின் மனமார்ந்த கருத்துக்கள்" data-en="What Our Travelers Say">
          மக்களின் மனமார்ந்த கருத்துக்கள்
        </h3>
        <p class="text-xs sm:text-sm text-gray-500 font-medium lang-text" data-ta="பெரம்பலூர் மாவட்டம் மற்றும் சுற்றுவட்டார மக்களின் நற்சான்றிதழ்கள்" data-en="Verified traveler reviews across Perambalur District & surrounding towns">
          பெரம்பலூர் மாவட்டம் மற்றும் சுற்றுவட்டார மக்களின் நற்சான்றிதழ்கள்
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-5 min-w-0">
        
        <div class="bg-white p-4 sm:p-5 rounded-3xl shadow-bento border border-gray-100 min-w-0">
          <div class="flex items-center gap-1 text-amber-400 text-sm mb-2">★★★★★</div>
          <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-medium break-words lang-text" 
            data-ta="&ldquo;சென்னை ஏர்போர்ட்டிற்கு அதிகாலை 3 மணிக்கு புக் செய்திருந்தோம். சொன்ன நேரத்திற்கு 10 நிமிடம் முன்பே வந்து நின்றார் செல்வபாரதி. கார் மிகவும் சுத்தமாகவும் ஏசி அருமையாகவும் இருந்தது.&rdquo;" 
            data-en="&ldquo;We booked a cab to Chennai Airport at 3:00 AM. Selvabarathi arrived 10 minutes early. The brand new Toyota Taisor was spotless and the AC was excellent!&rdquo;">
            &ldquo;சென்னை ஏர்போர்ட்டிற்கு அதிகாலை 3 மணிக்கு புக் செய்திருந்தோம். சொன்ன நேரத்திற்கு 10 நிமிடம் முன்பே வந்து நின்றார் செல்வபாரதி. கார் மிகவும் சுத்தமாகவும் ஏசி அருமையாகவும் இருந்தது.&rdquo;
          </p>
          <div class="mt-3.5 pt-2.5 border-t border-gray-100 flex items-center justify-between text-xs">
            <span class="font-black text-brand-dark lang-text" data-ta="சரவணன், பூலாம்பாடி" data-en="Saravanan, Poolambadi">சரவணன், பூலாம்பாடி</span>
            <span class="text-gray-400 font-medium lang-text" data-ta="சென்னை பயணம்" data-en="Chennai Trip">சென்னை பயணம்</span>
          </div>
        </div>

        <div class="bg-white p-4 sm:p-5 rounded-3xl shadow-bento border border-gray-100 min-w-0">
          <div class="flex items-center gap-1 text-amber-400 text-sm mb-2">★★★★★</div>
          <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-medium break-words lang-text" 
            data-ta="&ldquo;டொயோட்டா டைசர் கார் மிகவும் சௌகரியமாக இருந்தது. குடும்பத்துடன் திருப்பதி சென்றோம். பெரியவர்கள் ஏற இறங்க எளிதாக இருந்தது. டிரைவரின் பக்குவமான அணுகுமுறை பிடித்திருந்தது.&rdquo;" 
            data-en="&ldquo;The Toyota Taisor SUV was extremely comfortable. We traveled with our family to Tirupati. Smooth ingress for elders and very courteous driving.&rdquo;">
            &ldquo;டொயோட்டா டைசர் கார் மிகவும் சௌகரியமாக இருந்தது. குடும்பத்துடன் திருப்பதி சென்றோம். பெரியவர்கள் ஏற இறங்க எளிதாக இருந்தது. டிரைவரின் பக்குவமான அணுகுமுறை பிடித்திருந்தது.&rdquo;
          </p>
          <div class="mt-3.5 pt-2.5 border-t border-gray-100 flex items-center justify-between text-xs">
            <span class="font-black text-brand-dark lang-text" data-ta="மீனாட்சி சுந்தரம், பெரம்பலூர்" data-en="Meenakshi Sundaram, Perambalur">மீனாட்சி சுந்தரம், பெரம்பலூர்</span>
            <span class="text-gray-400 font-medium lang-text" data-ta="திருப்பதி தரிசனம்" data-en="Tirupati Darshan">திருப்பதி தரிசனம்</span>
          </div>
        </div>

        <div class="bg-white p-4 sm:p-5 rounded-3xl shadow-bento border border-gray-100 min-w-0">
          <div class="flex items-center gap-1 text-amber-400 text-sm mb-2">★★★★★</div>
          <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-medium break-words lang-text" 
            data-ta="&ldquo;அவசர மருத்துவ தேவைக்காக திருச்சி மருத்துவமனை செல்ல வேண்டியிருந்தது. வாட்ஸ்அப்பில் மெசேஜ் செய்த உடனே வந்து அழைத்துச் சென்றார். நம்பகமான சேவை!&rdquo;" 
            data-en="&ldquo;Needed an urgent ride to Trichy Hospital. As soon as I sent a WhatsApp message, he responded and arrived immediately. Truly trustworthy service!&rdquo;">
            &ldquo;அவசர மருத்துவ தேவைக்காக திருச்சி மருத்துவமனை செல்ல வேண்டியிருந்தது. வாட்ஸ்அப்பில் மெசேஜ் செய்த உடனே வந்து அழைத்துச் சென்றார். நம்பகமான சேவை!&rdquo;
          </p>
          <div class="mt-3.5 pt-2.5 border-t border-gray-100 flex items-center justify-between text-xs">
            <span class="font-black text-brand-dark lang-text" data-ta="கார்த்திகேயன், வேப்பந்தட்டை" data-en="Karthikeyan, Veppanthattai">கார்த்திகேயன், வேப்பந்தட்டை</span>
            <span class="text-gray-400 font-medium lang-text" data-ta="திருச்சி பயணம்" data-en="Trichy Medical Trip">திருச்சி பயணம்</span>
          </div>
        </div>

      </div>
    </section>

  </main>

    <!-- ================= STEP 1: DATE & TIME MODAL / BOTTOM SHEET ================= -->
  <div id="dateModalBackdrop" class="fixed inset-0 z-[70] bg-black/60 backdrop-blur-sm transition-opacity duration-300 opacity-0 pointer-events-none flex items-end sm:items-center justify-center p-0 sm:p-4">
    <!-- Overlay Click Dismiss Area -->
    <div class="absolute inset-0" onclick="closeAllModals()"></div>

    <!-- Sheet Card -->
    <div id="dateModalContent" class="relative z-10 w-full max-w-lg bg-white rounded-t-3xl sm:rounded-3xl shadow-2xl border border-gray-100 max-h-[92vh] sm:max-h-[85vh] flex flex-col transform transition-transform duration-300 translate-y-full sm:translate-y-8 sm:scale-95 opacity-0">
      
      <!-- Drag handle for mobile -->
      <div class="sm:hidden flex justify-center pt-3 pb-1 cursor-pointer" onclick="closeAllModals()">
        <div class="w-12 h-1.5 bg-gray-300 rounded-full"></div>
      </div>

      <!-- Header with Close Button -->
      <div class="px-5 sm:px-6 pt-3 sm:pt-4 pb-3 border-b border-gray-100 flex items-center justify-between shrink-0">
        <div>
          <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-brand-yellow/30 text-brand-dark text-[11px] font-black uppercase tracking-wider">
            <span>📅</span>
            <span class="lang-text" data-ta="படி 1: பயண நாள் & நேரம்" data-en="Step 1: Date & Time">படி 1: பயண நாள் & நேரம்</span>
          </span>
          <h3 class="text-base sm:text-lg font-black text-brand-dark mt-1">
            <span class="lang-text" data-ta="புறப்படும் நாள் & நேரத்தை தேர்வு செய்க" data-en="Select Travel Date & Time">புறப்படும் நாள் & நேரத்தை தேர்வு செய்க</span>
          </h3>
        </div>

        <button type="button" onclick="closeAllModals()" class="w-9 h-9 rounded-full bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold text-base flex items-center justify-center transition-colors cursor-pointer" aria-label="Close">
          ✕
        </button>
      </div>

      <!-- Scrollable Sheet Content -->
      <div class="px-5 sm:px-6 py-4 overflow-y-auto space-y-4">
        
        <!-- Route Summary Pill -->
        <div class="bg-gray-50 rounded-2xl p-3 border border-gray-200/90 flex items-center justify-between gap-2">
          <div class="min-w-0 flex-1">
            <div id="dateModalRoute" class="font-black text-brand-dark text-xs sm:text-sm truncate">
              பெரம்பலூர் ➔ சென்னை (~270 KM)
            </div>
            <div id="dateModalTripType" class="text-[11px] text-gray-500 font-bold mt-0.5">
              ஒரு வழிப் பயணம் (One-Way)
            </div>
          </div>
          <div class="text-right shrink-0">
            <span class="text-[10px] font-black px-2.5 py-1 rounded-full bg-brand-yellow text-brand-dark block">
              TN 46 AK 1244
            </span>
          </div>
        </div>

        <!-- 30-Day Horizontal Calendar Strip -->
        <div class="space-y-2">
          <div class="flex items-center justify-between gap-2">
            <label class="text-[11px] sm:text-xs font-black uppercase tracking-wider text-gray-500 flex items-center gap-1.5">
              <span class="lang-text" data-ta="📅 பயண நாள்" data-en="📅 Travel Date">📅 பயண நாள்</span>
            </label>
            <span id="selectedDateDisplay" class="text-[11px] font-black text-brand-dark bg-gray-100 px-2.5 py-0.5 rounded-full shrink-0">
              இன்று (Today)
            </span>
          </div>

          <div class="w-full min-w-0 overflow-hidden">
            <div id="calendarStrip" class="flex gap-2 overflow-x-auto no-scrollbar py-1.5 px-0.5 scroll-smooth max-w-full">
              <!-- Dynamically populated by JS (30 days) -->
            </div>
          </div>
        </div>

        <!-- Departure Time Section: Preset Pills + Custom Time Picker -->
        <div class="space-y-2 pt-1">
          <span class="text-[11px] font-bold text-gray-500 block lang-text" data-ta="புறப்படும் நேரம் / Pickup Time:" data-en="Select Pickup Time:">
            புறப்படும் நேரம் / Pickup Time:
          </span>
          
          <!-- Quick Time Pills -->
          <div class="grid grid-cols-3 gap-1.5 sm:gap-2">
            <button type="button" onclick="setTime('04:00 AM')" class="time-pill px-2 py-2 rounded-xl text-xs font-bold border border-gray-200 bg-white hover:border-brand-yellow transition-all text-center cursor-pointer">
              04:00 AM
            </button>
            <button type="button" onclick="setTime('06:00 AM')" class="time-pill px-2 py-2 rounded-xl text-xs font-bold border border-gray-200 bg-white hover:border-brand-yellow transition-all text-center cursor-pointer">
              06:00 AM
            </button>
            <button type="button" onclick="setTime('09:00 AM')" class="time-pill active px-2 py-2 rounded-xl text-xs font-bold border border-brand-yellow bg-brand-yellow text-brand-dark transition-all text-center shadow-sm cursor-pointer">
              09:00 AM
            </button>
            <button type="button" onclick="setTime('02:00 PM')" class="time-pill px-2 py-2 rounded-xl text-xs font-bold border border-gray-200 bg-white hover:border-brand-yellow transition-all text-center cursor-pointer">
              02:00 PM
            </button>
            <button type="button" onclick="setTime('06:00 PM')" class="time-pill px-2 py-2 rounded-xl text-xs font-bold border border-gray-200 bg-white hover:border-brand-yellow transition-all text-center cursor-pointer">
              06:00 PM
            </button>
            <button type="button" onclick="setTime('10:00 PM')" class="time-pill px-2 py-2 rounded-xl text-xs font-bold border border-gray-200 bg-white hover:border-brand-yellow transition-all text-center cursor-pointer">
              10:00 PM
            </button>
          </div>

          <!-- Custom Interactive Time Selector -->
          <div class="p-2.5 sm:p-3 rounded-2xl bg-brand-grayLight/80 border border-gray-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 mt-2">
            <div class="flex items-center gap-2 min-w-0">
              <span class="text-base sm:text-lg shrink-0">⏰</span>
              <div class="min-w-0">
                <span class="font-black text-xs text-brand-dark block truncate lang-text" data-ta="விருப்பமான நேரம் (Custom Time):" data-en="Custom Pickup Time:">
                  விருப்பமான நேரம் (Custom Time):
                </span>
                <span class="text-[10px] text-gray-500 truncate block lang-text" data-ta="துல்லியமான நேரத்தை தேர்வு செய்க" data-en="Pick any exact hour & minute">
                  துல்லியமான நேரத்தை தேர்வு செய்க
                </span>
              </div>
            </div>
            
            <div class="flex items-center gap-2 self-end sm:self-auto shrink-0">
              <input type="time" id="customTimePicker" onchange="setCustomTime(this.value)" value="09:00" class="px-3 py-1.5 rounded-xl border border-gray-300 text-xs sm:text-sm font-black bg-white text-brand-dark focus:outline-none focus:border-brand-yellow cursor-pointer shadow-sm">
              <span id="activeTimeBadge" class="text-xs font-black text-brand-dark px-2.5 py-1 rounded-lg bg-brand-yellow">
                09:00 AM
              </span>
            </div>
          </div>

        </div>

      </div>

      <!-- Sheet Footer: Continue to Step 2 -->
      <div class="p-4 sm:p-5 border-t border-gray-100 bg-white rounded-b-3xl shrink-0">
        <button type="button" onclick="goToStep2Modal()" class="w-full py-4 px-6 rounded-2xl bg-brand-yellow hover:bg-brand-yellowHover text-brand-dark font-black text-sm sm:text-base shadow-wa flex items-center justify-center gap-2 tactile-btn group cursor-pointer transition-all border border-brand-yellowHover">
          <span class="lang-text" data-ta="தொடரவும்" data-en="Continue">
            தொடரவும்
          </span>
          <span class="text-base sm:text-lg group-hover:translate-x-1.5 transition-transform">➔</span>
        </button>
      </div>

    </div>
  </div>

  <!-- ================= STEP 2: PASSENGERS & BOOKING MODAL / BOTTOM SHEET ================= -->
  <div id="bookingModalBackdrop" class="fixed inset-0 z-[70] bg-black/60 backdrop-blur-sm transition-opacity duration-300 opacity-0 pointer-events-none flex items-end sm:items-center justify-center p-0 sm:p-4">
    <!-- Overlay Click Dismiss Area -->
    <div class="absolute inset-0" onclick="closeAllModals()"></div>

    <!-- Sheet Card -->
    <div id="bookingModalContent" class="relative z-10 w-full max-w-lg bg-white rounded-t-3xl sm:rounded-3xl shadow-2xl border border-gray-100 max-h-[92vh] sm:max-h-[85vh] flex flex-col transform transition-transform duration-300 translate-y-full sm:translate-y-8 sm:scale-95 opacity-0">
      
      <!-- Drag handle indicator for mobile sheet -->
      <div class="sm:hidden flex justify-center pt-3 pb-1 cursor-pointer" onclick="closeAllModals()">
        <div class="w-12 h-1.5 bg-gray-300 rounded-full"></div>
      </div>

      <!-- Header with Back & Close Buttons -->
      <div class="px-5 sm:px-6 pt-3 sm:pt-4 pb-3 border-b border-gray-100 flex items-center justify-between shrink-0">
        <div class="flex items-center gap-2">
          <button type="button" onclick="backToStep1Modal()" class="w-8 h-8 rounded-full bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold text-sm flex items-center justify-center transition-colors cursor-pointer" title="Back">
            ←
          </button>
          <div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-brand-yellow/30 text-brand-dark text-[11px] font-black uppercase tracking-wider">
              <span>👥</span>
              <span class="lang-text" data-ta="படி 2: பயணிகள் & லக்கேஜ்" data-en="Step 2: Passengers & Luggage">படி 2: பயணிகள் & லக்கேஜ்</span>
            </span>
            <h3 class="text-base sm:text-lg font-black text-brand-dark mt-0.5">
              <span class="lang-text" data-ta="பயண விவரங்களை உறுதி செய்க" data-en="Confirm Trip & Passengers">பயண விவரங்களை உறுதி செய்க</span>
            </h3>
          </div>
        </div>

        <button type="button" onclick="closeAllModals()" class="w-9 h-9 rounded-full bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold text-base flex items-center justify-center transition-colors cursor-pointer" aria-label="Close">
          ✕
        </button>
      </div>

      <!-- Scrollable Sheet Content -->
      <div class="px-5 sm:px-6 py-4 overflow-y-auto space-y-4">
        
        <!-- Live Route & Date Pill Summary in Modal -->
        <div class="bg-gray-50 rounded-2xl p-3 border border-gray-200/90 flex items-center justify-between gap-2">
          <div class="min-w-0 flex-1">
            <div id="modalSummaryRoute" class="font-black text-brand-dark text-xs sm:text-sm truncate">
              பெரம்பலூர் ➔ சென்னை (~270 KM)
            </div>
            <div id="modalSummaryDateTime" class="text-[11px] text-gray-500 font-bold mt-0.5">
              இன்று (Today) • 09:00 AM • ஒரு வழி
            </div>
          </div>
          <div class="text-right shrink-0">
            <span class="text-[10px] font-black px-2 py-0.5 rounded-full bg-brand-yellow text-brand-dark block">
              TN 46 AK 1244
            </span>
          </div>
        </div>

        <!-- Passengers Counter Grid -->
        <div class="space-y-2.5">
          <label class="text-[11px] sm:text-xs font-black uppercase tracking-wider text-gray-500 flex items-center gap-1.5">
            <span class="lang-text" data-ta="👥 பயணிகள் எண்ணிக்கை" data-en="👥 Number of Passengers">👥 பயணிகள் எண்ணிக்கை</span>
            <span class="text-gray-400 font-normal">/ Max 4</span>
          </label>

          <div class="grid grid-cols-2 gap-2.5">
            <!-- Adults -->
            <div class="p-3 rounded-2xl bg-brand-grayLight/80 border border-gray-200 flex flex-col justify-between">
              <div>
                <span class="font-bold text-xs sm:text-sm text-brand-dark block lang-text" data-ta="பெரியவர்கள்" data-en="Adults (12+ yrs)">
                  பெரியவர்கள்
                </span>
                <span class="text-[10px] text-gray-400 lang-text" data-ta="அதிகபட்சம் 4 பேர்" data-en="Max 4 in Taisor">அதிகபட்சம் 4 பேர்</span>
              </div>
              <div class="flex items-center justify-between bg-white rounded-xl p-1 border border-gray-200 shadow-sm mt-2">
                <button type="button" onclick="adjustCount('adults', -1)" class="w-8 h-8 rounded-lg bg-gray-100 hover:bg-gray-200 font-black text-sm flex items-center justify-center transition-colors cursor-pointer">-</button>
                <span id="adultCount" class="w-6 text-center font-black text-sm text-brand-dark">2</span>
                <button type="button" onclick="adjustCount('adults', 1)" class="w-8 h-8 rounded-lg bg-brand-yellow hover:bg-brand-yellowHover font-black text-sm flex items-center justify-center transition-colors cursor-pointer">+</button>
              </div>
            </div>

            <!-- Children -->
            <div class="p-3 rounded-2xl bg-brand-grayLight/80 border border-gray-200 flex flex-col justify-between">
              <div>
                <span class="font-bold text-xs sm:text-sm text-brand-dark block lang-text" data-ta="குழந்தைகள்" data-en="Children (Under 12)">
                  குழந்தைகள்
                </span>
                <span class="text-[10px] text-gray-400 lang-text" data-ta="மடியில் / சீட்டில்" data-en="Infants & kids">மடியில் / சீட்டில்</span>
              </div>
              <div class="flex items-center justify-between bg-white rounded-xl p-1 border border-gray-200 shadow-sm mt-2">
                <button type="button" onclick="adjustCount('children', -1)" class="w-8 h-8 rounded-lg bg-gray-100 hover:bg-gray-200 font-black text-sm flex items-center justify-center transition-colors cursor-pointer">-</button>
                <span id="childCount" class="w-6 text-center font-black text-sm text-brand-dark">0</span>
                <button type="button" onclick="adjustCount('children', 1)" class="w-8 h-8 rounded-lg bg-brand-yellow hover:bg-brand-yellowHover font-black text-sm flex items-center justify-center transition-colors cursor-pointer">+</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Luggage Configurator -->
        <div class="space-y-2">
          <span class="text-[11px] font-bold text-gray-500 block lang-text" data-ta="பெரிய லக்கேஜ் சூட்கேஸ் உள்ளதா?" data-en="Do you have heavy luggage/suitcases?">
            பெரிய லக்கேஜ் சூட்கேஸ் உள்ளதா?
          </span>
          
          <div class="grid grid-cols-2 gap-2">
            <button type="button" id="luggageYesBtn" onclick="setLuggage(true)" class="p-2.5 sm:p-3 rounded-2xl border-2 border-brand-yellow bg-brand-yellowLight text-brand-dark font-black text-xs sm:text-sm flex items-center justify-center gap-1.5 transition-all tactile-btn cursor-pointer">
              <span>🧳</span>
              <span class="lang-text" data-ta="ஆம், லக்கேஜ் உண்டு" data-en="Yes, with Luggage">ஆம், லக்கேஜ் உண்டு</span>
            </button>
            <button type="button" id="luggageNoBtn" onclick="setLuggage(false)" class="p-2.5 sm:p-3 rounded-2xl border border-gray-200 bg-white text-gray-600 font-bold text-xs sm:text-sm flex items-center justify-center gap-1.5 transition-all tactile-btn cursor-pointer">
              <span>🎒</span>
              <span class="lang-text" data-ta="சிறிய பைகள் மட்டும்" data-en="Small Bags Only">சிறிய பைகள் மட்டும்</span>
            </button>
          </div>

          <!-- Expanded Luggage Breakdown -->
          <div id="luggageDetailsBox" class="p-3 rounded-2xl bg-amber-50/70 border border-amber-200 grid grid-cols-2 gap-2.5">
            <div class="flex items-center justify-between">
              <div>
                <span class="font-bold text-xs text-amber-950 block lang-text" data-ta="சூட்கேஸ்:" data-en="Suitcase:">சூட்கேஸ்:</span>
                <span class="text-[10px] text-amber-800/80 lang-text" data-ta="டிராலி பேக்" data-en="Trolley bag">டிராலி பேக்</span>
              </div>
              <div class="flex items-center gap-1 bg-white rounded-lg p-1 border border-amber-300">
                <button type="button" onclick="adjustCount('trolleys', -1)" class="w-6 h-6 rounded bg-gray-100 font-bold text-xs flex items-center justify-center cursor-pointer">-</button>
                <span id="trolleyCount" class="w-4 text-center font-black text-xs text-brand-dark">1</span>
                <button type="button" onclick="adjustCount('trolleys', 1)" class="w-6 h-6 rounded bg-brand-yellow font-bold text-xs flex items-center justify-center cursor-pointer">+</button>
              </div>
            </div>

            <div class="flex items-center justify-between">
              <div>
                <span class="font-bold text-xs text-amber-950 block lang-text" data-ta="கைப்பை:" data-en="Handbags:">கைப்பை:</span>
                <span class="text-[10px] text-amber-800/80 lang-text" data-ta="பேக்பேக்" data-en="Backpack">பேக்பேக்</span>
              </div>
              <div class="flex items-center gap-1 bg-white rounded-lg p-1 border border-amber-300">
                <button type="button" onclick="adjustCount('bags', -1)" class="w-6 h-6 rounded bg-gray-100 font-bold text-xs flex items-center justify-center cursor-pointer">-</button>
                <span id="bagCount" class="w-4 text-center font-black text-xs text-brand-dark">1</span>
                <button type="button" onclick="adjustCount('bags', 1)" class="w-6 h-6 rounded bg-brand-yellow font-bold text-xs flex items-center justify-center cursor-pointer">+</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Full Summary Box -->
        <div class="bg-gray-50 rounded-2xl p-3 border border-gray-200/90 text-left">
          <div class="text-[10px] font-black text-gray-400 uppercase tracking-wider lang-text" data-ta="முழுமையான பயண விவரம்" data-en="Complete Trip Summary">
            முழுமையான பயண விவரம்
          </div>
          <div id="summaryRouteText" class="font-black text-brand-dark text-sm mt-0.5">
            பெரம்பலூர் ➔ சென்னை (~270 KM)
          </div>
          <div id="summarySubText" class="text-xs text-gray-600 mt-0.5 leading-relaxed">
            2 பயணிகள் • 1 டிராலி • ஒரு வழி • Toyota Taisor SUV
          </div>
        </div>

      </div>

      <!-- Fixed Action Footer in Sheet -->
      <div class="p-4 sm:p-5 border-t border-gray-100 bg-white rounded-b-3xl shrink-0 space-y-2">
        <button type="button" onclick="submitBookingToWhatsApp()" class="w-full py-3.5 sm:py-4 px-4 sm:px-6 rounded-2xl bg-brand-whatsapp hover:bg-brand-whatsappDark text-white font-black text-sm sm:text-base shadow-wa flex items-center justify-center gap-2 tactile-btn group cursor-pointer transition-colors">
          <svg class="w-5 h-5 fill-current shrink-0 group-hover:scale-110 transition-transform" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.007c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86.174.086.275.072.376-.043.101-.116.433-.506.549-.68.116-.173.231-.145.39-.086s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.099.824zm-3.423-14.416c-6.627 0-12 5.373-12 12 0 2.159.57 4.184 1.564 5.938l-1.564 5.714 5.86-1.537c1.704.931 3.659 1.473 5.74 1.473 6.627 0 12-5.373 12-12s-5.373-12-12-12z"/></svg>
          <span class="lang-text" data-ta="வாட்ஸ்அப்பில் உடனடியாக புக் செய்க" data-en="Send Details & Book Cab via WhatsApp">
            வாட்ஸ்அப்பில் உடனடியாக புக் செய்க
          </span>
          <span class="text-base group-hover:translate-x-1 transition-transform">➔</span>
        </button>
        <p class="text-center text-[10px] text-gray-500 font-medium lang-text" data-ta="⚡ கட்டண விவரங்கள் & கார் உறுதிப்படுத்தல் உடனே வாட்ஸ்அப்பில் அனுப்பப்படும்." data-en="⚡ You will receive instant ride confirmation and quote directly on WhatsApp.">
          ⚡ கட்டண விவரங்கள் & கார் உறுதிப்படுத்தல் உடனே வாட்ஸ்அப்பில் அனுப்பப்படும்.
        </p>
      </div>

    </div>
  </div>

  <!-- ================= STICKY MOBILE BOTTOM BAR ================= -->
  <div id="mobileStickyBar" class="md:hidden fixed bottom-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md border-t border-gray-200 px-3 py-2.5 shadow-2xl flex items-center gap-2 max-w-full overflow-hidden transition-all duration-300">
    <a href="tel:+916385300259" class="flex-1 py-3 px-2 rounded-2xl bg-gray-100 text-brand-dark font-black text-xs sm:text-sm flex items-center justify-center gap-1.5 tactile-btn border border-gray-300">
      <span>📞</span>
      <span>6385300259</span>
    </a>
    <a href="https://api.whatsapp.com/send?phone=916385300259&text=%E0%AE%B5%E0%AE%A3%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%AE%E0%AF%8D!%20I%20want%20to%20enquire%20about%20booking%20a%20cab%20with%20PKS%20Travels." target="_blank" class="flex-1 py-3 px-2 rounded-2xl bg-brand-whatsapp text-white font-black text-xs sm:text-sm flex items-center justify-center gap-1.5 tactile-btn shadow-wa cursor-pointer">
      <span>🟢</span>
      <span class="lang-text" data-ta="WhatsApp புக்" data-en="WhatsApp Book">WhatsApp புக்</span>
    </a>
  </div>

  <!-- ================= FOOTER ================= -->
  <footer class="bg-white border-t border-gray-200 py-6 sm:py-8 px-4 text-center sm:text-left text-xs text-gray-500 w-full overflow-hidden">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3 sm:gap-4">
      <div class="flex flex-wrap items-center justify-center sm:justify-start gap-2 max-w-full">
        <img src="{b64_logo_badge}" alt="Logo" class="w-6 h-6 rounded-md shrink-0">
        <span class="font-black text-brand-dark text-xs sm:text-sm">PKS டிராவல்ஸ் (PKS Travels)</span>
        <span class="lang-text" data-ta="• பெரம்பலூர் மாவட்டம்" data-en="• Perambalur District">• பெரம்பலூர் மாவட்டம்</span>
      </div>
      <p class="font-medium text-[11px] sm:text-xs text-center sm:text-right">
        <span class="lang-text" data-ta="ஒயிட் டொயோட்டா டெய்சர் (TN 46 AK 1244) • நேரடி தொடர்பு:" data-en="White Toyota Taisor (TN 46 AK 1244) • Direct Line:">
          ஒயிட் டொயோட்டா டெய்சர் (TN 46 AK 1244) • நேரடி தொடர்பு:
        </span>
        <a href="tel:+916385300259" class="font-bold text-brand-dark hover:underline">+91 6385300259</a>
      </p>
    </div>
  </footer>

  <!-- ================= JAVASCRIPT ENGINE ================= -->
  <script>
    // Universal Unicode Escape Sequence Characters
    const EMOJIS = {{
      pin: '\\u{{1F4CD}}',
      flag: '\\u{{1F3C1}}',
      road: '\\u{{1F6E3}}\\uFE0F',
      repeat: '\\u{{1F504}}',
      calendar: '\\u{{1F4C5}}',
      clock: '\\u{{23F0}}',
      people: '\\u{{1F465}}',
      luggage: '\\u{{1F9F3}}',
      car: '\\u{{1F698}}',
      sparkles: '\\u{{2728}}',
      check: '\\u{{2705}}'
    }};

    // City Dictionary for Dropdowns
    const CITIES = {{
      pickup: [
        {{ val: 'Perambalur', ta: 'பெரம்பலூர் (Perambalur City / Bus Stand)', en: 'Perambalur (City / Bus Stand)' }},
        {{ val: 'Poolambadi', ta: 'பூலாம்பாடி (Poolambadi Home Base)', en: 'Poolambadi (Home Base)' }},
        {{ val: 'Veppanthattai', ta: 'வேப்பந்தட்டை (Veppanthattai)', en: 'Veppanthattai' }},
        {{ val: 'Ariyalur', ta: 'அரியலூர் (Ariyalur Rly Junction)', en: 'Ariyalur (Railway Junction / City)' }},
        {{ val: 'Trichy', ta: 'திருச்சி (Trichy City/Junction)', en: 'Trichy (City / Junction)' }},
        {{ val: 'Siruvachur', ta: 'சிறுவாச்சூர் (Siruvachur Temple)', en: 'Siruvachur (Temple / Town)' }},
        {{ val: 'Attur', ta: 'ஆத்தூர் (Attur)', en: 'Attur (Salem Border)' }},
        {{ val: 'Kunnam', ta: 'குன்னம் (Kunnam)', en: 'Kunnam' }},
        {{ val: 'Padalur', ta: 'பாடலூர் (Padalur)', en: 'Padalur' }},
        {{ val: 'Custom', ta: 'மற்ற ஊர்கள் / Custom Pickup Point', en: 'Other Location (Custom Pickup)' }}
      ],
      drop: [
        {{ val: 'Chennai', ta: 'சென்னை (Chennai - Airport/City)', en: 'Chennai (Airport / Central / OMR)' }},
        {{ val: 'Trichy Airport', ta: 'திருச்சி ஏர்போர்ட் (Trichy Airport/Junction)', en: 'Trichy International Airport (TRZ)' }},
        {{ val: 'Bangalore', ta: 'பெங்களூர் (Bangalore Electronic City)', en: 'Bangalore (City / Electronic City)' }},
        {{ val: 'Coimbatore', ta: 'கோயம்புத்தூர் (Coimbatore)', en: 'Coimbatore (City / Gandhipuram)' }},
        {{ val: 'Madurai', ta: 'மதுரை (Madurai - Temple/City)', en: 'Madurai (Meenakshi Temple / City)' }},
        {{ val: 'Salem', ta: 'சேலம் (Salem Junction)', en: 'Salem (City / Junction)' }},
        {{ val: 'Attur', ta: 'ஆத்தூர் (Attur)', en: 'Attur' }},
        {{ val: 'Perambalur', ta: 'பெரம்பலூர் (Perambalur)', en: 'Perambalur' }},
        {{ val: 'Thanjavur', ta: 'தஞ்சாவூர் (Thanjavur Big Temple)', en: 'Thanjavur (Big Temple / City)' }},
        {{ val: 'Kumbakonam', ta: 'கும்பகோணம் (Kumbakonam)', en: 'Kumbakonam (Temple City)' }},
        {{ val: 'Pondicherry', ta: 'பாண்டிச்சேரி (Pondicherry Beach)', en: 'Pondicherry (Beach / City)' }},
        {{ val: 'Tirupati', ta: 'திருப்பதி (Tirupati Balaji Darshan)', en: 'Tirupati (Balaji Darshan)' }},
        {{ val: 'Velankanni', ta: 'வேளாங்கண்ணி (Velankanni Church)', en: 'Velankanni (Basilica Church)' }},
        {{ val: 'Ooty', ta: 'ஊட்டி (Ooty Hills)', en: 'Ooty (Nilgiris Queen of Hills)' }},
        {{ val: 'Kodaikanal', ta: 'கொடைக்கானல் (Kodaikanal)', en: 'Kodaikanal (Princess of Hills)' }},
        {{ val: 'Custom', ta: 'மற்ற ஊர்கள் (Other Custom Destination)', en: 'Other Custom Destination' }}
      ]
    }};

    // State Store
    const state = {{
      lang: 'ta',
      tripType: 'oneway',
      pickup: 'Perambalur',
      customPickup: '',
      drop: 'Chennai',
      customDrop: '',
      distanceKM: 270,
      selectedDate: null,
      selectedTime: '09:00 AM',
      adults: 2,
      children: 0,
      hasLuggage: true,
      trolleys: 1,
      bags: 1,
      phone: '916385300259'
    }};

    // Distance Matrix from Perambalur District (One-Way KM)
    const distanceMatrix = {{
      'Perambalur-Chennai': 270,
      'Perambalur-Trichy Airport': 55,
      'Perambalur-Trichy': 55,
      'Perambalur-Bangalore': 340,
      'Perambalur-Coimbatore': 240,
      'Perambalur-Madurai': 185,
      'Perambalur-Salem': 140,
      'Perambalur-Attur': 55,
      'Perambalur-Poolambadi': 28,
      'Perambalur-Thanjavur': 85,
      'Perambalur-Kumbakonam': 95,
      'Perambalur-Pondicherry': 160,
      'Perambalur-Tirupati': 340,
      'Perambalur-Velankanni': 150,
      'Perambalur-Ooty': 310,
      'Perambalur-Kodaikanal': 250,
      'Poolambadi-Chennai': 270,
      'Poolambadi-Trichy Airport': 75,
      'Poolambadi-Trichy': 75,
      'Poolambadi-Bangalore': 310,
      'Poolambadi-Coimbatore': 225,
      'Poolambadi-Madurai': 205,
      'Poolambadi-Salem': 115,
      'Poolambadi-Attur': 35,
      'Poolambadi-Perambalur': 28,
      'Poolambadi-Thanjavur': 105,
      'Poolambadi-Kumbakonam': 110,
      'Poolambadi-Pondicherry': 150,
      'Poolambadi-Tirupati': 340,
      'Poolambadi-Velankanni': 170,
      'Poolambadi-Ooty': 295,
      'Poolambadi-Kodaikanal': 260,
      'Veppanthattai-Chennai': 275,
      'Ariyalur-Chennai': 290,
      'Siruvachur-Chennai': 260
    }};

    // Populate City Dropdowns based on Language
    function populateDropdowns() {{
      const pSelect = document.getElementById('pickupCity');
      const dSelect = document.getElementById('dropCity');
      const currentPickup = state.pickup;
      const currentDrop = state.drop;

      pSelect.innerHTML = '';
      CITIES.pickup.forEach(c => {{
        const opt = document.createElement('option');
        opt.value = c.val;
        opt.textContent = state.lang === 'ta' ? c.ta : c.en;
        if (c.val === currentPickup) opt.selected = true;
        pSelect.appendChild(opt);
      }});

      dSelect.innerHTML = '';
      CITIES.drop.forEach(c => {{
        const opt = document.createElement('option');
        opt.value = c.val;
        opt.textContent = state.lang === 'ta' ? c.ta : c.en;
        if (c.val === currentDrop) opt.selected = true;
        dSelect.appendChild(opt);
      }});
    }}

    // Initialize 30-Day Calendar Strip
    function initCalendar() {{
      const calendarStrip = document.getElementById('calendarStrip');
      calendarStrip.innerHTML = '';

      const today = new Date();
      const monthNames = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'];
      const dayNames = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];

      for (let i = 0; i < 30; i++) {{
        const dateObj = new Date();
        dateObj.setDate(today.getDate() + i);

        const dayName = dayNames[dateObj.getDay()];
        const dayNumber = dateObj.getDate();
        const monthName = monthNames[dateObj.getMonth()];
        const fullDateStr = dateObj.toLocaleDateString('en-GB', {{ day: '2-digit', month: 'short', year: 'numeric' }});

        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = `date-pill flex-shrink-0 w-15 py-2.5 px-1.5 rounded-2xl border text-center transition-all tactile-btn flex flex-col items-center justify-center cursor-pointer ${{
          i === 0 ? 'bg-brand-yellow border-brand-yellow text-brand-dark shadow-sm font-black scale-105' : 'bg-white border-gray-200 text-gray-700 hover:border-brand-yellow font-bold'
        }}`;

        const todayLabel = state.lang === 'ta' ? 'இன்று' : 'Today';

        btn.innerHTML = `
          <span class="text-[9px] uppercase font-bold tracking-wider ${{i === 0 ? 'text-brand-dark' : 'text-gray-400'}}">${{i === 0 ? todayLabel : dayName}}</span>
          <span class="text-base sm:text-lg font-black my-0.5">${{dayNumber}}</span>
          <span class="text-[9px] font-semibold">${{monthName}}</span>
        `;

        btn.onclick = () => selectDate(dateObj, fullDateStr, btn, i === 0);

        if (i === 0) {{
          state.selectedDate = fullDateStr;
        }}

        calendarStrip.appendChild(btn);
      }}
    }}

    // Select Date
    function selectDate(dateObj, dateStr, btnElement, isToday) {{
      state.selectedDate = dateStr;
      
      document.querySelectorAll('.date-pill').forEach(b => {{
        b.className = 'date-pill flex-shrink-0 w-15 py-2.5 px-1.5 rounded-2xl border text-center transition-all tactile-btn flex flex-col items-center justify-center bg-white border-gray-200 text-gray-700 hover:border-brand-yellow font-bold cursor-pointer';
      }});

      btnElement.className = 'date-pill flex-shrink-0 w-15 py-2.5 px-1.5 rounded-2xl border text-center transition-all tactile-btn flex flex-col items-center justify-center bg-brand-yellow border-brand-yellow text-brand-dark shadow-sm font-black scale-105 cursor-pointer';

      const todayPrefix = state.lang === 'ta' ? 'இன்று' : 'Today';
      document.getElementById('selectedDateDisplay').textContent = isToday ? `${{todayPrefix}} (${{dateStr}})` : dateStr;
      updateSummary();
    }}

    // Select Preset Time
    function setTime(timeStr) {{
      state.selectedTime = timeStr;
      
      document.querySelectorAll('.time-pill').forEach(btn => {{
        if (btn.textContent.includes(timeStr)) {{
          btn.className = 'time-pill active px-2 py-2 rounded-xl text-xs font-bold border border-brand-yellow bg-brand-yellow text-brand-dark transition-all text-center shadow-sm cursor-pointer';
        }} else {{
          btn.className = 'time-pill px-2 py-2 rounded-xl text-xs font-bold border border-gray-200 bg-white hover:border-brand-yellow transition-all text-center cursor-pointer';
        }}
      }});

      document.getElementById('activeTimeBadge').textContent = timeStr;
      updateSummary();
    }}

    // Custom Time Picker Handler
    function setCustomTime(time24) {{
      if (!time24) return;
      const [hours, minutes] = time24.split(':');
      let h = parseInt(hours, 10);
      const ampm = h >= 12 ? 'PM' : 'AM';
      h = h % 12;
      h = h ? h : 12;
      const formattedTime = `${{String(h).padStart(2, '0')}}:${{minutes}} ${{ampm}}`;

      state.selectedTime = formattedTime;
      document.getElementById('activeTimeBadge').textContent = formattedTime;

      document.querySelectorAll('.time-pill').forEach(btn => {{
        btn.className = 'time-pill px-2 py-2 rounded-xl text-xs font-bold border border-gray-200 bg-white hover:border-brand-yellow transition-all text-center cursor-pointer';
      }});

      updateSummary();
    }}

    // Set Trip Type (One-Way or Round-Trip)
    function setTripType(type) {{
      state.tripType = type;
      const oneWayBtn = document.getElementById('tripOneWay');
      const roundBtn = document.getElementById('tripRound');

      if (type === 'oneway') {{
        oneWayBtn.className = 'flex-1 sm:flex-initial px-4 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all bg-brand-yellow text-brand-dark shadow-sm text-center cursor-pointer';
        roundBtn.className = 'flex-1 sm:flex-initial px-4 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all text-gray-600 hover:text-brand-dark text-center cursor-pointer';
      }} else {{
        roundBtn.className = 'flex-1 sm:flex-initial px-4 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all bg-brand-yellow text-brand-dark shadow-sm text-center cursor-pointer';
        oneWayBtn.className = 'flex-1 sm:flex-initial px-4 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all text-gray-600 hover:text-brand-dark text-center cursor-pointer';
      }}
      calculateRoute();
    }}

    // Quick Select Route from Chips
    function quickSelectRoute(from, to) {{
      document.getElementById('pickupCity').value = from;
      document.getElementById('dropCity').value = to;
      calculateRoute();
    }}

    // Calculate Route Distance
    function calculateRoute() {{
      const from = document.getElementById('pickupCity').value;
      const to = document.getElementById('dropCity').value;
      
      const customPickupContainer = document.getElementById('customPickupContainer');
      const customDropContainer = document.getElementById('customDropContainer');

      if (from === 'Custom') {{
        customPickupContainer.classList.remove('hidden');
        state.customPickup = document.getElementById('customPickupInput').value;
      }} else {{
        customPickupContainer.classList.add('hidden');
        state.customPickup = '';
      }}

      if (to === 'Custom') {{
        customDropContainer.classList.remove('hidden');
        state.customDrop = document.getElementById('customDropInput').value;
      }} else {{
        customDropContainer.classList.add('hidden');
        state.customDrop = '';
      }}

      state.pickup = from;
      state.drop = to;

      let key = `${{from}}-${{to}}`;
      let baseKM = distanceMatrix[key] || distanceMatrix[`Perambalur-${{to}}`] || distanceMatrix[`Poolambadi-${{to}}`] || 250;

      if (to === 'Custom' || from === 'Custom') {{
        baseKM = 220;
      }}

      state.distanceKM = state.tripType === 'round' ? baseKM * 2 : baseKM;

      const roundTag = state.lang === 'ta' ? '(இரு வழி / Round)' : '(Round-Trip)';
      document.getElementById('distKMText').textContent = `~${{state.distanceKM}} KM`;
      updateSummary();
    }}

    // Adjust Passenger & Luggage Counts
    function adjustCount(type, delta) {{
      if (type === 'adults') {{
        state.adults = Math.max(1, Math.min(4, state.adults + delta));
        document.getElementById('adultCount').textContent = state.adults;
      }} else if (type === 'children') {{
        state.children = Math.max(0, Math.min(3, state.children + delta));
        document.getElementById('childCount').textContent = state.children;
      }} else if (type === 'trolleys') {{
        state.trolleys = Math.max(0, Math.min(3, state.trolleys + delta));
        document.getElementById('trolleyCount').textContent = state.trolleys;
      }} else if (type === 'bags') {{
        state.bags = Math.max(0, Math.min(4, state.bags + delta));
        document.getElementById('bagCount').textContent = state.bags;
      }}
      updateSummary();
    }}

    // Set Luggage Yes / No
    function setLuggage(val) {{
      state.hasLuggage = val;
      const yesBtn = document.getElementById('luggageYesBtn');
      const noBtn = document.getElementById('luggageNoBtn');
      const detailsBox = document.getElementById('luggageDetailsBox');

      if (val) {{
        yesBtn.className = 'p-3 rounded-2xl border-2 border-brand-yellow bg-brand-yellowLight text-brand-dark font-black text-xs sm:text-sm flex items-center justify-center gap-1.5 transition-all tactile-btn cursor-pointer';
        noBtn.className = 'p-3 rounded-2xl border border-gray-200 bg-white text-gray-600 font-bold text-xs sm:text-sm flex items-center justify-center gap-1.5 transition-all tactile-btn cursor-pointer';
        detailsBox.classList.remove('hidden');
      }} else {{
        noBtn.className = 'p-3 rounded-2xl border-2 border-brand-yellow bg-brand-yellowLight text-brand-dark font-black text-xs sm:text-sm flex items-center justify-center gap-1.5 transition-all tactile-btn cursor-pointer';
        yesBtn.className = 'p-3 rounded-2xl border border-gray-200 bg-white text-gray-600 font-bold text-xs sm:text-sm flex items-center justify-center gap-1.5 transition-all tactile-btn cursor-pointer';
        detailsBox.classList.add('hidden');
        state.trolleys = 0;
        state.bags = 0;
      }}
      updateSummary();
    }}

    // Update Summary Box (Fully Bilingual & Word-wrapped)
    function updateSummary() {{
      const pObj = CITIES.pickup.find(c => c.val === state.pickup);
      const dObj = CITIES.drop.find(c => c.val === state.drop);

      let fromName = state.pickup === 'Custom' ? (state.customPickup || (state.lang === 'ta' ? 'குறிப்பிட்ட ஊர்' : 'Custom Pickup')) : (state.lang === 'ta' ? pObj?.ta.split(' ')[0] : pObj?.en.split(' ')[0]);
      let dropName = state.drop === 'Custom' ? (state.customDrop || (state.lang === 'ta' ? 'சேருமிடம்' : 'Destination')) : (state.lang === 'ta' ? dObj?.ta.split(' ')[0] : dObj?.en.split(' ')[0]);

      const routeText = `${{fromName}} ➔ ${{dropName}} (~${{state.distanceKM}} KM)`;
      const summaryRouteEl = document.getElementById('summaryRouteText');
      if (summaryRouteEl) summaryRouteEl.textContent = routeText;
      const modalRouteEl = document.getElementById('modalSummaryRoute');
      if (modalRouteEl) modalRouteEl.textContent = routeText;

      let luggageSummary = '';
      if (state.lang === 'ta') {{
        luggageSummary = state.hasLuggage 
          ? `${{state.trolleys}} டிராலி + ${{state.bags}} கைப்பை` 
          : 'லக்கேஜ் இல்லை';
      }} else {{
        luggageSummary = state.hasLuggage 
          ? `${{state.trolleys}} Trolley + ${{state.bags}} Bag(s)` 
          : 'No Luggage';
      }}

      let tripLabel = '';
      if (state.lang === 'ta') {{
        tripLabel = state.tripType === 'round' ? 'இரு வழி (Round)' : 'ஒரு வழி (One-Way)';
      }} else {{
        tripLabel = state.tripType === 'round' ? 'Round-Trip' : 'One-Way';
      }}

      let paxSummary = '';
      if (state.lang === 'ta') {{
        paxSummary = `${{state.adults}} பெரியவர்கள்${{state.children > 0 ? `, ${{state.children}} குழந்தை` : ''}}`;
      }} else {{
        paxSummary = `${{state.adults}} Adult(s)${{state.children > 0 ? `, ${{state.children}} Child(ren)` : ''}}`;
      }}

      const summarySubEl = document.getElementById('summarySubText');
      if (summarySubEl) summarySubEl.textContent = `${{paxSummary}} • ${{luggageSummary}} • ${{state.selectedTime}} • ${{tripLabel}} • Toyota Taisor (TN46AK1244)`;
      const modalDateTimeEl = document.getElementById('modalSummaryDateTime');
      if (modalDateTimeEl) modalDateTimeEl.textContent = `${{state.selectedDate}} • ${{state.selectedTime}} • ${{tripLabel}}`;
    }}

    // Format Booking Message
    function getBookingText() {{
      const pObj = CITIES.pickup.find(c => c.val === state.pickup);
      const dObj = CITIES.drop.find(c => c.val === state.drop);

      const fromName = state.pickup === 'Custom' ? (state.customPickup || 'Custom Pickup Point') : (state.lang === 'ta' ? pObj?.ta : pObj?.en);
      const dropName = state.drop === 'Custom' ? (state.customDrop || 'Custom Destination') : (state.lang === 'ta' ? dObj?.ta : dObj?.en);
      
      const tripLabel = state.tripType === 'round' ? 'Round-Trip (இரு வழி பயணம்)' : 'One-Way (ஒரு வழி பயணம்)';
      const luggageInfo = state.hasLuggage 
        ? `${{state.trolleys}} Trolley Suitcase(s), ${{state.bags}} Handbag(s)` 
        : 'No Luggage (Small Bags Only)';

      return [
        'வணக்கம்! I would like to book a cab ride with *PKS Travels*:',
        '',
        `${{EMOJIS.pin}} *From:* ${{fromName}}`,
        `${{EMOJIS.flag}} *To:* ${{dropName}}`,
        `${{EMOJIS.road}} *Estimated Distance:* ~${{state.distanceKM}} KM`,
        `${{EMOJIS.repeat}} *Trip Type:* ${{tripLabel}}`,
        `${{EMOJIS.calendar}} *Date:* ${{state.selectedDate}}`,
        `${{EMOJIS.clock}} *Pickup Time:* ${{state.selectedTime}}`,
        `${{EMOJIS.people}} *Passengers:* ${{state.adults}} Adults${{state.children > 0 ? `, ${{state.children}} Children` : ''}}`,
        `${{EMOJIS.luggage}} *Luggage:* ${{luggageInfo}}`,
        `${{EMOJIS.car}} *Vehicle:* White Toyota Urban Cruiser Taisor (Clean AC SUV - TN 46 AK 1244)`,
        '',
        'Please confirm vehicle availability and send the best quote!'
      ].join('\\n');
    }}

    // Open Step 1 (Date & Time) Modal / Bottom Sheet
    function openStep1Modal() {{
      updateSummary();
      const backdrop = document.getElementById('dateModalBackdrop');
      const content = document.getElementById('dateModalContent');
      const stickyBar = document.getElementById('mobileStickyBar');
      
      backdrop.classList.remove('opacity-0', 'pointer-events-none');
      backdrop.classList.add('opacity-100');
      
      content.classList.remove('translate-y-full', 'sm:translate-y-8', 'sm:scale-95', 'opacity-0');
      content.classList.add('translate-y-0', 'sm:translate-y-0', 'sm:scale-100', 'opacity-100');
      
      if (stickyBar) {{
        stickyBar.classList.add('translate-y-full', 'opacity-0', 'pointer-events-none');
      }}
      document.body.style.overflow = 'hidden';
    }}

    // Move from Step 1 to Step 2 (Passengers & Luggage)
    function goToStep2Modal() {{
      const dateBackdrop = document.getElementById('dateModalBackdrop');
      const dateContent = document.getElementById('dateModalContent');
      
      dateBackdrop.classList.add('opacity-0', 'pointer-events-none');
      dateBackdrop.classList.remove('opacity-100');
      dateContent.classList.add('translate-y-full', 'sm:translate-y-8', 'sm:scale-95', 'opacity-0');
      dateContent.classList.remove('translate-y-0', 'sm:translate-y-0', 'sm:scale-100', 'opacity-100');

      setTimeout(() => {{
        const bookBackdrop = document.getElementById('bookingModalBackdrop');
        const bookContent = document.getElementById('bookingModalContent');
        
        bookBackdrop.classList.remove('opacity-0', 'pointer-events-none');
        bookBackdrop.classList.add('opacity-100');
        bookContent.classList.remove('translate-y-full', 'sm:translate-y-8', 'sm:scale-95', 'opacity-0');
        bookContent.classList.add('translate-y-0', 'sm:translate-y-0', 'sm:scale-100', 'opacity-100');
      }}, 150);
    }}

    // Go back from Step 2 to Step 1
    function backToStep1Modal() {{
      const bookBackdrop = document.getElementById('bookingModalBackdrop');
      const bookContent = document.getElementById('bookingModalContent');
      
      bookBackdrop.classList.add('opacity-0', 'pointer-events-none');
      bookBackdrop.classList.remove('opacity-100');
      bookContent.classList.add('translate-y-full', 'sm:translate-y-8', 'sm:scale-95', 'opacity-0');
      bookContent.classList.remove('translate-y-0', 'sm:translate-y-0', 'sm:scale-100', 'opacity-100');

      setTimeout(() => {{
        openStep1Modal();
      }}, 150);
    }}

    // Close any open modal
    function closeAllModals() {{
      const dateBackdrop = document.getElementById('dateModalBackdrop');
      const dateContent = document.getElementById('dateModalContent');
      const bookBackdrop = document.getElementById('bookingModalBackdrop');
      const bookContent = document.getElementById('bookingModalContent');
      const stickyBar = document.getElementById('mobileStickyBar');
      
      if (dateBackdrop) {{
        dateBackdrop.classList.add('opacity-0', 'pointer-events-none');
        dateBackdrop.classList.remove('opacity-100');
      }}
      if (dateContent) {{
        dateContent.classList.add('translate-y-full', 'sm:translate-y-8', 'sm:scale-95', 'opacity-0');
        dateContent.classList.remove('translate-y-0', 'sm:translate-y-0', 'sm:scale-100', 'opacity-100');
      }}
      if (bookBackdrop) {{
        bookBackdrop.classList.add('opacity-0', 'pointer-events-none');
        bookBackdrop.classList.remove('opacity-100');
      }}
      if (bookContent) {{
        bookContent.classList.add('translate-y-full', 'sm:translate-y-8', 'sm:scale-95', 'opacity-0');
        bookContent.classList.remove('translate-y-0', 'sm:translate-y-0', 'sm:scale-100', 'opacity-100');
      }}
      
      if (stickyBar) {{
        stickyBar.classList.remove('translate-y-full', 'opacity-0', 'pointer-events-none');
      }}
      document.body.style.overflow = '';
    }}

        // Submit Booking to WhatsApp from Modal
    function submitBookingToWhatsApp() {{
      const fullMessage = getBookingText();
      const waUrl = 'https://api.whatsapp.com/send?phone=' + state.phone + '&text=' + encodeURIComponent(fullMessage);
      window.open(waUrl, '_blank');
    }}

    // Smooth Scroll to Form on Mobile
    function scrollToBookingForm() {{
      const form = document.getElementById('bookingForm');
      if (form) {{
        form.scrollIntoView({{ behavior: 'smooth' }});
      }}
    }}

    // Full Site Language Toggle (100% of website copy)
    function toggleLanguage() {{
      state.lang = state.lang === 'ta' ? 'en' : 'ta';
      const langText = document.getElementById('langText');
      langText.textContent = state.lang === 'ta' ? 'English' : 'தமிழ்';

      // Update all .lang-text elements
      document.querySelectorAll('.lang-text').forEach(el => {{
        const val = el.getAttribute(`data-${{state.lang}}`);
        if (val) {{
          el.innerHTML = val;
        }}
      }});

      // Update input placeholders
      const pickupInput = document.getElementById('customPickupInput');
      if (pickupInput) {{
        pickupInput.placeholder = state.lang === 'ta' 
          ? 'புறப்படும் ஊர் அல்லது முகவரி உள்ளிடவும் (e.g. தெரு / லேண்ட்மார்க்)...' 
          : 'Enter pickup area, street, or landmark...';
      }}
      const dropInput = document.getElementById('customDropInput');
      if (dropInput) {{
        dropInput.placeholder = state.lang === 'ta' 
          ? 'செல்லும் ஊரின் பெயரை உள்ளிடவும் (Enter Destination City / Town)...' 
          : 'Enter destination city, town, or area...';
      }}

      // Refresh Dropdowns and Calendar
      populateDropdowns();
      initCalendar();
      calculateRoute();
      updateSummary();
    }}

    // Run on Load
    window.addEventListener('DOMContentLoaded', () => {{
      populateDropdowns();
      initCalendar();
      calculateRoute();
    }});
  </script>

</body>
</html>
'''

output_path = '/Users/madhavan/.gemini/antigravity/scratch/perambalur-taisor-cabs/index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated clean customer landing page index.html! Size: {os.path.getsize(output_path)} bytes")
