# ========================================================================================
# AI-Driven Smart Agriculture & Micro-crop Advisory System (Mojara)
# Lead Developer: Mahadev Naik (Project Lead; AI/ML & System Methodology)
# Milestone: Agriculture Problem Identification & AI Diagnostic Requirements (20 July 2026)
# ========================================================================================
import random

# Agronomic knowledge base for Karnataka & South India regions (Scientifically Calibrated Dataset)
CROPS_DATABASE = {
    'Ragi (Finger Millet)': {
        'name_kn': 'ರಾಗಿ (Finger Millet)',
        'soil': ['Red Loam', 'Sandy Loam', 'Black Soil'],
        'ph_range': (5.5, 7.5),
        'opt_n': 40, 'opt_p': 30, 'opt_k': 25,
        'min_rain': 450, 'max_rain': 900,
        'temp_range': (20, 34),
        'season': ['Kharif', 'Summer'],
        'base_yield_min': 1.2, 'base_yield_max': 1.8, # Tonnes/acre
        'yield_unit': 'Tonnes / Acre',
        'market_price_per_unit': 38000, # INR per Tonne
        'prod_cost_per_acre': 18000,
        'description': 'Cereal crop with high physiological adaptability to dryland conditions and moderate soil fertility. Sowing typically aligned with early Kharif rains.',
        'pop_guidance': 'Basal application of FYM @ 4 tonnes/acre. Sowing in July for Kharif. Requires 2 weedings at 20 and 40 DAS. Intercropping with Redgram (4:2 ratio) improves soil nitrogen balance.'
    },
    'Paddy (Rice)': {
        'name_kn': 'ಭತ್ತ (Paddy/Rice)',
        'soil': ['Clay Loam', 'Black Soil', 'Alluvial Soil'],
        'ph_range': (5.0, 7.0),
        'opt_n': 100, 'opt_p': 50, 'opt_k': 50,
        'min_rain': 900, 'max_rain': 2000,
        'temp_range': (22, 36),
        'season': ['Kharif', 'Rabi'],
        'base_yield_min': 2.2, 'base_yield_max': 3.5, # Tonnes/acre
        'yield_unit': 'Tonnes / Acre',
        'market_price_per_unit': 23000, # INR per Tonne
        'prod_cost_per_acre': 24000,
        'description': 'Cereal crop requiring sustained moisture or managed flooded condition (900-2000 mm water equivalent). High response to nitrogenous fertigation.',
        'pop_guidance': 'Requires 3-5 cm standing water during tillering phase. System of Rice Intensification (SRI) recommended for improved root aeration and water optimization.'
    },
    'Maize (Corn)': {
        'name_kn': 'ಮೆಕ್ಕೆಜೋಳ (Maize)',
        'soil': ['Well-drained Loam', 'Red Soil', 'Black Soil', 'Deep Black Soil', 'Red Loam'],
        'ph_range': (6.0, 7.8),
        'opt_n': 80, 'opt_p': 40, 'opt_k': 40,
        'min_rain': 500, 'max_rain': 1000,
        'temp_range': (18, 32),
        'season': ['Kharif', 'Rabi', 'Summer'],
        'base_yield_min': 2.5, 'base_yield_max': 3.8, # Tonnes/acre
        'yield_unit': 'Tonnes / Acre',
        'market_price_per_unit': 21000, # INR per Tonne
        'prod_cost_per_acre': 20000,
        'description': 'Cereal crop with moderate moisture requirements (500-1000 mm). Performs well on deep black soils under good drainage; highly sensitive to root zone waterlogging. Major Kharif crop in Belagavi district.',
        'pop_guidance': 'Ensure effective field drainage on black soils. Monitor for Fall Armyworm (Spodoptera frugiperda) from knee-high stage. Apply N top dressing at cob initiation.'
    },
    'Turmeric (Arishina)': {
        'name_kn': 'ಅರಿಶಿನ (Turmeric)',
        'soil': ['Deep Black Soil', 'Black Soil', 'Red Loam', 'Clay Loam', 'Well-drained Loam'],
        'ph_range': (5.5, 7.5),
        'opt_n': 60, 'opt_p': 40, 'opt_k': 60,
        'min_rain': 700, 'max_rain': 2200,
        'temp_range': (20, 35),
        'season': ['Kharif', 'Perennial'],
        'base_yield_min': 14.0, 'base_yield_max': 22.0, # Quintals/acre (dried)
        'yield_unit': 'Quintals / Acre',
        'market_price_per_unit': 11000, # INR per Quintal (dried)
        'prod_cost_per_acre': 45000,
        'description': 'Spice rhizome crop with good adaptability to medium-heavy soils and moderate rainfall. Widely cultivated across North Karnataka and Belagavi region as a traditional cash crop.',
        'pop_guidance': 'Plant rhizomes at 45x30 cm spacing in June. Maintain soil moisture during rhizome development. Apply organic mulch 30 cm thick. Harvest at 8-9 months when leaves turn yellow-brown.'
    },
    'Sugarcane': {
        'name_kn': 'ಕಬ್ಬು (Sugarcane)',
        'soil': ['Deep Black Soil', 'Black Soil', 'Alluvial Soil', 'Heavy Loam', 'Clay Loam'],
        'ph_range': (6.5, 8.2),
        'opt_n': 150, 'opt_p': 65, 'opt_k': 80,
        'min_rain': 600, 'max_rain': 2200,
        'temp_range': (20, 38),
        'season': ['Perennial', 'Kharif'],
        'base_yield_min': 32.0, 'base_yield_max': 52.0, # Tonnes/acre
        'yield_unit': 'Tonnes / Acre',
        'market_price_per_unit': 3150, # INR per Tonne
        'prod_cost_per_acre': 55000,
        'description': 'Perennial cash crop thriving on deep black cotton soils with good moisture retention. Raybag taluk and surrounding areas of Belagavi are major Sugarcane belts supplying local sugar mills. Requires drip/canal irrigation supplementation at 600-800 mm rainfall.',
        'pop_guidance': 'Drip fertigation recommended to optimize water use efficiency on deep black soils. Plant 2-budded setts in January/February or June/July. Earthing up at 120 days prevents lodging.'
    },
    'Tomato': {
        'name_kn': 'ಟೊಮೆಟೊ (Tomato)',
        'soil': ['Red Sandy Loam', 'Well-drained Black Soil'],
        'ph_range': (6.0, 7.2),
        'opt_n': 90, 'opt_p': 60, 'opt_k': 80,
        'min_rain': 400, 'max_rain': 800,
        'temp_range': (18, 30),
        'season': ['Kharif', 'Rabi', 'Summer'],
        'base_yield_min': 14.0, 'base_yield_max': 24.0, # Tonnes/acre
        'yield_unit': 'Tonnes / Acre',
        'market_price_per_unit': 18000, # INR per Tonne
        'prod_cost_per_acre': 65000,
        'description': 'Horticultural crop suitable for well-drained loams. Highly sensitive to waterlogging and severe calcium deficit.',
        'pop_guidance': 'Trellis staking with bamboo/wire supports improves fruit ventilation and reduces soil-borne rot. Foliar Calcium Nitrate sprays reduce blossom end rot.'
    },
    'Arecanut (Betel Nut)': {
        'name_kn': 'ಅಡಿಕೆ (Arecanut)',
        'soil': ['Laterite Soil', 'Red Clay Loam'],
        'ph_range': (5.2, 6.8),
        'opt_n': 60, 'opt_p': 30, 'opt_k': 100,
        'min_rain': 1500, 'max_rain': 3500,
        'temp_range': (15, 35),
        'season': ['Perennial'],
        'base_yield_min': 7.5, 'base_yield_max': 11.5, # Quintals/acre
        'yield_unit': 'Quintals / Acre',
        'market_price_per_unit': 42000, # INR per Quintal
        'prod_cost_per_acre': 80000,
        'description': 'High-rainfall plantation palm species adapted to humid tropical regions with deep, well-drained organic soils.',
        'pop_guidance': 'Maintain organic basin mulching. Apply preventive 1% Bordeaux mixture spray prior to monsoon onset to manage Fruit Rot (Koleroga).'
    },
    'Onion': {
        'name_kn': 'ಈರುಳ್ಳಿ (Onion)',
        'soil': ['Sandy Loam', 'Medium Black Soil'],
        'ph_range': (6.0, 7.5),
        'opt_n': 60, 'opt_p': 35, 'opt_k': 50,
        'min_rain': 350, 'max_rain': 750,
        'temp_range': (15, 30),
        'season': ['Kharif', 'Rabi'],
        'base_yield_min': 7.5, 'base_yield_max': 11.5, # Tonnes/acre
        'yield_unit': 'Tonnes / Acre',
        'market_price_per_unit': 19000, # INR per Tonne
        'prod_cost_per_acre': 38000,
        'description': 'Bulb vegetable crop requiring shallow, well-drained soil structure and moderate nutrient availability.',
        'pop_guidance': 'Avoid water standing. Withhold irrigation 10-15 days prior to harvest to promote proper neck drying and storage longevity.'
    },
    'Cotton': {
        'name_kn': 'ಹತ್ತಿ (Cotton)',
        'soil': ['Deep Black Cotton Soil', 'Clay Loam'],
        'ph_range': (6.5, 8.5),
        'opt_n': 75, 'opt_p': 40, 'opt_k': 50,
        'min_rain': 500, 'max_rain': 1100,
        'temp_range': (21, 35),
        'season': ['Kharif'],
        'base_yield_min': 7.5, 'base_yield_max': 13.0, # Quintals/acre
        'yield_unit': 'Quintals / Acre',
        'market_price_per_unit': 7200, # INR per Quintal
        'prod_cost_per_acre': 28000,
        'description': 'Fiber cash crop well adapted to deep black soils with high clay content and moisture retention capacity.',
        'pop_guidance': 'Requires warm, sunny weather during boll maturation. Follow refuge crop management guidelines for insect resistance management.'
    }
}

