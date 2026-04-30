import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

TIENDA = 'https://cdn.shopify.com/s/files/1/0588/7721/4871/files/'

photos = {
    'bor-036': TIENDA + '28-300-10_20M2400px72DPIS.jpg?v=1772728745',
    'bor-038': TIENDA + '28-300-10_20P12400px72DPIS.jpg?v=1772728745',
    'bor-063': TIENDA + 'BOR-352-P.png?v=1772727061',
    'bor-072': TIENDA + 'ALEXANDER_20ML2400_72DPISk.jpg?v=1772726366',
    'bor-073': 'https://socioscomerciales.borgatta.com.mx/cdn/shop/files/BOR-500_20F2400_72DPIS_1024x.jpg?v=1729674410',
    'bor-075': TIENDA + '500-031_20F2400px72DPIS.jpg?v=1772727304',
    'bor-076': TIENDA + '500-036_20F2400px72DPIS.jpg?v=1772727304',
    'bor-077': TIENDA + '500-032_20F2400px72DPIS_be749e15-6706-48f4-9040-30e600fbdb08.jpg?v=1772727290',
    'bor-078': TIENDA + '21-B_20F2400px72DPIS.jpg?v=1772727275',
    'bor-079': TIENDA + '500-012_20F2400px72DPIS_16586a97-ed69-4edb-a518-42f285ac5b8e.jpg?v=1772725700',
    'bor-080': TIENDA + '800-20_20F2400px72DPIS.jpg?v=1772728343',
    'bor-081': TIENDA + '0-001-442_20C2400px72DPIS.jpg?v=1772725786',
    'bor-083': TIENDA + 'CEPILLOS_22400px72DPIS-2.jpg?v=1772728161',
    'bor-087': TIENDA + 'VCECAZ_20342400_72DPIS.jpg?v=1772725730',
    'bor-089': TIENDA + 'VPBL_20A2400_72DPIS.jpg?v=1772725714',
    'bor-092': TIENDA + '0-000-705-12400px_1024x.jpg?v=1772725516',
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
