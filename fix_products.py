import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open(r'C:\Catalago Prodent\website\js\products-data.js', encoding='utf-8') as f:
    content = f.read()

# 1. Remove ae-scalers placeholder
content = re.sub(r"\s*\{id:'ae-scalers'[^{}]+\},?", '', content, flags=re.DOTALL)
print("ae-scalers removed")

# 2. Remove hf-instruments placeholder
content = re.sub(r"\s*\{id:'hf-instruments'[^{}]+\},?", '', content, flags=re.DOTALL)
print("hf-instruments removed")

# 3. Move primadent -> orthopremium, cat -> primadent
count = content.count("brand:'primadent'")
content = content.replace("brand:'primadent'", "brand:'orthopremium'")
# Fix their cat field - primadent products had cat:'materiales'
# We need to set them to cat:'primadent'
# They will appear around the area where brand was changed
# Use a targeted approach: find pd- id entries and update their cat
for pid in ['pd-composite', 'pd-adhesivo', 'pd-cemento']:
    pattern = r"(id:'" + pid + r"'[^{}]*?)cat:'[^']+'"
    content = re.sub(pattern, r"\1cat:'primadent'", content, flags=re.DOTALL)
print(f"primadent moved to orthopremium: {count} products")

# 4. Remove elasticos-ao placeholder
content = re.sub(r"\s*\{id:'elasticos-ao'[^{}]+\},?", '', content, flags=re.DOTALL)
print("elasticos-ao removed")

# 5. Add elasticos CAT_LABELS entry if missing
if "elasticos:" not in content:
    content = content.replace(
        "  fresas:       'Fresas',",
        "  fresas:       'Fresas',\n  elasticos:    'Elásticos',"
    )
if "primadent:" not in content:
    content = content.replace(
        "  fresas:       'Fresas',",
        "  fresas:       'Fresas',\n  primadent:    'Prime Dent',"
    )
print("CAT_LABELS checked")