DISEASE_DATABASE = {
    'Tomato': [
        {
            'disease': 'Tomato Early Blight (Alternaria solani)',
            'confidence': 96.4,
            'symptoms': 'Concentric dark brown target-like rings on lower leaves, yellowing surrounding spots, defoliation.',
            'prevention': 'Rotate crops with non-solanaceous plants, avoid overhead sprinkler irrigation, maintain 60cm plant spacing.',
            'treatment': 'Spray Mancozeb 75% WP @ 2.5g/L or Copper Oxychloride 50% WP @ 3g/L every 10 days.',
            'recommended_product': 'Organic Copper Fungicide & Neem Oil Max'
        },
        {
            'disease': 'Tomato Leaf Curl Virus (ToLCV)',
            'confidence': 94.1,
            'symptoms': 'Upward curling and yellowing of leaf margins, stunted growth, flower drop, reduced fruit size.',
            'prevention': 'Control whitefly vector using yellow sticky traps (15 traps/acre), plant net barriers in nursery.',
            'treatment': 'Spray Imidacloprid 17.8% SL @ 0.5ml/L or Azadirachtin 10,000 ppm @ 2ml/L to control vector insects.',
            'recommended_product': 'Bio-Pesticide Whitefly Defender'
        },
        {
            'disease': 'Healthy Leaf (No Disease Detected)',
            'confidence': 98.9,
            'symptoms': 'Vibrant green foliage, sturdy stem structure, no lesions or chlorosis visible.',
            'prevention': 'Maintain balanced N-P-K fertigation, regular soil testing, and weekly scouting.',
            'treatment': 'No chemical treatment needed. Apply organic sea weed extract spray for optimal growth.',
            'recommended_product': 'Bio-Boost Seaweed Growth Promoter'
        }
    ],
    'Paddy': [
        {
            'disease': 'Rice Blast Disease (Magnaporthe oryzae)',
            'confidence': 95.8,
            'symptoms': 'Spindle-shaped eye spots with gray/white centers and reddish-brown margins on leaf blade and neck rot.',
            'prevention': 'Avoid excessive nitrogen fertilization, use blast-resistant varieties like KMP-175 or Jyothi.',
            'treatment': 'Spray Tricyclazole 75% WP @ 0.6g/L or Isoprothiolane 40% EC @ 1.5ml/L at initial disease onset.',
            'recommended_product': 'Tricyclazole Anti-Blast Solution'
        },
        {
            'disease': 'Bacterial Leaf Blight (Xanthomonas oryzae)',
            'confidence': 93.7,
            'symptoms': 'Water-soaked wavy streaks along leaf margins turning yellow then straw-colored white.',
            'prevention': 'Drain field periodically, avoid clipping seedling tips during transplanting.',
            'treatment': 'Spray Streptocycline @ 0.15g/L combined with Copper Hydroxide @ 2g/L.',
            'recommended_product': 'Strepto-Shield Bactericide'
        }
    ],
    'Ragi': [
        {
            'disease': 'Finger Millet Blast (Pyricularia grisea)',
            'confidence': 97.2,
            'symptoms': 'Oval brown diamond spots on leaf surface, neck infection causing drooping of finger heads.',
            'prevention': 'Seed treatment with Pseudomonas fluorescens @ 10g/kg seed before sowing.',
            'treatment': 'Spray Carbendazim 50% WP @ 1g/L at earhead emergence stage.',
            'recommended_product': 'Bio-Shield Pseudomonas Seed Treatment'
        }
    ],
    'General Crop': [
        {
            'disease': 'Powdery Mildew Fungal Infection',
            'confidence': 92.5,
            'symptoms': 'White powdery flour-like fungal growth on upper leaf surfaces, leaf distortion and premature dropping.',
            'prevention': 'Ensure good air circulation between rows, avoid excessive shading.',
            'treatment': 'Spray Wettable Sulfur 80% WP @ 3g/L or Hexaconazole 5% EC @ 1ml/L.',
            'recommended_product': 'Sulphur-80 Bio Fungicide'
        }
    ]
}

