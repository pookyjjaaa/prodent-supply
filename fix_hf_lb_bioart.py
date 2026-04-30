import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

PRAC = 'https://cdn11.bigcommerce.com/s-54anm7w0kg/images/stencil/500x1800/products/'
BOR  = 'https://tienda.borgatta.com.mx/cdn/shop/files/'

photos = {
    # Hu-Friedy Gracey Standard (Practicon CDN)
    'hf-sg11-12':  PRAC + '9047/29195/7147515__29697.1751295155.jpg?c=1',
    'hf-sg13-14':  PRAC + '9208/29191/7147516__58871.1751295340.jpg?c=1',
    'hf-sg7-8':    PRAC + '8878/29198/7147513__53478.1751294964.jpg?c=1',
    'hf-sg15-16':  PRAC + '9334/29186/7147517__29965.1751295460.jpg?c=1',
    'hf-sg17-18':  PRAC + '9448/29185/7147518__01790.1751295596.jpg?c=1',
    # Hu-Friedy After Five (hufriedygroup.com)
    'hf-srpg11-12': 'https://www.hufriedygroup.com/sites/default/files/HuFriedyGroup-SG11_12XE2-Gracey-curette-harmony-full-2009.jpg',
    'hf-srpg13-14': 'https://www.hufriedygroup.com/sites/default/files/HuFriedyGroup-SG13_14XE2-Gracey-curette-harmony-full-2009.jpg',
    # Hu-Friedy Columbia (Practicon CDN)
    'hf-sc13-14':  PRAC + '9112/29214/7147523S__98637.1751295182.jpg?c=1',

    # Line Black / Borgatta
    'lb-arco-neo':    BOR + '02-523-15_20E_1024x.jpg?v=1772726149',
    'lb-xpression':   BOR + '90-069-01_20C2400_72DPIS_1024x.jpg?v=1772726868',
    'lb-xpression-c': BOR + 'X-PRESSION_20C_2042400px72DPIS_1024x.jpg?v=1772726320',
    'lb-elasticos':   BOR + 'Intraorales_20Borgatta_2052400px72DPIS_1024x.jpg?v=1772726239',
    'lb-b-action':    BOR + '90-063-00_20C_1024x.jpg?v=1772728515',
    'lb-black-duo':   BOR + '90-047-01_205F2400_72DPIS_1024x.jpg?v=1772726086',
    'lb-resorte':     BOR + 'GLINT_20TUBOS_204_1024x.jpg?v=1772727426',

    # Bioart articuladores principales
    'articulador-001': 'https://ddmolar.com/cdn/shop/products/articulador_4000s.jpg?v=1466118304&width=1946',
    'articulador-002': 'https://ddmolar.com/cdn/shop/products/articulador_a7_b9a56edc-7a71-4bc1-9607-cf51d28355a9.jpg?v=1503498752&width=1946',
    'articulador-003': 'https://azdentall.com/cdn/shop/files/2_ded3fdc3-860c-47e2-bbed-193c48803422.jpg?v=1744771510&width=1946',
    'articulador-004': 'https://bioart.com.br/produtos/produto_21/descricao_21/original/arco_facial_port.jpg',

    # Autoclave Gnatus
    'gnatus-auto': 'https://cdn.awsli.com.br/600x1000/2644/2644992/produto/231272381/pre-os-2026-04-09t100453-977-lxtpeok7tg.png',

    # Sensor RVG
    'primervg-sensor': 'https://universadent.com/wp-content/uploads/2020/03/rvg-62003-600x600.jpg',
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
