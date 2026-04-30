import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    # --- Bad-ratio articulador accessories (smilequip 670x180 banners → proper product photos) ---
    'articulador-006': 'https://oralkart.com/cdn/shop/files/Bio-Art_Dental_Articulator_Camper_s_Table.webp?v=1736597415&width=1946',
    'articulador-007': 'https://azdentall.com/cdn/shop/files/1_4_89bf94d6-cc46-4cdb-aa4f-03d30e5e88f2.jpg',
    'articulador-010': 'https://storage.googleapis.com/drive.dentacarts.com/public/products/509/50919_1.jpeg',

    # --- Remaining Squarespace Prime Dent → CDN alternatives ---
    'pdm-parafil-lab-kit4':  'https://firstchoicedentalsupplies.com/cdn/shop/products/PDParafil4.5gSyringe_1024x1024@2x.png?v=1634153499',
    'pdm-parafil-lab-kit10': 'https://tricountydental.com/cdn/shop/files/1-15-13.webp?v=1712857098&width=1946',
    'pdm-parafil-kit20':     'https://tricountydental.com/cdn/shop/files/1-15-13.webp?v=1712857098&width=1946',
    'pdm-mixing-spatulas':   'https://cdn11.bigcommerce.com/s-54anm7w0kg/images/stencil/1280x1280/products/8717/27464/71124610%5F%5F60579.1751294772.jpg?c=1',
    'pdm-brushes':           'https://cdn11.bigcommerce.com/s-54anm7w0kg/images/stencil/1280x1280/products/9485/18675/7140431__04261.1751295623.jpg?c=1',
    'pdm-needle-tips':       'https://cdn11.bigcommerce.com/s-54anm7w0kg/images/stencil/1280x1280/products/10699/32178/7039513%5F%5F71150.1771877421.jpg?c=1',
}

for pid, url in photos.items():
    pattern = f"(id:'{pid}'[^}}]*?)img:'[^']+'"
    new_content = re.sub(pattern,
                         lambda m, u=url: m.group(1) + f"img:'{u}'",
                         content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        changes += 1
        print(f"  Updated: {pid}")
    else:
        print(f"  SKIPPED: {pid}")

print(f"\nTotal: {changes} changes")
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("GUARDADO")
