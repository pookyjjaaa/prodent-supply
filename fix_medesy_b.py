import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0
BASE = 'https://www.medesy.it/site/wp-content/uploads/2023/01/Immagine_variante_prodotto_'
BASE2 = 'https://www.medesy.it/site/wp-content/uploads/2023/02/'

photos = {
    # Orthodontics
    'medesy-977':  BASE + '3000slash91_TC.jpg',
    'medesy-978':  BASE + '1680slash1.jpg',
    'medesy-979':  BASE + '1680slash2.jpg',
    'medesy-980':  BASE + '1680slash3.jpg',
    'medesy-981':  BASE + '1680slash4.jpg',
    'medesy-982':  BASE + '6141.jpg',
    'medesy-983':  BASE + '6140.jpg',
    'medesy-984':  BASE + '981slashORTO.jpg',
    # Accessories - trays
    'medesy-1000': BASE + '998slashFRS.jpg',
    'medesy-1001': BASE + '998slashFBS.jpg',
    'medesy-1002': BASE + '998slashFVS.jpg',
    'medesy-1003': BASE + '1150.jpg',
    'medesy-1004': BASE + '1151.jpg',
    'medesy-1005': BASE + '1152.jpg',
    'medesy-1006': BASE + '215slash1.jpg',
    'medesy-1007': BASE + '215slash2.jpg',
    'medesy-1008': BASE + '215slash3.jpg',
    'medesy-1009': BASE + '975slashG.jpg',
    'medesy-1010': BASE + '975slashR.jpg',
    'medesy-1011': BASE + '975slashB.jpg',
    'medesy-1012': BASE + '974slashG.jpg',
    'medesy-1013': BASE + '974slashR.jpg',
    'medesy-1014': BASE + '974slashB.jpg',
    'medesy-1015': BASE + '6161slashA.jpg',
    'medesy-1020': BASE + '6163.jpg',
    'medesy-1021': BASE + '8400.jpg',
    # Extraction forceps - English pattern
    'medesy-1027': BASE + '2500slash1.jpg',
    'medesy-1028': BASE + '2500slash2.jpg',
    'medesy-1029': BASE + '2500slash7.jpg',
    'medesy-1030': BASE + '2500slash17.jpg',
    'medesy-1031': BASE + '2500slash18.jpg',
    'medesy-1032': BASE + '2500slash18-A.jpg',
    'medesy-1033': BASE + '2500slash67.jpg',
    'medesy-1034': BASE + '2500slash4.jpg',
    'medesy-1035': BASE + '2500slash8.jpg',
    'medesy-1036': BASE + '2500slash73.jpg',
    'medesy-1037': BASE + '2500slash73-S.jpg',
    'medesy-1038': BASE + '2500slash20.jpg',
    'medesy-1039': BASE + '2500slash51.jpg',
    'medesy-1040': BASE + '2500slash69.jpg',
    # American pattern forceps
    'medesy-1041': BASE + '2650slash65.jpg',
    'medesy-1042': BASE + '2650slash18-R.jpg',
    'medesy-1043': BASE + '2650slash18-L.jpg',
    'medesy-1044': BASE + '2650slash16.jpg',
    'medesy-1045': BASE + '2650slash203.jpg',
    'medesy-1046': BASE + '2650slash151.jpg',
    # Mirrors
    'medesy-1048': BASE + '4903slash3.jpg',
    'medesy-1049': BASE + '4903slash4.jpg',
    'medesy-1050': BASE + '4903slash4RO.jpg',
    'medesy-1051': BASE + '4903slash5.jpg',
    'medesy-1052': BASE + '4903slash5RO.jpg',
    'medesy-1053': BASE + '4903slash5MA.jpg',
    'medesy-1054': BASE + '4905slash8.jpg',
    'medesy-1055': BASE2 + 'Immagine_variante_prodotto_4903slash10RO.jpg',
    # Cotton pliers
    'medesy-1056': BASE + '1124.jpg',
    'medesy-1057': BASE + '1123.jpg',
    'medesy-1058': BASE + '1122.jpg',
    'medesy-1059': BASE + '1022.jpg',
    'medesy-1060': BASE + '1124slashD.jpg',
    # Gracey curettes
    'medesy-1061': BASE + '625slash1-2AL.jpg',
    'medesy-1062': BASE2 + '625_3-4_C8_variante-completa.jpg',
    'medesy-1063': BASE2 + '628_5-6_C8_variante-completa.jpg',
    'medesy-1065': BASE2 + '628_11-12_C8_variante-completa-1.jpg',
    'medesy-1066': BASE2 + '628_13-14_C8_variante-completa-3.jpg',
    'medesy-1067': BASE2 + 'Immagine_variante_prodotto_625slashKITC8.png',
    'medesy-1068': BASE2 + 'Immagine_variante_prodotto_628slashKITC8.jpg',
    'medesy-1069': BASE2 + 'Immagine_variante_prodotto_669slashKITHL8-1.jpg',
    # Scalers
    'medesy-1070': BASE + '640slash24SL.jpg',
    'medesy-1071': BASE + '640slash1SL.jpg',
    'medesy-1072': BASE + '640slash2SL.jpg',
    'medesy-1073': BASE + '640slash3HL8.jpg',
    'medesy-1074': BASE + '640slash23HL8.jpg',
    # Goldstein composite instruments
    'medesy-1075': BASE + '492slash1.jpg',
    'medesy-1076': BASE + '492slash2.jpg',
    'medesy-1077': BASE + '492slash1T.jpg',
    'medesy-1078': BASE + '492slash2T.jpg',
    'medesy-1079': BASE + '492slash3T.jpg',
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