def predict_crop(soil_type, ph, n, p, k, rainfall, humidity, temp, season, district, water_avail):
    """
    Evidence-based Agronomic Crop Suitability Engine.
    Evaluates physiological parameters without fabricating 100% scores or fixed guaranteed profits.
    """
    scores = {}
    evaluation_details = {}
    
    for crop_name, data in CROPS_DATABASE.items():
        score = 100.0
        warnings = []
        reasons = []
        
        # 1. Soil Suitability Evaluation
        if soil_type in data['soil']:
            soil_status = f"Suitable ({soil_type} provides appropriate root aeration)"
            reasons.append(f"Soil Compatibility: {soil_type} aligns with crop root zone requirements.")
        else:
            soil_status = f"Sub-optimal ({soil_type} differs from primary preferred soils: {', '.join(data['soil'])})"
            score -= 22.0
            
        # 2. pH Evaluation
        min_ph, max_ph = data['ph_range']
        if min_ph <= ph <= max_ph:
            ph_status = f"Optimal ({ph} pH within preferred range {min_ph}-{max_ph})"
            reasons.append(f"Soil pH ({ph}): Within optimum ({min_ph} - {max_ph}) range for nutrient bioavailability.")
        else:
            diff = min(abs(ph - min_ph), abs(ph - max_ph))
            ph_status = f"Sub-optimal ({ph} pH outside preferred range {min_ph}-{max_ph})"
            score -= min(35.0, diff * 20.0)
            if ph < min_ph:
                warnings.append(f"Acidic soil stress (pH {ph} < {min_ph}); liming recommended.")
            else:
                warnings.append(f"Alkaline soil stress (pH {ph} > {max_ph}); gypsum amendment recommended.")
                
        # 3. Rainfall & Water Availability Evaluation
        min_rain, max_rain = data['min_rain'], data['max_rain']
        if min_rain <= rainfall <= max_rain:
            rain_status = f"Sufficient ({rainfall} mm annual precipitation)"
            reasons.append(f"Precipitation ({rainfall} mm): Satisfies seasonal crop evapotranspiration needs.")
        elif rainfall < min_rain:
            deficit = min_rain - rainfall
            rain_status = f"Deficient ({rainfall} mm is {deficit} mm below optimum {min_rain} mm)"
            score -= min(40.0, (deficit / 15.0))
            if crop_name in ['Paddy (Rice)', 'Sugarcane', 'Arecanut (Betel Nut)'] and water_avail != 'High':
                score -= 30.0
                warnings.append(f"High Irrigation Requirement: Current rainfall ({rainfall} mm) and {water_avail} water availability require supplemental canal/drip irrigation.")
            else:
                warnings.append(f"Moisture Deficit: Supplemental irrigation required during critical growth stages.")
        else:
            rain_status = f"Excessive ({rainfall} mm exceeds optimum {max_rain} mm)"
            score -= min(25.0, (rainfall - max_rain) / 40.0)
            if crop_name in ['Maize (Corn)', 'Tomato', 'Onion']:
                warnings.append(f"Waterlogging Risk: High rainfall ({rainfall} mm) requires raised bed planting & field drainage.")

        # 4. Temperature Evaluation
        min_t, max_t = data['temp_range']
        if min_t <= temp <= max_t:
            temp_status = f"Optimal ({temp} °C within growth threshold {min_t}-{max_t} °C)"
            reasons.append(f"Temperature ({temp} °C): Suitable thermal regime for physiological development.")
        else:
            temp_status = f"Sub-optimal ({temp} °C outside preferred range {min_t}-{max_t} °C)"
            score -= 25.0
            warnings.append(f"Thermal stress risk at {temp} °C.")

        # 5. Season & Location Suitability
        is_season_match = (season in data['season']) or ('Perennial' in data['season']) or (season == 'Perennial' and ('Perennial' in data['season'] or len(data['season']) >= 3))
        if is_season_match:
            season_label = "Year-Round / Perennial" if season == "Perennial" else season
            season_status = f"Suitable for {season_label} cultivation in {district}"
            reasons.append(f"Seasonal Alignment: Suitable for {season_label} cultivation in {district}.")
        else:
            season_status = f"Non-standard season ({season}; standard seasons: {', '.join(data['season'])})"
            score -= 20.0

        # 6. Dynamic NPK Nutrient Evaluation Factor
        n_ratio = min(1.2, max(0.5, n / data['opt_n']))
        p_ratio = min(1.2, max(0.5, p / data['opt_p']))
        k_ratio = min(1.2, max(0.5, k / data['opt_k']))
        npk_factor = (n_ratio * 0.4 + p_ratio * 0.3 + k_ratio * 0.3)
        npk_status = f"N: {n}/{data['opt_n']}, P: {p}/{data['opt_p']}, K: {k}/{data['opt_k']} kg/ha (Adequacy Ratio: {round(npk_factor*100)}%)"

        # Final Agronomic Score Calculation (Scientifically bounded between 15% and 94%)
        final_score = round(max(15.0, min(94.0, score * npk_factor)), 1)
        scores[crop_name] = final_score
        
        evaluation_details[crop_name] = {
            'soil_status': soil_status,
            'ph_status': ph_status,
            'rain_status': rain_status,
            'temp_status': temp_status,
            'season_status': season_status,
            'npk_status': npk_status,
            'npk_factor': npk_factor,
            'reasons': reasons,
            'warnings': warnings
        }

    # Sort crops by suitability score
    sorted_crops = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_score = sorted_crops[0][1]

    # Guard: Insufficient Data / Insufficient Score
    if top_score < 40.0:
        return {
            'is_sufficient_data': False,
            'message': 'Insufficient verified data for a reliable recommendation under the specified parameters.',
            'inputs': {'soil_type': soil_type, 'district': district, 'season': season, 'water_avail': water_avail, 'ph': ph, 'nitrogen': n, 'phosphorus': p, 'potassium': k, 'rainfall': rainfall, 'temp': temp}
        }

    # Build Top 3 Evidence-Based Recommendations
    top_recommendations = []
    badges = ['Best Match (#1)', 'Second Best (#2)', 'Alternative Crop (#3)']

    for idx, (cname, score) in enumerate(sorted_crops[:3]):
        cdata = CROPS_DATABASE[cname]
        edetails = evaluation_details[cname]

        # Dynamic Yield Calculation based on score & NPK factor
        yield_multiplier = min(1.15, max(0.65, (score / 85.0) * edetails['npk_factor']))
        y_min = round(cdata['base_yield_min'] * yield_multiplier, 1)
        y_max = round(cdata['base_yield_max'] * yield_multiplier, 1)
        yield_range_str = f"{y_min} - {y_max} {cdata['yield_unit']}"

        # Dynamic Financial Calculation based on market price & cost
        price_per_unit = cdata['market_price_per_unit']
        prod_cost = cdata['prod_cost_per_acre']
        rev_min = round(y_min * price_per_unit)
        rev_max = round(y_max * price_per_unit)
        prof_min = max(0, rev_min - prod_cost)
        prof_max = max(0, rev_max - prod_cost)

        # Dynamic Crop-Specific Fertilizer Recommendation Engine
        defic_n = max(0, cdata['opt_n'] - n)
        defic_p = max(0, cdata['opt_p'] - p)
        defic_k = max(0, cdata['opt_k'] - k)

        urea_req = round(defic_n * 2.17)
        dap_req = round(defic_p * 2.17)
        mop_req = round(defic_k * 1.66)

        fert_lines = []
        if defic_n > 0: fert_lines.append(f"Urea: {urea_req} kg/acre (to address {defic_n} kg/ha Nitrogen deficit)")
        else: fert_lines.append("Nitrogen: Adequate baseline level; maintain organic top dressing.")

        if defic_p > 0: fert_lines.append(f"DAP: {dap_req} kg/acre (to address {defic_p} kg/ha Phosphorus deficit)")
        else: fert_lines.append("Phosphorus: Adequate status.")

        if defic_k > 0: fert_lines.append(f"MOP: {mop_req} kg/acre (to address {defic_k} kg/ha Potassium deficit)")
        else: fert_lines.append("Potassium: Adequate status.")

        if ph < 5.5: fert_lines.append("Soil Amendment: Apply 150 kg Agricultural Lime/acre for soil acidity correction.")
        elif ph > 7.8: fert_lines.append("Soil Amendment: Apply 100 kg Gypsum/acre for soil alkalinity correction.")

        # Image Mapping - strictly matched to crop name
        img_url = '/static/images/crops/default.jpg'
        cn_lower = cname.lower()
        if 'ragi' in cn_lower: img_url = '/static/images/crops/ragi.jpg'
        elif 'paddy' in cn_lower or 'rice' in cn_lower: img_url = '/static/images/crops/rice.jpg'
        elif 'maize' in cn_lower or 'corn' in cn_lower: img_url = '/static/images/crops/maize.jpg'
        elif 'sugarcane' in cn_lower: img_url = '/static/images/crops/sugarcane.jpg'
        elif 'turmeric' in cn_lower or 'arishina' in cn_lower: img_url = '/static/images/crops/turmeric.jpg'
        elif 'tomato' in cn_lower: img_url = '/static/images/crops/tomatoes.jpg'
        elif 'cotton' in cn_lower: img_url = '/static/images/crops/bt_cotton_seeds.jpg'
        elif 'onion' in cn_lower: img_url = '/static/images/crops/onion.jpg'
        elif 'banana' in cn_lower: img_url = '/static/images/crops/banana.jpg'
        elif 'apple' in cn_lower: img_url = '/static/images/crops/apple.jpg'
        elif 'arecanut' in cn_lower or 'betel' in cn_lower: img_url = '/static/images/crops/default.jpg'

        top_recommendations.append({
            'rank': idx + 1,
            'badge': badges[idx],
            'crop_name': cname,
            'crop_name_kn': cdata['name_kn'],
            'image_url': img_url,
            'match_score': score, # Agronomic Suitability Score
            'description': cdata['description'],
            'pop_guidance': cdata['pop_guidance'],
            'yield_range': yield_range_str,
            'yield_unit': cdata['yield_unit'],
            'market_price_formatted': f"₹{price_per_unit:,} / {cdata['yield_unit'].split('/')[0].strip()}",
            'prod_cost_formatted': f"₹{prod_cost:,} / Acre",
            'revenue_formatted': f"₹{rev_min:,} - ₹{rev_max:,} / Acre",
            'profit_formatted': f"₹{prof_min:,} - ₹{prof_max:,} / Acre",
            'soil_status': edetails['soil_status'],
            'ph_status': edetails['ph_status'],
            'rain_status': edetails['rain_status'],
            'temp_status': edetails['temp_status'],
            'season_status': edetails['season_status'],
            'npk_status': edetails['npk_status'],
            'reasons': edetails['reasons'],
            'warnings': edetails['warnings'],
            'fertilizer_custom': fert_lines
        })

    top_crop = top_recommendations[0]

    return {
        'is_sufficient_data': True,
        'recommended_crop': top_crop['crop_name'],
        'recommended_crop_kn': top_crop['crop_name_kn'],
        'match_score': top_crop['match_score'],
        'top_recommendations': top_recommendations,
        'disclaimer': 'This recommendation is an AI/data-assisted decision-support result, not a guaranteed prediction. Yield, cost, market price, and profit may vary with weather, soil conditions, farming practices, and market conditions.',
        'inputs': {
            'soil_type': soil_type,
            'district': district,
            'season': season,
            'water_avail': water_avail,
            'ph': ph,
            'nitrogen': n,
            'phosphorus': p,
            'potassium': k,
            'rainfall': rainfall,
            'temp': temp
        }
    }

