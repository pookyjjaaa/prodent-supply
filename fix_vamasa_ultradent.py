import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()
changes = 0
photos = {
    # Opalescence toothpaste → opalescence.com official Shopify CDN
    'vamasa-024': 'https://opalescence.com/cdn/shop/files/PDP-HeroCarousel-Toothpaste-Original-Coolmint-Desktop.jpg?v=1762379840&width=1946',
    # Opalustre
    'vamasa-025': 'https://www.clinicalresearchdental.com/cdn/shop/products/Opalustre-4pk-Kit-open-in-box-3D-WHITEN_535x.jpg?v=1602686890',
    # Opalescence Endo 35%
    'vamasa-026': 'https://www.clinicalresearchdental.com/cdn/shop/files/opal-endo-open-kit_535x.jpg?v=1685388105',
    # UltraEz desensitizer
    'vamasa-027': 'https://www.clinicalresearchdental.com/cdn/shop/products/5721_UltraEz_Packaging_Right_535x.png?v=1654262777',
    # Opalescence Quick 45% → Boost (same category, in-office whitening)
    'vamasa-028': 'https://www.clinicalresearchdental.com/cdn/shop/products/4750-US_Opalescence-Boost-Intro-Kit-open_WHITEN_fc8af7b3-011d-4b60-8806-d46cfe0f54ed_535x.jpg?v=1604073065',
    # LC Block-Out Resin
    'vamasa-029': 'https://www.clinicalresearchdental.com/cdn/shop/products/240_LC-Block-Out-Resin-Kit-open2_WHITEN_4785b966-c8cc-4573-85b9-5b90fed0d83c_535x.jpg?v=1574116586',
    # Umbrella retractor
    'vamasa-030': 'https://www.clinicalresearchdental.com/cdn/shop/products/Ultradent-Umbrella-tongue-lip-cheek-retractor_535x.jpg?v=1614187923',
    # Iso Block lip/cheek retractor
    'vamasa-031': 'https://www.clinicalresearchdental.com/cdn/shop/products/331_IsoBlock-10pk-open-WHITEN_26869c87-f8ca-42f0-85b0-b0c20d084637_535x.jpg?v=1572316091',
    # Vinyl Cutters → UltraTrim scissors (same tray-making cutting category)
    'vamasa-032': 'https://www.clinicalresearchdental.com/cdn/shop/products/Ultradent-Ultra-Trim-Scalloping-Scissors_WHITEN_fe3a78c1-6338-4e68-905d-ca03b499b20d_535x.jpg?v=1572316091',
    # UltraTrim scalloping scissors
    'vamasa-033': 'https://www.clinicalresearchdental.com/cdn/shop/products/Ultradent-Ultra-Trim-Scalloping-Scissors_WHITEN_fe3a78c1-6338-4e68-905d-ca03b499b20d_535x.jpg?v=1572316091',
    # KleerView clear retractor
    'vamasa-034': 'https://www.clinicalresearchdental.com/cdn/shop/products/1821_KleerView-Adult-Size-open_WHITEN_535x.jpg?v=1608065094',
    # Ultrapro Tx prophy angle
    'vamasa-035': 'https://www.clinicalresearchdental.com/cdn/shop/products/Ultrapro-Tx-Prophy-Angle-Soft-single_PREVENT_6e4cfeb7-c60d-4d78-8f54-35f88661bf86_535x.jpg?v=1583187121',
    # Sable Seek caries indicator
    'vamasa-036': 'https://www.clinicalresearchdental.com/cdn/shop/products/233_Sable-Seek-Kit-open_PREPARE_b70e4e16-cd50-456d-9abe-d223f562de33_535x.jpg?v=1630097467',
    # SoftTray classic sheets
    'vamasa-037': 'https://www.clinicalresearchdental.com/cdn/shop/products/227_Sof-Tray-Classic-Sheets-Medium-open_WHITEN_535x.jpg?v=1590520813',
    # PropGard → E-Prop mouth prop (same bite block category)
    'vamasa-038': 'https://cdn11.bigcommerce.com/s-54anm7w0kg/images/stencil/500x1800/products/7399/26218/7102411__28579.1751293257.jpg?c=1',
    # InterGuard proxitector
    'vamasa-039': 'https://www.clinicalresearchdental.com/cdn/shop/products/3097_InterGuard-Kit-open_PREPARE_7fb21922-95b7-4860-9c64-02b6b5be4174_535x.jpg?v=1572316092',
    # Consepsis Scrub CHX
    'vamasa-040': 'https://www.clinicalresearchdental.com/cdn/shop/products/689_Consepsis-Scrub-IndiSpense-Syringe-open_PREPARE_d43903d2-affb-4b65-bc94-dc52e5008672_535x.jpg?v=1629129837',
    # OmniMatrix sectional
    'vamasa-041': 'https://www.clinicalresearchdental.com/cdn/shop/products/8801_Omni-Matrix-Universal-6.5mm-Winged-.001-SS-Orange-open_PREPARE_da942073-f573-486c-ab93-7e4b39231ef6_535x.jpg?v=1749580206',
    # OraSeal caulking putty
    'vamasa-042': 'https://www.clinicalresearchdental.com/cdn/shop/files/ultradent_oraseal_caulking_and_putty_535x.jpg?v=1765567401',
    # Astringedent X ferric sulfate
    'vamasa-043': 'https://www.clinicalresearchdental.com/cdn/shop/products/112_Astringedent-X-30ml-bottle-open_TM_535x.jpg?v=1725564230',
    # StarBrush intercoronal brush
    'vamasa-044': 'https://www.clinicalresearchdental.com/cdn/shop/products/Starbrush_0521_535x.jpg?v=1621955858',
    # UltraPak cord packer instrument
    'vamasa-045': 'https://www.clinicalresearchdental.com/cdn/shop/products/Fischers-Ultrapak-Packers-45-degree-to-handle_170-171__TM_535x.jpg?v=1576707208',
    # UltraPak retraction cord 000
    'vamasa-046': 'https://www.clinicalresearchdental.com/cdn/shop/products/e36f6c69-38f8-4a49-bb2b-22b1c0ce1516_535x.png?v=1625111003',
    # Porcelain Etch + Silane kit
    'vamasa-047': 'https://www.clinicalresearchdental.com/cdn/shop/files/ultradent__porcelain_etch_and_silane_535x.jpg?v=1772808241',
    # ViscoStat Clear aluminum chloride
    'vamasa-048': 'https://www.clinicalresearchdental.com/cdn/shop/products/6408_ViscoStat-Clear-IndiSpense-Syringe-refill-open_upright__TM_535x.jpg?v=1725393242',
    # Jiffy polishing cups/brushes
    'vamasa-049': 'https://www.clinicalresearchdental.com/cdn/shop/files/JiffyAssorted_535x.png?v=1682953034',
    # White Mac / White Mini Laser tips
    'vamasa-093': 'https://www.clinicalresearchdental.com/cdn/shop/products/White-Mac-Tip-single_TIPS_65933b86-fa1f-4fd4-9e45-4c2cc163a805_535x.jpg?v=1572316112',
}
for pid, url in photos.items():
    pattern = f"(id:'{pid}'[^}}]*?)img:'[^']+'"
    new_content = re.sub(pattern, lambda m, u=url: m.group(1) + f"img:'{u}'", content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        changes += 1
        print(f'  Updated: {pid}')
    else:
        print(f'  SKIPPED: {pid}')
print(f'\nTotal: {changes}')
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('GUARDADO')
