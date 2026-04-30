import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    # Micro aplicadores
    'AI001SF': 'https://surgimac.com/cdn/shop/files/MB1000-1103_3c6a20ae-551b-4db4-b86a-91de74112cdc.jpg',
    'AI001F':  'https://www.jmudental.com/cdn/shop/files/05_compressed_700x700.jpg',
    'AI001R':  'https://depositodentxpress.com/wp-content/uploads/2021/08/microbrush-microaplicadores-dentales-600x600.png',
    'AI002':   'https://azdentall.com/cdn/shop/files/02_2b476c06-f273-437d-9e23-31e2646748f1.jpg?v=1701229212',
    # Cucharilla impresión
    'AI003':   'https://universum-dental.com.mx/cdn/shop/products/image_10780b5f-1fc1-413a-a903-acdeb3b69032_1024x.png?v=1632670808',
    # Barrera protectora
    'AI004':   'https://nnamedical.com/wp-content/uploads/2026/03/rtfff-en.jpg',
    # Profilaxis
    'AI009':   'https://www.atomodental.com/cdn/shop/products/ATOMO_premium_quality_prophy_cup_-new_large.JPG?v=1528694232',
    # Pistola dosificadora 1:1
    'AI011':   'https://ansondental.com/cdn/shop/products/dispensing_gun_1024x1024.jpg?v=1543434574',
    # Puntas mezcladoras
    'AI013':   'https://www.atomodental.com/cdn/shop/files/mixing_tip_AA0853_large.jpg?v=1753583894',
    # Clip babero
    'AI021':   'https://surgimac.com/cdn/shop/files/bcwh.jpg?v=1744458892',
    # Caja babero
    'AI024':   'https://surgimac.com/cdn/shop/files/i19261__12587.1569010283.jpg?v=1752575390',
    # Retractor
    'AI033':   'https://www.premierdentalco.com/wp-content/uploads/2015/11/ComfortView_9061381_universal.jpg',
    # Puntas jeringa triple
    'AI038':   'https://medidenta.com/wp-content/uploads/2021/07/MD-Website-Thumbnails-Magic-Tips_01-500x500.jpg',
    # Jeringa triple metálica
    'AI039':   'https://azdentall.com/cdn/shop/files/11_4696b734-3581-4862-8757-c8b3e871e0da.jpg?v=1692935086',
    # Contraángulo desechable copa
    'AI044':   'https://ansondental.com/cdn/shop/products/maxpro2_soft_cup_0913897f-81e4-4a54-901e-105afc5bd891_1024x1024.jpg?v=1667001007',
    # Cánula aspiración
    'AI049':   'https://www.jmudental.com/cdn/shop/files/71G_512x512.jpg',
    # Eyector saliva
    'OPEST':   'https://www.jmudental.com/cdn/shop/files/61a_512x512.jpg',
    # Fresas diamante
    'fresa-BR-M': 'https://eagle-dental-burs.com/cdn/shop/files/Round_End_Tapered_Diamond_Burs_35b3996a-e301-46a4-8113-e026800146aa.png?v=1715073621',
    'fresa-BC':   'https://www.mrbur.com/cdn/shop/files/Round-Diamond-Bur-10-pcs.png?v=1744007018',
    # Brackets OrthoP
    'bkt-mbt022-metal': 'https://orthopremium.com.mx/wp-content/uploads/MBT-.018-1-300x300.webp',
    'bkt-roth022-cer':  'https://orthopremium.com.mx/wp-content/uploads/MALLA-RANURADO-ROTH-.022-300x300.webp',
    'bkt-evo-roth022':  'https://orthopremium.com.mx/wp-content/uploads/EVOLUTION-ROTH-.022-300x300.webp',
    # Pinzas ortodoncia
    'inst-pinzas-orto': 'https://orthopremium.com.mx/wp-content/uploads/N21150452-A-300x300.jpg',
    # Prime-Dent bonding resin (official primedentalmfg.com)
    'pdm-bonding-resin': 'https://images.squarespace-cdn.com/content/v1/5de863544ebd8e63f0f2684b/1577404168865-K6RYTNFCTO1VJTHJD3W7/LIGHT-CURE-DENTIN-ENAMEL-BONDING-ADHESIVE-2.jpg',
}

for pid, url in photos.items():
    pattern = f"(id:'{pid}'[^}}]*?)img:'[^']+'"
    new_content = re.sub(pattern,
                         lambda m, u=url: m.group(1) + f"img:'{u}'",
                         content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        changes += 1
        print(f"  Photo updated: {pid}")
    else:
        print(f"  SKIPPED: {pid}")

print(f"\nTotal cambios: {changes}")
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("GUARDADO")
