import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open(r'C:\Catalago Prodent\website\js\products-data.js', encoding='utf-8') as f:
    content = f.read()
existing_ids = set(re.findall(r"id:'([^']+)'", content))

new_products = """
  // ══════════════════════════════════════════
  // ZHERMACK LABORATORIO — Siliconas para Llaves y Duplicación
  // ══════════════════════════════════════════
  {id:'balsas-026', code:'ZETALABOR', cat:'materiales', brand:'balsas', name:'Zetalabor — Silicona-C para Laboratorio 85 Shore A',
   unit:'kit base+catalizador', img:'imagenes/balsas/pag_46.jpg',
   desc:'Silicona-C específica para laboratorio. Para control de estructura metálica, provisionales, máscaras gingivales y separador diente/yeso en mufla.',
   specs:['Tipo: Silicona-C','Dureza final: 85 Shore A','Mezcla manual','Compatible con catalizador Indurent Gel','Resistencia al calor 140°C']},

  {id:'balsas-027', code:'TITANIUM', cat:'materiales', brand:'balsas', name:'Titanium — Silicona-C para Laboratorio 95 Shore A Blanca',
   unit:'kit base+catalizador', img:'imagenes/balsas/pag_46.jpg',
   desc:'Silicona-C específica para laboratorio. Color blanco, alta resistencia al calor 180°C. Para estructura metálica, provisionales y máscaras gingivales.',
   specs:['Tipo: Silicona-C','Dureza final: 95 Shore A','Color: Blanco','Resistencia al calor 180°C','Compatible con Indurent Gel']},

  {id:'balsas-028', code:'PLATINUM85', cat:'materiales', brand:'balsas', name:'Platinum 85 — Silicona-A para Laboratorio 85 Shore A',
   unit:'kit base+catalizador', img:'imagenes/balsas/pag_48.jpg',
   desc:'Silicona-A de alta precisión para laboratorio. Contramufla, control estructura metálica, prótesis combinada, llave para provisionales. Color verde.',
   specs:['Tipo: Silicona-A','Proporción mezcla: 1:1','Dureza final: 85 Shore A','Color: Verde','Resistencia al calor >200°C','Memoria elástica: 99.5%']},

  {id:'balsas-029', code:'PLATINUM95', cat:'materiales', brand:'balsas', name:'Platinum 95 — Silicona-A para Laboratorio 95 Shore A Azul',
   unit:'kit base+catalizador', img:'imagenes/balsas/pag_48.jpg',
   desc:'Silicona-A alta precisión. Para cerámica prensada, enmufla prótesis removible, reparación de prótesis. Color azul.',
   specs:['Tipo: Silicona-A','Proporción mezcla: 1:1','Dureza final: 95 Shore A','Color: Azul','Resistencia al calor >200°C','Sin latex']},

  {id:'balsas-030', code:'ELITE-D22', cat:'materiales', brand:'balsas', name:'Elite Double 22 — Silicona-A para Duplicación 22 Shore A',
   unit:'kit base+catalizador', img:'imagenes/balsas/pag_50.jpg',
   desc:'Silicona-A para duplicación en laboratorio. Extrema fluidez, compatible con todos los yesos, resinas, materiales fosfáticos. Mezcla 1:1.',
   specs:['Tipo: Silicona-A','Proporción: 1:1','Dureza: 22 Shore A','Color: Verde claro','Memoria elástica: 99.95%','Reproducción detalles: 2μm']},

  // ══════════════════════════════════════════
  // EDENTA — Fresas de Diamante para Clínica
  // ══════════════════════════════════════════
  {id:'edenta-801', code:'G801.314.014', cat:'fresas', brand:'edenta', name:'Fresa Diamante Punta de Bola Ø14 — Verde (Grano Estándar)',
   unit:'pieza', img:'imagenes/balsas/pag_126.jpg',
   desc:'Fresa de diamante con punta de bola para alta velocidad. Vástago FG estándar 314.',
   specs:['Forma: Bola 801','Calibre vástago: FG 314','Diámetro: 14 (1/10)mm','Grano: Estándar (verde)','También en Ø: 7, 8, 9, 10, 12, 16, 18, 21, 23, 25']},

  {id:'edenta-802', code:'802.314.012', cat:'fresas', brand:'edenta', name:'Fresa Diamante Bola con Extensión Ø12',
   unit:'pieza', img:'imagenes/balsas/pag_126.jpg',
   desc:'Fresa de diamante bola con extensión para acceso a zonas de difícil acceso. Alta velocidad FG.',
   specs:['Forma: Bola con extensión 802','Calibre vástago: FG 314','Diámetro: 12 (1/10)mm','También en Ø14']},

  {id:'edenta-805', code:'G805.314.016', cat:'fresas', brand:'edenta', name:'Fresa Diamante Cono Invertido Ø16 — Verde',
   unit:'pieza', img:'imagenes/balsas/pag_126.jpg',
   desc:'Fresa diamante cono invertido. Para preparaciones oclusales y cavidades clase I. Alta velocidad FG.',
   specs:['Forma: Cono invertido 805','Calibre vástago: FG 314','Diámetro: 16 (1/10)mm','Grano: Estándar (verde)','También en Ø: 9, 10, 12, 18, 21']},

  {id:'edenta-806', code:'G806.314.012', cat:'fresas', brand:'edenta', name:'Fresa Diamante Cono Invertido con Extensión Ø12 — Verde',
   unit:'pieza', img:'imagenes/balsas/pag_126.jpg',
   desc:'Fresa diamante cono invertido con extensión. Alta velocidad FG.',
   specs:['Forma: Cono invertido con extensión 806','Calibre vástago: FG 314','Diámetro: 12 (1/10)mm','También en Ø: 10, 14']},

  {id:'edenta-838', code:'G838.314.012', cat:'fresas', brand:'edenta', name:'Fresa Diamante Cilindro Canto Redondeado Ø12 — Verde',
   unit:'pieza', img:'imagenes/balsas/pag_130.jpg',
   desc:'Fresa de diamante con forma de cilindro y canto redondeado. Alta velocidad FG.',
   specs:['Forma: Cilindro canto redondeado 838','Calibre vástago: FG 314','Diámetro: 12 (1/10)mm','También en Ø: 8, 9, 10, 14, 16']},

  {id:'edenta-839', code:'839.314.012', cat:'fresas', brand:'edenta', name:'Fresa Diamante Corte Frontal Ø12',
   unit:'pieza', img:'imagenes/balsas/pag_130.jpg',
   desc:'Fresa de diamante de corte frontal. Alta velocidad FG.',
   specs:['Forma: Corte frontal 839','Calibre vástago: FG 314','Diámetro: 12 (1/10)mm']},

  {id:'edenta-842', code:'G842.314.012', cat:'fresas', brand:'edenta', name:'Fresa Diamante Cilindro Punta Plana Ø12 — Verde',
   unit:'pieza', img:'imagenes/balsas/pag_130.jpg',
   desc:'Fresa de diamante con forma de cilindro y punta plana. Alta velocidad FG.',
   specs:['Forma: Cilindro punta plana 842','Calibre vástago: FG 314','Longitud: 12.00mm, Diámetro: 12 (1/10)mm']},

  {id:'edenta-845', code:'845.314.012', cat:'fresas', brand:'edenta', name:'Fresa Diamante Cono Punta Plana Ø12',
   unit:'pieza', img:'imagenes/balsas/pag_130.jpg',
   desc:'Fresa de diamante con forma de cono y punta plana. Alta velocidad FG.',
   specs:['Forma: Cono punta plana 845','Calibre vástago: FG 314','Diámetro: 12 (1/10)mm','También en Ø10']},

  {id:'edenta-845kr', code:'G845KR.314.018', cat:'fresas', brand:'edenta', name:'Fresa Diamante Cono Canto Redondeado Ø18 — Verde',
   unit:'pieza', img:'imagenes/balsas/pag_130.jpg',
   desc:'Fresa de diamante con forma de cono y canto redondeado. Alta velocidad FG.',
   specs:['Forma: Cono canto redondeado 845KR','Calibre vástago: FG 314','Diámetro: 18 (1/10)mm','También en Ø: 16, 25']},

  {id:'edenta-wt', code:'GW801.314.014', cat:'fresas', brand:'edenta', name:'Fresa Diamante White-Tiger Bola Ø14 — Diamantes Naturales',
   unit:'pieza', img:'imagenes/balsas/pag_140.jpg',
   desc:'Serie White-Tiger: diamantes naturales fijados por proceso LLD sobre vástago de acero inoxidable. Alto rendimiento abrasivo, vida útil extraordinariamente larga.',
   specs:['Serie: White-Tiger','Diamantes naturales','Proceso LLD','Alto rendimiento abrasivo','Vástago acero inoxidable','También: W368, GW878K, GW879K, W881']},

  {id:'edenta-cerapol', code:'0372RA', cat:'fresas', brand:'edenta', name:'Cerapol Super — Pulidor para Cerámica Ø50',
   unit:'pieza', img:'imagenes/balsas/pag_155.jpg',
   desc:'Pulidor para todas las restauraciones cerámicas con coronas parciales y completas. Alto brillo sin pasta. No requiere nueva cocción de glaseado.',
   specs:['Uso: Cerámica','Diámetro: 50 (1/10)mm','Longitud: 10mm','Sin pasta de pulido']},

  {id:'edenta-topbrush', code:'1502RA', cat:'fresas', brand:'edenta', name:'TopBrush SiC-Brushlets — Pulidor de Fibras SiC Ø70',
   unit:'pieza', img:'imagenes/balsas/pag_155.jpg',
   desc:'Fibras especiales con carburo de silicio (SiC) como medio abrasivo. Sin pasta de pulido. Cada cerda por separado es un elemento de pulido.',
   specs:['Medio abrasivo: SiC (carburo de silicio)','Sin pasta de pulido','Diámetro: 70 (1/10)mm','Longitud: 5mm']},

  {id:'edenta-flexisnap', code:'1295SO', cat:'fresas', brand:'edenta', name:'Flexi-Snap Kit — Discos Pulido Composite 20 pzas + 2 Mandriles',
   unit:'kit', img:'imagenes/balsas/pag_155.jpg',
   desc:'Discos de pulido para brillo natural en todo tipo de composites. Escasa rugosidad superficial para mejor brillo final.',
   specs:['20 pulidores de cada grano','2 mandriles incluidos','Uso: Composite','Clínica']},

  {id:'edenta-crownprep', code:'40035SO', cat:'fresas', brand:'edenta', name:'Crown Prep-Set — Kit Fresas Diamante para Cerámica CAD/CAM',
   unit:'kit', img:'imagenes/balsas/pag_165.jpg',
   desc:'Instrumentos de diamante para preparación de coronas de cerámica realizadas con tecnología CAD/CAM. Bordes redondeados, sin transiciones bruscas.',
   specs:['Tecnología: CAD/CAM','9 fresas incluidas','Cerámica integral','Incluye fresas G y F (grano fino)']},

  // ══════════════════════════════════════════
  // DENTALEZ — Piezas de Mano Alta Velocidad Concentrix
  // ══════════════════════════════════════════
  {id:'balsas-031', code:'CONC-SX', cat:'equipos', brand:'balsas', name:'Pieza de Mano Alta Velocidad Concentrix SX — Sin Fibra Óptica',
   unit:'pieza', img:'imagenes/balsas/pag_175.jpg',
   desc:'Pieza de mano alta velocidad sin fibra óptica. Baleros de acero lubricados, turbina push button. Conector LED o halógenos StarDental. 1 año de garantía.',
   specs:['Sin fibra óptica','Turbina push button','Baleros: Acero lubricados','Cabeza Ø10mm','Peso: 41-49g','1 año de garantía']},

  {id:'balsas-032', code:'CONC-SW', cat:'equipos', brand:'balsas', name:'Pieza de Mano Alta Velocidad Concentrix SW — Conector Rápido 360°',
   unit:'pieza', img:'imagenes/balsas/pag_175.jpg',
   desc:'Pieza de mano alta velocidad sin fibra óptica. Baleros de acero lubricados, turbina push button. Conector rápido de giro 360° de 2/3 o 4 líneas StarDental.',
   specs:['Sin fibra óptica','Conector rápido giro 360°','2/3 o 4 líneas StarDental','Turbina push button','1 año de garantía']},

  {id:'balsas-033', code:'CONC-FX', cat:'equipos', brand:'balsas', name:'Pieza de Mano Alta Velocidad Concentrix FX — 4 Líneas Entrada Fija',
   unit:'pieza', img:'imagenes/balsas/pag_175.jpg',
   desc:'Pieza de mano de 4 líneas entrada fija con baleros de acero inoxidable y turbina push button. 1 año de garantía.',
   specs:['4 líneas entrada fija','Baleros: Acero inoxidable','Turbina push button','1 año de garantía']},

  {id:'balsas-034', code:'CONC-FB', cat:'equipos', brand:'balsas', name:'Pieza de Mano Alta Velocidad Concentrix FB — 4 Líneas con Chuck Manual',
   unit:'pieza', img:'imagenes/balsas/pag_175.jpg',
   desc:'Pieza de mano de 4 líneas entrada fija con turbina y Chuck de acero inoxidable, manual (usa bota fresas). 1 año de garantía.',
   specs:['4 líneas entrada fija','Chuck acero inoxidable manual','Usa bota fresas','1 año de garantía']},

  // ══════════════════════════════════════════
  // SPRING HEALTH — Lámpara de Fotocurado LED
  // ══════════════════════════════════════════
  {id:'balsas-035', code:'SH-LED', cat:'equipos', brand:'balsas', name:'Lámpara de Fotocurado LED Spring Health',
   unit:'pieza', img:'imagenes/balsas/pag_186.jpg',
   desc:'Lámpara LED dental para fotopolimerización de resinas compuestas, sellantes y adhesivos. Dos niveles de intensidad: 500 y 900 mw/cm². Ciclos 16s ON / 15s OFF.',
   specs:['Peso: 28g','Longitud de onda: 450-490nm','Intensidad alta: 900mw/cm²','Intensidad baja: 500mw/cm²','Voltaje: 90-260V CA','Vida útil LED: +5000 horas','Incluye: lente 8mm, filtro protector ocular y soporte']},

  // ══════════════════════════════════════════
  // NOMAD — Sistema de Rayos X Portátil
  // ══════════════════════════════════════════
  {id:'balsas-036', code:'NOMAD', cat:'equipos', brand:'balsas', name:'Sistema de Rayos X Portátil Nomad',
   unit:'equipo', img:'imagenes/balsas/pag_190.jpg',
   desc:'Sistema Rayos-X inalámbrico portátil. Diseñado para adultos y pediátricos. Escudo protector de retrodifusión incluido, posición ajustable para múltiples ángulos.',
   specs:['Inalámbrico (batería NiCd 14.4V, 2Ahr)','Peso: 4 kg (3.6 kg sin batería)','Dimensiones: L33 / P15 / H30 cm','Con escudo protector de retrodifusión','Ideal para odontología móvil']},
"""

entries = re.findall(r"\{id:'[^']+'.+?\}", new_products, re.DOTALL)
block = ""
added = 0
for entry in entries:
    m = re.search(r"id:'([^']+)'", entry)
    if m and m.group(1) not in existing_ids:
        block += "  " + entry.strip() + ",\n"
        added += 1

print(f"Balsas/Edenta nuevos productos: {added}")

idx = content.rfind('];')
content = content[:idx].rstrip() + '\n' + block.rstrip(',') + '\n];\n'

total = len(re.findall(r"id:'[a-zA-Z0-9_-]+'", content))
print(f"Total productos: {total}")

with open(r'C:\Catalago Prodent\website\js\products-data.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("GUARDADO")
