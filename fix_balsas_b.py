import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

photos = {
    'pdm-tray-adhesive': 'https://images.squarespace-cdn.com/content/v1/5de863544ebd8e63f0f2684b/1577415304928-G3Z7Q8EKBWBE561Q1O9B/ImpressionTray_Adhesive-2.jpg',
    'balsas-018': 'https://www.dentalcity.com/CatalogImages/DENLN/18-12650-Product_Primary_Image-400X400.jpg',
    'balsas-019': 'https://cdn11.bigcommerce.com/s-emp9gstccl/images/stencil/1280x1280/products/7217/6210/thmb_ZHM-H003_2__55545.1612397785.jpg?c=2',
    'balsas-020': 'https://www.dentaltix.com/en/sites/default/files/styles/large/public/cubetas-impresion-plastico-transparente_0_0_1_0.jpg?itok=-wlQ04SW',
    'balsas-021': 'https://www.zhermack.com/public/uploads/ZH-Pack-Image-Zeta-1-Ultra-C810000.jpg',
    'balsas-022': 'https://www.dentaltix.com/en/sites/default/files/styles/large/public/zhermack_zeta_2_sporex_0.jpg?itok=hI8ju197',
    'balsas-023': 'https://5.imimg.com/data5/ECOM/Default/2023/7/327253902/HV/DX/SI/132871955/zetaclaveb-c306550-500x500.jpg',
    'balsas-024': 'https://www.dentaltix.com/en/sites/default/files/styles/large/public/yeso-iii-elite-model-ivory-3-kg.jpg?itok=DoUWdXau',
    'balsas-025': 'https://www.dentaltix.com/en/sites/default/files/styles/large/public/elite-model-fast_1_0.jpg?itok=tvdPZwaD',
    'balsas-026': 'https://www.dentaltix.com/en/sites/default/files/styles/large/public/silicona-zetalabor_0_0.jpg?itok=C_VnNUOf',
    'balsas-027': 'https://www.dentaltix.com/en/sites/default/files/styles/large/public/zh88525_0.jpg?itok=SLbK3jWW',
    'balsas-028': 'https://www.prestigedentalproducts.com/images/P/platinum%2085%20%28zhermack%29.jpg',
    'balsas-029': 'https://www.prestigedentalproducts.com/images/P/Platinum%2095%20%28Zhermack%29.jpg',
    'balsas-030': 'https://www.dentaltix.com/en/sites/default/files/styles/large/public/elite-double-22-fast.jpg?itok=GtmKNvE4',
    'balsas-031': 'https://cdn.shopify.com/s/files/1/0577/9498/6179/files/Concentrix_FX.jpg?v=1629245230',
    'balsas-032': 'https://cdn.shopify.com/s/files/1/0577/9498/6179/files/Concentrix_FX.jpg?v=1629245230',
    'balsas-033': 'https://cdn.shopify.com/s/files/1/0577/9498/6179/files/Concentrix_FX.jpg?v=1629245230',
    'balsas-034': 'https://cdn.shopify.com/s/files/1/0577/9498/6179/files/Concentrix_FX.jpg?v=1629245230',
    'balsas-035': 'https://www.brandywinedentalsupply.com/cdn/shop/files/tcover.jpg?v=1685548039&width=1946',
    'balsas-036': 'https://dexis.com/sites/g/files/wdvifx221/files/styles/optimized/public/Nomad%20Page%20Web%20Graphic%202025%20v2.png.webp',
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
