import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    # AI007: Dispensador de Barrera — upgrade 100x → 800x (mismo CDN surgimac)
    'AI007': 'https://surgimac.com/cdn/shop/files/1855_Barrier_Dispenser_800x.jpg?v=1689582056',

    # AI001R: Micro Aplicador Regular — reemplaza depositodentxpress 600x con azdentall 1946px
    'AI001R': 'https://azdentall.com/cdn/shop/files/02_2b476c06-f273-437d-9e23-31e2646748f1.jpg?v=1701229212&width=1946',

    # AI004: Barrera Protectora Azul — reemplaza nnamedical con jmudental 700x700
    'AI004': 'https://www.jmudental.com/cdn/shop/files/4_1_700x700.jpg?v=1759140020',

    # AI009: Copa Profiláctica — reemplaza atomodental con azdentall 1946px
    'AI009': 'https://azdentall.com/cdn/shop/files/01_34901815-421f-4ad6-9d5f-6bab3812bde4.jpg?v=1757058121&width=1946',

    # AI013: Puntas Mezcladoras Amarillas — reemplaza atomodental con surgimac 800x
    'AI013': 'https://surgimac.com/cdn/shop/files/dynamic_mixing_tip_dyn.._800x.jpg?v=1744458801',

    # AI038: Puntas para Jeringa Triple — reemplaza medidenta 500x con surgimac 800x
    'AI038': 'https://surgimac.com/cdn/shop/products/0009091_multicolored-disposable-plastic-air-water-syringe-tips-1500pk-mark3_800x.jpg?v=1703525656',

    # OPEST: Eyector de Saliva — upgrade jmudental 512x512 con azdentall 1946px
    'OPEST': 'https://azdentall.com/cdn/shop/files/07_7e3bda7a-7eba-4a8d-a72b-ffe274a210e8.jpg?v=1761290824&width=1946',

    # bor-022: Brackets Mirage MBT .022 — reemplaza universum QR con tienda.borgatta 1024x
    'bor-022': 'https://tienda.borgatta.com.mx/cdn/shop/files/300-582_1024x.jpg?v=1772728769',

    # bor-023: Brackets Cerámico Roth .022 — reemplaza depositodentxpress con tienda.borgatta 1024x
    'bor-023': 'https://tienda.borgatta.com.mx/cdn/shop/files/Zafiro_20Roth_2032400px72DPIS_1024x.jpg?v=1772725637',

    # bor-024: Brackets Mirage Mini Roth .018 — reemplaza universum QR con tienda.borgatta 1024x
    'bor-024': 'https://tienda.borgatta.com.mx/cdn/shop/files/Mirage_20Roth_2062400px72DPIS_1024x.jpg?v=1772728474',

    # vamasa-057: VALO Cordless — reemplaza garimadental 500x con clinicalresearchdental
    'vamasa-057': 'https://www.clinicalresearchdental.com/cdn/shop/products/Valo_Grand_535x.png?v=1580924276',

    # vamasa-065: File-Eze — reemplaza garimadental con clinicalresearchdental
    'vamasa-065': 'https://www.clinicalresearchdental.com/cdn/shop/products/1075_File-Eze-Kit-open_ENDODONTICS_535x.jpg?v=1619197923',

    # vamasa-066: Consepsis V — reemplaza garimadental con clinicalresearchdental
    'vamasa-066': 'https://www.clinicalresearchdental.com/cdn/shop/files/consepsis-indispense-kit-box-open-30ml_535x.jpg?v=1759756624',

    # vamasa-072: Puntas NanoTip — reemplaza garimadental con clinicalresearchdental
    'vamasa-072': 'https://www.clinicalresearchdental.com/cdn/shop/products/Ultradent_NaviTip-Tips-group_535x.jpg?v=1629473809',

    # vamasa-076: Puntas NaviTip — reemplaza garimadental con clinicalresearchdental
    'vamasa-076': 'https://www.clinicalresearchdental.com/cdn/shop/products/Ultradent_NaviTip-Tips-group_535x.jpg?v=1629473809',
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
