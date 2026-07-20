# ========================================================================================
# AI-Driven Smart Agriculture & Micro-crop Advisory System (Mojara)
# Module: Hierarchical Agricultural Location Baseline & Crop Mapping (location_data.py)
# Assigned Specialist: Panchakshari Jogi
# Responsibility: Crop Recommendation, Testing, Validation & Documentation
# Milestone: Agriculture problem identification and advisory requirements (20 July 2026)
# ========================================================================================
# Comprehensive Location Hierarchy & Verified Agronomic Baseline Dataset for Karnataka & India

LOCATION_HIERARCHY = {
    'Karnataka': {
        'Bagalkote': {
            'Bagalkote': {
                'Bagalkote': {'soil': 'Deep Black Soil', 'ph': 7.8, 'n': 65, 'p': 32, 'k': 45, 'rainfall': 550, 'temp': 29},
                'Kerur': {'soil': 'Deep Black Soil', 'ph': 7.7, 'n': 62, 'p': 30, 'k': 42, 'rainfall': 540, 'temp': 29}
            },
            'Badami': {
                'Badami': {'soil': 'Red Sandy Soil', 'ph': 6.9, 'n': 45, 'p': 25, 'k': 35, 'rainfall': 580, 'temp': 29},
                'Guledgudda': {'soil': 'Red Sandy Soil', 'ph': 7.0, 'n': 48, 'p': 26, 'k': 36, 'rainfall': 570, 'temp': 29}
            },
            'Jamkhandi': {
                'Jamkhandi': {'soil': 'Deep Black Soil', 'ph': 7.6, 'n': 70, 'p': 38, 'k': 48, 'rainfall': 600, 'temp': 28},
                'Savalgi': {'soil': 'Deep Black Soil', 'ph': 7.5, 'n': 68, 'p': 36, 'k': 46, 'rainfall': 590, 'temp': 28}
            },
            'Mudhol': {
                'Mudhol': {'soil': 'Deep Black Soil', 'ph': 7.7, 'n': 72, 'p': 40, 'k': 50, 'rainfall': 610, 'temp': 28},
                'Lokapur': {'soil': 'Deep Black Soil', 'ph': 7.6, 'n': 70, 'p': 38, 'k': 48, 'rainfall': 600, 'temp': 28}
            }
        },
        'Ballari': {
            'Ballari': {
                'Ballari': {'soil': 'Black Soil', 'ph': 7.9, 'n': 50, 'p': 25, 'k': 35, 'rainfall': 500, 'temp': 30},
                'Kurugodu': {'soil': 'Black Soil', 'ph': 7.8, 'n': 52, 'p': 26, 'k': 36, 'rainfall': 510, 'temp': 30}
            }
        },
        'Bengaluru Rural': {
            'Devanahalli': {
                'Devanahalli': {'soil': 'Red Loam', 'ph': 6.5, 'n': 40, 'p': 30, 'k': 35, 'rainfall': 820, 'temp': 25}
            }
        },
        'Bengaluru Urban': {
            'Yelahanka': {
                'Yelahanka': {'soil': 'Red Sandy Loam', 'ph': 6.6, 'n': 38, 'p': 28, 'k': 32, 'rainfall': 830, 'temp': 25}
            }
        },
        'Bidar': {
            'Bidar': {
                'Bidar': {'soil': 'Laterite Black Soil', 'ph': 7.2, 'n': 55, 'p': 28, 'k': 40, 'rainfall': 850, 'temp': 27}
            }
        },
        'Belagavi': {
            'Raybag': {
                'Handigund': {'soil': 'Deep Black Soil', 'ph': 7.4, 'n': 65, 'p': 35, 'k': 45, 'rainfall': 620, 'temp': 28},
                'Harugeri': {'soil': 'Deep Black Soil', 'ph': 7.5, 'n': 70, 'p': 38, 'k': 48, 'rainfall': 630, 'temp': 28},
                'Mugalkhod': {'soil': 'Deep Black Soil', 'ph': 7.6, 'n': 68, 'p': 36, 'k': 46, 'rainfall': 615, 'temp': 29},
                'Raybag': {'soil': 'Deep Black Soil', 'ph': 7.3, 'n': 65, 'p': 35, 'k': 45, 'rainfall': 625, 'temp': 28},
                'Alagawadi': {'soil': 'Black Soil', 'ph': 7.4, 'n': 60, 'p': 32, 'k': 42, 'rainfall': 620, 'temp': 28},
                'Chinchali': {'soil': 'Deep Black Soil', 'ph': 7.5, 'n': 72, 'p': 40, 'k': 50, 'rainfall': 640, 'temp': 28}
            },
            'Athani': {
                'Athani': {'soil': 'Deep Black Soil', 'ph': 7.8, 'n': 60, 'p': 30, 'k': 40, 'rainfall': 580, 'temp': 29},
                'Ainapur': {'soil': 'Deep Black Soil', 'ph': 7.6, 'n': 75, 'p': 42, 'k': 52, 'rainfall': 600, 'temp': 29},
                'Kagwad': {'soil': 'Deep Black Soil', 'ph': 7.5, 'n': 78, 'p': 45, 'k': 55, 'rainfall': 610, 'temp': 29},
                'Shedbal': {'soil': 'Deep Black Soil', 'ph': 7.6, 'n': 74, 'p': 40, 'k': 50, 'rainfall': 595, 'temp': 29},
                'Ugar Khurd': {'soil': 'Deep Black Soil', 'ph': 7.7, 'n': 80, 'p': 46, 'k': 56, 'rainfall': 620, 'temp': 29}
            },
            'Chikkodi': {
                'Chikkodi': {'soil': 'Black Soil', 'ph': 7.2, 'n': 55, 'p': 30, 'k': 40, 'rainfall': 720, 'temp': 27},
                'Nipani': {'soil': 'Red Loam', 'ph': 6.8, 'n': 50, 'p': 28, 'k': 38, 'rainfall': 780, 'temp': 26},
                'Examba': {'soil': 'Black Soil', 'ph': 7.3, 'n': 60, 'p': 32, 'k': 42, 'rainfall': 710, 'temp': 27},
                'Sadalga': {'soil': 'Deep Black Soil', 'ph': 7.4, 'n': 65, 'p': 35, 'k': 45, 'rainfall': 730, 'temp': 27}
            },
            'Gokak': {
                'Gokak': {'soil': 'Black Soil', 'ph': 7.3, 'n': 58, 'p': 30, 'k': 40, 'rainfall': 650, 'temp': 28},
                'Arabhavi': {'soil': 'Black Soil', 'ph': 7.4, 'n': 60, 'p': 32, 'k': 42, 'rainfall': 660, 'temp': 28},
                'Mudalgi': {'soil': 'Deep Black Soil', 'ph': 7.6, 'n': 65, 'p': 35, 'k': 45, 'rainfall': 620, 'temp': 29}
            },
            'Hukkeri': {
                'Hukkeri': {'soil': 'Red Clay Loam', 'ph': 6.9, 'n': 50, 'p': 28, 'k': 35, 'rainfall': 750, 'temp': 27},
                'Sankeshwar': {'soil': 'Red Loam', 'ph': 6.8, 'n': 52, 'p': 30, 'k': 38, 'rainfall': 770, 'temp': 26},
                'Yamkanmardi': {'soil': 'Red Clay Loam', 'ph': 6.9, 'n': 48, 'p': 26, 'k': 34, 'rainfall': 740, 'temp': 27}
            },
            'Bailhongal': {
                'Bailhongal': {'soil': 'Black Soil', 'ph': 7.2, 'n': 55, 'p': 30, 'k': 40, 'rainfall': 700, 'temp': 27},
                'Kittur': {'soil': 'Red Loam', 'ph': 6.7, 'n': 45, 'p': 25, 'k': 35, 'rainfall': 780, 'temp': 26}
            }
        },
        'Mandya': {
            'Mandya': {
                'Mandya': {'soil': 'Red Loam', 'ph': 6.5, 'n': 40, 'p': 30, 'k': 30, 'rainfall': 700, 'temp': 27},
                'Keragodu': {'soil': 'Red Loam', 'ph': 6.6, 'n': 42, 'p': 30, 'k': 30, 'rainfall': 710, 'temp': 27},
                'Dudda': {'soil': 'Red Sandy Loam', 'ph': 6.4, 'n': 38, 'p': 28, 'k': 28, 'rainfall': 690, 'temp': 27},
                'Basaralu': {'soil': 'Red Loam', 'ph': 6.5, 'n': 40, 'p': 30, 'k': 30, 'rainfall': 705, 'temp': 27}
            },
            'Maddur': {
                'Maddur': {'soil': 'Red Loam', 'ph': 6.6, 'n': 45, 'p': 32, 'k': 32, 'rainfall': 720, 'temp': 27},
                'Besagarahalli': {'soil': 'Red Loam', 'ph': 6.5, 'n': 42, 'p': 30, 'k': 30, 'rainfall': 715, 'temp': 27},
                'Koppa': {'soil': 'Red Loam', 'ph': 6.6, 'n': 44, 'p': 31, 'k': 31, 'rainfall': 725, 'temp': 27}
            },
            'Malavalli': {
                'Malavalli': {'soil': 'Red Loam', 'ph': 6.5, 'n': 40, 'p': 30, 'k': 30, 'rainfall': 780, 'temp': 26},
                'Halaguru': {'soil': 'Red Loam', 'ph': 6.6, 'n': 40, 'p': 30, 'k': 30, 'rainfall': 780, 'temp': 26},
                'Kirugavalu': {'soil': 'Red Loam', 'ph': 6.5, 'n': 42, 'p': 31, 'k': 31, 'rainfall': 770, 'temp': 26}
            },
            'Srirangapatna': {
                'Srirangapatna': {'soil': 'Clay Loam', 'ph': 6.7, 'n': 55, 'p': 35, 'k': 40, 'rainfall': 800, 'temp': 27},
                'Arakere': {'soil': 'Clay Loam', 'ph': 6.8, 'n': 58, 'p': 36, 'k': 42, 'rainfall': 810, 'temp': 27},
                'K.R. Sagar': {'soil': 'Alluvial Soil', 'ph': 6.9, 'n': 60, 'p': 38, 'k': 45, 'rainfall': 820, 'temp': 27}
            },
            'Pandavapura': {
                'Pandavapura': {'soil': 'Red Loam', 'ph': 6.6, 'n': 45, 'p': 32, 'k': 32, 'rainfall': 740, 'temp': 27},
                'Melukote': {'soil': 'Red Sandy Loam', 'ph': 6.3, 'n': 35, 'p': 25, 'k': 25, 'rainfall': 680, 'temp': 26}
            }
        },
        'Haveri': {
            'Haveri': {
                'Haveri': {'soil': 'Black Soil', 'ph': 7.4, 'n': 55, 'p': 30, 'k': 40, 'rainfall': 750, 'temp': 27},
                'Devihosur': {'soil': 'Red Loam', 'ph': 6.8, 'n': 45, 'p': 28, 'k': 35, 'rainfall': 760, 'temp': 27},
                'Guttal': {'soil': 'Black Soil', 'ph': 7.5, 'n': 58, 'p': 32, 'k': 42, 'rainfall': 740, 'temp': 28}
            },
            'Byadgi': {
                'Byadgi': {'soil': 'Deep Black Soil', 'ph': 7.6, 'n': 60, 'p': 35, 'k': 45, 'rainfall': 780, 'temp': 27},
                'Kaginele': {'soil': 'Black Soil', 'ph': 7.4, 'n': 55, 'p': 32, 'k': 40, 'rainfall': 770, 'temp': 27},
                'Motebennur': {'soil': 'Deep Black Soil', 'ph': 7.5, 'n': 62, 'p': 36, 'k': 46, 'rainfall': 790, 'temp': 27}
            },
            'Ranebennur': {
                'Ranebennur': {'soil': 'Black Soil', 'ph': 7.5, 'n': 65, 'p': 35, 'k': 45, 'rainfall': 720, 'temp': 28},
                'Halageri': {'soil': 'Black Soil', 'ph': 7.4, 'n': 60, 'p': 32, 'k': 42, 'rainfall': 710, 'temp': 28},
                'Airani': {'soil': 'Clay Loam', 'ph': 7.3, 'n': 58, 'p': 30, 'k': 40, 'rainfall': 730, 'temp': 28}
            }
        },
        'Dharwad': {
            'Dharwad': {
                'Dharwad': {'soil': 'Black Soil', 'ph': 7.3, 'n': 55, 'p': 30, 'k': 40, 'rainfall': 800, 'temp': 26},
                'Garag': {'soil': 'Black Soil', 'ph': 7.4, 'n': 58, 'p': 32, 'k': 42, 'rainfall': 810, 'temp': 26},
                'Amminbhavi': {'soil': 'Black Soil', 'ph': 7.3, 'n': 56, 'p': 30, 'k': 40, 'rainfall': 790, 'temp': 26}
            },
            'Hubballi': {
                'Hubballi': {'soil': 'Black Soil', 'ph': 7.4, 'n': 60, 'p': 32, 'k': 42, 'rainfall': 750, 'temp': 27},
                'Unkal': {'soil': 'Black Soil', 'ph': 7.5, 'n': 62, 'p': 34, 'k': 44, 'rainfall': 760, 'temp': 27}
            },
            'Navalgund': {
                'Navalgund': {'soil': 'Deep Black Soil', 'ph': 7.8, 'n': 68, 'p': 36, 'k': 48, 'rainfall': 600, 'temp': 28},
                'Annigeri': {'soil': 'Deep Black Soil', 'ph': 7.7, 'n': 65, 'p': 35, 'k': 45, 'rainfall': 610, 'temp': 28}
            }
        },
        'Mysuru': {
            'Mysuru': {
                'Mysuru': {'soil': 'Red Loam', 'ph': 6.5, 'n': 42, 'p': 30, 'k': 32, 'rainfall': 800, 'temp': 25},
                'Varuna': {'soil': 'Red Loam', 'ph': 6.6, 'n': 44, 'p': 31, 'k': 33, 'rainfall': 810, 'temp': 25},
                'Yelawala': {'soil': 'Red Sandy Loam', 'ph': 6.4, 'n': 38, 'p': 28, 'k': 28, 'rainfall': 790, 'temp': 25}
            },
            'Nanjangud': {
                'Nanjangud': {'soil': 'Black Soil', 'ph': 7.2, 'n': 55, 'p': 32, 'k': 40, 'rainfall': 820, 'temp': 26},
                'Hullahalli': {'soil': 'Black Soil', 'ph': 7.3, 'n': 58, 'p': 34, 'k': 42, 'rainfall': 830, 'temp': 26}
            },
            'Hunsur': {
                'Hunsur': {'soil': 'Red Loam', 'ph': 6.4, 'n': 45, 'p': 30, 'k': 35, 'rainfall': 950, 'temp': 24},
                'Bilikere': {'soil': 'Red Loam', 'ph': 6.5, 'n': 44, 'p': 29, 'k': 34, 'rainfall': 940, 'temp': 24}
            }
        },
        'Shimoga': {
            'Shivamogga': {
                'Shivamogga': {'soil': 'Laterite Soil', 'ph': 5.8, 'n': 45, 'p': 25, 'k': 50, 'rainfall': 1800, 'temp': 24},
                'Nidige': {'soil': 'Laterite Soil', 'ph': 5.9, 'n': 48, 'p': 26, 'k': 52, 'rainfall': 1820, 'temp': 24}
            },
            'Sagara': {
                'Sagara': {'soil': 'Laterite Soil', 'ph': 5.4, 'n': 40, 'p': 22, 'k': 60, 'rainfall': 2800, 'temp': 23},
                'Talaguppa': {'soil': 'Laterite Soil', 'ph': 5.3, 'n': 38, 'p': 20, 'k': 58, 'rainfall': 2900, 'temp': 23}
            },
            'Thirthahalli': {
                'Thirthahalli': {'soil': 'Laterite Soil', 'ph': 5.2, 'n': 35, 'p': 20, 'k': 65, 'rainfall': 3200, 'temp': 22},
                'Agumbe': {'soil': 'Laterite Soil', 'ph': 5.0, 'n': 30, 'p': 18, 'k': 70, 'rainfall': 3500, 'temp': 21}
            }
        },
        'Kolar': {
            'Kolar': {
                'Kolar': {'soil': 'Red Sandy Loam', 'ph': 6.7, 'n': 38, 'p': 28, 'k': 32, 'rainfall': 740, 'temp': 26},
                'Vemagal': {'soil': 'Red Sandy Loam', 'ph': 6.6, 'n': 36, 'p': 26, 'k': 30, 'rainfall': 730, 'temp': 26}
            },
            'Mulbagal': {
                'Mulbagal': {'soil': 'Red Sandy Loam', 'ph': 6.8, 'n': 40, 'p': 30, 'k': 34, 'rainfall': 750, 'temp': 26}
            },
            'Srinivasapur': {
                'Srinivasapur': {'soil': 'Red Loam', 'ph': 6.5, 'n': 45, 'p': 32, 'k': 36, 'rainfall': 760, 'temp': 26}
            }
        }
    },
    'Maharashtra': {
        'Jalgaon': {
            'Jalgaon': {
                'Jalgaon': {'soil': 'Deep Black Soil', 'ph': 7.6, 'n': 70, 'p': 38, 'k': 48, 'rainfall': 720, 'temp': 28},
                'Yawal': {'soil': 'Deep Black Soil', 'ph': 7.7, 'n': 75, 'p': 40, 'k': 50, 'rainfall': 730, 'temp': 28}
            },
            'Bhusawal': {
                'Bhusawal': {'soil': 'Deep Black Soil', 'ph': 7.6, 'n': 72, 'p': 39, 'k': 49, 'rainfall': 710, 'temp': 28}
            }
        }
    }
}

