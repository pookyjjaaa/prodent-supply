import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open(r'C:\Catalago Prodent\website\js\products-data.js', encoding='utf-8') as f:
    content = f.read()

changes = 0

# ─── 1. Borgatta-001~012: brackets/kits → ortodoncia (were 'instrumental') ───
for bid in ['borgatta-001','borgatta-002','borgatta-003','borgatta-004',
            'borgatta-005','borgatta-006','borgatta-007','borgatta-008',
            'borgatta-009','borgatta-010','borgatta-011','borgatta-012']:
    # Match the id and then its cat field
    old = f"id:'{bid}'[^}}]*?cat:'instrumental'"
    def replacer(m, bid=bid):
        return m.group(0).replace("cat:'instrumental'", "cat:'ortodoncia'")
    new_content = re.sub(old, replacer, content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        changes += 1
        print(f"  Fixed {bid}: instrumental → ortodoncia")

# ─── 2. LineaBlack: fix misclassified categories ─────────────────────────────
lb_fixes = {
    'lb-xpression':   ('alambres', 'ortodoncia'),
    'lb-xpression-c': ('alambres', 'ortodoncia'),
    'lb-b-action':    ('alambres', 'ortodoncia'),
    'lb-black-duo':   ('brackets', 'ortodoncia'),
    'lb-elasticos':   ('accesorios', 'ortodoncia'),
    'lb-resorte':     ('alambres', 'ortodoncia'),
}
for pid, (old_cat, new_cat) in lb_fixes.items():
    pattern = f"(id:'{pid}'[^}}]*?)cat:'{old_cat}'"
    new_content = re.sub(pattern, lambda m: m.group(1) + f"cat:'{new_cat}'", content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        changes += 1
        print(f"  Fixed {pid}: {old_cat} → {new_cat}")

# ─── 3. Balsas portaimpresión: instrumental → materiales ──────────────────
# Hi-Tray trays are more accurately 'materiales' (impression accessories)
for pid in ['balsas-019', 'balsas-020']:
    pattern = f"(id:'{pid}'[^}}]*?)cat:'instrumental'"
    new_content = re.sub(pattern, lambda m: m.group(1) + "cat:'materiales'", content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        changes += 1
        print(f"  Fixed {pid}: instrumental → materiales")

# ─── 4. Edenta photos — replace catalog page images with web product photos ──
edenta_photos = {
    'edenta-801':     'https://www.swallowdental.co.uk/media/catalog/product/cache/a7a6ae71dcce89f9bbe783a6b44f6c60/8/0/801.314.042.jpg',
    'edenta-802':     'https://www.dentaltix.com/en/sites/default/files/styles/large/public/it20492_1_0.jpg',
    'edenta-805':     'https://cdn11.bigcommerce.com/s-vy71tlujw/images/stencil/1280x1280/products/3428/7901/D7961%5F%5F98514.1699435967.386.513%5F%5F02789.1716543397.jpg',
    'edenta-806':     'https://www.dentaltix.com/en/sites/default/files/styles/large/public/it20492_1_0.jpg',
    'edenta-838':     'https://prodentusa.com/wp-content/uploads/2025/06/round-end-cylinder-838-1.0mm-head-diamond-bur-K2-dental-600x600.jpg',
    'edenta-839':     'https://prodentusa.com/wp-content/uploads/2025/06/end-cutter-839-1.2mm-head-all-grit-diamond-bur-K2-Dental-600x600.jpg',
    'edenta-842':     'https://www.dentaltix.com/en/sites/default/files/styles/large/public/842-extra-largo_0_0.jpg',
    'edenta-845':     'https://www.swallowdental.co.uk/media/catalog/product/cache/a7a6ae71dcce89f9bbe783a6b44f6c60/8/0/801.314.042.jpg',
    'edenta-845kr':   'https://www.pearsondental.com/catalog/img/E22-2370.jpg',
    'edenta-wt':      'https://www.pearsondental.com/catalog/img/E222528.jpg',
    'edenta-cerapol': 'https://www.dentaltix.com/en/sites/default/files/styles/large/public/cerapol-super-243-050-12uds.jpg',
    'edenta-flexisnap':'https://d2p3duacfnfxvs.cloudfront.net/dontalia-com/products/52492.jpg',
    'edenta-crownprep':'https://www.swallowdental.co.uk/media/catalog/product/cache/a7a6ae71dcce89f9bbe783a6b44f6c60/e/d/edenta_diamond_crown_prep-kit.png',
    'edenta-topbrush': 'https://www.pearsondental.com/catalog/img/E22-8118.jpg',
}
for pid, url in edenta_photos.items():
    # Replace img:'imagenes/balsas/pag_XXX.jpg' for this product
    pattern = f"(id:'{pid}'[^}}]*?)img:'[^']+'"
    new_content = re.sub(pattern, lambda m, u=url: m.group(1) + f"img:'{u}'", content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        changes += 1
        print(f"  Updated photo: {pid}")

print(f"\nTotal cambios: {changes}")

total = len(re.findall(r"id:'[a-zA-Z0-9_-]+'", content))
print(f"Total productos: {total}")

with open(r'C:\Catalago Prodent\website\js\products-data.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("GUARDADO")
