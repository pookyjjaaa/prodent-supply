// ===== NAVIGATION =====
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobile-menu');
if (hamburger) {
  hamburger.addEventListener('click', () => mobileMenu.classList.toggle('open'));
}

// Mark active nav link
document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(link => {
  if (link.href === location.href) link.classList.add('active');
});

// ===== CATALOG TABS =====
const tabs = document.querySelectorAll('.cat-tab');
const categories = document.querySelectorAll('.catalog-category');
const searchInput = document.getElementById('product-search');

function activateTab(slug) {
  tabs.forEach(t => t.classList.toggle('active', t.dataset.cat === slug));
  categories.forEach(c => c.classList.toggle('active', c.dataset.cat === slug));
}

tabs.forEach(tab => {
  tab.addEventListener('click', () => activateTab(tab.dataset.cat));
});

// ===== SEARCH (filters catalog images by page label) =====
if (searchInput) {
  searchInput.addEventListener('input', () => {
    const q = searchInput.value.trim().toLowerCase();
    if (!q) {
      document.querySelectorAll('.catalog-page-img').forEach(el => el.style.display = '');
      return;
    }
    document.querySelectorAll('.catalog-page-img').forEach(el => {
      const label = el.querySelector('.catalog-page-label')?.textContent.toLowerCase() || '';
      el.style.display = label.includes(q) ? '' : 'none';
    });
  });
}

// ===== LIGHTBOX =====
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
let currentImages = [];
let currentIndex = 0;

function openLightbox(imgSrc, images, index) {
  currentImages = images;
  currentIndex = index;
  lightboxImg.src = imgSrc;
  lightbox.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  lightbox?.classList.remove('open');
  document.body.style.overflow = '';
}

function lightboxNav(dir) {
  currentIndex = (currentIndex + dir + currentImages.length) % currentImages.length;
  lightboxImg.src = currentImages[currentIndex];
}

document.getElementById('lightbox-close')?.addEventListener('click', closeLightbox);
document.getElementById('lightbox-prev')?.addEventListener('click', () => lightboxNav(-1));
document.getElementById('lightbox-next')?.addEventListener('click', () => lightboxNav(1));
lightbox?.addEventListener('click', e => { if (e.target === lightbox) closeLightbox(); });
document.addEventListener('keydown', e => {
  if (!lightbox?.classList.contains('open')) return;
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowLeft') lightboxNav(-1);
  if (e.key === 'ArrowRight') lightboxNav(1);
});

// Wire up catalog page images
document.querySelectorAll('.catalog-category').forEach(cat => {
  const imgs = Array.from(cat.querySelectorAll('.catalog-page-img img')).map(i => i.src);
  cat.querySelectorAll('.catalog-page-img').forEach((el, idx) => {
    el.addEventListener('click', () => openLightbox(imgs[idx], imgs, idx));
  });
});

// ===== CART =====
const CART_KEY = 'prodent_cart';

function getCart() {
  try { return JSON.parse(localStorage.getItem(CART_KEY) || '[]'); }
  catch { return []; }
}
function saveCart(items) { localStorage.setItem(CART_KEY, JSON.stringify(items)); }

function cartFind(slug) { return getCart().find(i => i.slug === slug); }

function addToCart(slug, label, qty = 1, code = '', brand = '') {
  const cart = getCart();
  const existing = cart.find(i => i.slug === slug);
  if (existing) { existing.qty = qty; existing.code = code; existing.brand = brand; }
  else { cart.push({ slug, label, qty, code, brand }); }
  saveCart(cart);
}
function removeFromCart(slug) { saveCart(getCart().filter(i => i.slug !== slug)); }
function setCartQty(slug, qty) {
  if (qty < 1) { removeFromCart(slug); return; }
  const cart = getCart();
  const item = cart.find(i => i.slug === slug);
  if (item) { item.qty = qty; saveCart(cart); }
}
function clearCart() { saveCart([]); }

function toggleCartItem(slug, label) {
  cartFind(slug) ? removeFromCart(slug) : addToCart(slug, label, 1);
}

function updateCartBar() {
  const bar = document.getElementById('cart-bar');
  if (!bar) return;
  const n = getCart().length;
  const icon = bar.querySelector('.cart-bar-icon');
  const lbl = bar.querySelector('.cart-bar-label');
  if (icon) icon.textContent = n;
  if (lbl) lbl.textContent = n === 1 ? '1 producto seleccionado' : `${n} productos seleccionados`;
  bar.classList.toggle('visible', n > 0);
}

