#!/usr/bin/env python3
import json

def update_alcantara_prices():
    """Update Alcantara prices: regular 4200 MDL, Romb 4300 MDL"""
    
    # Load current catalog
    try:
        with open('assets/catalog.json', 'r', encoding='utf-8') as f:
            catalog = json.load(f)
    except FileNotFoundError:
        print("Error: assets/catalog.json not found")
        return
    
    updated_alcantara = 0
    updated_romb = 0
    
    for product in catalog['products']:
        # Update Alcantara products (non-romb) to 4200
        if product['groupId'] == 'alcantara':
            product['price'] = 4200
            updated_alcantara += 1
            print(f"Updated {product['code']} - {product['title']} to 4200 MDL")
        
        # Update Alcantara Romb products to 4300
        elif product['groupId'] == 'alc_romb':
            product['price'] = 4300
            updated_romb += 1
            print(f"Updated {product['code']} - {product['title']} to 4300 MDL")
    
    # Save updated catalog
    with open('assets/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    
    print(f"\nPrice update complete:")
    print(f"- {updated_alcantara} Alcantara products updated to 4200 MDL")
    print(f"- {updated_romb} Alcantara Romb products updated to 4300 MDL")

if __name__ == "__main__":
    update_alcantara_prices()