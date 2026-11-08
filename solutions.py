"""
solutions.py - Comprehensive 38-Class PlantVillage Agricultural Advisory Database
Covers all 38 categories: Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach,
Pepper Bell, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato.
"""

SOLUTIONS_DATABASE = {
    "Apple___Apple_scab": {
        "crop": "Apple",
        "disease": "Apple Scab",
        "pathogen": "Venturia inaequalis (Fungus)",
        "severity": "Medium to High",
        "symptoms": "Olive-green to black velvety spots on leaves, chlorotic halos, distorted foliage, and corky brown scabs on developing fruit.",
        "chemical_treatment": "Apply Captan 50 WP (2.5 g/L) or Difenoconazole 25% EC (0.5 ml/L) or Mancozeb 75% WP (2.5 g/L) at green tip and petal fall stages.",
        "organic_treatment": "Spray wettable sulfur (3 g/L) or Copper Oxychloride 50 WP (3 g/L). Apply Bacillus subtilis or neem oil (5 ml/L) early morning.",
        "prevention": "Rake and destroy fallen leaves in autumn to eradicate perithecia. Prune canopy for sunlight penetration and airflow.",
        "extension_source": "ICAR-CITH & Cornell Fruit Pathology Bulletin"
    },
    "Apple___Black_rot": {
        "crop": "Apple",
        "disease": "Black Rot (Frogeye Leaf Spot)",
        "pathogen": "Botryosphaeria obtusa (Fungus)",
        "severity": "High",
        "symptoms": "Small purple leaf spots expanding into 'frogeye' lesions with brown centers and dark purple margins; firm rot with pycnidia rings on fruit.",
        "chemical_treatment": "Spray Thiophanate-methyl 70 WP (1 g/L) or Captan 50 WP (2 g/L) from tight cluster through post-bloom sprays.",
        "organic_treatment": "Apply Bordeaux mixture (1%) or Copper Octanoate. Clear all mummified fruits and dead twigs from the orchard.",
        "prevention": "Prune out dead wood, fire blight cankers, and mummies in winter. Sterilize pruning shears between cuts with 70% ethanol.",
        "extension_source": "Penn State Extension Tree Fruit Production Guide"
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "disease": "Cedar Apple Rust",
        "pathogen": "Gymnosporangium juniperi-virginianae (Fungus)",
        "severity": "Medium",
        "symptoms": "Bright yellow-orange circular spots on upper leaf surfaces that develop tube-like fungal aecia structures on leaf undersides.",
        "chemical_treatment": "Spray Myclobutanil 10 WP (0.4 g/L) or Propiconazole 25 EC (1 ml/L) or Mancozeb at pink bud and petal fall stages.",
        "organic_treatment": "Apply wettable sulfur at 10-day intervals beginning at cluster stage. Remove nearby Eastern red cedar galls.",
        "prevention": "Eradicate or prune juniper/cedar trees within 1 to 2 miles. Choose resistant cultivars (e.g., Liberty, Freedom, Enterprise).",
        "extension_source": "Purdue University Extension - Rust Diseases of Apple"
    },
    "Apple___healthy": {
        "crop": "Apple",
        "disease": "Healthy Plant (No Disease Detected)",
        "pathogen": "None",
        "severity": "Healthy (Optimal)",
        "symptoms": "Vigorous green foliage, clear leaf margins, healthy shoot elongation, and normal fruit set without chlorosis or necrotic lesions.",
        "chemical_treatment": "No fungicide or bactericide treatment required.",
        "organic_treatment": "Apply cold-pressed seaweed extract (2 ml/L) or compost tea as a foliage tonic for enhanced vigor.",
        "prevention": "Maintain balanced N-P-K (12-12-17) nutrition, monitor soil moisture with tensiometer, and schedule preventive dormant oil sprays.",
        "extension_source": "ICAR Good Agricultural Practices (GAP) for Pome Fruit"
    },
    "Blueberry___healthy": {
        "crop": "Blueberry",
        "disease": "Healthy Plant (No Disease Detected)",
        "pathogen": "None",
        "severity": "Healthy (Optimal)",
        "symptoms": "Glossy green leaves, sturdy red/green canes, robust root system, and uniform berry development.",
        "chemical_treatment": "None needed.",
        "organic_treatment": "Mulch with pine bark or pine needles to maintain acidity (pH 4.5-5.2) and soil organic matter.",
        "prevention": "Maintain drip irrigation, check soil pH twice yearly, and ensure well-draining acidic sandy loam soil.",
        "extension_source": "Michigan State University Extension Blueberry Guide"
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "crop": "Cherry",
        "disease": "Powdery Mildew",
        "pathogen": "Podosphaera clandestina (Fungus)",
        "severity": "Medium to High",
        "symptoms": "White superficial powdery fungal coating on leaves and young shoots, leaves curling upward, distorted shoot tips, scarred fruit.",
        "chemical_treatment": "Spray Tebuconazole 250 EC (1 ml/L) or Quinoxyfen or Difenoconazole 25 EC (0.5 ml/L) at shuck fall and post-harvest.",
        "organic_treatment": "Spray Potassium Bicarbonate (4 g/L), neem oil 1% EC (5 ml/L), or diluted milk whey (1:9 ratio) in bright sunlight.",
        "prevention": "Prune internal canopy to boost airflow, avoid excessive nitrogen fertilization that stimulates tender foliage, avoid overhead watering.",
        "extension_source": "UC Davis IPM Cherry Powdery Mildew"
    },
    "Cherry_(including_sour)___healthy": {
        "crop": "Cherry",
        "disease": "Healthy Plant (No Disease Detected)",
        "pathogen": "None",
        "severity": "Healthy (Optimal)",
        "symptoms": "Lush dark green serrated leaves without shot-holes or spots; smooth bark, vigorous spur development.",
        "chemical_treatment": "No action required.",
        "organic_treatment": "Apply compost top-dressing and micronutrient spray (Zinc and Boron) prior to flowering.",
        "prevention": "Apply dormant copper spray in autumn to prevent bacterial canker; keep mulch 10 cm away from the trunk.",
        "extension_source": "Washington State University Tree Fruit Extension"
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "crop": "Corn (Maize)",
        "disease": "Gray Leaf Spot",
        "pathogen": "Cercospora zeae-maydis (Fungus)",
        "severity": "High",
        "symptoms": "Rectangular, brown to gray lesions restricted by leaf veins (0.5 to 2 inches long) creating blocky lesions; leaf blighting.",
        "chemical_treatment": "Apply Azoxystrobin 18.2% + Difenoconazole 11.4% SC (1 ml/L) or Pyraclostrobin 20% WG at V12 to VT (tasseling) stage.",
        "organic_treatment": "Foliar spray of Trichoderma harzianum (5 g/L) and copper hydroxide before tasseling if disease pressure is low.",
        "prevention": "Crop rotation with legumes for at least 2 years; select resistant corn hybrids with high GLS rating; till crop residues.",
        "extension_source": "Iowa State University Extension Corn Pathology"
    },
    "Corn_(maize)___Common_rust_": {
        "crop": "Corn (Maize)",
        "disease": "Common Rust",
        "pathogen": "Puccinia sorghi (Fungus)",
        "severity": "Medium",
        "symptoms": "Golden brown to cinnamon brown oval pustules (uredinia) scattered across both upper and lower leaf surfaces.",
        "chemical_treatment": "Spray Mancozeb 75 WP (2.5 g/L) or Propiconazole 25 EC (1 ml/L) or Tebuconazole when pustules first appear on mid-canopy leaves.",
        "organic_treatment": "Sulfur dusting (20 kg/ha) or spray liquid wettable sulfur (3 g/L); bio-agent Pseudomonas fluorescens (5 ml/L).",
        "prevention": "Plant resistant hybrid varieties (bearing Rp resistance genes); early planting to escape high late-season humidity and spores.",
        "extension_source": "ICAR-IIMR Indian Institute of Maize Research"
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn (Maize)",
        "disease": "Northern Corn Leaf Blight",
        "pathogen": "Exserohilum turcicum (Fungus)",
        "severity": "High",
        "symptoms": "Cigar-shaped, long elliptical grayish-green to tan lesions (1 to 6 inches long) starting on lower leaves and moving up.",
        "chemical_treatment": "Spray Azoxystrobin + Tebuconazole (1 ml/L) or Mancozeb 75 WP (2.5 g/L) when lesions reach third leaf below the ear before pollination.",
        "organic_treatment": "Foliar application of Bacillus amyloliquefaciens or Trichoderma viride (5 g/L).",
        "prevention": "Use resistant hybrids (Ht1, Ht2 genes), deep plowing of infected stubble post-harvest, and rotation with non-host crops.",
        "extension_source": "Purdue Extension Northern Corn Leaf Blight"
    },
    "Corn_(maize)___healthy": {
        "crop": "Corn (Maize)",
        "disease": "Healthy Plant (No Disease Detected)",
        "pathogen": "None",
        "severity": "Healthy (Optimal)",
        "symptoms": "Broad, arching deep-green leaves with crisp margins, sturdy stalks, and vigorous tassel/silking progress.",
        "chemical_treatment": "None required.",
        "organic_treatment": "Side-dress vermicompost or apply Jeevamrutha / seaweed extract during knee-high stage (V6).",
        "prevention": "Maintain split nitrogen dosing (basal, knee-high, tasseling), monitor fall armyworm traps, and maintain uniform soil moisture.",
        "extension_source": "ICAR Package of Practices for Maize"
    },
    "Grape___Black_rot": {
        "crop": "Grape",
        "disease": "Black Rot",
        "pathogen": "Guignardia bidwellii (Fungus)",
        "severity": "High",
        "symptoms": "Reddish-brown circular leaf spots with tiny black pycnidia pimples; berries shrivel into hard, black, wrinkled mummies.",
        "chemical_treatment": "Spray Mancozeb 75 WP (2.5 g/L) or Myclobutanil 10 WP (0.5 g/L) or Boscalid from early shoot growth through 4 weeks post-bloom.",
        "organic_treatment": "Bordeaux mixture 1% or Copper Octanoate sprays every 10-14 days; immediate hand collection and burial of dried mummies.",
        "prevention": "Winter canopy management to maximize air movement; remove wild grapes and abandoned vines within 500 meters.",
        "extension_source": "Ohio State University Extension Grape Disease Guide"
    },
    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape",
        "disease": "Esca (Black Measles / Petri Disease)",
        "pathogen": "Phaeomoniella chlamydospora & Fomitiporia mediterranea",
        "severity": "High / Chronic",
        "symptoms": "'Tiger-stripe' chlorotic interveinal bands with necrotic margins on leaves; dark spotting and split cracking on grape berries.",
        "chemical_treatment": "Paint pruning wounds immediately with Thiophanate-methyl or wound seal paste containing copper.",
        "organic_treatment": "Apply Trichoderma atroviride to fresh pruning cuts to protect vascular xylem from fungal invasion.",
        "prevention": "Delay pruning until late dormant period; disinfect pruning equipment regularly; remove and incinerate dying dead trunks.",
        "extension_source": "UC Davis Viticulture & Enology Esca Management"
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape",
        "disease": "Leaf Blight (Isariopsis Clavispora)",
        "pathogen": "Pseudocercospora clavispora (Fungus)",
        "severity": "Medium",
        "symptoms": "Irregular dark brown patches on leaf surface coalescing into scorched blighted foliage; premature leaf drop and delayed sugar accumulation.",
        "chemical_treatment": "Spray Carbendazim 50 WP (1 g/L) or Pyraclostrobin 20 WG (0.5 g/L) or Mancozeb 75 WP (2 g/L) during rainy periods.",
        "organic_treatment": "Foliar application of Copper Hydroxide (2.5 g/L) or potassium silicate (2 ml/L) to strengthen cuticle defenses.",
        "prevention": "Thin shoot density and maintain proper trellis canopy openness; rake and bury fallen foliage after seasonal harvest.",
        "extension_source": "ICAR-NRCG National Research Centre for Grapes, Pune"
    },
    "Grape___healthy": {
        "crop": "Grape",
        "disease": "Healthy Plant (No Disease Detected)",
        "pathogen": "None",
        "severity": "Healthy (Optimal)",
        "symptoms": "Vibrant emerald green leaves, strong tendril growth, clean canes, and uniform blossom clusters without powdery residue.",
        "chemical_treatment": "None required.",
        "organic_treatment": "Foliar spray of micronutrients (Boron, Zinc, Magnesium) at pre-bloom and pea-size berry stage.",
        "prevention": "Ensure good drainage, proper shoot positioning on trellises, and balanced potassium/magnesium fertilizer management.",
        "extension_source": "ICAR-NRCG Grape Production Guidelines"
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "crop": "Citrus / Orange",
        "disease": "Citrus Greening (Huanglongbing / HLB)",
        "pathogen": "Candidatus Liberibacter asiaticus (Bacteria vectored by Asian Citrus Psyllid)",
        "severity": "Extreme / Critical",
        "symptoms": "Asymmetric blotchy mottle chlorosis crossing leaf veins, yellow shoots ('yellow dragon'), small lopsided bitter green fruits.",
        "chemical_treatment": "Vector control is mandatory: Spray Imidacloprid 17.8 SL (0.5 ml/L) or Thiamethoxam 25 WG (0.3 g/L) or Dimethoate (1.5 ml/L).",
        "organic_treatment": "Apply foliar micronutrient blend (Zinc, Iron, Manganese, Boron) to sustain vascular transport; release Tamarixia radiata parasitoids.",
        "prevention": "Plant only certified disease-free budwood; install yellow sticky traps for psyllid monitoring; immediately rogue and destroy infected trees.",
        "extension_source": "USDA-APHIS & ICAR-CCRI Central Citrus Research Institute"
    },
    "Peach___Bacterial_spot": {
        "crop": "Peach",
        "disease": "Bacterial Spot",
        "pathogen": "Xanthomonas arboricola pv. pruni (Bacteria)",
        "severity": "High",
        "symptoms": "Water-soaked polygonal angular spots on leaves turning purplish-black and dropping out ('shot hole' appearance); pitted fruit lesions.",
        "chemical_treatment": "Apply Copper Hydroxide 53.8% WG (1.5 g/L) at dormant to bud break, followed by Oxytetracycline (Mycoshield) at bloom/petal fall.",
        "organic_treatment": "Copper sulfate + hydrated lime (Bordeaux mixture 0.5%) before leaf emergence; foliar sprays of Bacillus subtilis.",
        "prevention": "Avoid high-nitrogen fertilizer applications that cause succulent shoots; plant windbreaks to minimize sand-grit leaf abrasion.",
        "extension_source": "Rutgers NJAES Peach Bacterial Spot Management"
    },
    "Peach___healthy": {
        "crop": "Peach",
        "disease": "Healthy Plant (No Disease Detected)",
        "pathogen": "None",
        "severity": "Healthy (Optimal)",
        "symptoms": "Glossy lanceolate green leaves, smooth bark, clean shoot tips, and uniform fruit sizing.",
        "chemical_treatment": "None required.",
        "organic_treatment": "Compost mulch around drip line; foliar zinc spray during dormant stage.",
        "prevention": "Prune open-center vase architecture for aeration; monitor for peach tree borer at trunk base.",
        "extension_source": "Clemson Cooperative Extension Peach Bulletin"
    },
    "Pepper,_bell___Bacterial_spot": {
        "crop": "Bell Pepper (Capsicum)",
        "disease": "Bacterial Spot",
        "pathogen": "Xanthomonas euvesicatoria (Bacteria)",
        "severity": "High",
        "symptoms": "Small, water-soaked, circular to irregular dark brown lesions with yellow halos on leaves, causes severe defoliation and blistered fruit spots.",
        "chemical_treatment": "Foliar spray of Copper Oxychloride 50 WP (2.5 g/L) combined with Streptocycline or Kasugamycin 3% SL (1.5 ml/L).",
        "organic_treatment": "Apply Copper Octanoate or bio-control agents like Pseudomonas fluorescens (5 g/L) at nursery and transplanting stages.",
        "prevention": "Hot water seed treatment at 50°C for 25 minutes; use certified clean seed; avoid working in fields when foliage is wet.",
        "extension_source": "University of Florida IFAS Extension EDIS Pepper Disease"
    },
    "Pepper,_bell___healthy": {
        "crop": "Bell Pepper (Capsicum)",
        "disease": "Healthy Plant (No Disease Detected)",
        "pathogen": "None",
        "severity": "Healthy (Optimal)",
        "symptoms": "Sturdy upright bush, deep green leaves with no necrotic spots, crisp bell fruits forming with thick pericarp walls.",
        "chemical_treatment": "No fungicide or bactericide needed.",
        "organic_treatment": "Foliar spray of Panchagavya (3%) or seaweed extract every 15 days to encourage vigorous flowering.",
        "prevention": "Ensure well-drained loamy soil, stake plants to prevent ground contact, maintain drip irrigation.",
        "extension_source": "ICAR-IIHR Indian Institute of Horticultural Research"
    },
    "Potato___Early_blight": {
        "crop": "Potato",
        "disease": "Early Blight",
        "pathogen": "Alternaria solani (Fungus)",
        "severity": "Medium to High",
        "symptoms": "Dark brown circular spots with concentric rings creating a 'target board' pattern on older lower leaves, leaf yellowing.",
        "chemical_treatment": "Spray Chlorothalonil 75 WP (2 g/L) or Mancozeb 75 WP (2.5 g/L) or Azoxystrobin 23 SC (1 ml/L) at initial symptom onset.",
        "organic_treatment": "Apply Copper Hydroxide (2 g/L) or Neem seed kernel extract (NSKE 5%); foliar spray of Trichoderma viride.",
        "prevention": "3-year crop rotation with non-solanaceous crops; maintain optimal plant vigor with adequate potassium; avoid overhead sprinkler irrigation.",
        "extension_source": "ICAR-CPRI Central Potato Research Institute, Shimla"
    },
    "Potato___Late_blight": {
        "crop": "Potato",
        "disease": "Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "severity": "Extreme / Rapid Destruction",
        "symptoms": "Water-soaked pale to dark lesions expanding rapidly, white cottony mildew mold on underside of leaves in cool humid weather; foul rot odor.",
        "chemical_treatment": "Apply Cymoxanil 8% + Mancozeb 64% WP (2.5 g/L) or Metalaxyl-M + Mancozeb (2.5 g/L) or Dimethomorph 50 WP (1 g/L) immediately.",
        "organic_treatment": "Preventive Copper Oxychloride 50 WP (3 g/L) or Bordeaux mixture 1% before rainy spells; destroy infected haulms.",
        "prevention": "Use certified seed tubers; destroy cull piles; ridge soil high around stems to protect tubers from spore wash; check blight warnings.",
        "extension_source": "ICAR-CPRI Late Blight Forecasting & Advisory"
    },
    "Potato___healthy": {
        "crop": "Potato",
        "disease": "Healthy Plant (No Disease Detected)",
        "pathogen": "None",
        "severity": "Healthy (Optimal)",
        "symptoms": "Lush compound green leaves, robust stems, no water-soaked margins or target spots, healthy tuber bulking.",
        "chemical_treatment": "None required.",
        "organic_treatment": "Foliar potassium silicate or humic acid application at tuber initiation stage.",
        "prevention": "Proper earthing up at 30 and 45 days after planting; drip irrigation to keep canopy dry.",
        "extension_source": "ICAR-CPRI Good Agricultural Practices"
    },
    "Raspberry___healthy": {
        "crop": "Raspberry",
        "disease": "Healthy Plant (No Disease Detected)",
        "pathogen": "None",
        "severity": "Healthy (Optimal)",
        "symptoms": "Vigorous green canes, clean pinnate leaves, active flowering clusters, and firm plump developing drupelets.",
        "chemical_treatment": "No action needed.",
        "organic_treatment": "Apply aged compost mulch and organic bone meal for phosphorus enrichment.",
        "prevention": "Prune out old floricanes right after fruiting; maintain trellis wires for adequate air circulation.",
        "extension_source": "Pacific Northwest Extension Raspberry Guide"
    },
    "Soybean___healthy": {
        "crop": "Soybean",
        "disease": "Healthy Plant (No Disease Detected)",
        "pathogen": "None",
        "severity": "Healthy (Optimal)",
        "symptoms": "Trifoliate leaves with vibrant green coloration, robust root nodulation with pink nitrogen-fixing leghaemoglobin, clean pod formation.",
        "chemical_treatment": "None required.",
        "organic_treatment": "Inoculate seeds with Bradyrhizobium japonicum and PSB (Phosphate Solubilizing Bacteria) at sowing.",
        "prevention": "Maintain 45 cm row spacing, avoid waterlogging, and apply balanced sulfur (20 kg/ha) along with basal fertilizer.",
        "extension_source": "ICAR-IISR Indian Institute of Soybean Research, Indore"
    },
    "Squash___Powdery_mildew": {
        "crop": "Squash / Cucurbits",
        "disease": "Powdery Mildew",
        "pathogen": "Podosphaera xanthii (Fungus)",
        "severity": "Medium to High",
        "symptoms": "Fluffy white talcum powder-like fungal spots on upper and lower leaf surfaces, causing premature yellowing, drying, and leaf drop.",
        "chemical_treatment": "Spray Penconazole 10% EC (0.5 ml/L) or Kresoxim-methyl 44.3 SC (1 ml/L) or Dinocap 48 EC (1 ml/L).",
        "organic_treatment": "Spray Potassium Bicarbonate (4 g/L) + horticultural oil (5 ml/L), or wettable sulfur (2.5 g/L).",
        "prevention": "Choose resistant squash varieties (e.g., PMR hybrids); space vines generously; avoid shaded fields.",
        "extension_source": "Cornell University Cucurbit Pathology Guidelines"
    },
    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry",
        "disease": "Leaf Scorch",
        "pathogen": "Diplocarpon earlianum (Fungus)",
        "severity": "Medium",
        "symptoms": "Small purple irregularly-shaped blotches across upper leaf surface coalescing into scorched dark brown patches with red margins.",
        "chemical_treatment": "Spray Captan 50 WP (2 g/L) or Pyraclostrobin or Myclobutanil at first leaf expansion and post-bloom.",
        "organic_treatment": "Apply Copper Hydroxide (1.5 g/L) or sulfur dust; collect and burn affected leaves after harvesting berries.",
        "prevention": "Plant in raised beds covered with straw mulch or plastic mulch; avoid sprinkler watering; plant certified virus-free runners.",
        "extension_source": "UC Davis IPM Strawberry Leaf Scorch Guide"
    },
    "Strawberry___healthy": {
        "crop": "Strawberry",
        "disease": "Healthy Plant (No Disease Detected)",
        "pathogen": "None",
        "severity": "Healthy (Optimal)",
        "symptoms": "Lush trifoliate leaves with serrated edges, vigorous crown formation, healthy runner production, and clean conical red fruit.",
        "chemical_treatment": "None required.",
        "organic_treatment": "Foliar humic acid and micronutrient application (Calcium and Boron) for fruit firmness.",
        "prevention": "Keep fruit off wet soil using straw mulch; replace mother plants every 3 years to maintain high vigor.",
        "extension_source": "ICAR-IARI Division of Fruits & Horticultural Technology"
    },
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "disease": "Bacterial Spot",
        "pathogen": "Xanthomonas perforans / euvesicatoria (Bacteria)",
        "severity": "High",
        "symptoms": "Small circular greasy water-soaked spots on leaves that turn brown with a chlorotic yellow halo; leaf drop and scabbed fruit spots.",
        "chemical_treatment": "Spray Copper Oxychloride 50 WP (2.5 g/L) + Streptocycline (100 ppm, approx 1 g in 10 L water) at weekly intervals during wet weather.",
        "organic_treatment": "Apply Bacillus amyloliquefaciens (5 g/L) or Copper soap (Copper Octanoate); soak seeds in 1.3% sodium hypochlorite.",
        "prevention": "Avoid handling plants when wet; clean stakes and wire cages with 10% bleach; practice 2-year crop rotation.",
        "extension_source": "University of Florida IFAS Tomato Bacterial Spot Control"
    },
    "Tomato___Early_blight": {
        "crop": "Tomato",
        "disease": "Early Blight",
        "pathogen": "Alternaria linariae (Alternaria solani) (Fungus)",
        "severity": "High",
        "symptoms": "Brown to black lesions with concentric rings ('bullseye' appearance) on lower leaves, surrounded by yellow chlorotic tissue; stem collar rot.",
        "chemical_treatment": "Spray Mancozeb 75 WP (2.5 g/L) or Chlorothalonil 75 WP (2 g/L) or Azoxystrobin 18.2% + Difenoconazole 11.4% SC (1 ml/L).",
        "organic_treatment": "Apply Copper Hydroxide (2.5 g/L) or neem oil (5 ml/L); spray Trichoderma harzianum to foliage and root zone.",
        "prevention": "Mulch soil surface with black plastic or straw to stop soil-splash inoculant; stake and prune bottom 30 cm of leaves.",
        "extension_source": "NC State Extension Tomato Early Blight Factsheet"
    },
    "Tomato___Late_blight": {
        "crop": "Tomato",
        "disease": "Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "severity": "Extreme / Devastating",
        "symptoms": "Large, irregular water-soaked dark gray/brown greasy lesions on leaves and stems; fluffy white mold underneath; rapid whole plant wilt.",
        "chemical_treatment": "Immediately spray Cymoxanil + Mancozeb (2.5 g/L) or Dimethomorph 50 WP (1 g/L) or Mandipropamid (0.8 ml/L).",
        "organic_treatment": "Preventive Copper Oxychloride (3 g/L) or Bordeaux mixture 1% before persistent cool wet rains; pull and bag infected plants.",
        "prevention": "Locate plantings in full sun away from potato fields; drip irrigate only; eliminate volunteer tomato and potato weed hosts.",
        "extension_source": "Cornell University Vegetable MD Online Late Blight"
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "disease": "Leaf Mold",
        "pathogen": "Passalora fulva (Cladosporium fulvum) (Fungus)",
        "severity": "Medium to High (High in polyhouses)",
        "symptoms": "Pale greenish-yellow chlorotic spots on upper leaf surfaces matching olive-green to grayish velvety fungal patches on leaf undersides.",
        "chemical_treatment": "Spray Difenoconazole 25 EC (0.5 ml/L) or Chlorothalonil 75 WP (2 g/L) or Boscalid (0.5 g/L).",
        "organic_treatment": "Bio-fungicide spray of Bacillus subtilis or Copper Octanoate; vent polyhouses to keep relative humidity below 80%.",
        "prevention": "Maximize air circulation; space rows at least 60 cm apart; heat polyhouses slightly at dusk to prevent condensation on foliage.",
        "extension_source": "University of Massachusetts Greenhouse Tomato Diseases"
    },
    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "disease": "Septoria Leaf Spot",
        "pathogen": "Septoria lycopersici (Fungus)",
        "severity": "High",
        "symptoms": "Numerous small circular spots (2-3 mm) with dark brown borders and light gray/tan centers speckled with tiny black fruiting bodies (pycnidia).",
        "chemical_treatment": "Spray Chlorothalonil 75 WP (2 g/L) or Mancozeb 75 WP (2.5 g/L) or Azoxystrobin (1 ml/L) starting at first lower leaf spots.",
        "organic_treatment": "Apply Copper Hydroxide (2 g/L) or Serenade Garden (Bacillus subtilis); prune out affected lower leaves and dispose immediately.",
        "prevention": "Thoroughly clean plant stakes each season; mulch ground under plants; rotate fields away from tomatoes/potatoes for 3 seasons.",
        "extension_source": "University of Minnesota Extension Tomato Leaf Spot"
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato",
        "disease": "Two-Spotted Spider Mite Damage",
        "pathogen": "Tetranychus urticae (Arachnid Pest)",
        "severity": "Medium to High",
        "symptoms": "Fine yellow or white stippling on leaf surfaces, bronze dry appearance, delicate silk webbing on leaf undersides and branch forks.",
        "chemical_treatment": "Apply Spiromesifen 22.9 SC (1 ml/L) or Abamectin 1.9 EC (0.5 ml/L) or Fenpyroximate 5 EC (1 ml/L); rotate chemical modes.",
        "organic_treatment": "Spray insecticidal soap (10 ml/L) or cold-pressed neem oil (5 ml/L) under high pressure hitting undersides; release predatory Phytoseiulus mites.",
        "prevention": "Maintain adequate soil moisture; overhead misting can suppress mite breeding in hot dry conditions; control dusty roads near fields.",
        "extension_source": "ICAR-NBAIR National Bureau of Agricultural Insect Resources"
    },
    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "disease": "Target Spot",
        "pathogen": "Corynespora cassiicola (Fungus)",
        "severity": "Medium to High",
        "symptoms": "Small brown circular lesions with light brown centers and faint concentric rings on leaves and stems; severely affected leaves drop prematurely.",
        "chemical_treatment": "Spray Pyraclostrobin 20 WG (0.5 g/L) or Azoxystrobin + Difenoconazole (1 ml/L) or Chlorothalonil (2 g/L).",
        "organic_treatment": "Apply Copper sulfate pentahydrate or wettable sulfur (2 g/L); spray compost tea enriched with Bacillus spp.",
        "prevention": "Ensure good drainage; avoid high nitrogen fertility which causes dense foliage; prune suckers to improve light penetration.",
        "extension_source": "University of Florida Extension Target Spot of Tomato"
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "disease": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "pathogen": "Begomovirus (Vectored by Whitefly Bemisia tabaci)",
        "severity": "Extreme / Stunting",
        "symptoms": "Severe upward cupping and curling of leaf margins, yellowing (chlorosis) of interveinal leaf tissue, stunted bushy growth, flower abortion.",
        "chemical_treatment": "Control whitefly vector: Spray Diafenthiuron 50 WP (1 g/L) or Dinotefuran 20 SG (0.5 g/L) or Spiromesifen 22.9 SC (1 ml/L).",
        "organic_treatment": "Install 30 yellow sticky traps per acre; spray neem oil 10,000 ppm (2 ml/L) or Beauveria bassiana (5 g/L) against whiteflies.",
        "prevention": "Use 50-mesh insect-proof netting in nurseries; grow TYLCV-resistant hybrids; pull and destroy infected plants immediately.",
        "extension_source": "ICAR-IIHR Tomato Virus Disease Protocol"
    },
    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "disease": "Tomato Mosaic Virus (ToMV)",
        "pathogen": "Tobamovirus (Mechanically transmitted virus)",
        "severity": "High",
        "symptoms": "Mottled light and dark green mosaic patterns on leaves, fern-like distortion (shoestring effect), stunted plant growth, internal fruit browning.",
        "chemical_treatment": "No antiviral cure exists. Wash hands and tools in 20% non-fat dry milk solution or 10% trisodium phosphate (TSP).",
        "organic_treatment": "Apply skim milk spray (100 g dry milk powder per liter) to reduce mechanical transmission during pruning and tying.",
        "prevention": "Do not use tobacco products near plants; disinfect shears and stakes; plant certified resistant varieties (with Tm-2a gene).",
        "extension_source": "Cornell Vegetable MD Online Tomato Mosaic Virus"
    },
    "Tomato___healthy": {
        "crop": "Tomato",
        "disease": "Healthy Plant (No Disease Detected)",
        "pathogen": "None",
        "severity": "Healthy (Optimal)",
        "symptoms": "Robust deep green compound foliage, strong glandular trichomes, vigorous blossoms, and smooth glossy green-to-red fruit formation.",
        "chemical_treatment": "None required.",
        "organic_treatment": "Foliar application of calcium nitrate or eggshell tea at bloom time to prevent blossom end rot.",
        "prevention": "Regular deep watering (avoiding dry-wet cycles); proper trellising; balanced N-P-K nutrition with calcium and magnesium.",
        "extension_source": "ICAR Good Agricultural Practices for Solanaceous Crops"
    }
}

