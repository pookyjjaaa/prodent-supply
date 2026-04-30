import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    # ── Dentaltix blocked → Zhermack official CDN / other ──
    'balsas-001': 'https://www.zhermack.com/public/uploads/ZH-Web-Pack-Image-Hydrogum5-C302070_MDR.jpg',
    'balsas-004': 'https://www.zhermack.com/public/uploads/ZH-Web-Pack-Image-Orthoprint-C302145_MDR.jpg',
    'balsas-005': 'https://www.zhermack.com/public/uploads/ZH-Web-Pack-Image-Tropicalgin-fast-C302240_MDR.jpg',
    'balsas-006': 'https://www.zhermack.com/public/uploads/ZH-Web-Pack-Image-Hydrorise-Putty-C207010-MDR.jpg',
    'balsas-007': 'https://www.zhermack.com/public/uploads/ZH-Web-Pack-Image-Hydrorise-Putty-C207010-MDR.jpg',
    'balsas-008': 'https://www.zhermack.com/public/uploads/ZH-Web-Pack-Image-Hydrorise-Light-Body-C207000_MDR.jpg',
    'balsas-009': 'https://www.matestdental.com/cdn/shop/files/Hydrorise_Maxi_Heavy_fast.jpg?v=1728303376',
    'balsas-010': 'https://www.zhermack.com/public/uploads/ZH-Web-Pack-Image-Occlufast-Rock-C200726_MDR.jpg',
    'balsas-011': 'https://www.zhermack.com/public/uploads/ZH-Web-Pack-Image-Occlufast-CAD-C200800_MDR.jpg',
    'balsas-012': 'https://www.zhermack.com/public/uploads/ZH-Web-Pack-Image-Zetaplus-C100600.jpg',
    'balsas-013': 'https://www.zhermack.com/public/uploads/ZH-Web-Pack-Image-Oranwash_L-C100660.jpg',
    'balsas-014': 'https://www.zhermack.com/public/uploads/Zetalabor_C400790_MDR.jpg',
    'balsas-015': 'https://www.zhermack.com/public/uploads/Titanium_C400605_MDR.jpg',
    'balsas-017': 'https://surgimac.com/cdn/shop/files/microbrush-x-extended-refill-cartridge-v1_800x.jpg?v=1749405204',
    'balsas-020': 'https://cdn.dental-tribune.com/dti//0001/dc74f05a/cmVzaXplKHc9MTAyNztoPTU3OCk6c2hhcnBlbihsZXZlbD0wKTpvdXRwdXQoZm9ybWF0PWpwZWcp/up/dt/2021/05/Hy_tray_plastic_D5G-copy.jpg',
    'balsas-022': 'https://www.zhermack.com/public/uploads/ZH-Web-Pack-Image-Zeta-2-Sporex-C810011.jpg',
    'balsas-024': 'https://www.zhermack.com/public/uploads/Elite_Model.jpg',
    'balsas-025': 'https://www.zhermack.com/public/uploads/Elite_Model.jpg',
    'balsas-026': 'https://www.zhermack.com/public/uploads/Zetalabor_C400790_MDR.jpg',
    'balsas-027': 'https://www.zhermack.com/public/uploads/Titanium_C400605_MDR.jpg',
    'balsas-030': 'https://www.zhermack.com/public/uploads/Elite_Double22_C400832.jpg',
    'articulador-008': 'https://www.acedentalsupplies.com/wp-content/uploads/2020/05/MAGNETIC0.1.jpg',
    'edenta-802': 'https://www.swallowdental.co.uk/media/catalog/product/cache/a7a6ae71dcce89f9bbe783a6b44f6c60/b/u/bur_35.jpg',
    'edenta-806': 'https://cdn.vijaidental.com/product/798a7861-edef-4cee-af3b-2edff935635a/65e1ac2717607.webp',
    'edenta-842': 'https://www.swallowdental.co.uk/media/catalog/product/cache/a7a6ae71dcce89f9bbe783a6b44f6c60/i/m/image-cxf9xhanc-transformed.png',
    'edenta-cerapol': 'https://www.matestdental.com/cdn/shop/products/image_fff29fc1-3c95-4981-bd0a-6c1e51be6e76.jpg?v=1676125670',

    # ── Medesy PT probe URL corrections (space before "PT" stripped, not hyphenated) ──
    'medesy-616': 'https://www.medesy.it/site/wp-content/uploads/2023/01/Immagine_variante_prodotto_548slash1PT.jpg',
    'medesy-617': 'https://www.medesy.it/site/wp-content/uploads/2023/01/Immagine_variante_prodotto_548slash2PT.jpg',
    'medesy-618': 'https://www.medesy.it/site/wp-content/uploads/2023/01/Immagine_variante_prodotto_548slash3PT.jpg',
    'medesy-619': 'https://www.medesy.it/site/wp-content/uploads/2023/01/Immagine_variante_prodotto_548slash4PT.jpg',
    'medesy-620': 'https://www.medesy.it/site/wp-content/uploads/2023/01/Immagine_variante_prodotto_548slash5PT.jpg',
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
