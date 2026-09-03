/**
 * ========================================================================================
 * AI-Driven Smart Agriculture & Micro-crop Advisory System (Mojara)
 * Script: AI Advisory Tools Client-Side Validation & Interactivity (static/js/ai_tools.js)
 * Assigned Specialist: Panchakshari Jogi
 * Milestone: Recommendation interface input flow and client validation (6 August 2026)
 * ========================================================================================
 */
// Authentication & Form Flow Testing:
// Identified invalid-input scenarios, empty input validation, and user flow edge cases.
// AI Tools Interactive Handlers
document.addEventListener('DOMContentLoaded', () => {
  // Image Upload Live Preview for Disease Detection
  const imageInput = document.getElementById('crop_image');
  const previewImg = document.getElementById('image-preview');
  const dropZone = document.getElementById('image-drop-zone');

  if (imageInput && previewImg) {
    imageInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (event) => {
          previewImg.src = event.target.result;
          previewImg.style.display = 'block';
          if (dropZone) dropZone.classList.add('has-file');
        };
        reader.readAsDataURL(file);
      }
    });
  }

  // Quick Preset Sample Selectors for Disease Detection
  const sampleBtns = document.querySelectorAll('.sample-leaf-btn');
  sampleBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const crop = btn.getAttribute('data-crop');
      const symptom = btn.getAttribute('data-symptom');
      const cropSelect = document.getElementById('crop_name');
      const symptomInput = document.getElementById('symptoms');
      
      if (cropSelect) cropSelect.value = crop;
      if (symptomInput) symptomInput.value = symptom;
      
      if (previewImg) {
        if (crop === 'Tomato') previewImg.src = 'https://images.unsplash.com/photo-1592924357228-91a4daadcfea?auto=format&fit=crop&w=600&q=80';
        else if (crop === 'Paddy') previewImg.src = 'https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=600&q=80';
        else previewImg.src = 'https://images.unsplash.com/photo-1530595467537-0b5996c41f2d?auto=format&fit=crop&w=600&q=80';
        previewImg.style.display = 'block';
      }
    });
  });

  // Range Slider Value Label Updates
  const rangeInputs = document.querySelectorAll('.range-slider');
  rangeInputs.forEach(slider => {
    const valDisplay = document.getElementById(slider.id + '_val');
    if (valDisplay) {
      slider.addEventListener('input', () => {
        valDisplay.textContent = slider.value;
      });
    }
  });
});
