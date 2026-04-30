import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    # bor-093: pieza de mano Borgatta Stella Lux LED — estaba mostrando imagen de acetatos (¡muy incorrecto!)
    'bor-093': 'https://catalogo.borgatta.com.mx/cdn/shop/files/0-000-708-12400px_5a5a42ee-ed18-4231-94c4-a28a55dfe751_1024x.jpg?v=1764663538',

    # bkt-mbt022-metal: brackets MBT .022 — estaba usando la misma imagen que MBT .018
    'bkt-mbt022-metal': 'https://orthopremium.com.mx/wp-content/uploads/MBT-.022-1.webp',

    # AI022: espejo reflector forma muela — estaba usando misma imagen que inst-exploradores
    'AI022': 'https://azdentall.com/cdn/shop/products/06_617a0cd9-1731-4a2b-b39f-1d9207872331.jpg?v=1677742779&width=1946',

    # AI025-AI028: 4 cajas de aluminio distintas usaban la MISMA imagen — se diferencian ahora
    'AI025': 'https://d14ls4z5rsiju6.cloudfront.net/dentaliberica-es/products/caja-desinfeccion-conos-limas-y-fresas-72-hoyos-1-f173a.jpg',
    'AI026': 'https://dukaan.b-cdn.net/700x700/webp/upload_file_service/b86ebdb3-4366-4bf8-bfcf-704b0888c45e/bdfdd4-3afcee7dadd241caaa4aa533396bf908-mv2.webp',
    'AI027': 'https://azdentall.com/cdn/shop/products/1_3766d036-52e7-495d-b48b-7bccb74c1eff.jpg',
    'AI028': 'https://azdentall.com/cdn/shop/products/5_6ca59aef-f40f-4dad-a8a1-49ab5d2cbf36.jpg',
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
