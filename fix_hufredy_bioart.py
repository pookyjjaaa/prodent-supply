import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    # Hu-Friedy instrumentos (reemplaza imágenes de 52-102px)
    'hf-sg1-2':   'https://www.hufriedygroup.com/sites/default/files/HuFriedyGroup-SG1_2XE2-Gracey-curette-harmony-full-2009.jpg',
    'hf-sh6-7':   'https://cdn11.bigcommerce.com/s-54anm7w0kg/images/stencil/1280x1280/products/9049/29221/7147535%5F%5F91056.1751295157.jpg?c=1',
    'hf-s204s':   'https://cdn11.bigcommerce.com/s-54anm7w0kg/images/stencil/1280x1280/products/9134/29232/7147540%5F%5F94433.1751295232.jpg?c=1',
    'hf-pw6':     'https://dentalcity.com/CatalogImages/DENLN/18-5603-Product_Primary_Image-400X400.jpg',
    'hf-pqw6':    'https://www.skydentalsupply.com/picts/products/tnw800-pqw6_bw.webp',
    'hf-exs23-6': 'https://www.hufriedygroup.com/sites/default/files/EXS23___30_Round_handle_SE_full_rgb_5.jpg',
    'hf-exd5-6':  'https://cdn11.bigcommerce.com/s-54anm7w0kg/images/stencil/1280x1280/products/9392/29174/7147560%5F%5F40852.1751295526.jpg?c=1',

    # Bioart articulador accesorios (reemplaza imágenes de 168-200px)
    'articulador-005': 'https://bioart.com.br/produtos/produto_24/descricao_24/original/suporte_port.jpg',
    'articulador-006': 'https://bioart.com.br/produtos/produto_25/descricao_25/original/camper_port_esp.jpg',
    'articulador-007': 'https://bioart.com.br/produtos/produto_30/descricao_30/original/magnetic_port.jpg',
    'articulador-008': 'https://www.dentaltix.com/en/sites/default/files/styles/large/public/placa-metalica-montaje-por-tornillo-bio-art.jpg?itok=htPLlkMx',
    'articulador-009': 'https://bioart.com.br/produtos/produto_29/descricao_29/original/trilho_port.jpg',
    'articulador-010': 'https://smilequip.com/cdn/shop/products/Adjustable_Incisal_Guide_plane.jpg?v=1489520156',
    'articulador-011': 'https://bioart.com.br/produtos/produto_27/descricao_27/original/fox_port.jpg',
    'articulador-012': 'https://bioart.com.br/produtos/produto_32/descricao_32/original/bandeirola_port_esp.jpg',
    'articulador-013': 'https://bioart.com.br/produtos/produto_26/descricao_26/original/port.jpg',
    'articulador-014': 'https://images.tcdn.com.br/img/img_prod/585327/90_mesa_incisal_metalica_ajustavel_bio_art_3045_1_20231026174338.jpg',
    'articulador-015': 'https://bioart.com.br/produtos/produto_23/descricao_23/original/estojo_port.jpg',
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
