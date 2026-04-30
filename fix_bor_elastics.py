import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    # bor-055: Cadena Elástica Cerrada — reemplaza universum-dental (QR) con tienda.borgatta 1024x
    'bor-055': 'https://tienda.borgatta.com.mx/cdn/shop/files/conjunto-verde-neon_1024x.png?v=1772725221',

    # bor-057: Elásticos Intraorales Látex — reemplaza universum-dental (QR) con tienda.borgatta 1024x
    'bor-057': 'https://tienda.borgatta.com.mx/cdn/shop/files/Intraorales_20Borgatta_2052400px72DPIS_1024x.jpg?v=1772726239',
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
