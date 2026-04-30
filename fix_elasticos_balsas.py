import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

AO = 'https://americanortho.com/assets/Uploads/Products/Elastomerics/'
WL01 = AO + 'WL-01-624x624__FocusFillWyIwLjAwIiwiMC4wMCIsNjY0LDY2NF0.png'
WL03 = AO + 'WL-03-624x624__FocusFillWyIwLjAwIiwiMC4wMCIsNjY0LDY2NF0.png'
DTX = 'https://www.dentaltix.com/en/sites/default/files/styles/large/public/'

photos = {
    # Elásticos AO Wildlife — imagen genérica
    'elasticos-ao': WL01,
    # 1/8" group
    'el-101': WL03,  # Wallaby
    'el-110': WL03,  # Wolf
    'el-120': WL03,  # Elephant
    # 3/16" group
    'el-102': WL01,  # Dragon
    'el-111': WL01,  # Gorilla
    'el-121': WL01,  # Tortoise
    'el-131': WL01,  # Cheetah
    # 1/4" group
    'el-103': WL01,  # Falcon
    'el-112': WL01,  # Eagle
    'el-122': WL01,  # Sea Lion
    'el-132': WL01,  # Jaguar
    # 5/16" group
    'el-104': WL01,  # Ferret
    'el-113': WL01,  # Panda
    'el-123': WL01,  # Manatee
    'el-133': WL01,  # Leopard
    'el-143': WL01,  # Blue Whale
    # 3/8" group
    'el-105': WL01,  # Hyena
    'el-114': WL01,  # Tiger
    'el-124': WL01,  # Rhinoceros
    'el-134': WL01,  # Puma
    # 1/2"+ group
    'el-145': WL03,  # Gray Whale
    'el-106': WL03,  # Egret
    'el-107': WL03,  # Hawk

    # Zhermack balsas 001-017
    'balsas-001': DTX + 'hydrogum-alginato-menta.jpg?itok=VsYWeLF_',
    'balsas-002': 'https://cdn11.bigcommerce.com/s-emp9gstccl/images/stencil/1280x1280/products/7219/6214/ZHM-H005%5F%5F21631.1612397786.jpg?c=2',
    'balsas-003': 'https://odontodo.mx/wp-content/uploads/2021/11/Zhermack-Hydrocolor-5-Alginato-453gr-600x600.png',
    'balsas-004': DTX + 'alginato-orthoprint-zhermack_0.jpg?itok=rwFjIuFB',
    'balsas-005': DTX + 'zh_tropalgin_enl_0_0.jpg',
    'balsas-006': DTX + 'th3_hydrorise-putty_0_1.jpg?itok=rlm-p5RI',
    'balsas-007': DTX + 'th3_hydrorise-putty_0_1.jpg?itok=rlm-p5RI',
    'balsas-008': DTX + 'hydrorise-extralight-fast_0_0.jpg?itok=U68Brfc6',
    'balsas-009': DTX + 'zh06185-h_0.jpg?itok=zqPIkWQ7',
    'balsas-010': DTX + 'occlufast-rock-silicona-de-impresion.jpg?itok=I6tmgCXN',
    'balsas-011': DTX + 'occlufast-cad_0.jpg?itok=6Cg3af9Z',
    'balsas-012': DTX + 'zetaplus_0.jpg?itok=4jvMR7-t',
    'balsas-013': DTX + '49b5703f394f1295d231373c98a8e878_0.jpg?itok=cMg6UkL2',
    'balsas-014': DTX + 'silicona-zetalabor_0_0.jpg?itok=C_VnNUOf',
    'balsas-015': DTX + 'zh88525_0.jpg?itok=SLbK3jWW',
    'balsas-016': 'https://www.prestigedentalproducts.com/images/P/Elite%20Mix%20%28Zhermack%29.jpg',
    'balsas-017': DTX + 'microbrushx-aplicadores-negros-100-uds.jpg?itok=KJK2zRU3',
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
