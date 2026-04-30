import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    # AI012: Pistola 10:1 — imagen anterior era incorrecta
    'AI012': 'https://surgimac.com/cdn/shop/files/applicator-gun-110411_800x.jpg?v=1694420527',

    # AI031: Fresero de Plástico 60 espacios — imagen UUID incorrecta
    'AI031': 'https://www.dentaltix.com/en/sites/default/files/styles/large/public/fresero-dental-60-unidades-abierto.jpg?itok=oTPLWHeB',

    # AI032: Sujetador RX — imagen UUID incorrecta, ahora posicionador completo FPS3000
    'AI032': 'https://azdentall.com/cdn/shop/products/a2_e4bb3bb4-1c11-410b-b681-4b8511df1aa5.jpg?v=1678524789',

    # AI041AZ: Charola esterilizar GDE — imagen UUID incorrecta, ahora cassette JMU correcto
    'AI041AZ': 'https://www.jmudental.com/cdn/shop/files/1_8ef069d7-1bcd-4217-9f37-443899a9cfcf_700x700.jpg?v=1758273402',
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
