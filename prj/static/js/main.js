// Mojara Smart Agriculture Application Logic
function toggleSidebar() {
  const sidebar = document.getElementById('agri-sidebar');
  if (sidebar) {
    const isCollapsed = sidebar.classList.contains('collapsed');
    if (isCollapsed) {
      sidebar.classList.remove('collapsed');
      sidebar.classList.add('mobile-open');
      sessionStorage.setItem('sidebar_auto_closed', 'false');
    } else {
      sidebar.classList.add('collapsed');
      sidebar.classList.remove('mobile-open');
      sessionStorage.setItem('sidebar_auto_closed', 'true');
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const sidebar = document.getElementById('agri-sidebar');
  const sidebarClosedState = sessionStorage.getItem('sidebar_auto_closed');

  // 1. Maintain closed sidebar state if user previously selected a menu option
  if (sidebar && sidebarClosedState === 'true') {
    sidebar.classList.add('collapsed');
    sidebar.classList.remove('mobile-open');
  }

  // 2. Auto-close sidebar immediately when user selects ANY menu option (Desktop & Mobile)
  const sidebarLinks = document.querySelectorAll('.sidebar-link');
  sidebarLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (sidebar) {
        sidebar.classList.add('collapsed');
        sidebar.classList.remove('mobile-open');
        sessionStorage.setItem('sidebar_auto_closed', 'true');
      }
    });
  });

  // 3. Dark Mode Persistence
  const themeToggleBtn = document.getElementById('theme-toggle');
  const isDarkMode = localStorage.getItem('mojara_dark_mode') === 'true';
  
  if (isDarkMode) {
    document.body.classList.add('dark-mode');
    updateThemeIcon(true);
  }
  
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const activeDark = document.body.classList.toggle('dark-mode');
      localStorage.setItem('mojara_dark_mode', activeDark);
      updateThemeIcon(activeDark);
    });
  }
  
  function updateThemeIcon(isDark) {
    if (!themeToggleBtn) return;
    const icon = themeToggleBtn.querySelector('i');
    if (icon) {
      icon.className = isDark ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
    }
  }
  
  // 4. Auto Dismiss Flash Messages
  const alerts = document.querySelectorAll('.alert-mojara');
  alerts.forEach(alert => {
    setTimeout(() => {
      alert.style.opacity = '0';
      alert.style.transition = 'opacity 0.5s ease';
      setTimeout(() => alert.remove(), 500);
    }, 4500);
  });
});
