// NAV
const nav = document.getElementById('navbar');
window.addEventListener('scroll', () => nav.classList.toggle('scrolled', scrollY > 50));

let mobileOpen = false;
document.getElementById('navToggle').addEventListener('click', () => {
  const links = document.getElementById('navLinks');
  mobileOpen = !mobileOpen;
  if (mobileOpen) {
    Object.assign(links.style, {display:'flex',flexDirection:'column',position:'absolute',
      top:'100%',left:'0',right:'0',background:'rgba(8,8,8,.98)',
      padding:'24px',gap:'16px',borderTop:'1px solid var(--border)'});
  } else {
    links.style.display = '';
  }
});

document.querySelectorAll('#navLinks a').forEach(a =>
  a.addEventListener('click', () => { mobileOpen = false; document.getElementById('navLinks').style.display = ''; })
);

// SCROLL REVEAL
const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.08 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
