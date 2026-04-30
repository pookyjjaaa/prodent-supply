import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open(r'C:\Catalago Prodent\website\js\products-data.js', encoding='utf-8') as f:
    content = f.read()
existing_ids = set(re.findall(r"id:'([^']+)'", content))

new_products = """
  // ══════════════════════════════════════════
  // BORGATTA — Adicionales (brackets, alambres, elásticos, instrumentos, equipos)
  // ══════════════════════════════════════════

  // --- BRACKETS BLACK DUO ---
  {id:'bor-020', code:'90-047-01', cat:'ortodoncia', brand:'borgatta', name:'Brackets Black Duo Roth Súper Torque .022',
   unit:'juego 345 pzas', img:'imagenes/borgatta/pag_14.jpg',
   desc:'Cuerpo y base Black Duo diseñados para extra torque. Prescripción Roth .022.',
   specs:['Slot: .022','Prescripción: Roth Súper Torque','Malla 80','Línea Black']},

  {id:'bor-021', code:'90-063-00', cat:'ortodoncia', brand:'borgatta', name:'Bracket B-Action Torque en Base MBT .022',
   unit:'juego 3 pzas', img:'imagenes/borgatta/pag_16.jpg',
   desc:'Hecho en una sola pieza, slot suavizado y pulido para minimizar la fricción. Prescripción MBT.',
   specs:['Slot: .022','Prescripción: MBT','Una sola pieza','Línea Black']},

  {id:'bor-022', code:'300-582', cat:'ortodoncia', brand:'borgatta', name:'Brackets Mirage Sequence MBT .022',
   unit:'juego 3 pzas', img:'imagenes/borgatta/pag_22.jpg',
   desc:'Cuerpo metálico de ejemplar belleza y brillo. Prescripción MBT.',
   specs:['Slot: .022','Prescripción: MBT','Malla 80']},

  {id:'bor-023', code:'300-538', cat:'ortodoncia', brand:'borgatta', name:'Brackets Cerámico Roth .022',
   unit:'juego 345 pzas', img:'imagenes/borgatta/pag_20.jpg',
   desc:'Cuerpo cerámico de ejemplar belleza y translucidez. Prescripción Roth.',
   specs:['Slot: .022','Prescripción: Roth','Cuerpo cerámico','Alta translucidez']},

  {id:'bor-024', code:'300-512', cat:'ortodoncia', brand:'borgatta', name:'Brackets Mirage Sequence Mini Roth .018',
   unit:'juego 3 pzas', img:'imagenes/borgatta/pag_20.jpg',
   desc:'Fabricado en una sola pieza, cuerpo pulido, slot suavizado y malla 80. Prescripción Roth Mini.',
   specs:['Slot: .018','Prescripción: Roth Mini','Malla 80','Una sola pieza']},

  {id:'bor-025', code:'300-530', cat:'ortodoncia', brand:'borgatta', name:'Brackets Mirage Sequence Mini Ricketts .018',
   unit:'juego 345 pzas', img:'imagenes/borgatta/pag_22.jpg',
   desc:'Cuerpo en una sola pieza, malla 80, bordes y aletas redondeados. Prescripción Ricketts.',
   specs:['Slot: .018','Prescripción: Ricketts','Malla 80','Bordes redondeados']},

  {id:'bor-026', code:'70-100', cat:'ortodoncia', brand:'borgatta', name:'Brackets Glint Roth .022 — Línea Alternativa',
   unit:'juego 345 pzas', img:'imagenes/borgatta/pag_27.jpg',
   desc:'Cuerpo pulido y abrillantado para facilitar la higiene, retención mecánica de alta seguridad. Línea Glint.',
   specs:['Slot: .022','Prescripción: Roth','Malla 80','Línea Glint']},

  // --- TUBOS ---
  {id:'bor-027', code:'68-162-09', cat:'ortodoncia', brand:'borgatta', name:'Tubos Black Alexander Roth UR Dobles Convertibles .022 c/malla',
   unit:'paquete 5 pzas', img:'imagenes/borgatta/pag_16.jpg',
   desc:'Cuerpo de acero inoxidable de alto pulido. Tubos dobles convertibles con malla para molar superior derecho.',
   specs:['Slot: .022','Con malla','Convertibles','Línea Black']},

  {id:'bor-028', code:'69-162-17', cat:'ortodoncia', brand:'borgatta', name:'Tubos Black MBT UR Triples Convertibles .022 p/soldar',
   unit:'paquete 5 pzas', img:'imagenes/borgatta/pag_16.jpg',
   desc:'Fabricados para menor interferencia molar, con opción de soportar arcos extraorales. Para soldar.',
   specs:['Slot: .022','Para soldar','Convertibles','Prescripción MBT','Línea Black']},

  {id:'bor-029', code:'KIT301-022', cat:'ortodoncia', brand:'borgatta', name:'Kit de Tubos Borgatta Roth .022 c/malla — 4 tubos',
   unit:'kit 4 piezas', img:'imagenes/borgatta/pag_25.jpg',
   desc:'Paquete con 4 tubos para primer o segundo molar, cuerpo de una sola pieza y malla 80.',
   specs:['Slot: .022','Con malla 80','4 piezas (UR/UL/LR/LL)','Sencillos convertibles']},

  {id:'bor-030', code:'KIT71-022', cat:'ortodoncia', brand:'borgatta', name:'Kit de Tubos Glint Roth .022 c/malla — Línea Alternativa',
   unit:'kit 4 piezas', img:'imagenes/borgatta/pag_27.jpg',
   desc:'Cuerpo compacto y pulido para mayor comodidad. Disponibles en kit de 4 tubos.',
   specs:['Slot: .022','Con malla','Sencillos no convertibles','Línea Glint']},

  // --- BANDAS Y ACCESORIOS ---
  {id:'bor-031', code:'903-00002-AZ', cat:'ortodoncia', brand:'borgatta', name:'Estuche para Bandas Advance — Caja Acrílica 32 espacios',
   unit:'pieza', img:'imagenes/borgatta/pag_30.jpg',
   desc:'Caja en acrílico y plástico inyectado de alta resistencia para guardar bandas, brackets u otros accesorios. 32 espacios.',
   specs:['32 espacios','Material: Acrílico y plástico','Versión Advance']},

  {id:'bor-032', code:'500-020', cat:'ortodoncia', brand:'borgatta', name:'Adaptador de Bandas Autoclavable — 3 puntas',
   unit:'juego 3 puntas', img:'imagenes/borgatta/pag_30.jpg',
   desc:'Cuerpo de plástico altamente resistente, punta de acero inoxidable para asentar bandas con precisión. 100% autoclavable.',
   specs:['Punta cuadrada (500-020)','Punta triangular (500-020-1)','Punta redonda (500-020-2)','Autoclavable']},

  {id:'bor-033', code:'300-590', cat:'ortodoncia', brand:'borgatta', name:'Botones Linguales Borgatta — Plano p/soldar',
   unit:'paquete 10 pzas', img:'imagenes/borgatta/pag_30.jpg',
   desc:'Botones de tracción en base plana o curva para soldar o bondear. Malla mecánica de gran confianza.',
   specs:['Base plana para soldar','También disponibles c/malla (300-592)','Curvo c/malla (300-593)']},

  {id:'bor-034', code:'300-504', cat:'ortodoncia', brand:'borgatta', name:'Caja Lingual Borgatta Standard Abierta — 10 pzas',
   unit:'paquete 10 pzas', img:'imagenes/borgatta/pag_30.jpg',
   desc:'Fabricadas en acero inoxidable, bordes contorneados para mayor comodidad y anchura perfecta para ajustar instrumentos ortopédicos.',
   specs:['Acero inoxidable','Abierta c/g 10 pzas','También disponible universal (300-704)']},

  {id:'bor-035', code:'28-300-26', cat:'ortodoncia', brand:'borgatta', name:'Kit de Mini Moldes Borgatta — 7 piezas',
   unit:'kit 7 pzas', img:'imagenes/borgatta/pag_30.jpg',
   desc:'Moldes de plástico para resina fotocurable, incluye un mango de plástico para colocarlos.',
   specs:['7 piezas','Material: Plástico','Incluye mango']},

  // --- INSTRUMENTOS STRIPPING ---
  {id:'bor-036', code:'28-300-25', cat:'instrumental', brand:'borgatta', name:'Contrángulo para Lijas de Stripping',
   unit:'pieza', img:'imagenes/borgatta/pag_33.jpg',
   desc:'Contrángulo de reducción tipo E, cuerpo de aluminio. Trabaja exclusivamente con lijas automáticas del kit de stripping.',
   specs:['Reducción tipo E','Cuerpo aluminio','Compatible con lijas automáticas Borgatta']},

  {id:'bor-037', code:'28-300-10', cat:'instrumental', brand:'borgatta', name:'Kit para Stripping — Lijas, Maneral, Medidor, Pulidor y Pusher',
   unit:'kit', img:'imagenes/borgatta/pag_33.jpg',
   desc:'Instrumento manual para desgaste interproximal, incluye medidor de espacios y pusher para intercambio de lijas.',
   specs:['Incluye: Lijas, Maneral, Medidor de espacios, Pulidor y Pusher','Acero inoxidable grado médico']},

  {id:'bor-038', code:'0-002-116', cat:'instrumental', brand:'borgatta', name:'Instrumento de Stripping Tipo Sierra',
   unit:'pieza', img:'imagenes/borgatta/pag_33.jpg',
   desc:'Cuerpo metálico autoclavable, sostiene eficientemente las lijas cortas de tipo sierra.',
   specs:['Autoclavable','Para lijas cortas sierra','Con lijas recambio 0-002-117 y 0-002-118']},

  // --- ACCESORIOS DIAGNÓSTICO ---
  {id:'bor-039', code:'700-060', cat:'ortodoncia', brand:'borgatta', name:'Acetato Rígido Transparente para Retenedores — Calibre .060',
   unit:'paquete 10 pzas', img:'imagenes/borgatta/pag_36.jpg',
   desc:'Acetato blando y rígido para guardas oclusales y retenedores. Disponible en varios calibres.',
   specs:['Calibre: .060','10 piezas por paquete','También en .020, .030, .040, .080']},

  {id:'bor-040', code:'701-060', cat:'ortodoncia', brand:'borgatta', name:'Acetato Blando Transparente para Guardas — Calibre .060',
   unit:'paquete 10 pzas', img:'imagenes/borgatta/pag_36.jpg',
   desc:'Acetato blando calibre .060 para guardas oclusales. 10 piezas.',
   specs:['Calibre: .060','10 piezas por paquete','También en .035 y .080']},

  {id:'bor-041', code:'300-571', cat:'instrumental', brand:'borgatta', name:'Regla Ricketts',
   unit:'pieza', img:'imagenes/borgatta/pag_36.jpg',
   desc:'Perfecta aliada para una medición más acertada y un diagnóstico más eficiente. Hecha en plástico flexible. Medidas 190x200mm.',
   specs:['Material: Plástico flexible','Medidas: 190mm x 200mm','Incluye escalas cefalométricas']},

  {id:'bor-042', code:'17-222-11', cat:'ortodoncia', brand:'borgatta', name:'Papel de Trazado — Block 100 hojas',
   unit:'block 100 hojas', img:'imagenes/borgatta/pag_36.jpg',
   desc:'Block de 100 hojas de acetato de .003" de grosor, resistente a rasgaduras o curvaturas, separadas con hojas de papel cebolla.',
   specs:['100 hojas','Grosor: .003"','Separadas con papel cebolla','Línea Black']},

  // --- ALAMBRES ACERO INOXIDABLE ---
  {id:'bor-043', code:'0-000-620', cat:'ortodoncia', brand:'borgatta', name:'Alambre Acero Inoxidable Borgatta Redondo .020 — en Bolsa 10 pzas',
   unit:'bolsa 10 pzas', img:'imagenes/borgatta/pag_38.jpg',
   desc:'Acero inoxidable, alta rigidez, resistencia y gran pulido. Alta versatilidad, maleabilidad para la confección de aparatos intraorales.',
   specs:['Calibre: .020 redondo','10 piezas en bolsa','Disponible desde .012 a .040 y rectangulares']},

  {id:'bor-044', code:'03-030-58', cat:'ortodoncia', brand:'borgatta', name:'Alambre Black Acero Inoxidable .030 Redondo — 20 pzas',
   unit:'caja 20 pzas', img:'imagenes/borgatta/pag_38.jpg',
   desc:'Acero inoxidable altamente resistente a la corrosión. Empaques para maximizar aprovechamiento.',
   specs:['Calibre: .030 redondo','20 piezas por caja','Disponible desde .016 a .040 y rectangulares','Línea Black']},

  {id:'bor-045', code:'80-01-020', cat:'ortodoncia', brand:'borgatta', name:'Alambre iLine Acero Inoxidable .020 Redondo — en Tubo 20 pzas',
   unit:'tubo 20 pzas', img:'imagenes/borgatta/pag_38.jpg',
   desc:'Acero inoxidable de alta rigidez y pulido. En tubo de 20 piezas. Línea iLine.',
   specs:['Calibre: .020 redondo','20 piezas en tubo','Disponible desde .012 a .040 y rectangulares','Línea iLine']},

  {id:'bor-046', code:'200-100', cat:'ortodoncia', brand:'borgatta', name:'Alambre Wipla Media Caña Duro Elástico — 1.30 x 0.65 mm',
   unit:'paquete 20 pzas', img:'imagenes/borgatta/pag_38.jpg',
   desc:'Alambre de acero duro-elástico para confección de aparatos intraorales. Alta resistencia a la corrosión.',
   specs:['Medida: 1.30 x 0.65 mm','20 piezas','También en 1.50x0.75mm (200-101) y 1.75x0.90mm (200-102)']},

  {id:'bor-047', code:'300-509', cat:'instrumental', brand:'borgatta', name:'Torre Azul Formadora de Arcos Borgatta',
   unit:'pieza', img:'imagenes/borgatta/pag_38.jpg',
   desc:'Instrumento ligero y durable, calibrado para crear arcos en cinco calibres: .016, .017, .018, .019 y .021.',
   specs:['5 calibres: .016, .017, .018, .019, .021','Material ligero y durable','Mantiene forma sin deformar el alambre']},

  // --- ARCOS NiTi ---
  {id:'bor-048', code:'02-511-11', cat:'ortodoncia', brand:'borgatta', name:'Arcos Impulse NiTi .014 Redondo Superior — 10 pzas',
   unit:'caja 10 pzas', img:'imagenes/borgatta/pag_41.jpg',
   desc:'Arcos NiTi termoactivos que transmiten fuerzas gentiles e ininterrumpidas, cuidan el periodonto. Activos por temperatura oral.',
   specs:['Calibre: .014 redondo','10 piezas','Superior o Inferior disponible','Línea Black']},

  {id:'bor-049', code:'02-523-11', cat:'ortodoncia', brand:'borgatta', name:'Arcos Neo-Impulse NiTi .016x.016 Superior — 10 pzas',
   unit:'caja 10 pzas', img:'imagenes/borgatta/pag_41.jpg',
   desc:'NiTi calibrado para fuerzas ligeras y constantes. Ideales en etapas tempranas del tratamiento y fases intermedias. Línea Black.',
   specs:['Calibre: .016x.016','10 piezas','Superior e Inferior disponible','Línea Black']},

  {id:'bor-050', code:'02-528-01', cat:'ortodoncia', brand:'borgatta', name:'Arcos Bio-Impulse NiTi .016x.016 Superior — 10 pzas',
   unit:'caja 10 pzas', img:'imagenes/borgatta/pag_41.jpg',
   desc:'Arco programado con 3 fuerzas diferentes en el mismo: ligero para anteriores, media para premolares y fuerte para molares.',
   specs:['Calibre: .016x.016','3 zonas de fuerza programadas','10 piezas','Línea Black']},

  {id:'bor-051', code:'B0016-01-D', cat:'ortodoncia', brand:'borgatta', name:'Arcos NiTi Estéticos .016 Redondo Superior — 10 pzas',
   unit:'caja 10 pzas', img:'imagenes/borgatta/pag_41.jpg',
   desc:'Arcos de NiTi súper elásticos con cobertura de pintura epóxica color diente, para combinar con brackets cerámicos o zafiro.',
   specs:['Calibre: .016 redondo','Color diente','10 piezas','Disponible en .014, .016x.016, .016x.022']},

  // --- RESORTES ---
  {id:'bor-052', code:'300-575', cat:'ortodoncia', brand:'borgatta', name:'Rollo Resorte Cerrado Acero Inoxidable — c/1m',
   unit:'rollo 1 metro', img:'imagenes/borgatta/pag_44.jpg',
   desc:'Acero inoxidable calibrado para fuerzas constantes que cuidan al paciente. Empaque que reduce el desperdicio.',
   specs:['Longitud: 1 metro','Tipo: Cerrado','También abierto (300-576)']},

  {id:'bor-053', code:'10-000-01', cat:'ortodoncia', brand:'borgatta', name:'Resortes Impulse NiTi Cerrados .010x.035 200g — 10 pzas',
   unit:'caja 10 pzas', img:'imagenes/borgatta/pag_44.jpg',
   desc:'Resortes NiTi activados con temperatura oral. Mantienen forma sin variar la fuerza, garantizando desplazamiento molar continuo.',
   specs:['Calibre: .010x.035','Fuerza: 200g','Tipo: Cerrado c/ojal','10 piezas','Línea Black']},

  {id:'bor-054', code:'200-096', cat:'ortodoncia', brand:'borgatta', name:'Resorte Cerrado de NiTi 6mm — Ojal de acero',
   unit:'pieza', img:'imagenes/borgatta/pag_44.jpg',
   desc:'Fabricados con NiTi, gran desempeño y practicidad, ojales de acero. Disponible en 4 diámetros: 6, 9, 12 y 15mm.',
   specs:['Diámetro: 6mm','NiTi con ojal de acero','También 9mm (200-097), 12mm (200-098), 15mm (200-099)']},

  // --- CADENA ELÁSTICA ---
  {id:'bor-055', code:'300-026', cat:'ortodoncia', brand:'borgatta', name:'Cadena Elástica Cerrada — 2.3m (13 colores)',
   unit:'rollo 2.3m', img:'imagenes/borgatta/pag_47.jpg',
   desc:'Empaque especial para evitar desperdicios. Fabricada en neopreno. Disponible cerrada, media y abierta en 13 colores.',
   specs:['Longitud: 2.3m','Tipo: Cerrada','13 colores: Rojo, Plata, Azul, Verde Neón, Blanco, Amarillo, Rosa, Morado, Naranja, Negra, Aqua, Gris, Transparente','También media y abierta']},

  {id:'bor-056', code:'300-567', cat:'ortodoncia', brand:'borgatta', name:'Cuñas de Rotación Borgatta Transparente — 100 pzas',
   unit:'caja 100 pzas', img:'imagenes/borgatta/pag_47.jpg',
   desc:'Cuñas de rotación 100 piezas.',
   specs:['Color: Transparente','100 piezas','También disponible gris (300-568)']},

  // --- ELÁSTICOS INTRAORALES ---
  {id:'bor-057', code:'350-104', cat:'ortodoncia', brand:'borgatta', name:'Elásticos Intraorales Borgatta Látex 1/8" Mediano — 100 pzas',
   unit:'bolsa 100 pzas', img:'imagenes/borgatta/pag_49.jpg',
   desc:'Elásticos intraorales de látex. Disponibles en tamaños 1/8" a 3/8" y fuerzas Ligera, Media y Pesada.',
   specs:['Diámetro: 1/8" (3mm)','Fuerza: Media 4.5oz','100 piezas','Serie Wildlife: Wallaby(ligero), Lobo(medio), Elefante(pesado)','1/8"-3/16"-1/4"-5/16"-3/8"']},

  {id:'bor-058', code:'500-005-20', cat:'ortodoncia', brand:'borgatta', name:'Módulos Elásticos en S Surtido Classic — 5 tiras 100 pzas',
   unit:'5 tiras 100 pzas c/u', img:'imagenes/borgatta/pag_49.jpg',
   desc:'Módulos elásticos con gran resistencia a la fatiga, amplia variedad de estilos y colores, en presentación S (5 tiras con 100 piezas).',
   specs:['Presentación S: 5 tiras x 100 pzas','Colores: Transparente, Plata, Negro, Surtido Classic/Full/Fluorescente/Glow']},

  // --- PINZAS E INSTRUMENTOS ---
  {id:'bor-059', code:'BOR-1010-NH', cat:'instrumental', brand:'borgatta', name:'Pinza Corte Distal Sin Seguro — Línea Black',
   unit:'pieza', img:'imagenes/borgatta/pag_56.jpg',
   desc:'Pinza de corte filo diamante para alambre duro redondo hasta .020", rectangular hasta .018"x.025" y trenzado hasta .0175".',
   specs:['Capacidad redondo: hasta .020"','Capacidad rectangular: hasta .018"x.025"','Sin seguro','Línea Black']},

  {id:'bor-060', code:'BOR-1016', cat:'instrumental', brand:'borgatta', name:'Pinza Corte Distal Con Seguro — Línea Black',
   unit:'pieza', img:'imagenes/borgatta/pag_56.jpg',
   desc:'Pinza de corte filo diamante con seguro, para alambre duro redondo hasta .020" y trenzado hasta .0175".',
   specs:['Capacidad redondo: hasta .020"','Con seguro','Línea Black']},

  {id:'bor-061', code:'BOR-1000', cat:'instrumental', brand:'borgatta', name:'Pinza Corte de Ligadura Fino — Línea Black',
   unit:'pieza', img:'imagenes/borgatta/pag_56.jpg',
   desc:'Corta alambre flexible redondo hasta .015", angulada 15° para una mejor visión.',
   specs:['Capacidad: hasta .015" redondo','Angulada 15°','Línea Black']},

  {id:'bor-062', code:'BOR-1000-HWC', cat:'instrumental', brand:'borgatta', name:'Pinza Corte de Ligadura Cromada',
   unit:'pieza', img:'imagenes/borgatta/pag_56.jpg',
   desc:'Acero inoxidable con recubierta de cromo, corte diamante, angulada 15° para alambre blando hasta .020" de diámetro.',
   specs:['Recubrimiento: Cromo','Corte diamante','Angulada 15°','Capacidad: hasta .020"']},

  {id:'bor-063', code:'BOR-352', cat:'instrumental', brand:'borgatta', name:'Pinza Tweed para Hacer Omegas',
   unit:'pieza', img:'imagenes/borgatta/pag_58.jpg',
   desc:'Punta cóncava contorneada para ansas omega más uniformes. Con tres secciones .045", .060" y .075" de diámetro y .090" de longitud.',
   specs:['Uso: hacer omegas','3 secciones: .045", .060", .075"','Micrograbado antideslizante','Línea Black']},

  {id:'bor-064', code:'BOR-810-S', cat:'instrumental', brand:'borgatta', name:'Pinza Tweed para Arcos Rectangulares — Punta Corta',
   unit:'pieza', img:'imagenes/borgatta/pag_58.jpg',
   desc:'Para manejar alambre cuadrado o rectangular. Puntas un poco más cortas que la versión estándar.',
   specs:['Uso: arcos rectangulares','Puntas cortas','Para alambre cuadrado/rectangular','Línea Black']},

  {id:'bor-065', code:'BOR-805-N2', cat:'instrumental', brand:'borgatta', name:'Pinza para Torque Angosta con Llave 18/22',
   unit:'pieza', img:'imagenes/borgatta/pag_58.jpg',
   desc:'Pinza para torque angosta con llave, para slot .018 y .022.',
   specs:['Tipo: Angosta','Llave 18/22','Línea Black']},

  {id:'bor-066', code:'BOR-805-W2', cat:'instrumental', brand:'borgatta', name:'Pinza para Torque Ancha con Llave 18/22',
   unit:'pieza', img:'imagenes/borgatta/pag_58.jpg',
   desc:'Pinza para torque ancha con llave, para slot .018 y .022.',
   specs:['Tipo: Ancha','Llave 18/22','Línea Black']},

  {id:'bor-067', code:'BOR-507', cat:'instrumental', brand:'borgatta', name:'Director de Ligadura — Línea Black',
   unit:'pieza', img:'imagenes/borgatta/pag_60.jpg',
   desc:'Extremo bifurcado para asentamiento óptimo del arco en el slot y extremo cuadrado dentado para ajustar ligaduras. Acero inoxidable.',
   specs:['2 extremos funcionales','Acero inoxidable','Línea Black']},

  {id:'bor-068', code:'300-660', cat:'instrumental', brand:'borgatta', name:'Instrumento para Ligadura Elástica — Autoclavable',
   unit:'pieza', img:'imagenes/borgatta/pag_60.jpg',
   desc:'Facilita el manejo de módulos elásticos, su forma permite estirarlos sin romperlos o vencer su resistencia. Autoclavable.',
   specs:['Autoclavable','Para módulos elásticos']},

  {id:'bor-069', code:'BOR-503', cat:'instrumental', brand:'borgatta', name:'Dinamómetro Dontrix 16 oz — Línea Black',
   unit:'pieza', img:'imagenes/borgatta/pag_60.jpg',
   desc:'Dinamómetro de presión graduado hasta 16oz (453gr), para la medición de la fuerza en elásticos y resortes.',
   specs:['Capacidad: 16 oz (453 g)','Escala graduada','Línea Black']},

  {id:'bor-070', code:'300-594', cat:'instrumental', brand:'borgatta', name:'Dinamómetro Borgatta 100-1600g',
   unit:'pieza', img:'imagenes/borgatta/pag_60.jpg',
   desc:'Calibrado para medición eficiente de fuerza de elásticos y resortes. Extremos adaptables a cualquier ojal, cuerpo de aluminio.',
   specs:['Escala: 100-1600g','Cuerpo aluminio','Extremos adaptables a ojales']},

  // --- POSICIONADORES Y ACCESORIOS ---
  {id:'bor-071', code:'0-000-500', cat:'instrumental', brand:'borgatta', name:'Posicionador de Altura Estrella 1 — 2.0 a 3.5mm',
   unit:'pieza', img:'imagenes/borgatta/pag_62.jpg',
   desc:'Auxiliar para localizar el lugar ideal de colocación del bracket. Calibrado de 2.0 a 3.5mm.',
   specs:['Calibres: 2.0, 2.5, 3.0, 3.5 mm','También Estrella 2: 3.5-5.0mm (0-000-600)']},

  {id:'bor-072', code:'300-500', cat:'instrumental', brand:'borgatta', name:'Posicionador Alexander — 3.5 a 5.0mm',
   unit:'pieza', img:'imagenes/borgatta/pag_62.jpg',
   desc:'Auxiliar para la óptima colocación del bracket en cualquier técnica. Calibrado de 3.5 a 5.0mm.',
   specs:['Calibres: 3.5-5.0mm','También 2.5-6.0mm (300-500-1)']},

  {id:'bor-073', code:'0-000-400', cat:'instrumental', brand:'borgatta', name:'Pinza Porta Brackets con Coleta Borgatta',
   unit:'pieza', img:'imagenes/borgatta/pag_62.jpg',
   desc:'Diseñada para la cómoda colocación de cualquier bracket, mantiene el bracket en la pinza hasta que es presionado.',
   specs:['Con coleta para pequeñas correcciones','Para cualquier bracket']},

  {id:'bor-074', code:'0-001-450', cat:'instrumental', brand:'borgatta', name:'Caballete de Acrílico Grande 24 cm',
   unit:'pieza', img:'imagenes/borgatta/pag_62.jpg',
   desc:'Construcción de acrílico translúcido de 1cm de espesor. Puede albergar de 6 a 11 instrumentos Invecta.',
   specs:['Longitud: 24 cm','Capacidad: hasta 11 instrumentos','También chico 15 cm (0-001-451)','Material: acrílico translúcido 1cm']},

  // --- ORTOPEDIA ---
  {id:'bor-075', code:'130-H', cat:'ortodoncia', brand:'borgatta', name:'High Pull con Mentonera',
   unit:'pieza', img:'imagenes/borgatta/pag_66.jpg',
   desc:'Cintas de poliéster y resortes resistentes para el control del crecimiento mandibular. Incluye 2 resortes ligeros ajustables, mentonera suave chica y headgear de poliéster.',
   specs:['Cintas de poliéster','2 resortes ajustables','Incluye mentonera suave chica y headgear']},

  {id:'bor-076', code:'500-034', cat:'ortodoncia', brand:'borgatta', name:'High Pull Cervical con Módulo de Seguridad — Azul',
   unit:'pieza', img:'imagenes/borgatta/pag_66.jpg',
   desc:'Materiales 100% lavables e hipo-alergénicos. Módulos de seguridad incluidos. Para control horizontal de maxila. Compatibles con arcos extraorales.',
   specs:['100% lavable','Módulo de seguridad incluido','Compatible con arcos extraorales','Colores: Azul, Rosa, Mezclilla']},

  {id:'bor-077', code:'500-032', cat:'ortodoncia', brand:'borgatta', name:'Almohadilla Cervical con Módulo de Seguridad — Azul',
   unit:'pieza', img:'imagenes/borgatta/pag_66.jpg',
   desc:'Para tracción cervical completamente eficaz. Módulos de seguridad y relleno hipo-alérgénico. 100% lavable.',
   specs:['100% lavable','Hipo-alergénico','Módulo de seguridad','Colores: Azul, Rosa, Mezclilla']},

  {id:'bor-078', code:'21-A', cat:'ortodoncia', brand:'borgatta', name:'Mentonera Suave Mediana Borgatta',
   unit:'pieza', img:'imagenes/borgatta/pag_66.jpg',
   desc:'Material de gran confort y resistencia. Desempeño óptimo con headgear para tracciones mandibulares.',
   specs:['Talla: Mediana','También grande (21-B)']},

  {id:'bor-079', code:'500-011', cat:'ortodoncia', brand:'borgatta', name:'Arco Extraoral Chico Sin Omega Borgatta',
   unit:'pieza', img:'imagenes/borgatta/pag_66.jpg',
   desc:'Unión reforzada con clip de acero inoxidable y construcción de alta resistencia. Incluye funda para el arco.',
   specs:['Talla: Chico','Sin omega','Incluye funda','También mediano (500-012)']},

  {id:'bor-080', code:'800-1', cat:'ortodoncia', brand:'borgatta', name:'Acrílico Autocurable A*B Amarillo — 25g',
   unit:'frasco 25g', img:'imagenes/borgatta/pag_70.jpg',
   desc:'Gran variedad de colores para crear aparatos removibles. Moléculas de cadena cruzada para resistencia óptima.',
   specs:['Peso: 25g','Color: Amarillo','Disponible en: Azul marino, Naranja, Transparente, Verde limón, Verde, Rosa, Fucsia, Violeta','Líquido 125ml (800-20)']},

  {id:'bor-081', code:'0-001-442', cat:'ortodoncia', brand:'borgatta', name:'Caja Grande Ortodóntica Pastel Colors — 10 pzas',
   unit:'caja 10 pzas', img:'imagenes/borgatta/pag_70.jpg',
   desc:'Cajas ortodónticas Borgatta para guardar aparatos bucales removibles. Tapas y cajas intercambiables.',
   specs:['10 piezas','Colección Pastel Colors','También: Neón, Viva Colors, Temporada 1/2, Classic Colors chica']},

  {id:'bor-082', code:'0-000-111', cat:'equipos', brand:'borgatta', name:'Soplete Tipo Microtorch Borgatta',
   unit:'pieza', img:'imagenes/borgatta/pag_70.jpg',
   desc:'Gran herramienta en el soldado de aparatos de ortopedia o práctica general. Portátil, versátil, confiable y recargable. Llama hasta 1,300°C.',
   specs:['Temperatura: hasta 1,300°C','Portátil y recargable','También Eco (0-000-222): butano recargable']},

  // --- HIGIENE Y PROTECCIÓN ---
  {id:'bor-083', code:'300-808', cat:'desechables', brand:'borgatta', name:'Cepillo Dental NATBÚ ORTHO — Bambu c/carbón',
   unit:'pieza', img:'imagenes/borgatta/pag_75.jpg',
   desc:'Cepillo de bambú súper ligero. Cerdas con carbón activado para mayor sensación de limpieza. Corte en V para limpieza profunda.',
   specs:['Mango: Madera de bambú','Cerdas: Carbón activado','Corte en V','90% materiales amigables con el medio ambiente','Incluye cepillo interdental']},

  {id:'bor-084', code:'300-810', cat:'desechables', brand:'borgatta', name:'Cepillo Dental NATBÚ SENSITIVE — Bambu ultra-suave',
   unit:'pieza', img:'imagenes/borgatta/pag_75.jpg',
   desc:'Cerdas ultra-suaves que protegen dientes y encías. Mango ergonómico. Pensado para quienes sufren sensibilidad.',
   specs:['Mango: Bambú','Cerdas ultra-suaves','Para sensibilidad dental','90% materiales eco-amigables']},

  {id:'bor-085', code:'300-809', cat:'desechables', brand:'borgatta', name:'Cepillo Dental NATBÚ CARBÓN — Bambu',
   unit:'pieza', img:'imagenes/borgatta/pag_75.jpg',
   desc:'Cerdas con carbón activado para mayor limpieza y absorción del mal olor. Cambiar cada 2 meses máximo.',
   specs:['Mango: Bambú','Cerdas: Carbón activado','Absorbe mal olor','Eco-friendly']},

  {id:'bor-086', code:'GC4DBL', cat:'desechables', brand:'borgatta', name:'Cubrebocas Nivel IV Azul — caja 50 pzas',
   unit:'caja 50 pzas', img:'imagenes/borgatta/pag_90.jpg',
   desc:'Mascaras de protección nivel IV con alta eficacia contra micro-partículas. 4 capas, papel facial hipoalergénico, barra aluminio ajuste nasal.',
   specs:['Nivel IV','4 capas','Papel facial hipoalergénico','Barra de aluminio nasal','Colores: Violeta, Rosa mexicano, Azul, Negro, Menta, Ciruela']},

  {id:'bor-087', code:'VCECAZ', cat:'desechables', brand:'borgatta', name:'Set de Protección Borgatta 400 pzas — Azul',
   unit:'set 400 pzas', img:'imagenes/borgatta/pag_90.jpg',
   desc:'Combine y modernice su consultorio con el nuevo set de mascaras, campos, eyectores y vasos plásticos.',
   specs:['400 piezas','Colores: Azul, Ciruela, Violeta, Negro, Rosa mexicano, Verde menta','Dispensador disponible por separado (0-001-455)']},

  {id:'bor-088', code:'BEBC', cat:'desechables', brand:'borgatta', name:'Eyectores Borgatta Desechables Azul — 100 pzas',
   unit:'caja 100 pzas', img:'imagenes/borgatta/pag_90.jpg',
   desc:'Irrompibles, PVC libre de látex y ftalatos, puntas no removibles. Mantiene forma. Disponible en múltiples colores.',
   specs:['Material: PVC','Libre de látex y ftalatos','100 piezas','Múltiples colores disponibles']},

  {id:'bor-089', code:'VPBL', cat:'desechables', brand:'borgatta', name:'Vasos Plásticos Borgatta Azul — 1000 pzas',
   unit:'caja 1000 pzas', img:'imagenes/borgatta/pag_90.jpg',
   desc:'Vasitos plásticos diseñados para mayor resistencia y óptimo manejo de almacenamiento. Disponibles en múltiples colores.',
   specs:['1000 piezas (o 50 piezas -B)','Colores: Surtidos, Amarillo, Verde bosque, Naranja, Azul, Ciruela, Rosa mexicano, Negro, Verde menta, Verde limón, Violeta, Rojo']},

  // --- PIEZAS DE MANO ---
  {id:'bor-090', code:'0-001-001', cat:'equipos', brand:'borgatta', name:'Pieza de Mano Alta Velocidad Turbinetta Plus P-II',
   unit:'pieza', img:'imagenes/borgatta/pag_95.jpg',
   desc:'Cabezal estándar, cuerpo de latón cromado, diseño clásico de alta durabilidad y desempeño. Entrada de dos vías. Incluye botafresas, llave y lubricante.',
   specs:['Cabezal: Estándar','Cuerpo: Latón cromado','Entrada: 2 vías','Semisilencios estándar','Incluye: botafresas, llave y lubricante']},

  {id:'bor-091', code:'0-000-006', cat:'equipos', brand:'borgatta', name:'Pieza de Mano Alta Velocidad Turbinetta Plus P-III Mini',
   unit:'pieza', img:'imagenes/borgatta/pag_95.jpg',
   desc:'Cabezal mini, cómodo manejo, cuerpo antiderrapante. Entrada de dos vías. Incluye botafresas, llave y lubricante.',
   specs:['Cabezal: Mini','Cuerpo antiderrapante','Entrada: 2 vías','Semisilencios mini']},

  {id:'bor-092', code:'0-000-705', cat:'equipos', brand:'borgatta', name:'Pieza de Mano Alta Velocidad Borgatta Lite',
   unit:'pieza', img:'imagenes/borgatta/pag_95.jpg',
   desc:'Turbina sencilla pero poderosa, cabezal estándar. Cuerpo de acero inoxidable. Entrada de dos vías.',
   specs:['Cabezal: Estándar','Cuerpo: Acero inoxidable','Entrada: 2 vías']},

  {id:'bor-093', code:'0-000-708', cat:'equipos', brand:'borgatta', name:'Pieza de Mano Alta Velocidad Borgatta Stella Lux — LED',
   unit:'pieza', img:'imagenes/borgatta/pag_95.jpg',
   desc:'Iluminación LED autogenerada y cambio de fresas por push-button. Entrada de dos vías. Incluye botafresas, llave y lubricante.',
   specs:['Iluminación: LED autogenerada','Cambio de fresas: Push-button','Entrada: 2 vías','Incluye: botafresas, llave y lubricante']},
"""

# Filter out existing ids
entries = re.findall(r"\{id:'[^']+'.+?\}", new_products, re.DOTALL)
block = ""
added = 0
for entry in entries:
    m = re.search(r"id:'([^']+)'", entry)
    if m and m.group(1) not in existing_ids:
        block += "  " + entry.strip() + ",\n"
        added += 1

print(f"Borgatta productos nuevos a agregar: {added}")

idx = content.rfind('];')
content = content[:idx].rstrip() + '\n' + block.rstrip(',') + '\n];\n'

total = len(re.findall(r"id:'[a-zA-Z0-9_-]+'", content))
print(f"Total productos: {total}")

with open(r'C:\Catalago Prodent\website\js\products-data.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("GUARDADO")
