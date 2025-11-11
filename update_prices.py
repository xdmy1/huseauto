#!/usr/bin/env python3
import json

def update_product_prices():
    """Update product prices: 4200 MDL standard, 4300 MDL for Romb patterns"""
    
    catalog_file = "assets/catalog.json"
    
    try:
        with open(catalog_file, 'r', encoding='utf-8') as f:
            catalog = json.load(f)
    except FileNotFoundError:
        print("❌ assets/catalog.json not found!")
        return
    
    updated_products = 0
    romb_products = 0
    standard_products = 0
    
    for product in catalog['products']:
        old_price = product['price']
        
        # Check if product has "Romb" in title or groupId
        is_romb = ('romb' in product.get('title', '').lower() or 
                   'romb' in product.get('groupId', '').lower())
        
        if is_romb:
            new_price = 4300
            romb_products += 1
        else:
            new_price = 4200
            standard_products += 1
        
        if old_price != new_price:
            product['price'] = new_price
            updated_products += 1
            print(f"✅ Updated {product['title']} - {product['color']}: {old_price} → {new_price} MDL")
    
    # Save updated catalog
    with open(catalog_file, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    
    print(f"\n🎉 Price update complete:")
    print(f"- Updated {updated_products} products")
    print(f"- Romb products (4300 MDL): {romb_products}")
    print(f"- Standard products (4200 MDL): {standard_products}")
    print(f"- Total products: {len(catalog['products'])}")

if __name__ == "__main__":
    update_product_prices()