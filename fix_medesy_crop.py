import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0
skipped_manual = []

BASE = 'https://www.medesy.it/site/wp-content/uploads/2023/01/Immagine_variante_prodotto_'
BASE2 = 'https://www.medesy.it/site/wp-content/uploads/2023/02/'

# Products where filename is descriptive (not a Medesy code) — need manual lookup
# These will be handled separately
MANUAL = {
    'medesy-391': '877-Ti.jpg',         # Elevador 24G Titanio → related to 877
    'medesy-392': '879.jpg',            # Mead 7mm → Medesy 879
    'medesy-395': '882-Ti.jpg',         # Molt N.9 Titanio → related to 882
    'medesy-404': '3633-145.jpg',       # Mango bisturí angulado 145°
    'medesy-406': '3635-10.jpg',        # Láminas bisturí N.10
    'medesy-629': '569-1N.jpg',         # Sonda Nabers 1N → Medesy 569/1N
    'medesy-784': '608-3.jpg',          # Cleoid N.110
    'medesy-797': '3900-SM.jpg',        # Portaamalgama small
    'medesy-798': '3900-MD.jpg',        # Portaamalgama medium
    'medesy-799': '3900-LG.jpg',        # Portaamalgama large
    'medesy-800': '3900-JB.jpg',        # Portaamalgama jumbo
    'medesy-842': '4564-MO.jpg',        # Cortacoronas Montfort
    'medesy-843': '5420-ISO30.jpg',     # Plugger ISO30
    'medesy-844': '5420-ISO40.jpg',     # Plugger ISO40
    'medesy-845': '5420-ISO50.jpg',     # Plugger ISO50
    'medesy-846': '5420-ISO60.jpg',     # Plugger ISO60
    'medesy-847': '5420-ISO80.jpg',     # Plugger ISO80
    'medesy-849': '5430-ISO20.jpg',     # Spreader ISO20
    'medesy-850': '5430-ISO30.jpg',     # Spreader ISO30
    'medesy-851': '5430-ISO40.jpg',     # Spreader ISO40
    'medesy-1016': '8400-PEL.jpg',      # Dispensador pellets
    'medesy-1017': '975-N.jpg',         # Eyectores neutros (related to 975)
    'medesy-1018': '975-B.jpg',         # Eyectores azules
    'medesy-1019': '215-4.jpg',         # Pinza porta films
    'medesy-1022': '8400-OIL.jpg',      # Aceite lubricante
    'medesy-1023': '8400-US.jpg',       # Lavadora ultrasónica
    'medesy-1024': '8400-US.jpg',       # Lavadora ultrasónica (variant)
    'medesy-1025': '6163-EX.jpg',       # Maletín expositor
    'medesy-1026': '6163-TR.jpg',       # Trolley expositor
    'medesy-1047': '2500-KIT.jpg',      # Kit pinzas americana
}

# Extract all medesy-crop entries
hits = re.findall(
    r"(id:'(medesy-\d+)'[^}]*?)img:'imagenes/medesy-crop/([^']+)'",
    content, re.DOTALL
)

for full_match, pid, fname in hits:
    # Remove .jpg/.png extension
    base_name = re.sub(r'\.(jpg|png|webp)$', '', fname, flags=re.I)
    ext = re.search(r'\.(jpg|png|webp)$', fname, re.I)
    ext = ext.group(0) if ext else '.jpg'

    if pid in MANUAL:
        mfname = MANUAL[pid]
        url = BASE + mfname
    elif re.match(r'^\d+$', base_name):
        # Pure numeric: e.g. 884 → Immagine_variante_prodotto_884.jpg
        url = BASE + base_name + ext
    elif re.match(r'^\d+-\d', base_name):
        # Numeric with variant: e.g. 895-1 → 895slash1.jpg
        # Split at FIRST hyphen only
        parts = base_name.split('-', 1)
        url = BASE + parts[0] + 'slash' + parts[1] + ext
    elif re.match(r'^\d+', base_name):
        # Numeric with alpha suffix: e.g. 877-HK4 → 877slashHK4.jpg
        parts = base_name.split('-', 1)
        url = BASE + parts[0] + 'slash' + parts[1] + ext
    else:
        # Fully descriptive name — skip, log for manual handling
        skipped_manual.append((pid, fname))
        print(f"  MANUAL: {pid} ({fname})")
        continue

    pattern = f"(id:'{pid}'[^}}]*?)img:'[^']+'"
    new_content = re.sub(pattern,
                         lambda m, u=url: m.group(1) + f"img:'{u}'",
                         content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        changes += 1
        print(f"  Updated: {pid} → {url.split('/')[-1]}")
    else:
        print(f"  SKIPPED: {pid}")

print(f"\nTotal: {changes} changes")
if skipped_manual:
    print(f"Requieren URL manual: {len(skipped_manual)}")
    for pid, fname in skipped_manual:
        print(f"  {pid}: {fname}")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("GUARDADO")
