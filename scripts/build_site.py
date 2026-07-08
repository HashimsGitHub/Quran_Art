import pandas as pd
import json

def build_html():
    try:
        # Load the generated dataset
        df = pd.read_csv("quran_dataset.csv", dtype={"surah_number": str}).fillna("")
    except FileNotFoundError:
        print("Error: quran_dataset.csv not found. Please run your parser first.")
        return

    # Convert dataframe to a clean JSON string
    records_json = df.to_json(orient="records")

    # Generate the unique Surah dropdown options
    surah_list = sorted(df["surah_number"].unique())
    options_html = "".join([f'<option value="{num}">Sūra {int(num)}</option>' for num in surah_list])

    # Raw HTML template containing the exact styles and markup of the parent theme
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <title>Quran Art - Search Engine</title>
  <meta name="description" content="Search across the entire Holy Quran using English keywords. Beautiful responsive side-by-side translation layout matching the Quran Art theme.">

  <!-- Open Graph Meta Tags -->
  <meta property="og:url" content="https://quran-art.cloud/search">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Quran Art - Global Verse Search">
  <meta property="og:description" content="Search across the entire Holy Quran with translation from Abdullah Yusuf Ali.">
  <meta property="og:image" content="https://smbclouddrive.blob.core.windows.net/quran-art/QuranLogo.jpg">

  <!-- Favicon / Fonts -->
  <link rel="icon" href="https://smbclouddrive.blob.core.windows.net/quran-art/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" href="https://smbclouddrive.blob.core.windows.net/quran-art/favicon.png">
  <link rel="apple-touch-icon" href="https://smbclouddrive.blob.core.windows.net/quran-art/images/QuranLogo.png">
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri&display=swap');
    
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background: radial-gradient(circle at 20% 30%, #0a0601, #020100);
      font-family: 'Cinema', 'Georgia', 'Times New Roman', serif;
      color: #d4af37;
      line-height: 1.5;
      scroll-behavior: smooth;
      min-height: 100vh;
    }

    /* Royal gold border on body edge */
    body::before {
      content: "";
      position: fixed;
      top: 20px;
      left: 20px;
      right: 20px;
      bottom: 20px;
      pointer-events: none;
      border: 1px solid rgba(212, 175, 55, 0.4);
      border-radius: 4px;
      z-index: 10;
      box-shadow: 0 0 0 2px rgba(0,0,0,0.5), inset 0 0 20px rgba(212,175,55,0.15);
    }

    /* Royal arabesque pattern overlay */
    .royal-bg-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" opacity="0.045"><path fill="none" stroke="%23d4af37" stroke-width="0.7" d="M80 40 L120 40 L140 80 L120 120 L80 120 L60 80 Z M100 10 L110 30 L90 30 Z M100 150 L110 170 L90 170 Z M170 100 L150 90 L150 110 Z M30 100 L50 90 L50 110 Z"/><circle cx="100" cy="100" r="28" stroke="%23d4af37" fill="none" stroke-width="0.5"/><path d="M100 55 L118 100 L100 145 L82 100 Z" stroke="%23d4af37" fill="none" stroke-width="0.6"/><path d="M55 55 L75 75 L55 95 L35 75 Z" stroke="%23d4af37" fill="none" stroke-width="0.4"/><path d="M145 55 L165 75 L145 95 L125 75 Z" stroke="%23d4af37" fill="none" stroke-width="0.4"/></svg>');
      background-repeat: repeat;
      background-size: 80px;
      pointer-events: none;
      z-index: 0;
    }

    .container-custom {
      position: relative;
      z-index: 2;
      max-width: 1100px;
      margin: 0 auto;
      padding: 2rem 1.5rem 4rem;
    }

    /* Royal Header */
    .royal-header {
      text-align: center;
      margin-bottom: 2rem;
      padding: 1.2rem 1rem;
      border-bottom: 2px solid rgba(212, 175, 55, 0.6);
      border-top: 2px solid rgba(212, 175, 55, 0.3);
      background: linear-gradient(90deg, transparent, rgba(212,175,55,0.08), transparent);
    }
    .royal-header h1 {
      font-size: 2.8rem;
      letter-spacing: 4px;
      text-transform: uppercase;
      text-shadow: 0 0 8px #b8860b, 0 0 18px #8b6508;
      font-weight: 500;
    }
    .royal-header h1 span {
      font-size: 1.5rem;
      display: inline-block;
      vertical-align: middle;
      margin: 0 12px;
    }

    .ornament {
      display: flex;
      justify-content: center;
      gap: 12px;
      margin: 1rem 0;
    }
    .ornament .diamond {
      width: 8px;
      height: 8px;
      background: #d4af37;
      transform: rotate(45deg);
      box-shadow: 0 0 6px gold;
    }
    .ornament .line {
      width: 60px;
      height: 1px;
      background: linear-gradient(90deg, transparent, #d4af37, #d4af37, transparent);
      align-self: center;
    }

    /* Interactive Input Fields */
    .royal-input {
      background: rgba(10, 6, 1, 0.85);
      border: 1px solid rgba(212, 175, 55, 0.5);
      color: #f6e3a8;
      transition: all 0.3s ease;
    }
    .royal-input:focus {
      border-color: #f3cf6a;
      box-shadow: 0 0 10px rgba(212, 175, 55, 0.3);
      outline: none;
    }
    .royal-input option {
      background: #0a0601;
      color: #f6e3a8;
    }

    /* Verse Gold Frame Structure */
    .verse-gold-frame {
      background: linear-gradient(145deg, #c9a03d, #fde876, #b47c2e, #efcd82);
      padding: 3px; /* Thin majestic gold rim borders */
      border-radius: 20px 6px 20px 6px;
      box-shadow: 0 15px 30px -10px rgba(0,0,0,0.9);
      transition: transform 0.3s ease;
    }
    .verse-frame-inner {
      background: rgba(15, 11, 5, 0.95);
      padding: 1.5rem;
      border-radius: 18px 4px 18px 4px;
    }
    .arabic-font {
      font-family: 'Amiri', serif;
      line-height: 2.2;
    }

    .back-link {
      color: #e6c87a;
      text-transform: uppercase;
      font-size: 0.85rem;
      letter-spacing: 1px;
      transition: all 0.2s;
    }
    .back-link:hover {
      color: #ffffff;
      text-shadow: 0 0 5px gold;
    }

    @media (max-width: 780px) {
      body::before { top: 10px; left: 10px; right: 10px; bottom: 10px; }
      .royal-header h1 { font-size: 1.8rem; }
    }
  </style>
</head>
<body>

<div class="royal-bg-overlay"></div>

<div class="container-custom">
  
  <!-- Navigation Top Bar Link -->
  <div class="mb-4 flex justify-between items-center px-2">
    <a href="https://quran-art.cloud/" class="back-link">← 🏛️ Back to Gallery</a>
    <div class="text-xs text-amber-500/60 uppercase tracking-widest">Feature View</div>
  </div>

  <!-- Royal Theme Header Header Block -->
  <div class="royal-header">
    <div class="ornament">
      <div class="diamond"></div>
      <div class="line"></div>
      <div style="font-size: 1.8rem;">﷽</div>
      <div class="line"></div>
      <div class="diamond"></div>
    </div>
    <h1>
      <span>⚜️</span> VERSE KNOWLEDGE ENGINE <span>⚜️</span>
    </h1>
    <div class="ornament">
      <div class="line" style="width: 100px;"></div>
    </div>
  </div>

  <!-- Controls Dashboard Grid System -->
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
    <div class="md:col-span-1">
      <label class="block text-xs uppercase tracking-wider mb-2 text-amber-400/80 font-semibold">Browse Sūra</label>
      <select id="surahSelect" class="royal-input w-full rounded-lg px-4 py-3 text-sm cursor-pointer">
        __OPTIONS_PLACEHOLDER__
      </select>
    </div>
    <div class="md:col-span-2">
      <label class="block text-xs uppercase tracking-wider mb-2 text-amber-400/80 font-semibold">Global Key Term Query Search</label>
      <input id="searchInput" type="text" placeholder="Type keywords (e.g., 'Light', 'Merciful', 'Moon') to search across all Sūras..." 
             class="royal-input w-full rounded-lg px-4 py-3 text-sm placeholder-amber-700/60">
    </div>
  </div>

  <!-- Global Standalone Bismillah Header Placement -->
  <div class="text-center my-10 animate-pulse">
    <div class="arabic-font text-4xl md:text-5xl text-amber-300 tracking-wide select-none" dir="rtl">
      بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ
    </div>
    <div class="ornament mt-4">
      <div class="line" style="width: 120px; opacity: 0.3;"></div>
    </div>
  </div>

  <!-- Search Results Counter Context Area -->
  <div id="searchStatus" class="text-center text-sm tracking-wide text-amber-200/70 italic mb-6 hidden"></div>

  <!-- Infinite Scroll Content Core Feed -->
  <div id="verseContainer" class="space-y-6">
      <!-- Appended dynamically via Javascript UI layer mapping -->
  </div>
  
  <!-- Loading Indicator for Infinite Scroll -->
  <div id="loadingIndicator" class="text-center py-8 text-xs uppercase tracking-widest text-amber-500/50 hidden">
      Loading matching segments...
  </div>

  <!-- Standard Parent Matching Footer Component -->
  <div class="mt-12 text-center pt-6 border-t border-amber-500/20 text-xs tracking-wider text-amber-600/70 flex justify-between px-2 flex-wrap gap-4">
    <div>📜 Translation by Abdullah Yusuf Ali</div>
    <div>Copyright · 2026 &copy; · Hashim Hilal</div>
  </div>

</div>

<script>
  // Safely containing compiled python arrays
  const dataset = __DATASET_PLACEHOLDER__;

  const surahSelect = document.getElementById('surahSelect');
  const searchInput = document.getElementById('searchInput');
  const verseContainer = document.getElementById('verseContainer');
  const searchStatus = document.getElementById('searchStatus');
  const loadingIndicator = document.getElementById('loadingIndicator');

  let filteredData = [];
  let currentIndex = 0;
  const ITEMS_PER_PAGE = 30; 
  let debounceTimer;

  function updateFilterAndReset() {
      const selectedSurah = surahSelect.value;
      const searchQuery = searchInput.value.toLowerCase().trim();
      
      verseContainer.innerHTML = '';
      currentIndex = 0;

      if (searchQuery !== '') {
          // Global multi-surah search engine configuration
          filteredData = dataset.filter(item => item.english_translation.toLowerCase().includes(searchQuery));
          
          surahSelect.disabled = true;
          surahSelect.classList.add('opacity-40');
          searchStatus.textContent = `◈ Found ${filteredData.length} instances matching "${searchQuery}" across the entire Quran ◈`;
          searchStatus.classList.remove('hidden');
      } else {
          // Sequential Browse Mode
          filteredData = dataset.filter(item => item.surah_number === selectedSurah);
          
          surahSelect.disabled = false;
          surahSelect.classList.remove('opacity-40');
          searchStatus.classList.add('hidden');
      }

      if (filteredData.length === 0) {
          verseContainer.innerHTML = `<div class="text-center py-16 text-amber-600/50 text-sm tracking-wider uppercase border border-amber-500/10 rounded-xl bg-black/20">No matching verses located.</div>`;
          return;
      }

      renderNextBatch();
  }

  function renderNextBatch() {
      const nextIndex = Math.min(currentIndex + ITEMS_PER_PAGE, filteredData.length);
      const batch = filteredData.slice(currentIndex, nextIndex);
      
      const fragment = document.createDocumentFragment();

      batch.forEach(item => {
          const card = document.createElement('div');
          card.className = 'verse-gold-frame';
          
          card.innerHTML = `
              <div class="verse-frame-inner">
                  <div class="flex justify-between items-center text-xs font-semibold text-amber-500/50 tracking-widest uppercase border-b border-amber-500/10 pb-3 mb-4">
                      <span>Sūra ${parseInt(item.surah_number)}</span>
                      <span class="italic text-amber-600/70">${item.section}</span>
                  </div>
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
                      <!-- Arabic Column Frame -->
                      <div class="arabic-font text-right text-lg md:text-xl text-amber-100 leading-relaxed" dir="rtl">
                          ${item.arabic_text}
                      </div>
                      <!-- English Column Frame -->
                      <div class="text-amber-200/90 text-sm md:text-base leading-relaxed border-t md:border-t-0 md:border-l border-amber-500/10 pt-4 md:pt-0 md:pl-6 text-justify font-sans">
                          ${item.english_translation}
                      </div>
                  </div>
              </div>
          `;
          fragment.appendChild(card);
      });

      verseContainer.appendChild(fragment);
      currentIndex = nextIndex;

      if (currentIndex < filteredData.length) {
          loadingIndicator.classList.remove('hidden');
      } else {
          loadingIndicator.classList.add('hidden');
      }
  }

  function handleSearchInput() {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
          updateFilterAndReset();
      }, 250);
  }

  // Window scroll dynamic buffer monitor
  window.addEventListener('scroll', () => {
      if ((window.innerHeight + window.scrollY) >= document.documentElement.scrollHeight - 300) {
          if (currentIndex < filteredData.length) {
              renderNextBatch();
          }
      }
  });

  surahSelect.addEventListener('change', updateFilterAndReset);
  searchInput.addEventListener('input', handleSearchInput);

  // Boot configuration initial layout runtime execution
  updateFilterAndReset();
</script>
</body>
</html>
"""

    # Safe layout replacements values
    final_html = html_template.replace("__OPTIONS_PLACEHOLDER__", options_html)
    final_html = final_html.replace("__DATASET_PLACEHOLDER__", records_json)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(final_html)
    print("Successfully compiled aligned theme template: index.html")

if __name__ == "__main__":
    build_html()
