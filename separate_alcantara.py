#!/usr/bin/env python3
import json

def separate_alcantara_groups():
    """Separate Alcantara from Alcantara Romb in product groups"""
    
    # Load current catalog
    try:
        with open('assets/catalog.json', 'r', encoding='utf-8') as f:
            catalog = json.load(f)
    except FileNotFoundError:
        print("Error: assets/catalog.json not found")
        return
    
    # First, update productGroups to include separate Alcantara group
    # Check if we need to add the Alcantara group
    alcantara_group_exists = any(group['id'] == 'alcantara' for group in catalog['productGroups'])
    
    if not alcantara_group_exists:
        # Add Alcantara group after eco_alc
        new_group = {
            "id": "alcantara", 
            "title": "Huse Alcantara"
        }
        
        # Find position to insert (after eco_alc if it exists)
        insert_pos = 1  # Default position
        for i, group in enumerate(catalog['productGroups']):
            if group['id'] == 'eco_alc':
                insert_pos = i + 1
                break
        
        catalog['productGroups'].insert(insert_pos, new_group)
        print("Added new Alcantara group")
    
    # Now update the products - change Alcantara products to use 'alcantara' group
    updated_products = 0
    for product in catalog['products']:
        # Check if this is an Alcantara product (not Alcantara Romb)
        if product['groupId'] == 'eco_alc' and 'Alcantara' in product['title'] and 'Romb' not in product['title']:
            product['groupId'] = 'alcantara'
            updated_products += 1
            print(f"Updated {product['title']} - {product['code']} to alcantara group")
    
    # Update Alcantara Romb products to use 'alc_romb' group 
    updated_romb = 0
    for product in catalog['products']:
        if product['groupId'] == 'eco_alc' and 'Alcantara Romb' in product['title']:
            product['groupId'] = 'alc_romb'
            updated_romb += 1
            print(f"Updated {product['title']} - {product['code']} to alc_romb group")
    
    # Save updated catalog
    with open('assets/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    
    print(f"\nSeparation complete:")
    print(f"- {updated_products} Alcantara products moved to 'alcantara' group")
    print(f"- {updated_romb} Alcantara Romb products moved to 'alc_romb' group")
    print(f"- Total product groups: {len(catalog['productGroups'])}")
    
    # Display final group counts
    group_counts = {}
    for product in catalog['products']:
        group_id = product['groupId']
        group_counts[group_id] = group_counts.get(group_id, 0) + 1
    
    print("\nProduct count by group:")
    for group in catalog['productGroups']:
        count = group_counts.get(group['id'], 0)
        print(f"  {group['title']} ({group['id']}): {count} products")

if __name__ == "__main__":
    separate_alcantara_groups()