# Ordered class list matching standard PlantVillage dataset (38 classes)
CLASS_NAMES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

def get_solution(class_name: str) -> dict:
    """Retrieve full advisory dictionary for any class with universal key aliases."""
    raw = None
    clean_name = class_name.strip()
    if clean_name in SOLUTIONS_DATABASE:
        raw = SOLUTIONS_DATABASE[clean_name]
    else:
        # Check case-insensitive or partial match
        for k, v in SOLUTIONS_DATABASE.items():
            if k.lower() == clean_name.lower():
                raw = v
                break

    if raw is None:
        parts = clean_name.split("___")
        crop = parts[0].replace("_", " ").title()
        disease = parts[1].replace("_", " ").title() if len(parts) > 1 else "Foliar Condition"
        raw = {
            "crop": crop,
            "disease": disease,
            "pathogen": "Fungal / Bacterial Plant Pathogen",
            "severity": "Medium",
            "symptoms": f"Visible leaf discoloration, chlorotic halos, or necrotic lesions indicative of {disease}.",
            "chemical_treatment": "Consult local Krishi Vigyan Kendra (KVK). Recommended broad-spectrum fungicide: Mancozeb 75% WP (2.5 g/L) or Copper Oxychloride 50 WP (3 g/L).",
            "organic_treatment": "Spray cold-pressed neem oil 10,000 ppm (5 ml/L) + mild liquid soap (1 ml/L). Apply Trichoderma viride to soil and foliage.",
            "prevention": "Ensure proper spacing, crop rotation, and avoid overhead sprinkler watering to reduce humidity.",
            "extension_source": "ICAR-KVK National Advisory Service"
        }

    # Build universal output with both naming styles
    result = dict(raw)
    result["description"] = raw.get("symptoms", "")
    result["organic"] = raw.get("organic_treatment", "")
    result["chemical"] = raw.get("chemical_treatment", "")
    result["source"] = raw.get("extension_source", "ICAR & State Agricultural University Extension")
    
    # Generate clean 3-4 steps for control
    chem = raw.get("chemical_treatment", "")
    org = raw.get("organic_treatment", "")
    prev = raw.get("prevention", "")
    result["steps"] = [
        f"Early Intervention: {org.split('.')[0] if '.' in org else org}.",
        f"Chemical Spray: {chem.split('.')[0] if '.' in chem else chem}.",
        f"Field Sanitation: {prev.split('.')[0] if '.' in prev else prev}.",
        "Monitoring: Inspect lower leaf surfaces every 4-5 days during humid or cloudy weather."
    ]
    return result
