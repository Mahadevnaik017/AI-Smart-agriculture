// Mojara Multilingual Translation Dictionary (English & Kannada)
const i18nDictionary = {
  kn: {
    "brand_title": "ಮೊಜಾರಾ – ಸ್ಮಾರ್ಟ್ ಕೃಷಿ",
    "home": "ಮುಖಪುಟ",
    "marketplace": "ಮಾರುಕಟ್ಟೆ",
    "ai_crop": "ಎಐ ಬೆಳೆ ಶಿಫಾರಸು",
    "ai_fertilizer": "ಗೊಬ್ಬರ ಉಸ್ತುವಾರಿ",
    "ai_disease": "ರೋಗ ಪತ್ತೆ",
    "apmc_prices": "ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ",
    "schemes": "ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",
    "forum": "ರೈತ ಚರ್ಚಾ ವೇದಿಕೆ",
    "hero_title": "ಕೃಷಿ ತಂತ್ರಜ್ಞಾನ ಮತ್ತು ನೆರವು ನಿಮ್ಮ ಬೆರಳ ತುದಿಯಲ್ಲಿ",
    "hero_subtitle": "ಎಐ ಬೆಳೆ ಶಿಫಾರಸು, ಸಕಾಲಿಕ ಕೀಟ ಪತ್ತೆ ಮತ್ತು ನೇರ ಮಾರುಕಟ್ಟೆಯೊಂದಿಗೆ ನಿಮ್ಮ ಆದಾಯ ಹೆಚ್ಚಿಸಿ.",
    "explore_market": "ಮಾರುಕಟ್ಟೆ ವೀಕ್ಷಿಸಿ",
    "try_ai": "ಎಐ ಸಲಹೆ ಪಡೆಯಿರಿ",
    "add_to_cart": "ಕಾರ್ಟ್‌ಗೆ ಸೇರಿಸಿ",
    "buy_now": "ಈಗಲೇ ಖರೀದಿಸಿ",
    "organic": "ಸಾವಯವ",
    "mandi_prices": "ಇಂದಿನ ಎಪಿಎಂಸಿ ದರಗಳು",
    "login": "ಲಾಗಿನ್",
    "register": "ನೋಂದಣಿ",
    "dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
    "logout": "ನಿರ್ಗಮನ",
    "farmer_portal": "ರೈತರ ಪೋರ್ಟಲ್",
    "buyer_portal": "ಖರೀದಿದಾರರ ಪೋರ್ಟಲ್",
    "officer_portal": "ಕೃಷಿ ಅಧಿಕಾರಿ ಪೋರ್ಟಲ್",
    "admin_portal": "ಆಡಳಿತ ಮಂಡಳಿ",
    "recommended_crop": "ಶಿಫಾರಸು ಮಾಡಿದ ಬೆಳೆ",
    "expected_yield": "ನಿರೀಕ್ಷಿತ ಇಳುವರಿ",
    "profit_estimate": "ಅಂದಾಜು ಲಾಭ",
    "disease_name": "ಪತ್ತೆಯಾದ ಕಾಯಿಲೆ",
    "confidence": "ಖಚಿತತೆ",
    "treatment": "ಉಪಶಮನ ಕ್ರಮೊಗಳು"
  },
  en: {
    "brand_title": "Mojara – Smart Agriculture",
    "home": "Home",
    "marketplace": "Marketplace",
    "ai_crop": "AI Crop Match",
    "ai_fertilizer": "Fertilizer Guide",
    "ai_disease": "Disease Detector",
    "apmc_prices": "APMC Mandi Rates",
    "schemes": "Govt Schemes",
    "forum": "Community Forum",
    "hero_title": "Empowering Farmers with Smart AI & Direct Markets",
    "hero_subtitle": "Maximize your harvest yield with soil AI, real-time APMC mandi prices, and direct farm-to-buyer sales.",
    "explore_market": "Explore Marketplace",
    "try_ai": "Try AI Advisor",
    "add_to_cart": "Add to Cart",
    "buy_now": "Buy Now",
    "organic": "100% Organic",
    "mandi_prices": "Live APMC Prices",
    "login": "Sign In",
    "register": "Register",
    "dashboard": "Dashboard",
    "logout": "Sign Out",
    "farmer_portal": "Farmer Portal",
    "buyer_portal": "Buyer Portal",
    "officer_portal": "Agri Officer Portal",
    "admin_portal": "Admin Console",
    "recommended_crop": "Recommended Crop",
    "expected_yield": "Expected Yield",
    "profit_estimate": "Profit Estimate",
    "disease_name": "Detected Disease",
    "confidence": "Confidence",
    "treatment": "Treatment Plan"
  }
};

function setLanguage(lang) {
  localStorage.setItem('mojara_lang', lang);
  applyTranslations(lang);
}

function applyTranslations(lang) {
  const dict = i18nDictionary[lang] || i18nDictionary['en'];
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (dict[key]) {
      el.textContent = dict[key];
    }
  });
  
  // Highlight active language button
  document.querySelectorAll('.lang-btn').forEach(btn => {
    if (btn.getAttribute('data-lang') === lang) {
      btn.classList.add('btn-primary-mojara');
      btn.classList.remove('btn-secondary-mojara');
    } else {
      btn.classList.remove('btn-primary-mojara');
      btn.classList.add('btn-secondary-mojara');
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  const savedLang = localStorage.getItem('mojara_lang') || 'en';
  applyTranslations(savedLang);
});