# 6. Add real elasticos products
elasticos_block = """
  // -- Elasticos American Orthodontics Wildlife Series --
  {id:'el-101', code:'000-101', cat:'elasticos', brand:'elasticos', name:'Wallaby 1/8" (3mm) Ligero',    unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 1/8" 70gms.', specs:['Diametro: 1/8" (3mm)','Fuerza: Ligera 2.5oz / 70gms','100 pzas por bolsa']},
  {id:'el-110', code:'000-110', cat:'elasticos', brand:'elasticos', name:'Wolf 1/8" (3mm) Medio',        unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 1/8" 125gms.', specs:['Diametro: 1/8" (3mm)','Fuerza: Media 4.5oz / 125gms','100 pzas por bolsa']},
  {id:'el-120', code:'000-120', cat:'elasticos', brand:'elasticos', name:'Elephant 1/8" (3mm) Pesado',   unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 1/8" 180gms.', specs:['Diametro: 1/8" (3mm)','Fuerza: Pesada 6.5oz / 180gms','100 pzas por bolsa']},
  {id:'el-102', code:'000-102', cat:'elasticos', brand:'elasticos', name:'Dragon 3/16" (5mm) Ligero',    unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 3/16" 70gms.', specs:['Diametro: 3/16" (5mm)','Fuerza: Ligera 2.5oz / 70gms','100 pzas por bolsa']},
  {id:'el-111', code:'000-111', cat:'elasticos', brand:'elasticos', name:'Gorilla 3/16" (5mm) Medio',    unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 3/16" 125gms.', specs:['Diametro: 3/16" (5mm)','Fuerza: Media 4.5oz / 125gms','100 pzas por bolsa']},
  {id:'el-121', code:'000-121', cat:'elasticos', brand:'elasticos', name:'Tortoise 3/16" (5mm) Pesado',  unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 3/16" 180gms.', specs:['Diametro: 3/16" (5mm)','Fuerza: Pesada 6.5oz / 180gms','100 pzas por bolsa']},
  {id:'el-131', code:'000-131', cat:'elasticos', brand:'elasticos', name:'Cheetah 3/16" (5mm) Extra Pesado', unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 3/16" 225gms.', specs:['Diametro: 3/16" (5mm)','Fuerza: Extra Pesada 8oz / 225gms','100 pzas por bolsa']},
  {id:'el-103', code:'000-103', cat:'elasticos', brand:'elasticos', name:'Falcon 1/4" (6mm) Ligero',     unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 1/4" 70gms.', specs:['Diametro: 1/4" (6mm)','Fuerza: Ligera 2.5oz / 70gms','100 pzas por bolsa']},
  {id:'el-112', code:'000-112', cat:'elasticos', brand:'elasticos', name:'Eagle 1/4" (6mm) Medio',       unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 1/4" 125gms.', specs:['Diametro: 1/4" (6mm)','Fuerza: Media 4.5oz / 125gms','100 pzas por bolsa']},
  {id:'el-122', code:'000-122', cat:'elasticos', brand:'elasticos', name:'Sea Lion 1/4" (6mm) Pesado',   unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 1/4" 180gms.', specs:['Diametro: 1/4" (6mm)','Fuerza: Pesada 6.5oz / 180gms','100 pzas por bolsa']},
  {id:'el-132', code:'000-132', cat:'elasticos', brand:'elasticos', name:'Jaguar 1/4" (6mm) Extra Pesado', unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 1/4" 225gms.', specs:['Diametro: 1/4" (6mm)','Fuerza: Extra Pesada 8oz / 225gms','100 pzas por bolsa']},
  {id:'el-104', code:'000-104', cat:'elasticos', brand:'elasticos', name:'Ferret 5/16" (8mm) Ligero',    unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 5/16" 70gms.', specs:['Diametro: 5/16" (8mm)','Fuerza: Ligera 2.5oz / 70gms','100 pzas por bolsa']},
  {id:'el-113', code:'000-113', cat:'elasticos', brand:'elasticos', name:'Panda 5/16" (8mm) Medio',      unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 5/16" 125gms.', specs:['Diametro: 5/16" (8mm)','Fuerza: Media 4.5oz / 125gms','100 pzas por bolsa']},
  {id:'el-123', code:'000-123', cat:'elasticos', brand:'elasticos', name:'Manatee 5/16" (8mm) Pesado',   unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 5/16" 180gms.', specs:['Diametro: 5/16" (8mm)','Fuerza: Pesada 6.5oz / 180gms','100 pzas por bolsa']},
  {id:'el-133', code:'000-133', cat:'elasticos', brand:'elasticos', name:'Leopard 5/16" (8mm) Extra Pesado', unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 5/16" 225gms.', specs:['Diametro: 5/16" (8mm)','Fuerza: Extra Pesada 8oz / 225gms','100 pzas por bolsa']},
  {id:'el-143', code:'000-143', cat:'elasticos', brand:'elasticos', name:'Blue Whale 5/16" (8mm) Maximo', unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 5/16" 400gms.', specs:['Diametro: 5/16" (8mm)','Fuerza: Maxima 14oz / 400gms','100 pzas por bolsa']},
  {id:'el-105', code:'000-105', cat:'elasticos', brand:'elasticos', name:'Hyena 3/8" (10mm) Ligero',     unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 3/8" 70gms.', specs:['Diametro: 3/8" (10mm)','Fuerza: Ligera 2.5oz / 70gms','100 pzas por bolsa']},
  {id:'el-114', code:'000-114', cat:'elasticos', brand:'elasticos', name:'Tiger 3/8" (10mm) Medio',      unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 3/8" 125gms.', specs:['Diametro: 3/8" (10mm)','Fuerza: Media 4.5oz / 125gms','100 pzas por bolsa']},
  {id:'el-124', code:'000-124', cat:'elasticos', brand:'elasticos', name:'Rhinoceros 3/8" (10mm) Pesado', unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 3/8" 180gms.', specs:['Diametro: 3/8" (10mm)','Fuerza: Pesada 6.5oz / 180gms','100 pzas por bolsa']},
  {id:'el-134', code:'000-134', cat:'elasticos', brand:'elasticos', name:'Puma 3/8" (10mm) Extra Pesado', unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 3/8" 225gms.', specs:['Diametro: 3/8" (10mm)','Fuerza: Extra Pesada 8oz / 225gms','100 pzas por bolsa']},
  {id:'el-145', code:'000-145', cat:'elasticos', brand:'elasticos', name:'Gray Whale 1/2" (13mm) Maximo', unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 1/2" 400gms.', specs:['Diametro: 1/2" (13mm)','Fuerza: Maxima 14oz / 400gms','100 pzas por bolsa']},
  {id:'el-106', code:'000-106', cat:'elasticos', brand:'elasticos', name:'Egret 5/8" (16mm) Ligero',     unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 5/8" 70gms.', specs:['Diametro: 5/8" (16mm)','Fuerza: Ligera 2.5oz / 70gms','100 pzas por bolsa']},
  {id:'el-107', code:'000-107', cat:'elasticos', brand:'elasticos', name:'Hawk 3/4" (19mm) Medio',       unit:'bolsa 100 pzas', img:'imagenes/elasticos/elasticos-ao.jpg', desc:'Elastico intermaxilar latez 3/4" 125gms.', specs:['Diametro: 3/4" (19mm)','Fuerza: Media 4.5oz / 125gms','100 pzas por bolsa']},
"""

# Insert before closing ]
idx = content.rfind('];')
content = content[:idx].rstrip() + '\n' + elasticos_block.rstrip(',') + '\n];\n'
print(f"Elasticos block added: 23 products")

# Count total
total = len(re.findall(r"id:'[a-zA-Z0-9_-]+'", content))
print(f"Total products: {total}")

with open(r'C:\Catalago Prodent\website\js\products-data.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("SAVED")
