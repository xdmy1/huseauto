#!/usr/bin/env python3
import json
import os

def fix_brand_logos():
    """Connect available logos to brands in catalog"""
    
    # Load current catalog
    try:
        with open('assets/catalog.json', 'r', encoding='utf-8') as f:
            catalog = json.load(f)
    except FileNotFoundError:
        print("Error: assets/catalog.json not found")
        return
    
    # Get available logo files
    logos_path = 'assets/logos'
    if not os.path.exists(logos_path):
        print(f"Error: {logos_path} not found")
        return
    
    logo_files = [f for f in os.listdir(logos_path) if f.endswith(('.svg', '.png')) and not f.startswith('.')]
    
    # Create mapping from brand names to logo files
    logo_mapping = {
        'Audi': 'Audi-Logo_2016.svg',
        'BMW': 'BMW.svg', 
        'Chevrolet': 'Chevrolet 1.svg',
        'Citroën': 'citroen.svg',
        'Dodge': 'Dodge.svg',
        'FIAT': 'Fiat_(logo).svg',
        'Ford': 'Ford_logo_flat.svg',
        'HAVAL': 'Haval.svg',
        'Honda': 'honda.svg',
        'Hyundai': 'hyunday.svg',
        'Jeep': 'Jeep_logo.svg',
        'KIA': 'KIA_logo3.svg',
        'Land Rover': 'Land_Rover_logo_black_1.svg',
        'Lexus': 'lexus.svg',
        'Mercedes-Benz': 'Mercedes-Benz_free_logo.svg',
        'MINI': 'mini-cooper.svg',
        'Mitsubishi': 'mitsubishi.svg',
        'Nissan': 'Nissan_2020_logo.svg',
        'Renault': 'Renault.svg',
        'Alfa Romeo': 'Romeo_Logo.svg',
        'SEAT': 'SEAT_Logo_from_2017.svg',
        'Škoda': 'skoda.svg',
        'Subaru': 'subaru.svg', 
        'Suzuki': 'suzuki.svg',
        'Tesla': 'Tesla.svg',
        'Toyota': 'toyota.svg',
        'Volkswagen': 'Volkswagen_logo_2019.svg',
        'Volvo': 'volvo.svg'
    }
    
    # Update brands with logo paths
    updated_brands = 0
    
    for brand in catalog['brands']:
        brand_name = brand['name']
        
        # Check if brand has a logo mapping
        if brand_name in logo_mapping:
            logo_file = logo_mapping[brand_name]
            logo_path = f"assets/logos/{logo_file}"
            
            # Verify logo file exists
            if logo_file in logo_files:
                brand['logo'] = logo_path
                print(f"✅ {brand_name} -> {logo_file}")
                updated_brands += 1
            else:
                print(f"❌ {brand_name} -> {logo_file} (file not found)")
        else:
            # Check if already has a logo
            if 'logo' in brand:
                print(f"🔹 {brand_name} -> already has logo: {brand['logo']}")
            else:
                print(f"⚠️  {brand_name} -> no logo mapping found")
    
    # Save updated catalog
    with open('assets/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    
    print(f"\nLogo update complete:")
    print(f"- Updated {updated_brands} brands with logos")
    print(f"- Available logo files: {len(logo_files)}")
    
    # Show available logos that weren't used
    used_logos = set(logo_mapping.values())
    unused_logos = [f for f in logo_files if f not in used_logos]
    
    if unused_logos:
        print(f"- Unused logo files: {unused_logos}")

if __name__ == "__main__":
    fix_brand_logos()