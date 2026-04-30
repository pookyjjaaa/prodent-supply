import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    # AI029: Caja Sombreado Mezclador p/Resina — paleta de mezcla de colores
    'AI029': 'https://harvestdental.com/cdn/shop/products/Tray_ProductHero_1_700x933_032123__19561.1680550050.1280.1280_3dafecae-ea73-453d-8562-9b9beac52f60.png?v=1704399115',

    # AI030: Muelitas Caja Plástica p/Piezas Dentales — cajita en forma de muela
    'AI030': 'https://azdentall.com/cdn/shop/products/235.jpg?v=1675070209&width=1946',

    # AI042AM: Charola Esterilizar CH 5 Instrumentos — cassette esterilización pequeño
    'AI042AM': 'https://cdn.shopify.com/s/files/1/0903/7152/2842/files/5_Instruments_Cassette_Rack_for_Autoclave_1.png?v=1742373290',
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