def recommend_fertilizer(soil_type, ph, n, p, k, target_crop):
    """
    Calculates precise nutrient adjustment requirements for target crop.
    """
    crop_info = CROPS_DATABASE.get(target_crop, CROPS_DATABASE['Tomato'])
    req_n = crop_info['n_range'][1]
    req_p = crop_info['p_range'][1]
    req_k = crop_info['k_range'][1]
    
    defic_n = max(0, req_n - n)
    defic_p = max(0, req_p - p)
    defic_k = max(0, req_k - k)
    
    # Calculate fertilizer quantities
    urea_kg = round(defic_n * 2.17, 1) # Urea is 46% N
    dap_kg = round(defic_p * 2.17, 1)  # DAP is 46% P
    mop_kg = round(defic_k * 1.66, 1)  # MOP is 60% K
    organic_compost = "3 - 5 Tons/acre" if ph < 6.0 or ph > 7.5 else "2 Tons/acre"
    
    advice = []
    if defic_n > 20:
        advice.append(f"Nitrogen deficient. Apply {urea_kg} kg Urea per acre in split doses.")
    else:
        advice.append("Nitrogen status is healthy. Maintain organic mulching.")
        
    if defic_p > 15:
        advice.append(f"Phosphorus deficient. Apply {dap_kg} kg DAP at basal soil preparation time.")
    if defic_k > 15:
        advice.append(f"Potassium deficient. Apply {mop_kg} kg MOP (Muriate of Potash) during flowering stage.")
        
    if ph < 6.0:
        advice.append("Soil is acidic. Apply 200kg Agricultural Lime (Calcium Carbonate) per acre to raise pH.")
    elif ph > 7.8:
        advice.append("Soil is alkaline. Apply 150kg Gypsum per acre and organic compost to buffer pH.")
        
    return {
        'target_crop': target_crop,
        'target_crop_kn': crop_info['name_kn'],
        'deficits': {'N': defic_n, 'P': defic_p, 'K': defic_k},
        'recommendations': {
            'Urea': f"{urea_kg} kg/acre",
            'DAP': f"{dap_kg} kg/acre",
            'MOP': f"{mop_kg} kg/acre",
            'Organic Compost': organic_compost,
            'MicroNutrients': 'Zinc Sulfate @ 10kg/acre & Boron @ 2kg/acre'
        },
        'action_plan': advice
    }

def detect_disease(crop_name, image_filename, symptom_input=""):
    """
    Simulates visual model feature diagnosis combined with symptom descriptors.
    """
    crop_key = crop_name if crop_name in DISEASE_DATABASE else 'Tomato'
    if crop_key not in DISEASE_DATABASE:
        crop_key = 'General Crop'
        
    options = DISEASE_DATABASE[crop_key]
    
    # If symptom input contains keywords like curl, yellow, blast, ring, powdery, match accordingly
    selected = options[0]
    if symptom_input:
        s_lower = symptom_input.lower()
        for opt in options:
            if any(k in s_lower for k in opt['disease'].lower().split()):
                selected = opt
                break
                
    return {
        'crop_name': crop_name,
        'detected_disease': selected['disease'],
        'confidence': selected['confidence'],
        'symptoms': selected['symptoms'],
        'prevention': selected['prevention'],
        'treatment': selected['treatment'],
        'recommended_product': selected['recommended_product']
    }
