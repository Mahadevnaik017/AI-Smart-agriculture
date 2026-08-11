/**
 * ========================================================================================
 * AI-Driven Smart Agriculture & Micro-crop Advisory System (Mojara)
 * Script: Interactive Chart.js Visualizations (static/js/charts_config.js)
 * Assigned Specialist: Mallikarjun Vaddarganvi
 * Milestone: Frontend data requirements for visual components (11 August 2026)
 * ========================================================================================
 */
// Chart.js Configuration for Mojara Dashboards & Main Homepage Trading Graphs
document.addEventListener('DOMContentLoaded', () => {
  // 1. Homepage Mandi Price Trend Line Chart
  const homeMandiTrendCtx = document.getElementById('homeMandiTrendChart');
  if (homeMandiTrendCtx) {
    new Chart(homeMandiTrendCtx, {
      type: 'line',
      data: {
        labels: ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
        datasets: [
          {
            label: 'Mandya Ragi (₹/Quintal)',
            data: [3100, 3250, 3400, 3350, 3500, 3600],
            borderColor: '#2e7d32',
            backgroundColor: 'rgba(46, 125, 50, 0.15)',
            fill: true,
            tension: 0.35,
            borderWidth: 3
          },
          {
            label: 'Kolar Tomato (₹/Quintal)',
            data: [1800, 2100, 2600, 2900, 2700, 3200],
            borderColor: '#e63946',
            backgroundColor: 'rgba(230, 57, 70, 0.1)',
            fill: true,
            tension: 0.35,
            borderWidth: 3
          },
          {
            label: 'Shivamogga Arecanut (₹/Quintal)',
            data: [42000, 43500, 45000, 44000, 46000, 47500],
            borderColor: '#f57f17',
            backgroundColor: 'rgba(245, 127, 23, 0.1)',
            fill: false,
            tension: 0.35,
            borderWidth: 3
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { position: 'top' },
          tooltip: { mode: 'index', intersect: false }
        },
        scales: {
          y: { grid: { color: 'rgba(0,0,0,0.05)' } },
          x: { grid: { display: false } }
        }
      }
    });
  }

  // 2. Homepage District Trading Volume Bar Chart
  const homeDistrictVolumeCtx = document.getElementById('homeDistrictVolumeChart');
  if (homeDistrictVolumeCtx) {
    new Chart(homeDistrictVolumeCtx, {
      type: 'bar',
      data: {
        labels: ['Mandya', 'Shivamogga', 'Kolar', 'Chitradurga', 'Hassan'],
        datasets: [{
          label: 'Mandi Trading Volume (Tons)',
          data: [420, 580, 390, 310, 460],
          backgroundColor: ['#1b5e3b', '#2e7d32', '#4caf50', '#81c784', '#a5d6a7'],
          borderRadius: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false }
        },
        scales: {
          y: { grid: { color: 'rgba(0,0,0,0.05)' } },
          x: { grid: { display: false } }
        }
      }
    });
  }

  // 3. Farmer Sales Performance Chart
  const farmerSalesCtx = document.getElementById('farmerSalesChart');
  if (farmerSalesCtx) {
    new Chart(farmerSalesCtx, {
      type: 'line',
      data: {
        labels: ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
        datasets: [{
          label: 'Monthly Earnings (₹)',
          data: [3200, 4800, 5400, 6100, 7800, 11300],
          borderColor: '#2d6a4f',
          backgroundColor: 'rgba(82, 183, 136, 0.2)',
          fill: true,
          tension: 0.4,
          borderWidth: 3,
          pointRadius: 5
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false }
        },
        scales: {
          y: { grid: { color: 'rgba(0,0,0,0.05)' } },
          x: { grid: { display: false } }
        }
      }
    });
  }

  // 4. Admin Platform Analytics Charts
  const adminRevenueCtx = document.getElementById('adminRevenueChart');
  if (adminRevenueCtx) {
    fetch('/api/analytics/dashboard')
    .then(res => res.json())
    .then(data => {
      new Chart(adminRevenueCtx, {
        type: 'bar',
        data: {
          labels: data.revenue_labels,
          datasets: [{
            label: 'Platform GMV Revenue (₹)',
            data: data.revenue_data,
            backgroundColor: '#40916c',
            borderRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
      });
    });
  }

  const categoryDoughnutCtx = document.getElementById('categoryShareChart');
  if (categoryDoughnutCtx) {
    new Chart(categoryDoughnutCtx, {
      type: 'doughnut',
      data: {
        labels: ['Fresh Crops', 'Certified Seeds', 'Bio Fertilizers', 'Agri Tools', 'Bio Pesticides'],
        datasets: [{
          data: [45, 20, 15, 12, 8],
          backgroundColor: ['#2d6a4f', '#52b788', '#d4a373', '#8c5e36', '#74c69d']
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    });
  }

  // 5. Officer Regional District Yield Chart
  const districtYieldCtx = document.getElementById('districtYieldChart');
  if (districtYieldCtx) {
    new Chart(districtYieldCtx, {
      type: 'radar',
      data: {
        labels: ['Mandya', 'Haveri', 'Dharwad', 'Kolar', 'Shimoga', 'Mysuru'],
        datasets: [{
          label: 'District Crop Yield Index (Tons/Acre)',
          data: [3.4, 2.8, 3.1, 2.5, 2.1, 2.9],
          borderColor: '#e65100',
          backgroundColor: 'rgba(230, 81, 0, 0.2)'
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    });
  }
});
