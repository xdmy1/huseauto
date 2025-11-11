#!/usr/bin/env python3
import json
import os
import re
from pathlib import Path

def parse_model_files():
    """Parse all car model files and extract model names with year ranges"""
    
    masini_folder = Path("masini")
    catalog_file = Path("assets/catalog.json")
    
    if not masini_folder.exists():
        print("❌ masini folder not found!")
        return
    
    if not catalog_file.exists():
        print("❌ assets/catalog.json not found!")
        return
    
    # Load current catalog
    with open(catalog_file, 'r', encoding='utf-8') as f:
        catalog = json.load(f)
    
    # Create brand mapping (normalize names)
    brand_mapping = {}
    for brand in catalog['brands']:
        brand_name = brand['name']
        # Create different possible file names
        possible_names = [
            f"{brand_name}.txt",
            f"{brand_name.upper()}.txt", 
            f"{brand_name.lower()}.txt",
            f"{brand_name.title()}.txt"
        ]
        
        # Special case mappings
        if brand_name == "Mercedes-Benz":
            possible_names.extend(["mercedes.txt", "Mercedes.txt", "MERCEDES.txt"])
        
        for possible_name in possible_names:
            file_path = masini_folder / possible_name
            if file_path.exists():
                brand_mapping[brand_name] = file_path
                break
    
    print(f"📁 Found model files for {len(brand_mapping)} brands")
    
    # Parse each brand's models
    updated_brands = 0
    
    for brand in catalog['brands']:
        brand_name = brand['name']
        
        if brand_name not in brand_mapping:
            print(f"⚠️  No model file found for {brand_name}")
            continue
        
        file_path = brand_mapping[brand_name]
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            new_models = []
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Extract model name with years
                model_name = extract_model_with_years(line, brand_name)
                if model_name:
                    new_models.append({
                        "name": model_name,
                        "years": "2000-2025"  # Keep for compatibility but won't be used
                    })
            
            if new_models:
                brand['models'] = new_models
                updated_brands += 1
                print(f"✅ Updated {brand_name}: {len(new_models)} models")
            else:
                print(f"⚠️  No models parsed for {brand_name}")
                
        except Exception as e:
            print(f"❌ Error processing {brand_name}: {e}")
    
    # Save updated catalog
    with open(catalog_file, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    
    print(f"\n🎉 Update complete:")
    print(f"- Updated {updated_brands} brands")
    print(f"- Total brands: {len(catalog['brands'])}")

def extract_model_with_years(line, brand_name):
    """Extract model name with year range from a line"""
    
    # Remove brand prefix if it exists
    line_clean = line
    if line.startswith(brand_name):
        line_clean = line[len(brand_name):].strip()
    
    # Try to extract year ranges in different formats
    year_patterns = [
        r'(\d{4})–(\d{4})',  # 2004–2011
        r'(\d{4})-(\d{4})',   # 2004-2011  
        r'din (\d{4})',       # din 2017
        r'(\d{4})–(\d{4})',  # with different dash
        r'(\d{4})\s*-\s*(\d{4})'  # with spaces
    ]
    
    years_found = None
    original_line = line_clean
    
    for pattern in year_patterns:
        match = re.search(pattern, line_clean)
        if match:
            if 'din' in pattern:
                # Format: din YYYY
                start_year = match.group(1)
                years_found = f"({start_year}+)"
                # Remove the "din YYYY" part
                line_clean = re.sub(r'\s*din\s*\d{4}.*', '', line_clean).strip()
            else:
                # Format: YYYY–YYYY
                start_year = match.group(1)
                end_year = match.group(2)
                years_found = f"({start_year}–{end_year})"
                # Remove the year range
                line_clean = re.sub(pattern, '', line_clean).strip()
            break
    
    if not years_found:
        # Try to find any 4-digit year
        year_match = re.search(r'\b(\d{4})\b', line_clean)
        if year_match:
            year = year_match.group(1)
            if 1980 <= int(year) <= 2030:  # Reasonable car year range
                years_found = f"({year})"
                line_clean = re.sub(r'\b\d{4}\b', '', line_clean).strip()
    
    # Clean up the model name
    model_name = clean_model_name(line_clean)
    
    if years_found and model_name:
        return f"{model_name} {years_found}"
    elif model_name:
        # If no years found, return just the model name
        return model_name
    else:
        return None

def clean_model_name(name):
    """Clean up model name by removing extra info"""
    
    # Remove common prefixes/suffixes
    name = re.sub(r'^\s*[-–]\s*', '', name)  # Remove leading dashes
    name = re.sub(r'\s*[-–]\s*$', '', name)  # Remove trailing dashes
    
    # Remove parenthetical info that's not year-related
    # But keep important model info like (E46), (W123), etc.
    name = re.sub(r'\s*\([^)]*(?:banchetă|spate|locuri|vedere|rândul|scaune|fără|cu|mecanism)[^)]*\)', '', name, flags=re.IGNORECASE)
    
    # Remove common descriptive phrases
    descriptive_phrases = [
        r'\s*hatchback\s*\d*\s*uși',
        r'\s*sedan\s*\d*\s*uși',
        r'\s*universal',
        r'\s*hatchback',
        r'\s*sedan',
        r'\s*\d+\s*locuri',
        r'\s*facelift\s*\d*',
        r'\s*versiuni?\s+[^(]*',
        r'\s*\(vezi\s+secțiunea[^)]*\)',
    ]
    
    for phrase in descriptive_phrases:
        name = re.sub(phrase, '', name, flags=re.IGNORECASE)
    
    # Clean up multiple spaces and trim
    name = re.sub(r'\s+', ' ', name).strip()
    
    return name if name else None

if __name__ == "__main__":
    parse_model_files()