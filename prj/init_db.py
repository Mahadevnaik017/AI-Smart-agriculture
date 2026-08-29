from app import create_app
from models import db, User, Category, Product, MarketPrice, GovtScheme, Announcement, ForumPost, ForumComment, Order, OrderItem, Review, Complaint, Advertisement, AgriQuote
from datetime import datetime, timedelta

app = create_app()

def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        print("[+] Initializing seed database tables...")
        
        # 1. Demo Users
        admin = User(
            name="Mojara Admin Master",
            email="admin@mojara.org",
            role="admin",
            phone="+91 8023456789",
            district="Bengaluru Urban",
            state="Karnataka",
            is_verified=True
        )
        admin.set_password("admin123")
        
        officer = User(
            name="Dr. K. S. Patil (Agri Officer)",
            email="officer@mojara.org",
            role="officer",
            phone="+91 9448012345",
            district="Dharwad",
            state="Karnataka",
            is_verified=True
        )
        officer.set_password("officer123")
        
        farmer1 = User(
            name="Ramesh Gowda",
            email="farmer@mojara.org",
            role="farmer",
            phone="+91 9845012345",
            address="Village Dodda Byranahalli, Mandya District",
            district="Mandya",
            state="Karnataka",
            is_verified=True
        )
        farmer1.set_password("farmer123")
        
        farmer2 = User(
            name="Basavarajappa H.",
            email="farmer2@mojara.org",
            role="farmer",
            phone="+91 9741098765",
            address="Post Hirekerur, Haveri District",
            district="Haveri",
            state="Karnataka",
            is_verified=True
        )
        farmer2.set_password("farmer123")
        
        buyer = User(
            name="Suma Reddy",
            email="buyer@mojara.org",
            role="buyer",
            phone="+91 9880123456",
            address="Flat 402, Green Acres Apt, Indiranagar, Bengaluru",
            district="Bengaluru Urban",
            state="Karnataka",
            is_verified=True
        )
        buyer.set_password("buyer123")
        
        db.session.add_all([admin, officer, farmer1, farmer2, buyer])
        db.session.commit()
        print("[OK] Demo Users seeded.")
        
        # 2. Categories
        cat_crops = Category(name="Fresh Crops", name_kn="ತಾಜಾ ಬೆಳೆಗಳು", description="Directly harvested grains, pulses, fruits and vegetables", icon="fa-wheat-awn")
        cat_seeds = Category(name="Certified Seeds", name_kn="ಪ್ರಮಾಣೀಕೃತ ಬೀಜಗಳು", description="High yielding hybrid and heirloom seeds", icon="fa-seedling")
        cat_fertilizer = Category(name="Bio Fertilizers", name_kn="ಸಾವಯವ ಗೊಬ್ಬರಗಳು", description="Soil boosters, vermicompost and NPK complexes", icon="fa-flask-vial")
        cat_tools = Category(name="Agri Tools & Equipment", name_kn="ಕೃಷಿ ಉಪಕರಣಗಳು", description="Sprayers, drip kits, spades, harvest nets", icon="fa-tractor")
        cat_pesticides = Category(name="Bio Pesticides", name_kn="ಜೈವಿಕ ಕೀಟನಾಶಕಗಳು", description="Neem oil extracts and eco-friendly fungicides", icon="fa-shield-halved")
        
        db.session.add_all([cat_crops, cat_seeds, cat_fertilizer, cat_tools, cat_pesticides])
        db.session.commit()
        print("[OK] Categories seeded.")
        
        # 3. Products
        products = [
            Product(
                farmer_id=farmer1.id,
                category_id=cat_crops.id,
                title="Organic Mandya Finger Millet (Ragi)",
                title_kn="ಮಂಡ್ಯ ಸಾವಯವ ರಾಗಿ",
                description="100% Organically cultivated native Mandya Ragi. Rich in calcium, iron, and fiber.",
                price=65.0,
                unit="kg",
                stock_quantity=500,
                district="Mandya",
                is_organic=True,
                image_url="/static/images/crops/ragi.jpg",
                status="approved"
            ),
            Product(
                farmer_id=farmer1.id,
                category_id=cat_crops.id,
                title="Farm Fresh Red Tomatoes (Grade A)",
                title_kn="ಫ್ರೆಶ್ ಕೆಂಪು ಟೊಮೆಟೊ",
                description="Sun-ripened firm red tomatoes direct from farm fields. Ideal for commercial cooking and sauces.",
                price=32.0,
                unit="kg",
                stock_quantity=1200,
                district="Mandya",
                is_organic=False,
                image_url="/static/images/crops/tomatoes.jpg",
                status="approved"
            ),
            Product(
                farmer_id=farmer2.id,
                category_id=cat_crops.id,
                title="Premium Sona Masoori Rice (Raw Paddy)",
                title_kn="ಪ್ರೀಮಿಯಂ ಸೋನಾ ಮಸೂರಿ ಅಕ್ಕಿ",
                description="Aromatic, medium-grain 12-month aged Sona Masoori raw rice. Low GI, fluffy texture.",
                price=54.0,
                unit="kg",
                stock_quantity=2500,
                district="Haveri",
                is_organic=True,
                image_url="/static/images/crops/rice.jpg",
                status="approved"
            ),
            Product(
                farmer_id=farmer2.id,
                category_id=cat_seeds.id,
                title="Hybrid Bt Cotton Seeds (High Yield - 450g Pack)",
                title_kn="ಹೈಬ್ರಿಡ್ ಬಿಟಿ ಹತ್ತಿ ಬೀಜಗಳು",
                description="Drought-tolerant high lint percentage cotton seeds treated with bio-fungicide.",
                price=850.0,
                unit="bag",
                stock_quantity=80,
                district="Haveri",
                is_organic=False,
                image_url="/static/images/crops/bt_cotton_seeds.jpg",
                status="approved"
            ),
            Product(
                farmer_id=farmer1.id,
                category_id=cat_fertilizer.id,
                title="Pure Enriched Vermicompost (50kg Bag)",
                title_kn="ಪ್ರೀಮಿಯಂ ಎರೆಹುಳು ಗೊಬ್ಬರ",
                description="Earthworm processed 100% organic soil amendment. Restores soil microbial flora and NPK availability.",
                price=480.0,
                unit="bag",
                stock_quantity=150,
                district="Mandya",
                is_organic=True,
                image_url="/static/images/crops/vermicompost.jpg",
                status="approved"
            ),
            Product(
                farmer_id=farmer2.id,
                category_id=cat_tools.id,
                title="Battery Powered Knapsack Agri Sprayer (16 Litres)",
                title_kn="ಬ್ಯಾಟರಿ ಆಧಾರಿತ ಕೃಷಿ ಸ್ಪೇರ್",
                description="Heavy duty 12V 8Ah battery agricultural sprayer with stainless steel lance and 4 nozzles.",
                price=2650.0,
                unit="piece",
                stock_quantity=25,
                district="Haveri",
                is_organic=False,
                image_url="/static/images/crops/sprayer.jpg",
                status="approved"
            ),
            Product(
                farmer_id=farmer1.id,
                category_id=cat_pesticides.id,
                title="Neem Oil Bio-Pesticide (10,000 PPM - 1 Litre)",
                title_kn="ಸಾವಯವ ಬೇವಿನ ಎಣ್ಣೆ ಕೀಟನಾಶಕ",
                description="Cold pressed pure neem seed oil concentrate. Effective against aphids, whiteflies, thrips and leaf miners.",
                price=340.0,
                unit="bottle",
                stock_quantity=90,
                district="Mandya",
                is_organic=True,
                image_url="/static/images/crops/neem_oil.jpg",
                status="approved"
            )
        ]
        db.session.add_all(products)
        db.session.commit()
        print("[OK] Products seeded.")
        
        # 4. APMC Market Prices
        prices = [
            MarketPrice(commodity="Finger Millet (Ragi)", commodity_kn="ರಾಗಿ", district="Mandya", mandi_name="Mandya APMC", min_price=3200, max_price=3850, modal_price=3600),
            MarketPrice(commodity="Paddy (Sona Masoori)", commodity_kn="ಭತ್ತ (ಸೋನಾ ಮಸೂರಿ)", district="Haveri", mandi_name="Haveri APMC", min_price=2400, max_price=2950, modal_price=2750),
            MarketPrice(commodity="Tomato", commodity_kn="ಟೊಮೆಟೊ", district="Kolar", mandi_name="Kolar APMC", min_price=1800, max_price=3200, modal_price=2500),
            MarketPrice(commodity="Maize", commodity_kn="ಮೆಕ್ಕೆಜೋಳ", district="Davanagere", mandi_name="Davanagere APMC", min_price=1900, max_price=2350, modal_price=2180),
            MarketPrice(commodity="Cotton", commodity_kn="ಹತ್ತಿ", district="Dharwad", mandi_name="Hubballi APMC", min_price=6800, max_price=7900, modal_price=7450),
            MarketPrice(commodity="Onion", commodity_kn="ಈರುಳ್ಳಿ", district="Chitradurga", mandi_name="Chitradurga APMC", min_price=1500, max_price=2600, modal_price=2200),
            MarketPrice(commodity="Arecanut (Betel Nut)", commodity_kn="ಅಡಿಕೆ", district="Shimoga", mandi_name="Shivamogga APMC", min_price=42000, max_price=51000, modal_price=47500)
        ]
        db.session.add_all(prices)
        
        # 5. Expanded Government Schemes (Including Bhoomi & Raitha Siri Schemes)
        schemes = [
            GovtScheme(
                title="Karnataka Raitha Siri Scheme (Millet Growers Cash Incentive)",
                title_kn="ಕರ್ನಾಟಕ ರೈತ ಸಿರಿ ಯೋಜನೆ (ಸಿರಿಧಾನ್ಯ ಬೆಳೆಗಾರರಿಗೆ ಪ್ರೋತ್ಸಾಹಧನ)",
                category="Financial Subsidy",
                description="Karnataka Government's flagship millet promotion scheme providing a direct financial incentive of Rs 10,000 per hectare directly into bank accounts of farmers cultivating minor millets (Ragi, Navane, Same, Sajje, Haraka, Baragu).",
                description_kn="ಸಿರಿಧಾನ್ಯಗಳನ್ನು (ರಾಗಿ, ನವಣೆ, ಸಾಮೆ, ಸಜ್ಜೆ, ಹರಕ, ಬರಗು) ಬೆಳೆಯುವ ರೈತರಿಗೆ ಹೆಕ್ಟೇರ್‌ಗೆ 10,000 ರೂ.ಗಳ ನೇರ ಪ್ರೋತ್ಸಾಹಧನ ಯೋಜನೆಯಾಗಿದೆ.",
                eligibility="Farmers in Karnataka cultivating minor millets with registered Pahani RTC in Fruits Portal.",
                benefit_amount="Rs 10,000 / Hectare (Direct Bank Transfer)",
                apply_link="https://raitamitra.karnataka.gov.in",
                officer_contact="Toll-Free Helpline: 1800-425-3553 / Local Raitha Samparka Kendra"
            ),
            GovtScheme(
                title="Karnataka Bhoomi Scheme (Online Pahani RTC & Land Records Portal)",
                title_kn="ಕರ್ನಾಟಕ ಭೂಮಿ ಯೋಜನೆ (ಆನ್‌ಲೈನ್ ಪಹಣಿ ಆರ್‌ಟಿಸಿ ಮತ್ತು ಭೂ ದಾಖಲೆಗಳ ಪೋರ್ಟಲ್)",
                category="Land Records & Property",
                description="Karnataka Government's flagship Bhoomi project providing digital Pahani RTC land ownership records, revenue survey maps, online mutation status tracking, and direct linking for Parihara drought compensation payout.",
                description_kn="ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಬೃಹತ್ ಯೋಜನೆ: ಡಿಜಿಟಲ್ ಭೂಮಿ ಪೋರ್ಟಲ್ ಮೂಲಕ ಆನ್‌ಲೈನ್ ಪಹಣಿ (RTC), ಹಕ್ಕು ಬದಲಾವಣೆ ಮತ್ತು ಪರಿಹಾರ ಹಣದ ತಕ್ಷಣದ ಪರಿಶೀಲನೆ.",
                eligibility="All agricultural land holding farmers across all 31 districts of Karnataka possessing Survey Number & Hissa.",
                benefit_amount="Instant Digital Pahani RTC & Direct Parihara Relief Payout",
                apply_link="https://bhoomi.karnataka.gov.in",
                officer_contact="Bhoomi Helpline: 080-22113255 / District Tahsildar Office"
            ),
            GovtScheme(
                title="PM-KISAN Samman Nidhi Scheme",
                title_kn="ಪಿಎಂ-ಕಿಸಾನ್ ಸಮ್ಮಾನ್ ನಿಧಿ ಯೋಜನೆ",
                category="Financial Subsidy",
                description="Direct cash transfer of Rs 6,000 per year in 3 equal installments of Rs 2,000 directly into Aadhaar-linked bank accounts of landholding farmers.",
                description_kn="ಎಲ್ಲಾ ಭೂಮಿಯನ್ನು ಹೊಂದಿರುವ ರೈತ ಕುಟುಂಬಗಳಿಗೆ ವರ್ಷಕ್ಕೆ 6,000 ರೂ.ಗಳ ನೇರ ಆದಾಯ ಸಹಾಯಧನ (ವರ್ಷಕ್ಕೆ 3 ಕಂತುಗಳು).",
                eligibility="Small & Marginal farmers holding cultivable land record (Pahani / RTC in Karnataka).",
                benefit_amount="Rs 6,000 / year (Direct Bank Transfer)",
                apply_link="https://pmkisan.gov.in",
                officer_contact="Helpline: 155261 / Raitha Samparka Kendra"
            ),
            GovtScheme(
                title="Karnataka Krishi Bhagya Scheme (Farm Ponds & Drip Irrigation)",
                title_kn="ಕರ್ನಾಟಕ ಕೃಷಿ ಭಾಗ್ಯ ಯೋಜನೆ (ಕೃಷಿ ಹೊಂಡ ಮತ್ತು ಹನಿ ನೀರಾವರಿ)",
                category="Irrigation & Water Conservation",
                description="State subsidy up to 80% for constructing polythene-lined farm ponds (Krishi Houda), diesel/solar pump sets, micro-drip networks, and polyhouses in rainfed districts.",
                description_kn="ಮಳೆ ಆಶ್ರಿತ ಕೃಷಿ ಪ್ರದೇಶಗಳಲ್ಲಿ ಕೃಷಿ ಹೊಂಡ ನಿರ್ಮಾಣ, ಡೀಸೆಲ್/ಸೋಲಾರ್ ಪಂಪ್‌ಸೆಟ್ ಮತ್ತು ಹನಿ ನೀರಾವರಿಗೆ 80% ಸಬ್ಸಿಡಿ.",
                eligibility="Rainfed agriculture farmers in notified dryland districts of Karnataka with Pahani RTC.",
                benefit_amount="50% to 80% Subsidy (Up to Rs 1.75 Lakhs)",
                apply_link="https://raitamitra.karnataka.gov.in",
                officer_contact="District Agriculture Officer / Assistant Director of Agriculture"
            ),
            GovtScheme(
                title="PM Fasal Bima Yojana (Comprehensive Crop Insurance)",
                title_kn="ಪ್ರಧಾನ ಮಂತ್ರಿ ಫಸಲ್ ಭೀಮಾ ಯೋಜನೆ (ಬೆಳೆ ವಿಮೆ)",
                category="Crop Insurance",
                description="Comprehensive insurance protection against crop loss due to flood, drought, hail, pests, or unseasonal rains with low farmer premium rates (1.5% for Rabi, 2% for Kharif).",
                description_kn="ಬರ, ಪ್ರವಾಹ ಮತ್ತು ಕೀಟಬಾಧೆಯಿಂದ ಉಂಟಾಗುವ ಬೆಳೆ ನಷ್ಟಕ್ಕೆ ಕನಿಷ್ಠ ಪ್ರೀಮಿಯಂ ದರದಲ್ಲಿ 100% ವಿಮಾ ರಕ್ಷಣೆ.",
                eligibility="All farmers growing notified crops (Paddy, Ragi, Maize, Cotton, Onion) in notified gram panchayats.",
                benefit_amount="100% Sum Insured Coverage (Up to Rs 45,000/acre)",
                apply_link="https://pmfby.gov.in",
                officer_contact="Common Service Centers (CSC) / Local Bank Branch"
            ),
            GovtScheme(
                title="Soil Health Card Scheme (Soil NPK Testing & Fertilizer Card)",
                title_kn="ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ ಯೋಜನೆ",
                category="Soil Health & Testing",
                description="Free soil sampling and lab analysis reporting 12 soil parameters (pH, EC, N, P, K, S, Zn, Fe, Cu, Mn, B) with custom crop fertilizer recommendations.",
                description_kn="ಉಚಿತ ಮಣ್ಣಿನ ಪರೀಕ್ಷೆ ಮತ್ತು 12 ಮಣ್ಣಿನ ನಿಯತಾಂಕಗಳ ಸಮಗ್ರ ವರದಿ ಹಾಗೂ ಗೊಬ್ಬರ ಶಿಫಾರಸು ಕಾರ್ಡ್.",
                eligibility="All farmers across all districts of Karnataka.",
                benefit_amount="Free Soil Lab Testing & Custom Fertilizer Report",
                apply_link="https://soilhealth.dac.gov.in",
                officer_contact="Local Raitha Samparka Kendra Soil Testing Lab"
            ),
            GovtScheme(
                title="Chief Minister Raitha Vidya Nidhi (Farmer Children Scholarship)",
                title_kn="ಮುಖ್ಯಮಂತ್ರಿ ರೈತ ವಿದ್ಯಾ ನಿಧಿ ಯೋಜನೆ (ವಿದ್ಯಾರ್ಥಿವೇತನ)",
                category="Student Scholarship",
                description="Financial scholarship for children of registered farmers pursuing higher education from SSLC/High School up to Post Graduation and Professional Degrees.",
                description_kn="ರೈತರ ಮಕ್ಕಳಿಗೆ ಪಿಯುಸಿ, ಐಟಿಐ, ಡಿಪ್ಲೊಮಾ, ಪದವಿ ಹಾಗೂ ವೃತ್ತಿಪರ ಶಿಕ್ಷಣಕ್ಕಾಗಿ ಉಚಿತ ವಿದ್ಯಾರ್ಥಿವೇತನ ಸಹಾಯಧನ.",
                eligibility="Children of farmers registered under the Fruits Portal (FID ID in Karnataka).",
                benefit_amount="Rs 2,500 to Rs 11,000 / year",
                apply_link="https://ssp.postmatric.karnataka.gov.in",
                officer_contact="State Scholarship Portal Helpline / Department of Agriculture"
            ),
            GovtScheme(
                title="PM Krishi Sinchayee Yojana (Per Drop More Crop - Drip Subsidy)",
                title_kn="ಪ್ರಧಾನ ಮಂತ್ರಿ ಕೃಷಿ ಸಿಂಚಾಯಿ ಯೋಜನೆ (ಹನಿ ನೀರಾವರಿ ಸಬ್ಸಿಡಿ)",
                category="Irrigation & Water Conservation",
                description="90% subsidy for Small & Marginal farmers and 80% subsidy for General farmers for installing micro-drip and sprinkler irrigation equipment.",
                description_kn="ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ಹನಿ ಮತ್ತು ತುಂತುರು ನೀರಾವರಿ ಅಳವಡಿಸಲು 90% ಸಬ್ಸಿಡಿ ಧನಸಹಾಯ.",
                eligibility="Farmers possessing cultivable agricultural land with water source (well/borewell/canal).",
                benefit_amount="90% Subsidy on Drip & Sprinkler Systems",
                apply_link="https://pmksy.gov.in",
                officer_contact="Horticulture / Agriculture Department Field Officer"
            ),
            GovtScheme(
                title="Sub-Mission on Agricultural Mechanization (SMAM Machinery Subsidy)",
                title_kn="ಕೃಷಿ ಯಾಂತ್ರೀಕರಣ ಯೋಜನೆ (ಟ್ರ್ಯಾಕ್ಟರ್ ಮತ್ತು ಯಂತ್ರೋಪಕರಣ ಸಬ್ಸಿಡಿ)",
                category="Mechanization & Tools",
                description="50% subsidy on purchase of agricultural tractors, power tillers, rotavators, multi-crop threshers, and power sprayers.",
                description_kn="ಟ್ರ್ಯಾಕ್ಟರ್, ಪವರ್ ಟಿಲ್ಲರ್, ರೋಟವೇಟರ್ ಮತ್ತು ಕೃಷಿ ಯಂತ್ರೋಪಕರಣಗಳ ಖರೀದಿಗೆ 50% ಸರ್ಕಾರಿ ಸಬ್ಸಿಡಿ.",
                eligibility="Individual farmers, Self-Help Groups (SHGs), and Farmer Producer Organizations (FPOs).",
                benefit_amount="50% Subsidy (Up to Rs 3.0 Lakhs)",
                apply_link="https://agrimachinery.nic.in",
                officer_contact="Assistant Director of Agriculture (Mechanization Cell)"
            ),
            GovtScheme(
                title="Paramparagat Krishi Vikas Yojana (PKVY Organic Farming Cluster)",
                title_kn="ಪರಂಪರಾಗತ ಕೃಷಿ ವಿಕಾಸ ಯೋಜನೆ (ಸಾವಯವ ಕೃಷಿ ಪ್ರೋತ್ಸಾಹ)",
                category="Organic Farming",
                description="Financial support of Rs 50,000 per hectare over 3 years for organic farming clusters, organic seed procurement, bio-inputs, and PGS organic certification.",
                description_kn="ಸಾವಯವ ಕೃಷಿ ಕ್ಲಸ್ಟರ್‌ಗಳಿಗೆ, ಸಾವಯವ ಬಿತ್ತನೆ ಬೀಜ ಮತ್ತು ಬಯೋ-ಇನ್‌ಪುಟ್‌ಗಳಿಗೆ ಹೆಕ್ಟೇರ್‌ಗೆ 50,000 ರೂ. ಸಹಾಯಧನ.",
                eligibility="Farmer clusters having minimum 20 hectares land formed under PKVY organic groups.",
                benefit_amount="Rs 50,000 / Hectare over 3 Years",
                apply_link="https://pgsindia-ncof.gov.in",
                officer_contact="District Organic Farming Cell Officer"
            ),
            GovtScheme(
                title="Mukhyamantri Anugraha Yojane (Livestock Damage Compensation)",
                title_kn="ಮುಖ್ಯಮಂತ್ರಿ ಅನುಗ್ರಹ ಯೋಜನೆ (ಜಾನುವಾರು ನಷ್ಟ ಪರಿಹಾರ)",
                category="Financial Subsidy",
                description="Immediate financial compensation of Rs 10,000 for death of cattle/buffalo and Rs 5,000 for death of sheep/goat owned by small farmers.",
                description_kn="ಆಕಳು, ಎಮ್ಮೆ ಮರಣ ಹೊಂದಿದರೆ 10,000 ರೂ. ಮತ್ತು ಕುರಿ, ಮೇಕೆಗೆ 5,000 ರೂ.ಗಳ ತಕ್ಷಣದ ಆರ್ಥಿಕ ಪರಿಹಾರ.",
                eligibility="All livestock-owning farmers in Karnataka.",
                benefit_amount="Rs 5,000 to Rs 10,000 per animal",
                apply_link="https://ahvs.karnataka.gov.in",
                officer_contact="Veterinary Officer / Local Veterinary Dispensary"
            )
        ]
        db.session.add_all(schemes)
        
        # 6. Announcements
        announcement = Announcement(
            officer_id=officer.id,
            title="Advisory: Fall Armyworm Advisory for Maize Farmers in North Karnataka",
            title_kn="ಉತ್ತರ ಕರ್ನಾಟಕದ ಮೆಕ್ಕೆಜೋಳ ಬೆಳೆಗಾರರಿಗೆ ಕೀಟಬಾಧೆ ಮುನ್ನೆಚ್ಚರಿಕೆ",
            content="Agricultural Department advises early scouting for Fall Armyworm in maize fields. Spray Emamectin Benzoate 5% SG @ 0.4g/L at whorl stage if larvae count exceeds threshold.",
            district="Dharwad",
            priority="High"
        )
        db.session.add_all([announcement])
        
        # 7. Forum Posts & Comments
        post1 = ForumPost(
            user_id=farmer1.id,
            title="Best organic remedy for tomato leaf curl virus?",
            content="My tomato patch is showing severe upward leaf curling in young shoots. I prefer organic methods over heavy chemicals. Any suggestions from agri officers?",
            category="Pest Control"
        )
        db.session.add(post1)
        db.session.commit()
        
        comment1 = ForumComment(
            post_id=post1.id,
            user_id=officer.id,
            comment="Namaste Ramesh avare. Leaf curl is transmitted by whiteflies. Install yellow sticky traps (15 per acre) immediately and spray Neem oil (10,000 ppm) @ 2ml per litre of water twice a week.",
            is_officer_verified=True
        )
        db.session.add(comment1)
        
        # 8. Sample Orders
        order1 = Order(
            buyer_id=buyer.id,
            total_amount=1330.0,
            shipping_address="Flat 402, Green Acres Apt, Indiranagar, Bengaluru - 560038",
            payment_method="UPI",
            payment_status="Completed",
            order_status="Delivered",
            created_at=datetime.utcnow() - timedelta(days=2)
        )
        db.session.add(order1)
        db.session.commit()
        
        item1 = OrderItem(
            order_id=order1.id,
            product_id=products[0].id,
            farmer_id=farmer1.id,
            quantity=10,
            price_per_unit=65.0,
            subtotal=650.0
        )
        item2 = OrderItem(
            order_id=order1.id,
            product_id=products[4].id,
            farmer_id=farmer1.id,
            quantity=1,
            price_per_unit=480.0,
            subtotal=480.0
        )
        db.session.add_all([item1, item2])
        
        # 9. Sample Advertisements
        ad1 = Advertisement(
            title="Subsidized Drip Irrigation Kits for Karnataka Farmers",
            image_url="https://images.unsplash.com/photo-1563514227147-6d2ff665a6a0?auto=format&fit=crop&w=1200&q=80",
            target_url="/schemes",
            location_banner="home_top",
            is_active=True
        )
        db.session.add(ad1)

        # 10. Sample Agricultural Quotes / Statements
        quotes = [
            AgriQuote(
                quote_text="Jai Jawan, Jai Kisan – Farmers are the true backbone of India's prosperity & food dignity.",
                author_source="Lal Bahadur Shastri",
                category="Indian Agriculture"
            ),
            AgriQuote(
                quote_text="Agriculture is our wisest pursuit; it contributes most to real national wealth and sustainable living.",
                author_source="National Farmers Commission",
                category="Sustainability"
            ),
            AgriQuote(
                quote_text="To a farmer, soil is not dirt—it is the living seedbed of life and foundation of human survival.",
                author_source="ICAR Soil Mission",
                category="Food Security"
            ),
            AgriQuote(
                quote_text="Sustainable farming feeds the present without stealing soil fertility from future generations.",
                author_source="Krishi Vigyan Kendra",
                category="Sustainability"
            ),
            AgriQuote(
                quote_text="Technology in the hands of a farmer transforms arduous labor into smart, bountiful harvests.",
                author_source="AgriTech Innovation Forum",
                category="Technology"
            ),
            AgriQuote(
                quote_text="Agriculture is the greatest art on earth, silently nourishing billions with every sunrise.",
                author_source="Rural Development Trust",
                category="Rural Development"
            ),
            AgriQuote(
                quote_text="Empowering smallholder farmers secures family dignity and economic resilience across rural India.",
                author_source="NABARD Agricultural Board",
                category="Rural Development"
            )
        ]
        db.session.add_all(quotes)
        
        db.session.commit()
        print("[SUCCESS] Seeding completed with 7 meaningful agricultural quotes and verified datasets!")

if __name__ == '__main__':
    seed_database()
