import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

SUR = 'https://surgimac.com/cdn/shop/files/'
JMU = 'https://www.jmudental.com/cdn/shop/'
AZD = 'https://azdentall.com/cdn/shop/'
OPM = 'https://orthopremium.com.mx/wp-content/uploads/'
PDM = 'https://images.squarespace-cdn.com/content/v1/5de863544ebd8e63f0f2684b/'

photos = {
    'AI007':  SUR + 'mydent-defend-barrier-film-bf-1500_800x.jpg?v=1747842880',
    'AI008':  SUR + 'cargus-international-mark3-angle-with-cup-247-100_800x.jpg?v=1762190923',
    'AI010':  JMU + 'files/03_d04fd404-346b-4675-96dd-84e08ad67f4a_700x700.jpg?v=1749179107',
    'AI012':  JMU + 'files/03_7bdc5a9e-9400-4a8e-a5ed-5ec1ecb44c0c_700x700.jpg?v=1718126956',
    'AI014':  SUR + 'nqC45_RE_800x.jpg?v=1740490183',
    'AI015':  JMU + 'products/37003002-1_700x700.jpg?v=1718126186',
    'AI016':  SUR + 'VP-8108_8111-C_BMixingTips_fb5b0ec2-fed9-439a-96b2-51f9204c0c80.jpg',
    'AI017':  SUR + 'mt-core_6b2b724c-0a05-4f75-8005-8f35f160991b.jpg?v=1744458703',
    'AI018':  SUR + 'mt-core_6b2b724c-0a05-4f75-8005-8f35f160991b.jpg?v=1744458703',
    'AI019':  SUR + 'S439IOT_media_01_800x.jpg?v=1740489896',
    'AI020':  SUR + 'S439IOT_media_01_800x.jpg?v=1740489896',
    'AI022':  JMU + 'products/10107006-3_700x700.jpg?v=1718126206',
    'AI023':  JMU + 'files/1_4be305a4-f714-4aed-8503-6ae50c602554_700x700.jpg?v=1718127042',
    'AI024NE': JMU + 'files/20631069_compressed_700x700.jpg?v=1767151561',
    'AI025':  AZD + 'files/12_948de3b4-68d7-4b5a-a463-f9ca3d419fb7.jpg?v=1749203382&width=1946',
    'AI026':  AZD + 'files/12_948de3b4-68d7-4b5a-a463-f9ca3d419fb7.jpg?v=1749203382&width=1946',
    'AI027':  AZD + 'files/12_948de3b4-68d7-4b5a-a463-f9ca3d419fb7.jpg?v=1749203382&width=1946',
    'AI028':  AZD + 'files/12_948de3b4-68d7-4b5a-a463-f9ca3d419fb7.jpg?v=1749203382&width=1946',
    'AI029':  SUR + '5001014_1_febc2ace-bae0-4bc9-a476-210064f05fcb_800x.jpg?v=1734065563',
    'AI030':  AZD + 'files/1_4811f254-4c97-47c8-93d3-fb6717024491.jpg?v=1702884278&width=1946',
    'AI031':  SUR + 'getImage_8fb719a3-d4ea-4141-ac42-3c5f986aa8e4.jpg?v=1689411903&width=645',
    'AI032':  AZD + 'products/2_06e915e3-c7c8-4c5f-8b42-24833c8d29f9.jpg?v=1673313173&width=1946',
    'AI035':  SUR + '0006148_disposable-bite-blocks-100pk-mark3_5.jpg?v=1683523843',
    'AI040':  JMU + 'products/32303001-2_700x700.jpg?v=1718125956',
    'AI041AZ': JMU + 'files/12_7692a094-26fb-4202-a456-366721b3dc32_700x700.jpg?v=1718126078',
    'AI042AM': AZD + 'files/1_6788ca6b-e9df-4e06-9736-69a52b17008d.jpg?v=1764149436&width=1946',
    'AI043':  AZD + 'files/11_5353337c-5a5d-4b2e-b85c-6e4794445711.jpg?v=1741662673&width=1946',
    'AI045':  AZD + 'files/2_947b9978-4fad-48bc-8b13-c0ec3bf42b61.jpg?v=1724901234&width=1946',
    'AI046AM': AZD + 'files/2_947b9978-4fad-48bc-8b13-c0ec3bf42b61.jpg?v=1724901234&width=1946',
    'AI047':  AZD + 'products/S02_cffa3024-c5b5-47d0-8939-697f2b3cdecd.jpg?v=1678340169&width=1946',
    'AI048':  JMU + 'files/01_7a0f2f1c-92bd-4bf3-bf1d-623a7dd3e319_700x700.jpg?v=1718127579',
    'bkt-mbt018-metal': OPM + 'MBT-.018-1.webp',
    'bkt-roth018-metal': OPM + 'ROTH-.018-2.webp',
    'bkt-roth022-metal': OPM + 'eclipse-rot22-combo-img.webp',
    'bkt-evo-mbt022':    OPM + 'EVOLUTION-MBT-.022.webp',
    'inst-tijeras':      SUR + 'SurgiMacNeedleHolder5.5_800x.jpg?v=1751055698',
    'inst-exploradores': JMU + 'products/10107006-3_700x700.jpg?v=1718126206',
    'pd-composite': PDM + '1577158009924-66L2DRATNPRHII21DMQN/Micro_Hybrid-Syringe-2.jpg',
    'pd-adhesivo':  PDM + '1577404168865-K6RYTNFCTO1VJTHJD3W7/LIGHT-CURE-DENTIN-ENAMEL-BONDING-ADHESIVE-2.jpg',
    'pd-cemento':   AZD + 'files/0_49a226e8-89b6-4438-b0b0-d3859530cfd3.jpg?v=1765957142&width=1946',
    'ae-scalers':   'https://www.safcodental.com/media/catalog/product/e/j/ejcay.jpg',
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
