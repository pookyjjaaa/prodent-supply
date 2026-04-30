import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    # ── Periosteal elevators (titanium) ──
    'medesy-391': 'https://www.pearsondental.com/catalog/img/M36-2950.jpg',
    'medesy-392': 'https://www.pearsondental.com/catalog/img/M36-2950.jpg',
    'medesy-395': 'https://www.pearsondental.com/catalog/img/M36-0416.jpg',

    # ── Surgical instruments / scalpels ──
    'medesy-404': 'https://www.pearsondental.com/catalog/img/M36-1768.jpg',
    'medesy-406': 'https://surgimac.com/cdn/shop/files/38dfc109-2aea-4144-b64b-59d55a6c358a_800x.jpg?v=1740960876',

    # ── Nabers furcation probe ──
    'medesy-629': 'https://surgimac.com/cdn/shop/files/Probe_Nabers_2N_1003677_800x.jpg?v=1774287396',

    # ── Amalgam carriers (all share same listing image) ──
    'medesy-797': 'https://www.matestdental.com/cdn/shop/files/Screenshot2025-02-15120538.jpg?v=1739610578&width=995',
    'medesy-798': 'https://www.matestdental.com/cdn/shop/files/Screenshot2025-02-15120538.jpg?v=1739610578&width=995',
    'medesy-799': 'https://www.matestdental.com/cdn/shop/files/Screenshot2025-02-15120538.jpg?v=1739610578&width=995',
    'medesy-800': 'https://www.matestdental.com/cdn/shop/files/Screenshot2025-02-15120538.jpg?v=1739610578&width=995',

    # ── Crown remover (cortacoronas) ──
    'medesy-842': 'https://surgimac.com/cdn/shop/files/vdr-surgimac-crownbridgeremovingpliers-13-1175_800x.png?v=1745357010',

    # ── Accessories / consumables ──
    'medesy-1016': 'https://surgimac.com/cdn/shop/files/Pellet-Dispenser-Small-Pellets-28R825_800x.png?v=1740945972',
    'medesy-1017': 'https://surgimac.com/cdn/shop/files/700-714-2_41e3fe49-589a-4a80-a1d7-ba11a4909e15.jpg?v=1749410848',
    'medesy-1018': 'https://surgimac.com/cdn/shop/files/saliva-ejectors-ZCBI.jpg?v=1752929879',
    'medesy-1019': 'https://surgimac.com/cdn/shop/files/CurvedHemostatForcepswithLockingMechanism_800x.jpg?v=1745357958',
    'medesy-1022': 'https://surgimac.com/cdn/shop/files/1200269_front_800x.jpg?v=1684968652',
    'medesy-1023': 'https://surgimac.com/cdn/shop/files/QualaUltraCleaner_final_8cfafae4-360d-4cc6-8e9e-14ca4c124cab.jpg?v=1752579485',
    'medesy-1024': 'https://surgimac.com/cdn/shop/files/QualaUltraCleaner_final_27fe9c90-addc-49ff-9c1c-15af26de4c55.jpg?v=1697143264',

    # ── Extraction forceps ──
    'medesy-1037': 'https://www.pearsondental.com/catalog/img/Medesy_Tooth%20Forceps.jpg',
    'medesy-1038': 'https://www.pearsondental.com/catalog/img/Medesy_Tooth%20Forceps.jpg',
    'medesy-1040': 'https://www.pearsondental.com/catalog/img/Medesy_Tooth%20Forceps.jpg',
    'medesy-1047': 'https://www.pearsondental.com/catalog/img/m365762.JPG',

    # ── Gracey curettes (Medesy Nerissimo, actual product photos from Practicon) ──
    'medesy-1064': 'https://cdn11.bigcommerce.com/s-54anm7w0kg/images/stencil/500x1800/products/8197/26910/70941108__70238.1751294171.jpg?c=1',
    'medesy-1066': 'https://cdn11.bigcommerce.com/s-54anm7w0kg/images/stencil/500x1800/products/8237/26915/70941110__14511.1751294189.jpg?c=1',
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
        print(f"  SKIPPED (not found or already set): {pid}")

print(f"\nTotal: {changes} changes")
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("GUARDADO")
