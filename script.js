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

// Close mobile nav on link click
document.querySelectorAll('#navLinks a').forEach(a =>
  a.addEventListener('click', () => { mobileOpen = false; document.getElementById('navLinks').style.display = ''; })
);

// MENU TABS
document.querySelectorAll('.menu-tab').forEach(tab =>
  tab.addEventListener('click', function() {
    document.querySelectorAll('.menu-tab').forEach(t => t.classList.remove('active'));
    this.classList.add('active');
    const f = this.dataset.filter;
    document.querySelectorAll('.menu-card').forEach(c =>
      c.style.display = (f === 'all' || c.dataset.cat === f) ? '' : 'none'
    );
  })
);

// BUILDER STATE
const BASE = 8;
const state = {
  bun:     { v:'Brioche', p:0 },
  protein: { v:'Manzo 150g', p:0 },
  cheese:  { v:'Cheddar', p:0 },
  sauce:   { v:'Salsa Segreta Buns 50', p:0 },
  toppings: []
};

function pick(el, cat) {
  el.parentElement.querySelectorAll('.opt').forEach(o => o.classList.remove('sel'));
  el.classList.add('sel');
  state[cat] = { v: el.dataset.v, p: parseFloat(el.dataset.p) || 0 };
  refresh();
}

function tog(el) {
  const v = el.dataset.v, p = parseFloat(el.dataset.p) || 0;
  if (el.classList.contains('sel')) {
    el.classList.remove('sel');
    state.toppings = state.toppings.filter(t => t.v !== v);
  } else {
    if (state.toppings.length >= 4) {
      el.style.animation = 'shake .35s';
      setTimeout(() => el.style.animation = '', 400);
      return;
    }
    el.classList.add('sel');
    state.toppings.push({ v, p });
  }
  refresh();
}

function refresh() {
  document.getElementById('sv-bun').textContent     = state.bun.v;
  document.getElementById('sv-protein').textContent = state.protein.v;
  document.getElementById('sv-cheese').textContent  = state.cheese.v;
  document.getElementById('sv-sauce').textContent   = state.sauce.v;
  const tops = state.toppings.map(t => t.v);
  document.getElementById('sv-toppings').textContent = tops.length ? tops.join(', ') : 'Nessuno';
  const extra = state.bun.p + state.protein.p + state.cheese.p +
    state.toppings.reduce((s,t) => s+t.p, 0) + state.sauce.p;
  document.getElementById('sv-total').textContent = '€' + (BASE + extra).toFixed(2).replace('.',',');
}

// ⚠️ SOSTITUISCI questo numero con il numero reale del locale (es. 393331234567)
const WA_NUMBER = '3917693475';

// CART
const cart = [];

function openCart() {
  document.getElementById('cartPanel').classList.add('open');
  document.getElementById('cartOverlay').classList.add('open');
}

function closeCart() {
  document.getElementById('cartPanel').classList.remove('open');
  document.getElementById('cartOverlay').classList.remove('open');
}

function addToCart(name, price, details) {
  if (!details) {
    const idx = cart.findIndex(i => i.name === name && !i.details);
    if (idx >= 0) { cart[idx].qty++; renderCart(); openCart(); return; }
  }
  cart.push({ name, price, qty: 1, details: details || null });
  renderCart();
  openCart();
}

function addBuilderToCart() {
  const { bun, protein, cheese, sauce, toppings } = state;
  const extra = bun.p + protein.p + cheese.p + toppings.reduce((s,t)=>s+t.p,0) + sauce.p;
  const price = BASE + extra;
  const details = {
    bun: bun.v, protein: protein.v, cheese: cheese.v,
    toppings: toppings.length ? toppings.map(t=>t.v).join(', ') : 'Nessuno',
    sauce: sauce.v
  };
  addToCart('Panino Personalizzato', price, details);
  const btn = document.getElementById('btn-add-builder');
  const orig = btn.innerHTML;
  btn.textContent = '✓ Aggiunto al carrello!';
  setTimeout(() => btn.innerHTML = orig, 1600);
}

function orderItem(name, price) {
  addToCart(name, price, null);
}

