import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

CRD = 'https://www.clinicalresearchdental.com/cdn/shop/'

photos = {
    'vamasa-001': CRD + 'products/4750-US_Opalescence-Boost-Intro-Kit-open_WHITEN_fc8af7b3-011d-4b60-8806-d46cfe0f54ed_535x.jpg?v=1604073065',
    'vamasa-002': CRD + 'files/Opalescence-PF-10-percent-Mint-Patient-Kit-open_535x.jpg?v=1747833159',
    'vamasa-003': CRD + 'products/Opalescence_Go_Mint_and_Mint_3D_2_535x.jpg?v=1572377433',
    'vamasa-004': CRD + 'products/1824_OpalDam-Green-Kit-open-no-box_WHITEN_89c1a7de-91e4-4274-b523-e8335381b896_535x.jpg?v=1579723499',
    'vamasa-005': CRD + 'products/UltraSeal-XT-plus-sealant-syringe-with-Inspiral-Brush-Tip-3D_PREVENT-HYGIENE_535x.jpg?v=1631290004',
    'vamasa-006': CRD + 'products/3532_UltraSeal-XT-hydro-Opaque-White-Kit-open1_PREVENT-highdef_535x.jpg?v=1631290727',
    'vamasa-007': CRD + 'products/enamelast-unit-dose-single-walterberry_535x.jpg?v=1745510029',
    'vamasa-008': CRD + 'files/consepsis-indispense-kit-box-open-30ml_535x.jpg?v=1759756624',
    'vamasa-009': CRD + 'products/8801_Omni-Matrix-Universal-6.5mm-Winged-.001-SS-Orange-open_PREPARE_da942073-f573-486c-ab93-7e4b39231ef6_535x.jpg?v=1749580206',
    'vamasa-010': CRD + 'products/111_Astringedent-30ml-bottle-open_TM_535x.jpg?v=1741103609',
    'vamasa-011': CRD + 'files/ultradent-pq1-single-resin-bonding_535x.jpg?v=1736363988',
    'vamasa-012': CRD + 'files/773164_ultra_etch_4pk_kit_package_535x.jpg?v=1773258181',
    'vamasa-013': CRD + 'products/415_Ultra-Blend-plus-Kit-open_BOND-ETCH_535x.jpg?v=1756406832',
    'vamasa-014': CRD + 'products/4551_Peak-Universal-Bond-Total-Etch-Intro-Kit-open_BOND-ETCH_535x.jpg?v=1572316109',
    'vamasa-015': CRD + 'files/JiffyAssorted_535x.png?v=1682953034',
    'vamasa-016': 'https://infoapac.ultradent.com/hs-fs/hubfs/Forma_packaging.jpg',
    'vamasa-017': CRD + 'products/5540_Ultradent-Diamond-Polish-Mint-0.5micron-2pk-open_FINISH_535x.jpg?v=1585329117',
    'vamasa-018': CRD + 'products/PermaSeal-syringe-with-tip_FINISH_535x.jpg?v=1585666210',
    'vamasa-019': CRD + 'products/Valo_Grand_535x.png?v=1580924276',
    'vamasa-020': CRD + 'products/ChlorCid-V-IndiSpense-syringe_ENDODONTICS_535x.jpg?v=1629475288',
    'vamasa-021': CRD + 'products/645_ViscoStat-IndiSpense-Syringe-open_TM_535x.jpg?v=1725389901',
    'vamasa-022': CRD + 'products/Ultradent-UltraCal-XS-Calcium-Hydroxide-Paste-Syringes_535x.png?v=1617912925',
    'vamasa-023': CRD + 'files/947_PermaFlo_A1_2pk_box_open_1022_535x.jpg?v=1749145468',
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
