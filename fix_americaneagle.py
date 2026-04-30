import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

AE = 'https://amerdental.com/cdn/shop/files/'
AEP = 'https://amerdental.com/cdn/shop/products/'
AMED = 'https://www.am-eagle.de/wp-content/uploads/'

photos = {
    'ae-001': AE  + 'AE-103.png?v=1689086492&width=4096',
    'ae-002': AE  + 'AE-104_new.png?v=1689090259&width=4096',
    'ae-003': AE  + 'AE-105.png?v=1689091466&width=4096',
    'ae-004': AE  + 'AE-107.png?v=1689087482&width=4096',
    'ae-005': AE  + 'AE-108.png?v=1689088496&width=4096',
    'ae-006': AEP + 'AE-148_mfg_v2.png?v=1670874305&width=4096',
    'ae-007': AEP + 'AE_149_mfg_v2.png?v=1670870892&width=4096',
    'ae-008': AE  + 'AE-166_mfg_v2.jpg?v=1772046636&width=4096',
    'ae-009': AMED + 'AEGA11-12XPZ.jpg',
    'ae-010': AE  + 'AE-169_mfg_v2.jpg?v=1772047981&width=4096',
    'ae-011': AMED + 'AECB1-2X-1.jpg',
    'ae-012': AE  + 'AE-101.png?v=1689020731&width=4096',
    'ae-013': AE  + 'AE-111.png?v=1689342516&width=4096',
    'ae-014': AE  + 'AE-100_MFG_V2.jpg?v=1772045116&width=4096',
    'ae-015': AE  + 'AE-112.png?v=1689343891&width=4096',
    'ae-016': AE  + 'AE-110.png?v=1689104838&width=4096',
    'ae-017': AMED + 'AESETX.jpg',
    'ae-018': AE  + 'AE-164.png?v=1703714428&width=4096',
    'ae-019': AE  + 'AE-334_mfg_v2.jpg?v=1773424506&width=4096',
    'ae-020': AMED + 'AEEXP11-12_2024.jpg',
    'ae-021': AMED + 'AEEXP23X-1.jpg',
    'ae-022': 'https://younginnovations.com/sites/default/files/Kontainer/aem4.jpg',
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
