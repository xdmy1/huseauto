#!/usr/bin/env python3
import json

def fix_brand_capitalization():
    """Fix capitalization of specific brands in catalog"""
    
    # Load current catalog
    try:
        with open('assets/catalog.json', 'r', encoding='utf-8') as f:
            catalog = json.load(f)
    except FileNotFoundError:
        print("Error: assets/catalog.json not found")
        return
    
    # Brand name fixes - old name -> new name
    brand_fixes = {
        'geely': 'Geely',
        'Geely': 'Geely',  # Keep if already correct
        'chery': 'Chery', 
        'Chery': 'Chery',  # Keep if already correct
        'peugeot': 'Peugeot',
        'PEUGEOT': 'Peugeot',
        'dodge': 'Dodge',
        'DODGE': 'Dodge'
    }
    
    updated_brands = 0
    
    for brand in catalog['brands']:
        old_name = brand['name']
        
        # Check if this brand needs fixing
        if old_name in brand_fixes:
            new_name = brand_fixes[old_name]
            if old_name != new_name:
                brand['name'] = new_name
                print(f"✅ Updated: '{old_name}' → '{new_name}'")
                updated_brands += 1
            else:
                print(f"🔹 Already correct: '{old_name}'")
    
    # Save updated catalog
    with open('assets/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    
    print(f"\nCapitalization fix complete:")
    print(f"- Updated {updated_brands} brand names")
    print(f"- Total brands: {len(catalog['brands'])}")

if __name__ == "__main__":
    fix_brand_capitalization()