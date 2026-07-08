import os
import glob
import json
from bs4 import BeautifulSoup
import pandas as pd

INPUT_DIR = "./quran_html" 
OUTPUT_JSON = "quran_dataset.json"
OUTPUT_CSV = "quran_dataset.csv"

def parse_local_html(file_path):
    """Parses a single local HTML file and extracts structured verses."""
    # Extract surah number from filename (e.g., '001.html' -> '001')
    surah_num = os.path.basename(file_path).split('.')[0]
    
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Target the primary container we analyzed
    entry_content = soup.find('div', class_='entry-content')
    if not entry_content:
        print(f"Warning: No 'entry-content' found in {file_path}")
        return []

    verses_data = []
    current_section = "Section 1"  # Default fallback standard
    
    # Process immediate children to preserve linear reading order
    for element in entry_content.find_all(['div', 'p'], recursive=False):
        
        # Track Section changes
        if element.get('class') and 'section' in element.get('class'):
            current_section = element.get_text(strip=True)
            continue
            
        # Extract individual Verses
        if element.get('class') and 'verse' in element.get('class'):
            arabic_div = element.find('div', class_='arabic-text')
            english_div = element.find('div', class_='english-text')
            
            arabic_raw = arabic_div.get_text(strip=True) if arabic_div else ""
            english_raw = english_div.get_text(strip=True) if english_div else ""
            
            # Clean ayah marker character if present in the Arabic field
            if "۝" in arabic_raw:
                arabic_raw = arabic_raw.replace("۝", "").strip()
            
            # Push into our structured row layout
            verses_data.append({
                "surah_number": surah_num,
                "section": current_section,
                "arabic_text": arabic_raw,
                "english_translation": english_raw
            })
            
    return verses_data

def main():
    # Gather all 3-digit numbered html files (ignoring index.html)
    search_path = os.path.join(INPUT_DIR, "[0-9][0-9][0-9].html")
    html_files = sorted(glob.glob(search_path))
    
    if not html_files:
        print(f"No matching HTML files found in '{INPUT_DIR}'. Check your directory path.")
        return

    all_verses = []
    print(f"Found {len(html_files)} files to process...")

    for file_path in html_files:
        print(f"Processing: {os.path.basename(file_path)}")
        file_verses = parse_local_html(file_path)
        all_verses.extend(file_verses)

    # --- Export Results ---
    if all_verses:
        # 1. Save Master JSON
        with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
            json.dump(all_verses, f, ensure_ascii=False, indent=4)
        print(f"\nSaved master payload to {OUTPUT_JSON}")
        
        # 2. Save Master CSV
        df = pd.DataFrame(all_verses)
        df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
        print(f"Saved master tabular view to {OUTPUT_CSV}")
    else:
        print("No verses extracted. Check class parsing mappings.")

if __name__ == "__main__":
    main()