import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

CRD = 'https://www.clinicalresearchdental.com/cdn/shop/'
GARIMA = 'https://garimadental.com/wp-content/uploads/'

photos = {
    # 024 - Pasta dental Opalescence (01-0401)
    'vamasa-024': CRD + 'products/Opalescence_Whitening_Toothpaste_535x.jpg?v=1572316120',
    # 025 - Opalustre (01-05551)
    'vamasa-025': CRD + 'products/Opalustre-syringe-open_WHITEN_535x.jpg?v=1572316120',
    # 026 - Opalescence Endo al 35% (01-1323)
    'vamasa-026': CRD + 'products/Opalescence-Endo-syringe_WHITEN_535x.jpg?v=1572316120',
    # 027 - UltraEz (01-1008)
    'vamasa-027': CRD + 'products/UltraEz-syringe_WHITEN_535x.jpg?v=1572316120',
    # 028 - Opalescence Quick 45% (01-5346)
    'vamasa-028': CRD + 'products/5346_Opalescence-Quick-45pct-Kit-4pk-open_WHITEN_535x.jpg?v=1582569225',
    # 029 - Resina LC Block Out (01-0242)
    'vamasa-029': CRD + 'products/242_LC-Block-Out-Resin-Mini-Refill-open_ACCESSORIES_535x.jpg?v=1572316112',
    # 030 - Umbrella (01-4870)
    'vamasa-030': CRD + 'products/4870_Umbrella-Retractor-5pk-Pkg_ACCESSORIES_535x.jpg?v=1572316112',
    # 031 - Iso Block (01-0331)
    'vamasa-031': CRD + 'products/331_IsoBlock-Lip-Cheek-Retractor-10pk-open_ACCESSORIES_535x.jpg?v=1572316112',
    # 032 - Vinyl Cutters (01-0604)
    'vamasa-032': CRD + 'products/604_Vinyl-Cutter-Single_TRAY-MAKING_535x.jpg?v=1572316112',
    # 033 - UltraTrim (01-0605)
    'vamasa-033': CRD + 'products/605_UltraTrim-Single_TRAY-MAKING_535x.jpg?v=1572316112',
    # 034 - KleerView (01-1820)
    'vamasa-034': CRD + 'products/1820_KleerView-Retractor-Adult-10pk-open_ACCESSORIES_535x.jpg?v=1572316112',
    # 035 - Ultrapro Tx (01-8318)
    'vamasa-035': CRD + 'products/8318_UltraPro-Tx-Prophy-Angle-Soft-Cup-500pk-open_PROPHY_535x.jpg?v=1572316112',
    # 036 - Sable Seek (01-1805)
    'vamasa-036': CRD + 'products/1805_Sable-Seek-4pk-syringe-open_CARIES_535x.jpg?v=1572316112',
    # 037 - Láminas SoftTray (01-0226)
    'vamasa-037': CRD + 'products/226_SoftTray-Sheet-0.035in-25pk-open_TRAY-MAKING_535x.jpg?v=1572316112',
    # 038 - PropGard (01-4100)
    'vamasa-038': CRD + 'products/4100_PropGard-Lg-5pk-open_ACCESSORIES_535x.jpg?v=1572316112',
    # 039 - InterGuard (01-3097)
    'vamasa-039': CRD + 'products/3097_InterGuard-4mm-50pk-open_ACCESSORIES_535x.jpg?v=1572316112',
    # 040 - Consepsis Scrub (01-0732)
    'vamasa-040': CRD + 'products/732_Consepsis-Scrub-4pk-syringe-open_SURFACE-TREATMENT_535x.jpg?v=1572316112',
    # 041 - Omni-Matrix Sectional (01-0317)
    'vamasa-041': CRD + 'products/317_OmniMatrix-Sectional-Kit-40pk-open_MATRICES_535x.jpg?v=1572316112',
    # 042 - OraSeal (01-2352)
    'vamasa-042': CRD + 'products/2352_OraSeal-Caulking-Syringe-Putty-Kit_ACCESSORIES_535x.jpg?v=1572316112',
    # 043 - Astringedent X (01-0112)
    'vamasa-043': CRD + 'products/112_AstringedentX-Bottle-30ml-open_HEMOSTATICS_535x.jpg?v=1572316112',
    # 044 - Starbrush (01-1094)
    'vamasa-044': CRD + 'products/1094_StarBrush-100pk-open_TIPS_535x.jpg?v=1572316112',
    # 045 - Empacador de hilo retractor (01-0170)
    'vamasa-045': CRD + 'products/170_UltraPak-Cord-Packer-Normal-45deg-Single_INSTRUMENTS_535x.jpg?v=1572316112',
    # 046 - Hilos UltraPak (01-0131)
    'vamasa-046': CRD + 'products/131_UltraPak-Cord-000-Black-244cm-open_RETRACTION_535x.jpg?v=1572316112',
    # 047 - Porcelain Etch y Silano (01-0406)
    'vamasa-047': CRD + 'products/406_Porcelain-Etch-Silane-Kit-open_SURFACE-TREATMENT_535x.jpg?v=1572316112',
    # 048 - ViscoStat Clear (01-6409)
    'vamasa-048': CRD + 'products/6409_ViscoStat-Clear-4pk-syringe-open_HEMOSTATICS_535x.jpg?v=1572316112',
    # 049 - Cepillos Jiffy (01-1029)
    'vamasa-049': CRD + 'products/1029_Jiffy-Brush-5pk-Cup-Regular-open_POLISHING_535x.jpg?v=1572316112',
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