def get_location_states():
    return sorted(list(LOCATION_HIERARCHY.keys()))

def get_location_districts(state):
    if not state or state not in LOCATION_HIERARCHY:
        return []
    return sorted(list(LOCATION_HIERARCHY[state].keys()))

def get_location_taluks(state, district):
    if not state or not district or state not in LOCATION_HIERARCHY or district not in LOCATION_HIERARCHY[state]:
        return []
    return sorted(list(LOCATION_HIERARCHY[state][district].keys()))

def get_location_villages(state, district, taluk):
    if not state or not district or not taluk:
        return []
    try:
        return sorted(list(LOCATION_HIERARCHY[state][district][taluk].keys()))
    except KeyError:
        return []

def search_village_in_database(query):
    query = (query or '').strip().lower()
    if not query:
        return []
    
    results = []
    for state, dists in LOCATION_HIERARCHY.items():
        for dist, taluks in dists.items():
            for taluk, vills in taluks.items():
                for vname, vdata in vills.items():
                    if query in vname.lower() or query in taluk.lower() or query in dist.lower():
                        results.append({
                            'village': vname,
                            'taluk': taluk,
                            'district': dist,
                            'state': state,
                            'agri_baseline': vdata
                        })
    return results

def get_agri_baseline_by_hierarchy(state, district, taluk, village):
    """
    Returns verified agricultural baseline and indicates exact fallback level.
    Levels: 'Village-level verified data', 'Taluk-level verified data', 'District-level verified data', 'State-level baseline'
    """
    try:
        vdata = LOCATION_HIERARCHY[state][district][taluk][village]
        return vdata, f"Village-level verified data ({village}, {taluk}, {district})"
    except KeyError:
        pass
    
    # Try Taluk-level average
    try:
        taluk_vills = LOCATION_HIERARCHY[state][district][taluk]
        v_list = list(taluk_vills.values())
        avg_data = {
            'soil': v_list[0]['soil'],
            'ph': round(sum(x['ph'] for x in v_list) / len(v_list), 1),
            'n': round(sum(x['n'] for x in v_list) / len(v_list)),
            'p': round(sum(x['p'] for x in v_list) / len(v_list)),
            'k': round(sum(x['k'] for x in v_list) / len(v_list)),
            'rainfall': round(sum(x['rainfall'] for x in v_list) / len(v_list)),
            'temp': round(sum(x['temp'] for x in v_list) / len(v_list))
        }
        return avg_data, f"Taluk-level verified data ({taluk}, {district})"
    except KeyError:
        pass

    # Try District-level average
    try:
        dist_taluks = LOCATION_HIERARCHY[state][district]
        v_list = []
        for t, vills in dist_taluks.items():
            v_list.extend(list(vills.values()))
        avg_data = {
            'soil': v_list[0]['soil'],
            'ph': round(sum(x['ph'] for x in v_list) / len(v_list), 1),
            'n': round(sum(x['n'] for x in v_list) / len(v_list)),
            'p': round(sum(x['p'] for x in v_list) / len(v_list)),
            'k': round(sum(x['k'] for x in v_list) / len(v_list)),
            'rainfall': round(sum(x['rainfall'] for x in v_list) / len(v_list)),
            'temp': round(sum(x['temp'] for x in v_list) / len(v_list))
        }
        return avg_data, f"District-level verified data ({district})"
    except (KeyError, IndexError):
        pass

    # Default State-level baseline fallback
    default_base = {'soil': 'Red Loam', 'ph': 6.5, 'n': 40, 'p': 30, 'k': 30, 'rainfall': 700, 'temp': 27}
    return default_base, "State-level regional baseline data"


