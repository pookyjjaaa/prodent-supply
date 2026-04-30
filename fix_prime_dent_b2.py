import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    'pdm-lc-glass-ionomer': 'https://firstchoicedentalsupplies.com/cdn/shop/products/PDLCIonomer_600x400_bac4e8a0-91a1-4d54-8b73-14daac8b8363_1024x1024.png?v=1594333760',
    'pdm-zoe-cement':        'https://tricountydental.com/cdn/shop/files/Prime-DentZincOxideEugenol_Zoe_CementKitsm.png?v=1769548520&width=1946',
    # pdm-surgical-cement: Not found — use ZOE cement image as closest fallback
    'pdm-surgical-cement':   'https://tricountydental.com/cdn/shop/files/Prime-DentZincOxideEugenol_Zoe_CementKitsm.png?v=1769548520&width=1946',
    'pdm-copal-varnish':     'https://tricountydental.com/cdn/shop/files/Prime-DentCopalVarnish15mlBottlesm.png?v=1767216661&width=1946',
    'pdm-porcelain-repair':  'https://firstchoicedentalsupplies.com/cdn/shop/files/PDPorcelainRepairKit_600x400_2d50abc5-40a9-4bd3-bed9-6d9f074de5b5_1024x1024.jpg?v=1688060243',
    'pdm-silane':            'https://firstchoicedentalsupplies.com/cdn/shop/products/PDSilaneBondEnhancer4Syr.Kit2_1024x1024.png?v=1619478388',
    'pdm-bonding-resin':     'https://dentimedonline.com/wp-content/uploads/2020/11/SURFACE-SEALANT-primedent.jpg',
    'pdm-hema-desensitizer': 'https://firstchoicedentalsupplies.com/cdn/shop/products/PDHema_1024x1024.png?v=1589940791',
    'pdm-prime-gel':         'https://firstchoicedentalsupplies.com/cdn/shop/products/AcidoJeringaAzul-CloseUp_1024x1024.png?v=1589946739',
    'pdm-pit-fissure':       'https://firstchoicedentalsupplies.com/cdn/shop/products/PitandFissureSealant1_1024x1024.png?v=1594335468',
    'pdm-prime-paste':       'https://firstchoicedentalsupplies.com/cdn/shop/products/PDProphyPasteMint_600x400_7c137ce4-8908-4957-a948-111add499f7a_1024x1024.png?v=1628883360',
    'pdm-root-canal':        'https://amplemeds.com/cdn/shop/files/Prime-Dental-RC-Seal.jpg?v=1757499757&width=1946',
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
