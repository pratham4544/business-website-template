// Empty for now, but you can add interactivity later
console.log('Website Loaded');

document.addEventListener('DOMContentLoaded', function() {
  'use strict';
  
  // Mobile Menu Toggle
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const navMenu = document.querySelector('header nav');
  
  if(mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', function() {
      navMenu.classList.toggle('active');
      this.classList.toggle('active');
    });
  }
  
  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      if(targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if(targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 70,
          behavior: 'smooth'
        });
        
        // Close mobile menu if open
        if(navMenu.classList.contains('active')) {
          navMenu.classList.remove('active');
          mobileMenuBtn.classList.remove('active');
        }
      }
    });
  });
  
  // Add sticky header on scroll
  const header = document.querySelector('header');
  const scrollThreshold = 50;
  
  window.addEventListener('scroll', function() {
    if(window.scrollY > scrollThreshold) {
      header.classList.add('sticky');
    } else {
      header.classList.remove('sticky');
    }
  });
  
  // Simple counter animation for stats
  function animateCounter(el, target) {
    let count = 0;
    const duration = 2000; // 2 seconds
    const interval = 50; // Update every 50ms
    const steps = Math.floor(duration / interval);
    const increment = target / steps;
    
    const timer = setInterval(() => {
      count += increment;
      if(count >= target) {
        clearInterval(timer);
        count = target;
      }
      el.textContent = Math.floor(count);
    }, interval);
  }
  
  // Initialize counters when they come into view
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting) {
        const statsElements = entry.target.querySelectorAll('.stat h3');
        statsElements.forEach(el => {
          const target = parseInt(el.textContent.replace(/\+|\D/g, ''));
          el.textContent = '0';
          animateCounter(el, target);
        });
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });
  
  // Observe stats section
  const statsSection = document.querySelector('.about-stats');
  if(statsSection) {
    observer.observe(statsSection);
  }
  
  console.log('TechnoIT Website Loaded');
});