function updateAddButtons() {
  const cart = getCart();
  document.querySelectorAll('.btn-add-cart').forEach(btn => {
    const item = cart.find(i => i.slug === btn.dataset.slug);
    btn.classList.toggle('in-cart', !!item);
    btn.textContent = item ? `✓ Agregado (${item.qty})` : '+ Agregar a cotización';
  });
}

// Wire cart buttons
document.querySelectorAll('.btn-add-cart').forEach(btn => {
  btn.addEventListener('click', () => {
    toggleCartItem(btn.dataset.slug, btn.dataset.label);
    updateCartBar();
    updateAddButtons();
  });
});

updateCartBar();
updateAddButtons();

// ===== COTIZACION PAGE =====
function renderCartItems() {
  const section = document.getElementById('cart-items-section');
  if (!section) return;
  const cart = getCart();
  const list = section.querySelector('.cart-items-list');
  const empty = section.querySelector('.cart-empty-msg');
  const clearBtn = section.querySelector('.cart-clear-btn');

  if (!list) return;
  list.innerHTML = '';

  if (cart.length === 0) {
    if (empty) empty.style.display = '';
    if (clearBtn) clearBtn.style.display = 'none';
    return;
  }
  if (empty) empty.style.display = 'none';
  if (clearBtn) clearBtn.style.display = '';

  cart.forEach(({ slug, label, qty }) => {
    const row = document.createElement('div');
    row.className = 'cart-item-row';
    row.dataset.slug = slug;
    row.innerHTML = `
      <span class="cart-item-name">${label}</span>
      <div class="cart-item-qty">
        <button class="qty-btn qty-minus" aria-label="Reducir cantidad">−</button>
        <span class="qty-val">${qty}</span>
        <button class="qty-btn qty-plus" aria-label="Aumentar cantidad">+</button>
        <button class="cart-item-remove" aria-label="Quitar ${label}">✕</button>
      </div>`;
    let q = qty;
    row.querySelector('.qty-minus').addEventListener('click', () => {
      q = Math.max(1, q - 1);
      row.querySelector('.qty-val').textContent = q;
      setCartQty(slug, q);
      updateAddButtons();
    });
    row.querySelector('.qty-plus').addEventListener('click', () => {
      q++;
      row.querySelector('.qty-val').textContent = q;
      setCartQty(slug, q);
      updateAddButtons();
    });
    row.querySelector('.cart-item-remove').addEventListener('click', () => {
      removeFromCart(slug);
      renderCartItems();
      updateCartBar();
      updateAddButtons();
    });
    list.appendChild(row);
  });
}

if (document.getElementById('cart-items-section')) {
  renderCartItems();
  document.querySelector('.cart-clear-btn')?.addEventListener('click', () => {
    clearCart();
    renderCartItems();
    updateCartBar();
    updateAddButtons();
  });
}

// ===== WHATSAPP QUOTE (cotizacion page) =====
const waForm = document.getElementById('wa-form');
if (waForm) {
  waForm.addEventListener('submit', e => {
    e.preventDefault();
    const nombre = document.getElementById('nombre').value.trim();
    const clinica = document.getElementById('clinica').value.trim();
    const ciudad = document.getElementById('ciudad').value.trim();
    const notas = document.getElementById('productos').value.trim();
    const cart = getCart();

    let productosTxt = '';
    if (cart.length > 0) {
      productosTxt += cart.map(i => {
        const code  = i.code  ? `[${i.code}] `  : '';
        const brand = i.brand ? ` · ${i.brand}` : '';
        const qty   = i.qty > 1 ? ` (x${i.qty})` : '';
        return `• ${code}${i.label}${brand}${qty}`;
      }).join('\n');
    }
    if (notas) {
      productosTxt += (productosTxt ? '\n\n' : '') + '*Notas adicionales:*\n' + notas;
    }
    if (!productosTxt) productosTxt = '(sin especificar)';

    const msg = `Hola, me interesa cotizar productos de ProDent Supply.

*Nombre:* ${nombre}
*Clínica:* ${clinica || 'N/A'}
*Ciudad:* ${ciudad}
*Catálogos de interés:*
${productosTxt}`;
    window.open(`https://wa.me/523311098409?text=${encodeURIComponent(msg)}`, '_blank');
  });
}