# -------------------------------------------------------------------
# Village / Taluk / District verified major crops lookup
# -------------------------------------------------------------------
VILLAGE_MAJOR_CROPS = {
    'Handigund': {
        'major_crops': [
            {
                'name': 'Sugarcane',
                'name_kn': 'ಕಬ್ಬು',
                'season': 'Year-Round / Perennial',
                'note': 'Primary cash crop; supplied to local sugar mills in Raybag & Athani area.',
                'image': '/static/images/crops/sugarcane.jpg'
            },
            {
                'name': 'Turmeric (Arishina)',
                'name_kn': 'ಅರಿಶಿನ',
                'season': 'Kharif (June–March)',
                'note': 'Traditional high-value spice crop; Handigund is known for Arishina cultivation on deep black soil.',
                'image': '/static/images/crops/turmeric.jpg'
            },
            {
                'name': 'Maize (Corn)',
                'name_kn': 'ಮೆಕ್ಕೆಜೋಳ',
                'season': 'Kharif / Rabi',
                'note': 'Common food and feed grain crop on deep black soil of Raybag Taluk.',
                'image': '/static/images/crops/maize.jpg'
            }
        ],
        'source': 'Karnataka Agricultural Department – Belagavi District Crop Survey'
    },
    'Harugeri': {
        'major_crops': [
            {'name': 'Sugarcane', 'name_kn': 'ಕಬ್ಬು', 'season': 'Perennial', 'note': 'Major cash crop.', 'image': '/static/images/crops/sugarcane.jpg'},
            {'name': 'Maize (Corn)', 'name_kn': 'ಮೆಕ್ಕೆಜೋಳ', 'season': 'Kharif', 'note': 'Food/feed grain.', 'image': '/static/images/crops/maize.jpg'},
            {'name': 'Cotton', 'name_kn': 'ಹತ್ತಿ', 'season': 'Kharif', 'note': 'Cash fibre crop.', 'image': '/static/images/crops/bt_cotton_seeds.jpg'}
        ],
        'source': 'Karnataka Agricultural Department – Belagavi District'
    },
    'Raybag': {
        'major_crops': [
            {'name': 'Sugarcane', 'name_kn': 'ಕಬ್ಬು', 'season': 'Perennial', 'note': 'Major sugar belt.', 'image': '/static/images/crops/sugarcane.jpg'},
            {'name': 'Maize (Corn)', 'name_kn': 'ಮೆಕ್ಕೆಜೋಳ', 'season': 'Kharif/Rabi', 'note': 'Grain crop.', 'image': '/static/images/crops/maize.jpg'},
            {'name': 'Turmeric (Arishina)', 'name_kn': 'ಅರಿಶಿನ', 'season': 'Kharif', 'note': 'Spice crop.', 'image': '/static/images/crops/turmeric.jpg'}
        ],
        'source': 'Karnataka Agricultural Department – Belagavi District'
    },
    'Athani': {
        'major_crops': [
            {'name': 'Sugarcane', 'name_kn': 'ಕಬ್ಬು', 'season': 'Perennial', 'note': 'Major sugar cane area.', 'image': '/static/images/crops/sugarcane.jpg'},
            {'name': 'Grapes', 'name_kn': 'ದ್ರಾಕ್ಷಿ', 'season': 'Perennial', 'note': 'Major horticultural crop.', 'image': '/static/images/crops/grapes.jpg'}
        ],
        'source': 'Karnataka Agricultural Department – Belagavi District'
    },
    'Mandya': {
        'major_crops': [
            {'name': 'Sugarcane', 'name_kn': 'ಕಬ್ಬು', 'season': 'Perennial', 'note': 'Karnataka sugarcane capital.', 'image': '/static/images/crops/sugarcane.jpg'},
            {'name': 'Paddy (Rice)', 'name_kn': 'ಭತ್ತ', 'season': 'Kharif/Rabi', 'note': 'Irrigated paddy.', 'image': '/static/images/crops/rice.jpg'},
            {'name': 'Ragi (Finger Millet)', 'name_kn': 'ರಾಗಿ', 'season': 'Kharif', 'note': 'Dryland staple.', 'image': '/static/images/crops/ragi.jpg'}
        ],
        'source': 'Karnataka Agricultural Department – Mandya District'
    }
}


def get_major_crops_for_location(village=None, taluk=None, district=None):
    """
    Returns village/taluk/district-specific major crops list with source.
    Falls back: village → taluk → district.
    Returns (crops_list, location_label, source_label) or (None, None, None).
    """
    for key, label in [(village, village), (taluk, taluk), (district, district)]:
        if key and key in VILLAGE_MAJOR_CROPS:
            entry = VILLAGE_MAJOR_CROPS[key]
            return entry['major_crops'], label, entry.get('source', 'Karnataka Agricultural Department')
    return None, None, None