function updateQty(idx, delta) {
  cart[idx].qty += delta;
  if (cart[idx].qty <= 0) cart.splice(idx, 1);
  renderCart();
}

function removeFromCart(idx) {
  cart.splice(idx, 1);
  renderCart();
}

function renderCart() {
  const container = document.getElementById('cartItems');
  const badge     = document.getElementById('cartBadge');
  const totalEl   = document.getElementById('cart-total');
  const totalQty  = cart.reduce((s,i) => s + i.qty, 0);
  const totalPrice= cart.reduce((s,i) => s + i.price * i.qty, 0);

  badge.textContent = totalQty;
  badge.classList.toggle('hidden', totalQty === 0);
  totalEl.textContent = '€' + totalPrice.toFixed(2).replace('.',',');

  if (!cart.length) {
    container.innerHTML = '<p class="cart-empty">Il carrello è vuoto<br>Aggiungi qualcosa dal menu 🍔</p>';
    return;
  }
  container.innerHTML = cart.map((item, idx) => `
    <div class="cart-item">
      <div class="cart-item-hd">
        <span class="cart-item-name">${item.name}</span>
        <span class="cart-item-price">€${(item.price * item.qty).toFixed(2).replace('.',',')}</span>
      </div>
      ${item.details ? `<div class="cart-item-details">
        🥖 ${item.details.bun} &nbsp;·&nbsp; 🥩 ${item.details.protein} &nbsp;·&nbsp; 🧀 ${item.details.cheese}<br>
        🥬 ${item.details.toppings} &nbsp;·&nbsp; 🫙 ${item.details.sauce}
      </div>` : `<div class="cart-item-details">€${item.price.toFixed(2).replace('.',',')} cad.</div>`}
      <div class="cart-item-ft">
        <div class="qty-ctrl">
          <button class="qty-btn" onclick="updateQty(${idx},-1)">−</button>
          <span class="qty-val">${item.qty}</span>
          <button class="qty-btn" onclick="updateQty(${idx},1)">+</button>
        </div>
        <button class="cart-remove" onclick="removeFromCart(${idx})">Rimuovi</button>
      </div>
    </div>`).join('');
}

function checkoutCart() {
  if (!cart.length) return;
  openModal();
}

// MODAL
function openModal() {
  document.getElementById('orderModal').classList.add('open');
}

function closeModal() {
  document.getElementById('orderModal').classList.remove('open');
  ['f-name','f-phone','f-time'].forEach(id => document.getElementById(id).classList.remove('err'));
}

document.getElementById('orderModal').addEventListener('click', function(e) {
  if (e.target === this) closeModal();
});

function validateModal() {
  const name  = document.getElementById('f-name').value.trim();
  const phone = document.getElementById('f-phone').value.trim();
  const time  = document.getElementById('f-time').value;
  document.getElementById('f-name').classList.toggle('err', !name);
  document.getElementById('f-phone').classList.toggle('err', !phone);
  document.getElementById('f-time').classList.toggle('err', !time);
  return (name && phone && time) ? { name, phone, time } : null;
}

function confirmOrder() {
  const data = validateModal();
  if (!data) return;
  closeModal();

  const lines = cart.map(item => {
    let line = `• ${item.qty}x ${item.name} — €${(item.price * item.qty).toFixed(2).replace('.',',')}`;
    if (item.details) {
      line += `\n   ${item.details.bun} |  ${item.details.protein} |  ${item.details.cheese}`;
      line += `\n   ${item.details.toppings} |  ${item.details.sauce}`;
    }
    return line;
  }).join('\n\n');

  const total = cart.reduce((s,i) => s + i.price * i.qty, 0);

  const msg =
` *Ordine Buns 50*

 Nome: ${data.name}
 Telefono: ${data.phone}
 Orario ritiro: ${data.time}

${lines}

 *Totale: €${total.toFixed(2).replace('.',',')}*

 Grazie!`;

  window.open(`https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(msg)}`, '_blank');
  cart.length = 0;
  renderCart();
}

// SCROLL REVEAL
const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.08 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
