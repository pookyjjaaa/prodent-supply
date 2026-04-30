import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    # Arco Facial Standard Bioart
    'articulador-004': 'https://smilequip.com/cdn/shop/products/arco_std.jpg?v=1489520156',
    # Soporte del Tenedor
    'articulador-005': 'https://ddmolar.com/cdn/shop/products/soportedegarfo.png?v=1618769874&width=1946',
    # Mesa de Camper
    'articulador-006': 'https://smilequip.com/cdn/shop/products/campers_table.jpg?v=1489520156',
    # Placa de Montaje Magnética
    'articulador-007': 'https://smilequip.com/cdn/shop/products/Magnetic_Mounting_Plate.jpg?v=1489520156',
    # Placa de Montaje Riel
    'articulador-009': 'https://www.acedentalsupplies.com/wp-content/uploads/2023/12/monting-plate-2-bio-art.jpg',
    # Regla Fox
    'articulador-011': 'https://www.acedentalsupplies.com/wp-content/uploads/2020/05/fox-ruler-1.jpg',
    # Banderola de Broadrick
    'articulador-012': 'https://www.acedentalsupplies.com/wp-content/uploads/2020/05/Flag-bio-art.jpg',
    # Tenedor para Desdentado
    'articulador-013': 'https://ddmolar.com/cdn/shop/products/desde4ntado_ajustable.jpg?v=1533515769&width=1946',
    # Estuche para Articulador
    'articulador-015': 'https://www.dentalstore.com.co/wp-content/uploads/2023/04/Estuche-Plastico-Articulador-A7-Plus-600x600.png',
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
