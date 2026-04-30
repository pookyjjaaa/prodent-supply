import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

TIENDA = 'https://tienda.borgatta.com.mx/cdn/shop/files/'
CATALOGO = 'https://catalogo.borgatta.com.mx/cdn/shop/files/'

photos = {
    'borgatta-001': TIENDA + 'X-PRESSIO_CC_81N-MET_1024x.png?v=1772728794',
    'borgatta-002': TIENDA + 'X-PRESSION-CER_1024x.png?v=1772727663',
    'borgatta-003': TIENDA + '301-646_20F_1024x.jpg?v=1772727047',
    'borgatta-004': TIENDA + 'BOR-88002_20E2400px72DPIS_1024x.jpg?v=1772728568',
    'borgatta-005': TIENDA + '90-045-01_20C2400px72DPIS_1024x.jpg?v=1772728655',
    'borgatta-006': TIENDA + '90-055-01_20C2400px72DPIS_1024x.jpg?v=1772728639',
    'borgatta-007': CATALOGO + 'Balck_20Duo_20C_2022400px72DPIS_77b9e149-74f5-4db9-bf95-89783eb95bc9_1024x.jpg?v=1764664837',
    'borgatta-008': TIENDA + 'Kit_20Memory_202_2400px72DPIS_1024x.jpg?v=1772725828',
    'borgatta-009': TIENDA + 'Nova_20Metalico_1024x.jpg?v=1772728489',
    'borgatta-010': TIENDA + 'Mirage_20Roth_2062400px72DPIS_1024x.jpg?v=1772728474',
    'borgatta-011': CATALOGO + 'iLine_20Estetico_20Roth_2042400px72DPIS_1024x.jpg?v=1700094793',
    'borgatta-012': CATALOGO + 'Zafiro_20Roth_2032400px72DPIS_7058956a-45d1-4921-b8a9-b7dde9fba829_1024x.jpg?v=1764665455',
    'borgatta-013': TIENDA + '80400-1_1024x.png?v=1772727539',
    'borgatta-014': TIENDA + '480-810M_20A2400px72DPIS_1024x.jpg?v=1772727246',
    'borgatta-015': TIENDA + '480-820M-C_1024x.png?v=1772728582',
    'borgatta-016': 'https://www.ivoclar.com/medias/532629AN.jpg',
    'borgatta-017': TIENDA + '500-024_20500-026_20G_20CF_1024x.jpg?v=1772727616',
    'borgatta-018': TIENDA + '300-700M_20A2400px72DPIS_1024x.jpg?v=1772728109',
    'borgatta-019': CATALOGO + '300-600M_1024x.png?v=1770884468',
    'bor-020': TIENDA + '90-047-01_205F2400_72DPIS_1024x.jpg?v=1772726086',
    'bor-021': TIENDA + '90-063-00_20C_1024x.jpg?v=1772728515',
    'bor-022': 'https://universum-dental.com.mx/cdn/shop/products/image_5e4aa2d4-137f-4481-9dbd-e41c09e7a501_1024x.jpg?v=1615942212',
    'bor-023': 'https://depositodentxpress.com/wp-content/uploads/2021/10/brackets-ceramico-roth-022-600x600.png',
    'bor-024': 'https://universum-dental.com.mx/cdn/shop/products/image_8a07754f-ef1d-41ea-a15f-7e6207c18ff8_1024x.jpg?v=1615941717',
    'bor-025': TIENDA + '300-530_1024x.jpg?v=1772727641',
    'bor-026': 'https://dentexpro.mx/cdn/shop/files/GLINT-ROTH-22.webp?v=1767762136',
    'bor-027': TIENDA + '68-172-80_203_42400_72DPIS_1024x.jpg?v=1772726309',
    'bor-028': TIENDA + 'GAC_20TUBOS_201_6edfe3ed-af78-4dad-86f8-0bac45091e6f_1024x.jpg?v=1772727478',
    'bor-029': TIENDA + 'KIT_20301-722_20M_1024x.jpg?v=1772728783',
    'bor-030': TIENDA + 'GLINT_20TUBOS_204_1024x.jpg?v=1772727426',
    'bor-031': CATALOGO + '903-00002-A_20C2400px72DPIS_278cf755-7de5-4e8e-8335-1452b6984d4a_1024x.jpg?v=1770885783',
    'bor-032': CATALOGO + 'ADAPTADOR2400_72DPIS_b1b5ef37-b555-4698-b612-f58b40bdf50d_1024x.jpg?v=1764664660',
    'bor-033': TIENDA + '300-593_20M2400px72DPIS_1024x.jpg?v=1772728372',
    'bor-034': TIENDA + '300-704_20F_1024x.jpg?v=1772726405',
    'bor-035': CATALOGO + '28-300-26_20_20A2400px72DPIS_158fc3dd-85c8-4127-999d-3cac74c6ccb8_1024x.jpg?v=1764665076',
    'bor-037': TIENDA + '28-300-10_20M2400px72DPIS_1024x.jpg?v=1772728745',
    'bor-039': CATALOGO + 'ACETATOS-M_1024x.png?v=1764665123',
    'bor-040': CATALOGO + 'ACETATOS-M_1024x.png?v=1764665123',
    'bor-041': TIENDA + '300-571_20F_1024x.jpg?v=1772726008',
    'bor-042': TIENDA + '17-222-11_20E_1024x.jpg?v=1772725998',
    'bor-043': TIENDA + 'AZUL_1024x.jpg?v=1772726351',
    'bor-044': TIENDA + '03-014-63_20E2400_72DPIS_1024x.jpg?v=1772725610',
    'bor-045': TIENDA + '0-000-620_20E2400px72DPIS_1024x.jpg?v=1772727383',
    'bor-046': TIENDA + '200-102_20C2400px72DPIS_1024x.jpg?v=1772727370',
    'bor-047': TIENDA + '300-509_20M2400px72DPIS_1024x.jpg?v=1772725972',
    'bor-048': CATALOGO + '02-511-14_20E2400px72DPIS_1223494c-b0db-49e4-9214-1cacbbb944f2_1024x.jpg?v=1764664936',
    'bor-049': CATALOGO + '02-523-15_20E_6ba1bbfd-7fae-451d-9e73-1b552516aaac_1024x.jpg?v=1764664012',
    'bor-050': CATALOGO + '02-528-57_20E_73c62ca4-47c5-49b7-a3c6-98c15f8ded83_1024x.jpg?v=1764663997',
    'bor-051': TIENDA + 'ARCOS_20NITRILO_1024x.jpg?v=1772726194',
    'bor-052': TIENDA + 'ARCOS_2022400px72DPIS_1024x.jpg?v=1772727523',
    'bor-053': 'https://dentistdepot.mx/wp-content/uploads/2021/09/RESORTE-DE-ACERO-BORGATTA-ORTODONCIA-BRACKETS-DEPOSITO-DENTAL-ONLINE.png',
    'bor-054': 'https://dentistdepot.mx/wp-content/uploads/2021/09/RESORTE-DE-ACERO-CERRADO-BORGATTA-ORTODONCIA-DENTISTA-ODONTOLOGIA-DEPOSITO-DENTAL-ONLINE.png',
    'bor-055': 'https://universum-dental.com.mx/cdn/shop/products/image_515230dd-c2a5-4ec1-a7ed-f5a4508a3e1a_1024x.jpg?v=1608398513',
    'bor-056': TIENDA + 'conjunto-verde-neon_1024x.png?v=1772725221',
    'bor-057': 'https://universum-dental.com.mx/cdn/shop/products/image_076d6210-72d0-47c0-84de-25e7e2f56c82_1024x.jpg?v=1608398548',
    'bor-058': TIENDA + 'Intraorales_20Borgatta_2052400px72DPIS_1024x.jpg?v=1772726239',
    'bor-059': TIENDA + 'Intraorales_20Borgatta_2052400px72DPIS_1024x.jpg?v=1772726239',
    'bor-060': TIENDA + 'Intraorales_20Borgatta_2052400px72DPIS_1024x.jpg?v=1772726239',
    'bor-061': TIENDA + 'BOR-1016-P_1024x.png?v=1772726682',
    'bor-062': TIENDA + 'BOR-1001-P_1024x.png?v=1772727885',
    'bor-064': CATALOGO + 'BOR-220_20P_1024x.jpg?v=1764665178',
    'bor-065': TIENDA + 'BOR-805H-P_1024x.png?v=1772726652',
    'bor-066': CATALOGO + 'BOR-158BJ-P_1024x.png?v=1764665380',
    'bor-067': TIENDA + 'BOR-142_20P_1024x.jpg?v=1772726666',
    'bor-068': TIENDA + 'ALEXANDER_20ML2400_72DPISk_1024x.jpg?v=1772726366',
    'bor-069': TIENDA + 'BOR-521_20P_1024x.jpg?v=1772725239',
    'bor-070': 'https://files.plytix.com/api/v1.1/file/public_files/pim/assets/f9/00/33/62/623300f9ee52d5d20ae24d8e/images/65/b0/14/65/6514b06576e3b8b78f9241b9/0-000-400.JPG',
    'bor-071': 'https://depositodentalvq.com.mx/wp-content/uploads/2023/03/Separador-500x487.jpg',
    'bor-074': TIENDA + 'HYRAX_2042400px72DPIS_1024x.jpg?v=1772727114',
    'bor-082': TIENDA + 'KIT300-821_20T2400px72DPIS_1024x.jpg?v=1772725567',
    'bor-084': TIENDA + 'Ceras_2012400px72DPIS_1024x.jpg?v=1772725595',
    'bor-085': TIENDA + 'CEPILLOS_22400px72DPIS-2_1024x.jpg?v=1772728161',
    'bor-086': TIENDA + '0-003-003-32400px_1024x.jpg?v=1772727033',
    'bor-088': TIENDA + '0-001-001-22400px_1024x.jpg?v=1772726878',
    'bor-090': TIENDA + 'HYRAX_2042400px72DPIS_1024x.jpg?v=1772727114',
    'bor-091': TIENDA + 'BOR-88002_20E2400px72DPIS_1024x.jpg?v=1772728568',
    'bor-093': CATALOGO + 'ACETATOS-M_1024x.png?v=1764665123',
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
