// ===== PRODENT SUPPLY — PRODUCT DATABASE =====
// Extracted from official supplier catalogs
// Categories: desechables, fresas, ortodoncia, instrumental, primadent, otros

const CATALOG_PRODUCTS = [

  // ══════════════════════════════════════════
  // DESECHABLES  (Ortho Premium · 48 productos)
  // ══════════════════════════════════════════
  { id:'AI001SF', code:'AI001SF', cat:'desechables', brand:'orthopremium', name:'Micro Aplicador Super Fino',
    unit:'caja 100 pz', img:'imagenes/products/AI001SF.jpg',
    desc:'Aplicador desechable de punta super fina para material fluido de alta precisión.',
    specs:['Punta: Super fina','Uso: Adhesivos, bonding, selladores fluidos','Colores identificadores incluidos','Desechable, uso único'] },

  { id:'AI001F', code:'AI001F', cat:'desechables', brand:'orthopremium', name:'Micro Aplicador Fino',
    unit:'caja 100 pz', img:'imagenes/products/AI001F.jpg',
    desc:'Micro aplicador de punta fina para materiales de baja y media viscosidad.',
    specs:['Punta: Fina','Uso: Adhesivos, agentes de unión','Desechable, uso único'] },

  { id:'AI001R', code:'AI001R', cat:'desechables', brand:'orthopremium', name:'Micro Aplicador Regular',
    unit:'caja 100 pz', img:'imagenes/products/AI001R.jpg',
    desc:'Micro aplicador de punta regular para materiales de viscosidad media a alta.',
    specs:['Punta: Regular','Uso: Resinas, materiales restauradores','Desechable, uso único'] },

  { id:'AI002', code:'AI002', cat:'desechables', brand:'orthopremium', name:'Micro Cepillo',
    unit:'caja 100 pz', img:'imagenes/products/AI002.jpg',
    desc:'Micro cepillo desechable de fibras suaves para aplicación precisa de materiales.',
    specs:['Cabeza: Fibras suaves','Uso: Materiales de consistencia cremosa','Desechable, uso único'] },

  { id:'AI003', code:'AI003', cat:'desechables', brand:'orthopremium', name:'Cucharilla de Impresión Verde',
    unit:'paquete 10 pz', img:'imagenes/products/AI003.jpg',
    desc:'Cucharilla desechable de color verde para toma de impresiones dentales.',
    specs:['Color: Verde','Material: Plástico resistente','Compatible con alginato y siliconas','Desechable, uso único'] },

  { id:'AI004', code:'AI004', cat:'desechables', brand:'orthopremium', name:'Barrera Protectora Azul',
    unit:'1 200 hojas', img:'imagenes/products/AI004.jpg',
    desc:'Rollo de barrera protectora para superficies clínicas. Protege contra contaminación cruzada.',
    specs:['Color: Azul','Material: Polietileno','Uso: Protección de equipos y superficies','Corte fácil'] },

  { id:'AI007', code:'AI007', cat:'instrumental', brand:'orthopremium', name:'Dispensador de Barrera Protectora',
    unit:'pieza', img:'imagenes/products/AI007.jpg',
    desc:'Dispensador de pared para rollos de barrera protectora. Instalación fácil, color blanco.',
    specs:['Color: Blanco','Material: Plástico ABS de alta resistencia','Compatible con rollo AI004','Instalación mural'] },

  { id:'AI008', code:'AI008', cat:'desechables', brand:'orthopremium', name:'Cepillo Profiláctico',
    unit:'paquete 100 pz', img:'imagenes/products/AI008.jpg',
    desc:'Cepillo profiláctico desechable tipo copa plana para pulido y limpieza dental.',
    specs:['Tipo: Copa plana','Uso: Profilaxis y pulido dental','Compatible con contrángulo estándar','Desechable, uso único'] },

  { id:'AI009', code:'AI009', cat:'desechables', brand:'orthopremium', name:'Copa Profiláctica',
    unit:'paquete 100 pz', img:'imagenes/products/AI009.jpg',
    desc:'Copa profiláctica de caucho natural para pulido dental. Máxima adaptación a la superficie.',
    specs:['Material: Caucho natural','Uso: Pulido y profilaxis','Compatible con contrángulo estándar','Desechable, uso único'] },

  { id:'AI010', code:'AI010', cat:'desechables', brand:'orthopremium', name:'Godete de Plástico (varias medidas)',
    unit:'pieza', img:'imagenes/products/AI010.jpg',
    desc:'Godete desechable de plástico para mezcla de materiales dentales. Disponible en 3, 5 y 6 cm.',
    specs:['Medidas: 3 cm, 5 cm, 6 cm','Material: Plástico','Uso: Mezcla de cementos y materiales'] },

  { id:'AI011', code:'AI011', cat:'instrumental', brand:'orthopremium', name:'Pistola Dosificadora de Cartuchos 1:1',
    unit:'pieza', img:'imagenes/products/AI011.jpg',
    desc:'Pistola para cartuchos de impresión en proporción 1:1. Dosificación uniforme y controlada.',
    specs:['Proporción: 1:1','Uso: Silicones A, poliéter y materiales de impresión','Compatible con cartuchos estándar 1:1','Alta resistencia y durabilidad'] },

  { id:'AI012', code:'AI012', cat:'instrumental', brand:'orthopremium', name:'Pistola Dosificadora de Cartuchos 10:1',
    unit:'pieza', img:'imagenes/products/AI012.jpg',
    desc:'Pistola para cartuchos en proporción 10:1. Ideal para adhesivos y selladores de dos componentes.',
    specs:['Proporción: 10:1','Uso: Adhesivos, selladores bicomponente','Compatible con cartuchos estándar 10:1'] },

  { id:'AI013', code:'AI013', cat:'desechables', brand:'orthopremium', name:'Puntas Mezcladoras Amarillas 70×14mm',
    unit:'50 pz', img:'imagenes/products/AI013.jpg',
    desc:'Puntas mezcladoras amarillas 70×14mm para cartuchos 1:1. Mezcla homogénea sin burbujas.',
    specs:['Color: Amarillo','Dimensiones: 70×14 mm','Proporción: 1:1','Mezcla estática de alta eficiencia'] },

  { id:'AI014', code:'AI014', cat:'desechables', brand:'orthopremium', name:'Punta Intra Oral Amarilla Ø0.5mm',
    unit:'100 pz', img:'imagenes/products/AI014.jpg',
    desc:'Punta intra oral amarilla de diámetro 0.5 mm para aplicación intraoral ultra precisa.',
    specs:['Color: Amarillo','Diámetro: 0.5 mm','Uso: Aplicación en zonas de difícil acceso'] },

  { id:'AI015', code:'AI015', cat:'desechables', brand:'orthopremium', name:'Punta Mezcladora Naranja',
    unit:'50 pz', img:'imagenes/products/AI015.jpg',
    desc:'Punta mezcladora naranja para materiales de alta viscosidad.',
    specs:['Color: Naranja','Uso: Materiales de alta viscosidad'] },

  { id:'AI016', code:'AI016', cat:'desechables', brand:'orthopremium', name:'Punta Mezcladora Azul',
    unit:'50 pz', img:'imagenes/products/AI016.jpg',
    desc:'Punta mezcladora azul para silicona de adición y poliéter.',
    specs:['Color: Azul','Uso: Silicona de adición y poliéter'] },

  { id:'AI017', code:'AI017', cat:'desechables', brand:'orthopremium', name:'Punta Mezcladora Café 40×100mm 1:1',
    unit:'50 pz', img:'imagenes/products/AI017.jpg',
    desc:'Punta mezcladora café 40×100mm para cartuchos 1:1 de gran volumen.',
    specs:['Color: Café','Dimensiones: 40×100 mm','Proporción: 1:1',] },

  { id:'AI018', code:'AI018', cat:'desechables', brand:'orthopremium', name:'Punta Mezcladora Café 37×10mm 1:1',
    unit:'100 pz', img:'imagenes/products/AI018.jpg',
    desc:'Punta mezcladora café compacta 37×10mm para cartuchos 1:1.',
    specs:['Color: Café','Dimensiones: 37×10 mm','Proporción: 1:1',] },

  { id:'AI019', code:'AI019', cat:'desechables', brand:'orthopremium', name:'Punta Intra Oral Transparente Ø1mm',
    unit:'100 pz', img:'imagenes/products/AI019.jpg',
    desc:'Punta intra oral transparente diámetro 1 mm para aplicación con máxima visibilidad.',
    specs:['Diámetro: 1 mm','Color: Transparente','Uso: Aplicación intraoral con visibilidad total'] },

  { id:'AI020', code:'AI020', cat:'desechables', brand:'orthopremium', name:'Punta Intra Oral Transparente Ø0.5mm',
    unit:'100 pz', img:'imagenes/products/AI020.jpg',
    desc:'Punta intra oral transparente de diámetro 0.5 mm para aplicación ultra fina.',
    specs:['Diámetro: 0.5 mm','Color: Transparente',] },

  { id:'AI021', code:'AI021', cat:'desechables', brand:'orthopremium', name:'Clip de Babero Dental 39.7cm',
    unit:'pieza', img:'imagenes/products/AI021.jpg',
    desc:'Clip de cadena metálica con puntas de plástico para sujetar baberos dentales. 39.7 cm.',
    specs:['Longitud: 39.7 cm','Material: Metal con punta plástica','Uso: Sujeción de baberos','Fácil ajuste'] },

  { id:'AI022', code:'AI022', cat:'instrumental', brand:'orthopremium', name:'Espejo Forma Muela 24.6×13.4cm',
    unit:'pieza', img:'imagenes/products/AI022.jpg',
    desc:'Espejo reflectante con forma de muela para fotopolimerización de superficies posteriores.',
    specs:['Dimensiones: 24.6×13.4×0.5 cm','Forma: Muela dental','Uso: Fotopolimerización de caras linguales y distales'] },

  { id:'AI023', code:'AI023', cat:'instrumental', brand:'orthopremium', name:'Lente Naranja Protección UV',
    unit:'pieza', img:'imagenes/products/AI023.jpg',
    desc:'Lente de protección naranja contra radiación UV para el operador durante fotopolimerización.',
    specs:['Color: Naranja','Protección: Rayos UV / luz azul','Uso: Durante fotopolimerización','Montura ligera y ergonómica'] },

  { id:'AI024', code:'AI024', cat:'desechables', brand:'orthopremium', name:'Caja de Babero Dental C/500pz',
    unit:'caja 500 pz', img:'imagenes/products/AI024.jpg',
    desc:'Caja de baberos dentales desechables de papel plastificado absorbente. 500 pzas.',
    specs:['Material: Papel plastificado + polietileno','Colores: Blanco, celeste, rosa','Desechable, uso único'] },

  { id:'AI024NE', code:'AI024NE', cat:'desechables', brand:'orthopremium', name:'Caja de Babero Dental Negro C/500pz',
    unit:'caja 500 pz', img:'imagenes/products/AI024NE.jpg',
    desc:'Baberos negros desechables. Estéticos y discretos, ideales para clínicas de fotografía dental.',
    specs:['Color: Negro','Material: Papel plastificado','Estético — ideal para fotografía dental','Desechable, uso único'] },

  { id:'AI025', code:'AI025', cat:'instrumental', brand:'orthopremium', name:'Caja Aluminio p/Fresas y Limas 72 cav.',
    unit:'pieza', img:'imagenes/products/AI025.jpg',
    desc:'Caja de aluminio anodizado con 72 cavidades para organizar y esterilizar fresas y limas. Modelo Z003.',
    specs:['Material: Aluminio anodizado','Cavidades: 72','Modelo: Z003','Autoclavable','Uso: Fresas y limas endodónticas'] },

  { id:'AI026', code:'AI026', cat:'instrumental', brand:'orthopremium', name:'Caja Aluminio p/Limas 72 cav.',
    unit:'pieza', img:'imagenes/products/AI026.jpg',
    desc:'Caja de aluminio de 72 cavidades exclusiva para limas endodónticas. Modelo Z004.',
    specs:['Material: Aluminio anodizado','Cavidades: 72','Modelo: Z004','Autoclavable','Uso: Organización y esterilización de limas'] },

  { id:'AI027', code:'AI027', cat:'instrumental', brand:'orthopremium', name:'Caja Aluminio p/Fresas 30 cav. Base Hueca',
    unit:'pieza', img:'imagenes/products/AI027.jpg',
    desc:'Caja de aluminio base hueca (ventilada) para 30 fresas. Permite circulación de vapor en autoclave.',
    specs:['Material: Aluminio','Cavidades: 30','Base: Hueca/ventilada','Autoclavable','Para fresas de alta velocidad'] },

  { id:'AI028', code:'AI028', cat:'instrumental', brand:'orthopremium', name:'Caja Aluminio p/Fresas 30 cav. Base Sólida',
    unit:'pieza', img:'imagenes/products/AI028.jpg',
    desc:'Caja de aluminio base sólida para 30 fresas. Almacenamiento y esterilización segura.',
    specs:['Material: Aluminio','Cavidades: 30','Base: Sólida','Autoclavable','Para fresas de alta velocidad'] },

  { id:'AI029', code:'AI029', cat:'instrumental', brand:'orthopremium', name:'Caja Sombreado Mezclador p/Resina',
    unit:'pieza', img:'imagenes/products/AI029.jpg',
    desc:'Caja de sombreado con mezclador para selección y comparación de tonos de resina compuesta.',
    specs:['Color: Naranja','Uso: Selección y mezcla de tonos de resina','Desechable'] },

  { id:'AI030', code:'AI030', cat:'instrumental', brand:'orthopremium', name:'Muelitas Caja Plástica p/Piezas Dentales',
    unit:'caja 10 pz', img:'imagenes/products/AI030.jpg',
    desc:'Cajitas plásticas individuales con forma de muela para transporte de piezas dentales. 10 pzas.',
    specs:['Material: Plástico','Uso: Transporte y entrega de piezas dentales al paciente'] },

  { id:'AI031', code:'AI031', cat:'instrumental', brand:'orthopremium', name:'Fresero de Plástico 60 Espacios',
    unit:'pieza', img:'imagenes/products/AI031.jpg',
    desc:'Fresero de plástico con tapa para organizar y proteger hasta 60 fresas de alta velocidad.',
    specs:['Espacios: 60','Material: Plástico resistente','Uso: Organización de fresas de alta velocidad','Con tapa protectora'] },

  { id:'AI032', code:'AI032', cat:'instrumental', brand:'orthopremium', name:'Sujetador de Impresiones Radiográficas',
    unit:'pieza', img:'imagenes/products/AI032.jpg',
    desc:'Sujetador para películas y sensores radiográficos. Posicionamiento correcto y reproducible.',
    specs:['Material: Plástico resistente','Uso: Películas y sensores RX','Posicionamiento reproducible','Autoclavable'] },

  { id:'AI033', code:'AI033/034', cat:'instrumental', brand:'orthopremium', name:'Retractor de Labio GDE/CH TPE Blanco',
    unit:'pieza', img:'imagenes/products/AI033.jpg',
    desc:'Retractor de labio en TPE blanco. Flexibilidad y confort para el paciente. Disponible en dos tallas.',
    specs:['Material: TPE elástico','Color: Blanco','Tallas: Grande (GDE) y Chico (CH)','Reusable','Autoclavable'] },

  { id:'AI035', code:'AI035/036/037', cat:'instrumental', brand:'orthopremium', name:'Bloque de Mordida CH/M/GDE',
    unit:'pieza', img:'imagenes/products/AI035.jpg',
    desc:'Bloque de mordida en espuma de polietileno para apertura bucal durante procedimientos. Tres tallas.',
    specs:['Material: Espuma de polietileno','Colores: Surtidos','Tallas: CH, M, GDE','Uso: Apertura bucal en procedimientos extensos'] },

  { id:'AI038', code:'AI038', cat:'desechables', brand:'orthopremium', name:'Puntas para Jeringa Triple Colores (bote 250pz)',
    unit:'bote 250 pz', img:'imagenes/products/AI038.jpg',
    desc:'Puntas de plástico de colores para jeringa triple aire-agua. 250 pzas en bote dispensador.',
    specs:['Colores: Surtidos','Uso: Jeringa triple estándar','Desechable, uso único'] },

  { id:'AI039', code:'AI039', cat:'instrumental', brand:'orthopremium', name:'Jeringa Triple de Agua y Aire Metálica',
    unit:'pieza', img:'imagenes/products/AI039.jpg',
    desc:'Jeringa triple metálica de acero inoxidable para aire, agua y niebla. Alta durabilidad.',
    specs:['Material: Acero inoxidable','Funciones: Aire, agua y niebla','Autoclavable','Conexión estándar universal'] },

  { id:'AI040', code:'AI040/040M/040G', cat:'desechables', brand:'orthopremium', name:'Cucharillas para Fluoruro en Gel',
    unit:'paquete', img:'imagenes/products/AI040.jpg',
    desc:'Cucharillas desechables de plástico flexible para aplicación de flúor en gel. Tres tallas.',
    specs:['Tallas: Chica (CH), Mediana (M), Grande (G)','Material: Plástico flexible','Uso: Aplicación de fluoruro en gel','Desechable, uso único'] },

  { id:'AI041AZ', code:'AI041AZ', cat:'instrumental', brand:'orthopremium', name:'Charola Esterilizar GDE 8 Instrumentos',
    unit:'pieza', img:'imagenes/products/AI041AZ.jpg',
    desc:'Charola grande de plástico termoresistente azul para esterilizar y organizar hasta 8 instrumentos.',
    specs:['Color: Azul','Capacidad: 8 instrumentos','Material: Plástico termoresistente','Autoclavable'] },

  { id:'AI042AM', code:'AI042AM', cat:'instrumental', brand:'orthopremium', name:'Charola Esterilizar CH 5 Instrumentos',
    unit:'pieza', img:'imagenes/products/AI042AM.jpg',
    desc:'Charola chica amarilla para esterilizar y organizar hasta 5 instrumentos dentales.',
    specs:['Color: Amarillo','Capacidad: 5 instrumentos','Autoclavable'] },

  { id:'AI043', code:'AI043', cat:'instrumental', brand:'orthopremium', name:'Colimadores Posicionadores RX',
    unit:'set', img:'imagenes/products/AI043.jpg',
    desc:'Set completo de colimadores y posicionadores Dent para radiografías periapicales y de aleta.',
    specs:['Tipo: Set completo','Uso: RX periapical y aleta de mordida','Reusable','Autoclavable','Alta precisión de posicionamiento'] },

  { id:'AI044', code:'AI044', cat:'desechables', brand:'orthopremium', name:'Contraángulo Desechable Copa Suave',
    unit:'pieza', img:'imagenes/products/AI044.jpg',
    desc:'Contraángulo desechable con copa de profilaxis suave integrada. Uso único.',
    specs:['Tipo: Copa suave integrada','Desechable, uso único','Velocidad: Contrángulo estándar','Sin necesidad de esterilización'] },

  { id:'AI045', code:'AI045', cat:'instrumental', brand:'orthopremium', name:'Anillo Codificador Instrumentos Grande',
    unit:'paquete', img:'imagenes/products/AI045.jpg',
    desc:'Anillos de silicona de colores para identificar y organizar instrumentos dentales. Talla grande.',
    specs:['Talla: Grande','Material: Silicona','Colores: Surtidos','Autoclavable','Uso: Identificación de instrumentos'] },

  { id:'AI046AM', code:'AI046AM', cat:'instrumental', brand:'orthopremium', name:'Anillo Codificador Instrumentos Chico',
    unit:'paquete', img:'imagenes/products/AI046AM.jpg',
    desc:'Anillos de silicona de colores para identificar instrumentos. Talla chica. Autoclavables.',
    specs:['Talla: Chica','Material: Silicona','Colores: Surtidos','Autoclavable'] },

  { id:'AI047', code:'AI047', cat:'desechables', brand:'orthopremium', name:'Block Papel para Mezclar Dental (10 libretas)',
    unit:'10 libretas', img:'imagenes/products/AI047.jpg',
    desc:'Block de papel satinado para mezcla de cementos y materiales dentales. 10 libretas por paquete.',
    specs:['Superficie: Papel satinado resistente','Uso: Mezcla de cementos, óxido de zinc, ionómeros'] },

  { id:'AI048', code:'AI048', cat:'instrumental', brand:'orthopremium', name:'Cinta Testigo 21mm × 50mts',
    unit:'rollo 50 mts', img:'imagenes/products/AI048.jpg',
    desc:'Cinta testigo química para control de esterilización en autoclave. Cambia de color al completar el ciclo.',
    specs:['Ancho: 21 mm','Largo: 50 metros por rollo','Tipo: Indicador químico Clase 1','Uso: Control de ciclos de autoclave'] },

  { id:'AI049', code:'AI049', cat:'desechables', brand:'orthopremium', name:'Cánula de Aspiración Blanca CQ (25pz)',
    unit:'paquete 25 pz', img:'imagenes/products/AI049.jpg',
    desc:'Cánulas de aspiración desechables color blanco, curvadas. 25 pzas por paquete.',
    specs:['Color: Blanco','Forma: Curvada','Desechable, uso único','Conexión estándar'] },

  { id:'OPEST', code:'OPEST', cat:'desechables', brand:'orthopremium', name:'Eyector de Saliva (bolsa 100pz)',
    unit:'bolsa 100 pz', img:'imagenes/products/OPEST.jpg',
    desc:'Eyectores de saliva desechables. Colores surtidos (azul y blanco). 100 pzas por bolsa.',
    specs:['Colores: Azul y blanco','Desechable, uso único','Conexión estándar a eyector','Flexible y ergonómico'] },

  // ══════════════════════════════════════════
  // FRESAS DE DIAMANTE  (Ortho Premium)
  // ══════════════════════════════════════════
  { id:'fresa-BR-M', code:'BR series · M', cat:'fresas', brand:'orthopremium', name:'Fresa Taper Round – Grano Medio',
    unit:'pieza', img:'imagenes/products/fresa-BR-M.jpg',
    desc:'Fresa cónica redondeada de grano medio (azul). Tallado y preparación de cavidades con precisión.',
    specs:['Forma: Taper Round (Cónica redondeada)','Grano: Medio (M) · Azul','Shank: FG estándar','Reg. Sanitario: 0597E2024 SSA','Modelos: BR-23, BR-25, BR-26, BR-28, BR-31, BR-40, BR-41, BR-45, BR-46, BR-49'] },

  { id:'fresa-BR-largo', code:'BR-L series · M', cat:'fresas', brand:'orthopremium', name:'Fresa Taper Round Largo – Grano Medio',
    unit:'pieza', img:'imagenes/products/fresa-BR-largo.jpg',
    desc:'Fresa cónica redondeada de cabeza larga. Acceso a zonas de difícil visibilidad.',
    specs:['Forma: Taper Round Largo','Grano: Medio (M)','Modelos: BR-L31, BR-L40, BR-L41, BR-L46','Uso: Preparaciones profundas y de acceso reducido'] },

  { id:'fresa-BC', code:'BC series · M', cat:'fresas', brand:'orthopremium', name:'Fresa Ball Convexity – Grano Medio',
    unit:'pieza', img:'imagenes/products/fresa-BC.jpg',
    desc:'Fresa de bola convexa de grano medio. Ideal para preparaciones oclusales y acabados de bordes.',
    specs:['Forma: Ball Convexity (Bola convexa)','Grano: Medio (M)','Modelos: BC-31, BC-32, BC-42, BC-43','Uso: Preparaciones oclusales'] },

  { id:'fresa-SI', code:'SI series', cat:'fresas', brand:'orthopremium', name:'Fresa Straight Ogival – Medio/Fino',
    unit:'pieza', img:'imagenes/products/fresa-SI.jpg',
    desc:'Fresa recta ogival para acabados y preparaciones con ángulo de convergencia definido.',
    specs:['Forma: Straight Ogival (Recta ogival)','Granos: M y F','Modelos: SI-45, SI-46, SI-47, SI-48','Uso: Acabados y preparaciones en ángulo'] },

  { id:'fresa-SF', code:'SF series · M', cat:'fresas', brand:'orthopremium', name:'Fresa Straight Flat – Grano Medio',
    unit:'pieza', img:'imagenes/products/fresa-SF.jpg',
    desc:'Fresa recta plana para desgaste plano y terminados de superficies.',
    specs:['Forma: Straight Flat (Recta plana)','Grano: Medio (M)','Modelos: SF-11, SF-12, SF-13, SF-15, SF-21, SF-31, SF-41, SF-42','Uso: Desgaste plano y terminados'] },

  { id:'fresa-SR', code:'SR series', cat:'fresas', brand:'orthopremium', name:'Fresa Straight Round – Fino',
    unit:'pieza', img:'imagenes/products/fresa-SR.jpg',
    desc:'Fresa recta de cabeza redondeada en grano fino. Para pulido y acabado de restauraciones.',
    specs:['Forma: Straight Round','Grano: Fino (F)','Modelos: SR-11, SR-12, SR-13, SR-21, SR-31, SR-41, SR-42','Uso: Acabado y pulido'] },

  { id:'fresa-TC', code:'TC series', cat:'fresas', brand:'orthopremium', name:'Fresa Taper Cone – Fino / Extra Fino',
    unit:'pieza', img:'imagenes/products/fresa-TC.jpg',
    desc:'Fresa cónica (taper cone) en grano fino y extra fino. Terminados precisos y acabado final.',
    specs:['Forma: Taper Cone (Cónica)','Granos: F (Fino) y EX (Extra fino)','Modelos: TC-21, TC-26, TC-27, TC-28','Uso: Terminados precisos y acabado final'] },

  { id:'fresa-WR', code:'WR series · M', cat:'fresas', brand:'orthopremium', name:'Fresa Wheel Round – Grano Medio',
    unit:'pieza', img:'imagenes/products/fresa-WR.jpg',
    desc:'Fresa rueda de carro para tallados, surcos de orientación y biselados.',
    specs:['Forma: Wheel Round (Rueda de carro)','Grano: Medio (M)','Modelos: WR-13, WR-44','Uso: Surcos de orientación y biselados'] },

  { id:'fresa-EX', code:'EX/DI series', cat:'fresas', brand:'orthopremium', name:'Fresa Special Shape / Double Inverted',
    unit:'pieza', img:'imagenes/products/fresa-EX.jpg',
    desc:'Fresas de formas especiales y cono invertido doble para contornos y retenciones en resina.',
    specs:['Formas: Special Shape (EX) y Double Inverted Cone (DI)','Modelos: EX-11, EX-12, EX-18, DI-41, DI-42','Uso: Contornos, retenciones y acceso intracanal'] },

  // ══════════════════════════════════════════
  // ORTODONCIA HD  (Ortho Premium / Eclipse)
  // ══════════════════════════════════════════
  { id:'bkt-mbt018-metal', code:'MBT .018 Eclipse', cat:'ortodoncia', brand:'orthopremium', name:'Brackets Metálicos MBT .018 – Eclipse',
    unit:'set 20 brackets', img:'imagenes/products/bkt-mbt018-metal.jpg',
    desc:'Brackets metálicos de acero inoxidable con prescripción MBT slot .018". Línea Eclipse. Malla 80 base.',
    specs:['Prescripción: MBT','Slot: .018"','Material: Acero inoxidable','Tecnología: MIM','Malla 80 para máxima adhesión','Posición grabada con láser','Bordes redondeados en slot para mínima fricción'] },

  { id:'bkt-mbt022-metal', code:'MBT .022 Eclipse', cat:'ortodoncia', brand:'orthopremium', name:'Brackets Metálicos MBT .022 – Eclipse',
    unit:'set 20 brackets', img:'imagenes/products/bkt-mbt022-metal.jpg',
    desc:'Brackets metálicos prescripción MBT slot .022". Alta precisión dimensional y durabilidad.',
    specs:['Prescripción: MBT','Slot: .022"','Material: Acero inoxidable MIM','Malla 80 base','Torque, angulación y rotación precisa','Bordes redondeados'] },

  { id:'bkt-roth018-metal', code:'Roth .018 Eclipse', cat:'ortodoncia', brand:'orthopremium', name:'Brackets Metálicos Roth .018 – Eclipse',
    unit:'set 20 brackets', img:'imagenes/products/bkt-roth018-metal.jpg',
    desc:'Brackets metálicos prescripción Roth slot .018". Clasificación simplificada, alta calidad.',
    specs:['Prescripción: Roth','Slot: .018"','Material: Acero inoxidable','Malla 80 base','Clasificación simplificada por packaging'] },

  { id:'bkt-roth022-metal', code:'Roth .022 Eclipse', cat:'ortodoncia', brand:'orthopremium', name:'Brackets Metálicos Roth .022 – Eclipse',
    unit:'set 20 brackets', img:'imagenes/products/bkt-roth022-metal.jpg',
    desc:'Brackets metálicos prescripción Roth slot .022". El sistema más usado en México. Máxima durabilidad.',
    specs:['Prescripción: Roth','Slot: .022"','Material: Acero inoxidable MIM','Malla 80 base','Resistencia superior al desgaste'] },

  { id:'bkt-roth022-cer', code:'Roth .022 Cerámico Plus', cat:'ortodoncia', brand:'orthopremium', name:'Brackets Cerámicos Roth .022 – Plus',
    unit:'set 20 brackets', img:'imagenes/products/bkt-roth022-cer.jpg',
    desc:'Brackets cerámicos estéticos prescripción Roth .022". Alta resistencia y discreción total.',
    specs:['Prescripción: Roth','Slot: .022"','Material: Cerámica policristalina','Estética: Sin manchado','Malla metálica para adhesión segura','Torque preciso'] },

  { id:'bkt-evo-roth022', code:'Evolution Roth .022', cat:'ortodoncia', brand:'orthopremium', name:'BKT Autoligado Evolution – Roth .022',
    unit:'set', img:'imagenes/products/bkt-evo-roth022.jpg',
    desc:'Bracket interactivo de autoligado con tapa NiTi. Roth .022. Tecnología de soldadura láser. Máximo confort.',
    specs:['Tipo: Autoligado interactivo','Prescripción: Roth','Slot: .022"','Tapa: NiTi resistente a deformación','Soldadura láser en base','Acero inoxidable 17-4 con tecnología MIM','Malla 80 base','Reg. Sanitario: 1829C2023 SSA','Diseño de precisión en slot: mínima fricción'] },

  { id:'bkt-evo-mbt022', code:'Evolution MBT .022', cat:'ortodoncia', brand:'orthopremium', name:'BKT Autoligado Evolution – MBT .022',
    unit:'set', img:'imagenes/products/bkt-evo-mbt022.jpg',
    desc:'Bracket interactivo de autoligado Evolution MBT .022. Eficiencia máxima, menor tiempo de tratamiento.',
    specs:['Tipo: Autoligado interactivo','Prescripción: MBT','Slot: .022"','Tapa: NiTi','Soldadura láser','Acero inox 17-4 MIM','Superficies ultra suaves en slot','Esfera en gancho para máxima retención'] },

  // ══════════════════════════════════════════
  // INSTRUMENTAL  (Premium Orthodontics + General)
  // ══════════════════════════════════════════
  { id:'inst-pinzas-orto', code:'Pinzas Ortodoncia', cat:'instrumental', brand:'orthopremium', name:'Pinzas para Ortodoncia – Acero Inoxidable',
    unit:'pieza', img:'imagenes/products/inst-pinzas-orto.jpg',
    desc:'Amplia línea de pinzas especializadas para procedimientos de ortodoncia. Acero inoxidable quirúrgico.',
    specs:['Marca: Premium Orthodontics','Material: Acero inoxidable quirúrgico','Tipos: Pinzas de corte, doblado, ligado y alate','Autoclavable','Acabado espejo o satinado','Alta durabilidad y precisión'] },

  { id:'inst-tijeras', code:'Tijeras Dentales', cat:'instrumental', brand:'orthopremium', name:'Tijeras y Portaagujas Dentales',
    unit:'pieza', img:'imagenes/products/inst-tijeras.jpg',
    desc:'Tijeras hemostáticas y portaagujas de acero inoxidable. Cierre suave y preciso.',
    specs:['Material: Acero inoxidable','Tipos: Hemostáticas, portaagujas, tejido blando','Autoclavable','Articulación de alta precisión'] },

  { id:'inst-exploradores', code:'Exploradores y Espejos', cat:'instrumental', brand:'orthopremium', name:'Exploradores y Espejos Dentales',
    unit:'pieza', img:'imagenes/products/inst-exploradores.jpg',
    desc:'Instrumentos de exploración y diagnóstico. Espejos, exploradores y sondas de alta calidad.',
    specs:['Material: Acero inoxidable','Incluye: Espejo #4 y #5, explorador 11/12, sonda periodontal','Mango ergonómico','Autoclavable'] },

  // ══════════════════════════════════════════
  // PRIME DENT  (Materiales restauradores)
  // ══════════════════════════════════════════
  { id:'pd-composite', code:'Prime Dent Composite', cat:'primadent', brand:'primadent', name:'Resina Compuesta Prime Dent',
    unit:'jeringa', img:'imagenes/products/pd-composite.jpg',
    desc:'Resina compuesta de nanotecnología para restauraciones directas anteriores y posteriores.',
    specs:['Tecnología: Nanopartículas híbridas','Alta resistencia al desgaste','Amplia gama de colores VITA','Radiopaca','Alta resistencia a la fractura','Excelente pulido y lustre final'] },

  { id:'pd-adhesivo', code:'Prime Dent Bond', cat:'primadent', brand:'primadent', name:'Adhesivo Universal Prime Dent',
    unit:'frasco', img:'imagenes/products/pd-adhesivo.jpg',
    desc:'Sistema adhesivo universal de 7a generación. Técnica grabado total, autograbado o selectivo.',
    specs:['Generación: 7a (universal)','Técnicas: Grabado total, autograbado, selectivo en esmalte','Alta resistencia de unión a dentina y esmalte','MDP para adhesión a metal y circonio','No requiere capa adhesiva adicional'] },

  { id:'pd-cemento', code:'Prime Dent Cement', cat:'primadent', brand:'primadent', name:'Cemento de Ionómero de Vidrio',
    unit:'polvo + líquido', img:'imagenes/products/pd-cemento.jpg',
    desc:'Cemento de ionómero de vidrio de alta resistencia para cementación y obturaciones.',
    specs:['Tipo: Ionómero de vidrio convencional','Liberación de flúor sostenida','Alta resistencia compresiva','Biocompatible','Uso: Cementación, obturación, forro cavitario'] },

  // ══════════════════════════════════════════
  // CATÁLOGOS ESPECIALIZADOS (representativos)
  // ══════════════════════════════════════════
  { id:'ae-scalers', code:'American Eagle EXD', cat:'americaneagle', brand:'americaneagle', name:'Scalers y Curetas American Eagle',
    unit:'pieza', img:'imagenes/products/ae-scalers.jpg',
    desc:'Instrumental de raspado y alisado radicular American Eagle. Serie EXD con mango DuraLite.',
    specs:['Marca: American Eagle Instruments','Serie: EXD (Extended Durability)','Mango: DuraLite® octagonal','Material: Acero inoxidable de alta templanza','Mayor filo y durabilidad 30% superior','Autoclavable'] },

  { id:'hf-instruments', code:'Hu-Friedy Premium', cat:'hufriedygroup', brand:'hufriedygroup', name:'Instrumental Hu-Friedy',
    unit:'pieza', img:'imagenes/products/hf-instruments.jpg',
    desc:'Instrumental dental Hu-Friedy de primera calidad mundial. Scalers, curetas, instrumentos restaurativos y más.',
    specs:['Marca: Hu-Friedy Group','Fabricación: USA — más de 100 años de experiencia','Material: Acero inoxidable de alta aleación','Autoclavable','Garantía de por vida en el instrumento','Amplia gama: endodoncia, periodoncia, cirugía, restaurativa'] },

  { id:'medesy-forceps', code:'Medesy Forceps', cat:'medesy', brand:'medesy', name:'Forceps y Elevadores Medesy',
    unit:'pieza', img:'imagenes/products/medesy-forceps.jpg',
    desc:'Forceps y elevadores para exodoncia Medesy. Fabricación italiana de alta precisión.',
    specs:['Marca: Medesy — Italia','Material: Acero inoxidable Cr-Mo 18/8','Acabado: Satinado','Ergonomía óptima para cirugía','Autoclavable','Tipos: Forceps superiores, inferiores, pediátricos; Elevadores'] },

  { id:'vamasa-varios', code:'Vamasa Catalogo', cat:'vamasa', brand:'vamasa', name:'Catálogo Vamasa – Material Dental',
    unit:'pieza', img:'imagenes/vamasa/pag_02.jpg',
    desc:'Amplia variedad de productos dental Vamasa: instrumental, desechables y materiales.',
    specs:['Distribuidor: Vamasa','Categorías: Instrumental, desechables, equipos','Alta disponibilidad de inventario','Entrega rápida'] },

  { id:'borgatta-mat', code:'Borgatta México', cat:'borgatta', brand:'borgatta', name:'Material Borgatta México 2021',
    unit:'pieza', img:'imagenes/borgatta/pag_02.jpg',
    desc:'Materiales e instrumental dental del catálogo Borgatta México 2021.',
    specs:['Distribuidor: Borgatta','Catálogo: México 2021','Amplia línea de productos','Precios competitivos'] },

  { id:'balsas-varios', code:'Balsas Dental', cat:'balsas', brand:'balsas', name:'Catálogo Balsas Dental',
    unit:'pieza', img:'imagenes/balsas/pag_02.jpg',
    desc:'Productos del catálogo Balsas Dental. Amplia variedad de materiales e instrumental.',
    specs:['Distribuidor: Balsas Dental','Catálogo completo disponible','Solicita precio por producto específico'] },

  { id:'elasticos-ao', code:'Elásticos A.O.', cat:'elasticos', brand:'elasticos', name:'Elásticos de Ortodoncia A.O.',
    unit:'bolsa', img:'imagenes/elasticos/pag_01.jpg',
    desc:'Elásticos de látex para ortodoncia. Variedad de tamaños y fuerzas para tracción intermaxilar.',
    specs:['Material: Látex natural','Usos: Tracción intermaxilar, tracción de caninos','Fuerzas: Light, Medium, Heavy','Tamaños: 3/16", 1/4", 5/16", 3/8" y más','Registro sanitario SSA'] },

  { id:'lb-kit', code:'Línea Black', cat:'lineablack', brand:'lineablack', name:'Kit Línea Black – Material Estético',
    unit:'kit', img:'imagenes/lineablack/pag_01.jpg',
    desc:'Línea Black: materiales e instrumental de alto desempeño con acabado negro satinado. Estética profesional.',
    specs:['Color: Negro satinado','Alta visibilidad en campo clínico','Autoclavable','Uso: Fotografía dental y procedimientos estéticos'] },

  { id:'bioart-artic', code:'Articulador Bioart', cat:'articulador', brand:'articulador', name:'Articulador Semiajustable Bioart',
    unit:'pieza', img:'imagenes/articulador/pag_02.jpg',
    desc:'Articulador dental semiajustable Bioart. Reproducción fiel de los movimientos mandibulares.',
    specs:['Marca: Bioart — Brasil','Tipo: Semiajustable con arco facial','Material: Aleación de aluminio de alta resistencia','Reproduce movimientos: Protrusivo, lateralidades, apertura/cierre','Incluye: Arco facial y accesorios','Uso: Diagnóstico, rehabilitación oral y prótesis total'] },

  { id:'gnatus-auto', code:'Autoclave Gnatus', cat:'autoclave', brand:'autoclave', name:'Autoclave Gnatus – Esterilización Clase B',
    unit:'equipo', img:'imagenes/autoclave/pag_02.jpg',
    desc:'Autoclave Gnatus de esterilización a vapor. Clase B. Ciclos programables y control digital.',
    specs:['Marca: Gnatus — Brasil','Clase: B (esterilización completa con vacío fraccional)','Capacidad: 12L – 22L (según modelo)','Temperatura: 121°C / 134°C','Ciclos: Rápido, instrumental, textil, priones','Display: Digital con registro de ciclos','Certificaciones: ANVISA, INMETRO'] },

  { id:'primervg-sensor', code:'Prime RVG', cat:'primervg', brand:'primervg', name:'Sensor de Radiografía Digital Prime RVG',
    unit:'equipo', img:'imagenes/primervg/pag_01.jpg',
    desc:'Sensor digital intraoral Prime RVG para radiografías periapicales de alta resolución.',
    specs:['Marca: Prime RVG','Resolución: Alta definición','Reducción de dosis: Hasta 90% vs película convencional','Imagen instantánea','Compatible con software de diagnóstico','Conector: USB','Tamaños: 1 y 2'] },
];

// Map category slugs to display names
const CAT_LABELS = {
  desechables: 'Desechables',
  fresas: 'Fresas de Diamante',
  ortodoncia: 'Ortodoncia HD',
  instrumental: 'Instrumental',
  primadent: 'Prime Dent',
  americaneagle: 'American Eagle',
  hufriedygroup: 'Hu-Friedy',
  medesy: 'Medesy',
  vamasa: 'Vamasa',
  borgatta: 'Borgatta',
  balsas: 'Balsas Dental',
  elasticos: 'Elásticos A.O.',
  lineablack: 'Línea Black',
  articulador: 'Articulador Bioart',
  autoclave: 'Autoclave Gnatus',
  primervg: 'Prime RVG',
};
