import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    'pdm-parafil':          'https://images.squarespace-cdn.com/content/v1/5de863544ebd8e63f0f2684b/75fa169e-df29-428f-b851-f41b42e60f5f/refill-syringes-Parafil-2023.jpg',
    'pdm-nanohybrid':       'https://images.squarespace-cdn.com/content/v1/5de863544ebd8e63f0f2684b/1577154937803-U4ARNHW3ZGPQXWNUJZAL/composite_azul_3tubos-2.jpg',
    'pdm-hybrid':           'https://images.squarespace-cdn.com/content/v1/5de863544ebd8e63f0f2684b/1577157569144-THYQB4QS0DRN933OLUDZ/hybrid_composite_3jeringas-2.jpg',
    'pdm-chemcure':         'https://images.squarespace-cdn.com/content/v1/5de863544ebd8e63f0f2684b/1577203231715-5HNT8ZQHMVNQPFTZ1M4V/composite_paste_box-2.jpg',
    'pdm-automix-cement':   'https://images.squarespace-cdn.com/content/v1/5de863544ebd8e63f0f2684b/1577244211490-FOWVETGDXDR37OY3FR5W/DUAL-CURE-COMPOSITE-2.jpg',
    'pdm-lc-glass-ionomer': 'https://images.squarespace-cdn.com/content/v1/5de863544ebd8e63f0f2684b/11019087-0d4b-4bd1-bed0-be0bcb3273b2/glass_ionomer_set-2-v2.jpg',
    'pdm-self-etch':        'https://images.squarespace-cdn.com/content/v1/5de863544ebd8e63f0f2684b/1579994901493-IS5MARIV05DSP490FTN2/self-etch-bonding-agent.jpg',
    'pdm-ortho-adhesive-lc':'https://images.squarespace-cdn.com/content/v1/5de863544ebd8e63f0f2684b/a244980e-75da-4d5c-9a86-03a479d16b6e/VLC_orthodont_box-2-v2.jpg',
    'pdm-band-cement':      'https://images.squarespace-cdn.com/content/v1/5de863544ebd8e63f0f2684b/1577500924512-EFTM59073IWJ7OMYKOT6/DualCore_Glass_Ionomer-2.jpg',
}

for pid, url in photos.items():
    pattern = f"(id:'{pid}'[^}}]*?)img:'[^']+'"
    new_content = re.sub(pattern,
                         lambda m, u=url: m.group(1) + f"img:'{u}'",
                         content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        changes += 1
        print(f"  Photo updated: {pid}")
    else:
        print(f"  SKIPPED: {pid}")

print(f"\nTotal cambios: {changes}")
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("GUARDADO")
