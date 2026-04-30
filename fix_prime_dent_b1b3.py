import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    # --- Batch 1: Composites & adhesives ---
    'pd-composite':    'https://firstchoicedentalsupplies.com/cdn/shop/products/ResinaMicro-Hybrid_1024x1024@2x.png?v=1589859357',
    'pd-adhesivo':     'https://firstchoicedentalsupplies.com/cdn/shop/products/AdhesiveBondingPD_1024x1024@2x.png?v=1589861222',
    'pdm-parafil':     'https://firstchoicedentalsupplies.com/cdn/shop/products/PDParafil4.5gSyringe_1024x1024.png?v=1634153499',
    'pdm-nanohybrid':  'https://firstchoicedentalsupplies.com/cdn/shop/products/PDNHSyringe_600x400_86690c6b-1b81-4663-9eb3-ab5cc9941f98_1024x1024.png?v=1590704632',
    'pdm-hybrid':      'https://firstchoicedentalsupplies.com/cdn/shop/products/PDHSyringe-UniversalImage_1024x1024@2x.png?v=1589859684',
    'pdm-chemcure':    'https://firstchoicedentalsupplies.com/cdn/shop/products/PD5.5Bond_1024x1024@2x.png?v=1670949276',
    'pdm-parafil-gingiva': 'https://apexdentalexpress.com/cdn/shop/products/primedental9999-7100gingivakit_1024x1024.jpg?v=1636921325',
    'pdm-parafil-stain':   'https://apexdentalexpress.com/cdn/shop/products/DENTAL-PARAFIL-STAIN_1024x1024@2x.jpg?v=1589980063',
    'pdm-veneer-cement':   'https://tricountydental.com/cdn/shop/files/Prime-Dent_Veneer_Cement_Translucent.png?v=1769641997&width=1946',

    # --- Batch 3: Misc accessories ---
    'pdm-rc-cream':        'https://firstchoicedentalsupplies.com/cdn/shop/products/RC-Cream_1024x1024@2x.png?v=1589941707',
    'pdm-dental-dam':      'https://firstchoicedentalsupplies.com/cdn/shop/products/PDDentalDam_600x400_518704cb-996a-4716-8c04-98bc86a41fb8_1024x1024@2x.png?v=1607115362',
    'pdm-block-out-resin': 'https://firstchoicedentalsupplies.com/cdn/shop/products/PDBlockOut_1024x1024@2x.png?v=1658764404',
    'pdm-ortho-adhesive-lc': 'https://firstchoicedentalsupplies.com/cdn/shop/products/PDOrthoAdhesive2SyringeKit_1024x1024@2x.png?v=1589911630',
    'pdm-ortho-adhesive-sc': 'https://firstchoicedentalsupplies.com/cdn/shop/products/PDOneStepOrthoBonding2SyringeKit2_1024x1024@2x.png?v=1619478128',
    'pdm-tray-adhesive':   'https://apexdentalexpress.com/cdn/shop/products/Capture_c1dcc734-7c49-4f05-acc6-cf91591ab00e_1024x1024.png?v=1586133489',
    'pdm-band-cement':     'https://apexdentalexpress.com/cdn/shop/products/s-l500_2_1024x1024.jpg?v=1675114353',
    'pdm-prime-core':      'https://apexdentalexpress.com/cdn/shop/products/s-l1600_7_1024x1024@2x.jpg?v=1586423921',
    'pdm-mixing-pads':     'https://apexdentalexpress.com/cdn/shop/products/57_1024x1024.png?v=1678739535',
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
