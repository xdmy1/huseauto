#!/usr/bin/env python3
import json

def update_skoda_and_clean_catalog():
    """Add Škoda models and remove duplicate brands"""
    
    # Load current catalog
    try:
        with open('assets/catalog.json', 'r', encoding='utf-8') as f:
            catalog = json.load(f)
    except FileNotFoundError:
        print("Error: assets/catalog.json not found")
        return
    
    # New Škoda models to add
    new_skoda_models = [
        {"name": "Fabia I sedan/hatchback/universal – bancheta spate din 2 bucăți", "years": "2000-2025"},
        {"name": "Fabia II hatchback (banchetă întreagă)", "years": "2000-2025"},
        {"name": "Fabia II hatchback/universal – bancheta spate din 2 bucăți", "years": "2000-2025"},
        {"name": "Fabia II Sport (RS) hatchback", "years": "2000-2025"},
        {"name": "Karoq (Active) fără cotieră spate din 2017 / Volkswagen Taos I din 2020 (cu tapițerie suplimentară pentru tetierele spate)", "years": "2000-2025"},
        {"name": "Karoq (Ambition) fără cotieră spate din 2017", "years": "2000-2025"},
        {"name": "Karoq (Style) cu cotieră spate din 2017", "years": "2000-2025"},
        {"name": "Kodiaq (Active) fără cotieră spate din 2016", "years": "2000-2025"},
        {"name": "Kodiaq (Ambition, Scout) cu cotieră spate din 2016", "years": "2000-2025"},
        {"name": "Kodiaq (Style) cu cotieră spate din 2016", "years": "2000-2025"},
        {"name": "Octavia A5 Ambiente (banchetă întreagă)", "years": "2000-2025"},
        {"name": "Octavia A5 Elegance hatchback/universal – bancheta spate din 2 bucăți", "years": "2000-2025"},
        {"name": "Octavia A7 Ambiente hatchback/universal fără cotieră spate", "years": "2000-2025"},
        {"name": "Octavia A7 Elegance hatchback/universal cu cotieră spate", "years": "2000-2025"},
        {"name": "Octavia A7 RS hatchback/universal (scaune față sport)", "years": "2000-2025"},
        {"name": "Octavia A8 (Active, Ambition) din 2019", "years": "2000-2025"},
        {"name": "Octavia A8 RS hatchback/universal (scaune față sport) din 2020", "years": "2000-2025"},
        {"name": "Octavia Tour hatchback/universal", "years": "2000-2025"},
        {"name": "Octavia Tour Sport hatchback", "years": "2000-2025"},
        {"name": "Rapid (banchetă întreagă) din 2014", "years": "2000-2025"},
        {"name": "Rapid I/II – bancheta spate din 2 bucăți din 2014 / Volkswagen Polo din 2020 (fără cotieră spate)", "years": "2000-2025"},
        {"name": "Rapid I/II – bancheta spate din 2 bucăți din 2014 / Volkswagen Polo din 2020 (cu cotieră spate)", "years": "2000-2025"},
        {"name": "Rapid I/II Sport din 2014 / Volkswagen Polo Sport din 2020 (fără cotieră spate)", "years": "2000-2025"},
        {"name": "Rapid I/II Sport din 2014 / Volkswagen Polo Sport din 2020 (cu cotieră spate)", "years": "2000-2025"},
        {"name": "Roomster", "years": "2000-2025"},
        {"name": "Superb II (Elegance) hatchback", "years": "2000-2025"},
        {"name": "Superb II (Ambition) hatchback", "years": "2000-2025"},
        {"name": "Superb II facelift hatchback", "years": "2000-2025"},
        {"name": "Superb III (Active) (spătar pasager transformabil) din 2015", "years": "2000-2025"},
        {"name": "Superb III (Active) (spătare față identice) din 2015", "years": "2000-2025"},
        {"name": "Superb III (Ambition, Style) (spătar pasager transformabil) din 2015", "years": "2000-2025"},
        {"name": "Superb III (Ambition, Style) (spătare față identice) din 2015", "years": "2000-2025"},
        {"name": "Yeti (spătar pasager transformabil) din 2013", "years": "2000-2025"},
        {"name": "Yeti (spătare față identice) din 2009", "years": "2000-2025"}
    ]
    
    # First, remove duplicate brands by name
    seen_brands = set()
    unique_brands = []
    
    for brand in catalog['brands']:
        brand_name = brand['name']
        if brand_name not in seen_brands:
            seen_brands.add(brand_name)
            unique_brands.append(brand)
        else:
            print(f"Removed duplicate brand: {brand_name}")
    
    catalog['brands'] = unique_brands
    
    # Find and update Škoda brand
    skoda_brand = None
    for brand in catalog['brands']:
        if brand['name'] == 'Škoda':
            skoda_brand = brand
            break
    
    if skoda_brand:
        # Clear existing Škoda models and add new ones
        skoda_brand['models'] = new_skoda_models
        print(f"Updated Škoda with {len(new_skoda_models)} models")
    else:
        print("Error: Škoda brand not found")
        return
    
    # Save updated catalog
    with open('assets/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    
    print(f"\nUpdate complete:")
    print(f"- Added {len(new_skoda_models)} Škoda models")
    print(f"- Total brands after deduplication: {len(catalog['brands'])}")

if __name__ == "__main__":
    update_skoda_and_clean_catalog()