import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

# All from official primedentalmfg.com Squarespace CDN
BASE = 'https://images.squarespace-cdn.com/content/v1/5de863544ebd8e63f0f2684b/'
photos = {
    # Parafil LAB series
    'pdm-parafil-lab':       BASE + '1576898827212-J7DI0BOG30UPA9071G8N/parafil-lab-1.png',
    'pdm-parafil-lab-kit4':  BASE + '1576991162021-1IT8HVGRATY8U7L08PBN/parafil-lab-10.jpg',
    'pdm-parafil-lab-kit10': BASE + '1576991162021-1IT8HVGRATY8U7L08PBN/parafil-lab-10.jpg',
    'pdm-parafil-lab-opaque':BASE + '183ab78a-59cb-4cf9-ac30-507f41cd1b02/refill-syringes-Parafil-Lab-2023.jpg',
    'pdm-parafil-lab-primer':BASE + '183ab78a-59cb-4cf9-ac30-507f41cd1b02/refill-syringes-Parafil-Lab-2023.jpg',
    'pdm-parafil-lab-modeler':BASE + '183ab78a-59cb-4cf9-ac30-507f41cd1b02/refill-syringes-Parafil-Lab-2023.jpg',
    # Parafil other
    'pdm-parafil-gingiva':   BASE + '1587832636883-CZKKJASQV51KUZUZ955O/GINGIVA-TRIO-web.jpg',
    'pdm-parafil-stain':     BASE + '061ea685-1fc2-4a1c-83be-c4bcb2e59908/parafil-stain-V2.jpg',
    'pdm-parafil-kit20':     BASE + '1577154462391-ZITEKO3D2V4258TL3GZ9/kits.jpg',
    # Cements
    'pdm-veneer-cement':     BASE + '8e77bfd3-3f98-4b6a-8b5c-75c7d4ea9a86/veneer-cement-product-main.jpg',
    'pdm-zoe-cement':        BASE + '72bca001-77b1-4f18-a004-3ab4b04af8f0/ZOE-CEMENT-POWDER-%26-LIQUID-2-v2.jpg',
    'pdm-surgical-cement':   BASE + 'a370e9b2-5f4c-421e-80b5-756127826446/zoe_cement-2-v2.jpg',
    'pdm-copal-varnish':     BASE + '7aa2c283-81a5-4f70-a567-9c21d4c69394/Copal_2Botellas-2-v2.jpg',
    # Bond & Etch
    'pdm-porcelain-repair':  BASE + '1579996122731-7T4EGHMM9A1T80W9UT7K/porcelain-repair-kit-2.jpg',
    'pdm-silane':            BASE + '1579996716178-ILPOXML9TIE6G49RCHHA/SILIANE-BOND-ENHANCER-2.jpg',
    'pdm-hema-desensitizer': BASE + '18a3be63-624a-46ff-9c99-ab9f49a32f5a/HEMA-DESENSITIZER-2.jpg',
    # Prevent & Prepare
    'pdm-prime-gel':         BASE + '1577411999087-8LR8K6CK8ODKXXJ7H8SF/Prime_Topical-2.jpg',
    'pdm-pit-fissure':       BASE + '1577410287550-4DKSNHOZNVUDEHN1HY5T/pit%26fissure_sealant-2.jpg',
    'pdm-prime-paste':       BASE + '8077aa36-3cd6-4e1b-bfe3-b867bbd499e4/Prime_Paste_2bottles-2-v2.jpg',
    # Endodontics
    'pdm-root-canal':        BASE + '1577414125599-MSV2EXBTFW68YPRSZRVN/RootCanal_Kit-2.jpg',
    'pdm-rc-cream':          BASE + '8867c4e4-2c5a-4e07-ae1c-98b57f580619/RootCanal_2jeringas-16x9.jpg',
    # Whitening/Isolation
    'pdm-dental-dam':        BASE + '1577419559075-8PIDHRQ9II8QQRQVQ17S/light-cure-dental-dam.jpg',
    'pdm-block-out-resin':   BASE + '1577420073475-1ZT0ZWB7CF5Z6V6XKB05/block-out-resin.jpg',
    # Core build-up
    'pdm-prime-core':        BASE + '1577420769432-YMLFTYIXLP236UIXZ4TJ/CoreBuild_Paste-2.jpg',
    # Orthodontics
    'pdm-ortho-adhesive-sc': BASE + 'c11b1bae-1f2c-4a5f-b425-a6c53fa4fa96/OneStep_Ortho_Box-2-v2.jpg',
    # Accessories
    'pdm-mixing-pads':       BASE + '1577508474002-2K5ABWIGMC19E5OGDV2K/papel_Stock.jpg',
    'pdm-mixing-spatulas':   BASE + '1577509090649-Z8W87FX23WAMGNAK0FW1/lanzetas-2.jpg',
    'pdm-brushes':           BASE + '1577509356280-ZET58SZWTB0XGN0XAMNU/brochas_tool-2.jpg',
    'pdm-needle-tips':       BASE + '1577509560082-3NVMPWPBONNAIZ6EOL1D/brochas_tool-22.jpg',
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
