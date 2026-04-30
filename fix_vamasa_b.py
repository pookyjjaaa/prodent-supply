import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

CRD = 'https://www.clinicalresearchdental.com/cdn/shop/'
GARIMA = 'https://garimadental.com/wp-content/uploads/'

photos = {
    'vamasa-050': CRD + 'products/4018_Jiffy-Universal-Extra-Oral-Adjusting-Polishing-Kit-open_FINISH_535x.jpg?v=1576162540',
    'vamasa-051': CRD + 'files/JiffyAssorted_535x.png?v=1682953034',
    'vamasa-052': 'https://images.ctfassets.net/wfptrcrbtkd0/7d8oFL5wl4W8a1exq1Lvv3/dce2e5cc357ecc267df420db91fb7cf6/Jiffy_Sales_Sheet_Composite_3D_Edited_1__1_.png?fm=webp',
    'vamasa-053': CRD + 'products/3059_Composite-Wetting-Resin-Mini-Refill-open_COMPOSITES_546b5180-64ff-4f04-8e8e-5fde0d4a3172_535x.jpg?v=1576701904',
    'vamasa-054': CRD + 'products/4680-Jiffy-Proximal-Saw-Stainless-Steel-open_535x.jpg?v=1636137586',
    'vamasa-055': CRD + 'products/4670-Jiffy-Diamonds-Strip-Perforated-Narrow-Assorted-group-3D_535x.jpg?v=1636138481',
    'vamasa-056': CRD + 'files/UltraTect-orange-lenses-black-elements_535x.jpg?v=1721234584',
    'vamasa-057': GARIMA + '2021/01/57A-500x500-1.jpg',
    'vamasa-058': CRD + 'products/5972_VALO-Grand-Cordless-Kit-open_EQUIPMENT_535x.jpg?v=1580924530',
    'vamasa-059': CRD + 'files/963_PermaFlo_Pink_2pk_Box_Open_0522_535x.jpg?v=1749146292',
    'vamasa-060': CRD + 'files/PermaFlo_Purple_2pk_535x.jpg?v=1749149334',
    'vamasa-061': CRD + 'products/5912_PermaFlo-DC-A2-Refill-Kit-open_CROWN-BRIDGE_f912a19d-dfcb-460e-aab4-6c640af53ee3_535x.jpg?v=1576872972',
    'vamasa-062': CRD + 'products/5900-EndoREZ-Kit-open_ENDODONTICS_535x.jpg?v=1574284445',
    'vamasa-063': CRD + 'products/3059_Composite-Wetting-Resin-Mini-Refill-open_COMPOSITES_546b5180-64ff-4f04-8e8e-5fde0d4a3172_535x.jpg?v=1576701904',
    'vamasa-064': CRD + 'products/Ultradent-Citric-Acid-IndiSpense-syringe_ENDODONTICS_535x.jpg?v=1628890279',
    'vamasa-065': GARIMA + '2025/03/File-Eze-syringe-with-tip-1.2syg.png',
    'vamasa-066': GARIMA + '2023/03/Consepsis-V-IndiSpense-syringe_ENDODONTICS-highdef.png',
    'vamasa-067': CRD + 'products/Ultradent_EDTA_18_percent_Solution_IndiSpense_syringe_535x.png?v=1606331658',
    'vamasa-068': CRD + 'products/Black-Mini-Tip_TIPS_0fdb35bf-46e0-4808-9bf0-284fea391f83_535x.jpg?v=1590509518',
    'vamasa-069': CRD + 'products/Inspiral-Brush-Tip_TIPS_b15c936f-5f7e-4e8d-92b3-5d523cd22276_535x.jpg?v=1581694037',
    'vamasa-070': CRD + 'products/1120_Micro-Capillary-Tip-5mm-20pk-open_TIPS_535x.jpg?v=1629470621',
    'vamasa-071': CRD + 'products/Ultradent_Endo-Eze-Tips-22ga-20ga-19ga-18ga-group_535x.jpg?v=1629479341',
    'vamasa-072': GARIMA + '2025/03/Ultradent-Tips-NaviTip-Tips-30ga-25mm-1.png',
    'vamasa-073': CRD + 'products/Endo-Eze-Irrigator-Tip_TIPS_535x.jpg?v=1572316112',
    'vamasa-074': CRD + 'products/Blue-Mini-Dento-Infusor-Tip_TIPS_bc6d8cc4-a10a-42e5-9a39-9877fe550e6c_535x.jpg?v=1579630845',
    'vamasa-075': CRD + 'products/NaviTip-31ga-Sideport-21mm_yellow_-single_TIPS_6d9be753-a0d7-4b3e-bef0-a8dcb7df1f09_535x.jpg',
    'vamasa-076': GARIMA + '2025/03/Ultradent-Tips-NaviTip-Tips-30ga-25mm-1.png',
    'vamasa-077': CRD + 'files/Comfort_Hub_Tip_01_3D_535x.jpg?v=1693592852',
    'vamasa-078': CRD + 'products/1452_NaviTip-FX-Tip-17mm-white-single_TIPS_24022152-9945-4e83-8f5d-0fb91e4e92eb_535x.jpg?v=1572316112',
    'vamasa-079': CRD + 'products/Capillary-Tip-0.014-purple_TIPS_535x.jpg?v=1581714775',
    'vamasa-080': CRD + 'products/1120_Micro-Capillary-Tip-5mm-20pk-open_TIPS_535x.jpg?v=1629470621',
    'vamasa-081': CRD + 'products/SST-Surgical-Suction-Tip_TIPS-highdef_600x450_cb93acc4-5cf9-4ec0-8a04-dc3df829d3c6_535x.png?v=1597778211',
    'vamasa-082': CRD + 'products/Ultradent_IntraOral-Clear-Tip_535x.png?v=1638887380',
    'vamasa-083': CRD + 'products/1680_Skini-Syringe-20pk-package_SYRINGES_535x.jpg?v=1572316115',
    'vamasa-084': CRD + 'products/205_Luer-Lock-Cap-White-20pk-open_TIPS_45d71fcd-dd05-404e-bdc8-3732f4b14316_535x.jpg?v=1572316112',
    'vamasa-085': CRD + 'products/TriAway-Adapter_SYRINGES_535x.jpg?v=1572316113',
    'vamasa-086': CRD + 'products/1357_Black-Micro-FX-Tip-100pk-open_TIPS_6c8f3406-7e9e-4879-8d34-9555114f68b4_535x.jpg?v=1572316112',
    'vamasa-087': CRD + 'products/Blue-Micro-Tip_TIPS_535x.jpg?v=1579642129',
    'vamasa-088': CRD + 'products/1357_Black-Micro-FX-Tip-100pk-open_TIPS_6c8f3406-7e9e-4879-8d34-9555114f68b4_535x.jpg?v=1572316112',
    'vamasa-089': CRD + 'products/193_Black-Mini-Brush-Tips-with-Tipsocs-20pk-open_TIPS_fd8cf578-fb9b-4684-b3d2-db7d6d0b3183_535x.jpg?v=1572316112',
    'vamasa-090': CRD + 'products/5799_OpalCups-Finishing-20pk-open_WHITEN_535x.jpg?v=1602686931',
    'vamasa-091': CRD + 'products/1.2ml-Syringe_SYRINGES_535x.jpg?v=1581708489',
    'vamasa-092': CRD + 'products/Ultradent-Syringe-Cover-with-syringe_SYRINGES_535x.jpg?v=1572316115',
    'vamasa-093': CRD + 'products/White-Mac-Tip-single_TIPS_65933b86-fa1f-4fd4-9e45-4c2cc183a805_535x.jpg?v=1572316112',
    'vamasa-094': CRD + 'products/Ultradent-Luer-Vacuum-Adapter-notip-closed_535x.jpg?v=1612312476',
    'vamasa-095': 'https://stanfordtudepositodental.com.mx/wp-content/uploads/2022/03/Sutura-surgeasy-silk-3-0.png',
    'vamasa-096': 'https://plus.odontologybg.com/wp-content/uploads/2020/10/SURS4-SUTURA-SURGEASY-ABSORBIBLE-4-0_25ab462a-526d-4b80-86f6-a4033730413d-1200x1200.png',
    'vamasa-097': CRD + 'products/Ribbond-thm-bondable-reinforcement-ribbon-kit_535x.png?v=1585595203',
    'vamasa-098': CRD + 'products/Ribbond_scissors_535x.jpg?v=1572316120',
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
