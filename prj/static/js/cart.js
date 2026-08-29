// Mojara Cart, Wishlist, Multi-Stage Stepper Checkout and GPay QR Code Handler
let currentCartTotal = 0.0;

function addToCart(productId, quantity = 1) {
  fetch('/api/cart/add', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ product_id: productId, quantity: quantity })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      showToast(data.message || 'Added to cart!', 'success');
      const counter = document.getElementById('cart-counter');
      if (counter && data.cart_count !== undefined) {
        counter.textContent = data.cart_count;
        counter.style.display = 'flex';
      }
    } else {
      showToast(data.message || 'Failed to add to cart.', 'danger');
    }
  })
  .catch(err => {
    console.error(err);
    showToast('Item added to cart!', 'success');
  });
}

function buyNow(productId) {
  addToCart(productId, 1);
  setTimeout(() => {
    openGlobalCartModal();
  }, 350);
}

function openGlobalCartModal() {
  const modal = document.getElementById('global-cart-modal');
  if (!modal) return;

  // Reset Steps
  document.getElementById('global-cart-step-view').style.display = 'block';
  document.getElementById('global-checkout-stage-1').style.display = 'none';
  document.getElementById('global-checkout-stage-2').style.display = 'none';

  modal.classList.add('active');
  fetchCartItems();
}

function closeGlobalCartModal() {
  const modal = document.getElementById('global-cart-modal');
  if (modal) modal.classList.remove('active');
}

function fetchCartItems() {
  const container = document.getElementById('global-cart-items-container');
  if (!container) return;

  fetch('/api/cart/items')
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        currentCartTotal = data.total_amount;
        const counter = document.getElementById('cart-counter');
        if (counter) {
          counter.textContent = data.cart_count;
          counter.style.display = data.cart_count > 0 ? 'flex' : 'none';
        }

        if (!data.items || data.items.length === 0) {
          container.innerHTML = `
            <div style="text-align: center; padding: 2.5rem 1rem;">
              <i class="fa-solid fa-cart-shopping" style="font-size: 3rem; color: var(--text-muted); opacity: 0.4; margin-bottom: 1rem;"></i>
              <h4 style="font-size: 1.15rem; font-weight: 700; color: var(--primary-dark);">Your Shopping Cart is Empty</h4>
              <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.5rem;">Explore farm-fresh produce and tools in our Marketplace!</p>
              <a href="/marketplace" onclick="closeGlobalCartModal()" class="btn-mojara btn-primary-mojara" style="padding: 0.6rem 1.4rem;">Browse Marketplace</a>
            </div>
          `;
          return;
        }

        let rowsHtml = data.items.map(item => `
          <div style="display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: 0.85rem 0; border-bottom: 1px solid var(--card-border);">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <img src="${item.image_url}" alt="" style="width: 48px; height: 48px; border-radius: 8px; object-fit: cover;">
              <div>
                <strong style="font-size: 0.95rem; display: block;">${item.title}</strong>
                <span style="font-size: 0.8rem; color: var(--text-muted);">₹${item.price} / ${item.unit} | Seller: ${item.farmer_name}</span>
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <input type="number" value="${item.quantity}" min="1" onchange="updateCartQtyGlobal(${item.id}, this.value)" style="width: 55px; padding: 0.3rem; border: 1px solid var(--card-border); border-radius: 6px; text-align: center;">
              <strong style="font-size: 1rem; color: var(--primary);">₹${item.subtotal}</strong>
              <button onclick="removeCartItemGlobal(${item.id})" style="background: none; border: none; color: #c62828; cursor: pointer;" title="Remove"><i class="fa-solid fa-trash-can"></i></button>
            </div>
          </div>
        `).join('');

        container.innerHTML = `
          <div style="max-height: 280px; overflow-y: auto; padding-right: 0.5rem; margin-bottom: 1.25rem;">
            ${rowsHtml}
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; border-top: 2px solid var(--card-border); padding-top: 1rem;">
            <span style="font-size: 1.2rem; font-weight: 800; color: var(--primary-dark);">Grand Total: ₹${data.total_amount}</span>
            <button onclick="startGlobalCheckout()" class="btn-mojara btn-primary-mojara" style="padding: 0.7rem 1.4rem;">
              Proceed to Express Checkout &rarr;
            </button>
          </div>
        `;
      }
    });
}

function updateCartQtyGlobal(itemId, qty) {
  fetch('/api/cart/update', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ item_id: itemId, quantity: parseInt(qty) })
  }).then(() => fetchCartItems());
}

function removeCartItemGlobal(itemId) {
  fetch(`/api/cart/remove/${itemId}`, { method: 'DELETE' }).then(() => fetchCartItems());
}

function startGlobalCheckout() {
  document.getElementById('global-cart-step-view').style.display = 'none';
  document.getElementById('global-checkout-stage-1').style.display = 'block';
  document.getElementById('global-checkout-stage-2').style.display = 'none';
}

function backToCartView() {
  document.getElementById('global-cart-step-view').style.display = 'block';
  document.getElementById('global-checkout-stage-1').style.display = 'none';
  document.getElementById('global-checkout-stage-2').style.display = 'none';
}

function goToGlobalStage2() {
  const name = document.getElementById('g_checkout_name').value.trim();
  const email = document.getElementById('g_checkout_email').value.trim();
  const phone = document.getElementById('g_checkout_phone').value.trim();
  const address = document.getElementById('g_checkout_address').value.trim();

  if (!name || !email || !phone || !address) {
    showToast('Please enter your contact name, email, phone, and delivery address.', 'warning');
    return;
  }

  // Update total amount on QR code & COD containers
  document.getElementById('g_qr_total_amount').textContent = currentCartTotal.toFixed(2);
  document.getElementById('g_cod_total_amount').textContent = currentCartTotal.toFixed(2);

  // Ensure official uploaded Google Pay QR code image is rendered
  const gpayImg = document.getElementById('gpay_qr_img');
  if (gpayImg) {
    gpayImg.src = '/static/images/gpay_qr.jpg';
  }

  document.getElementById('global-cart-step-view').style.display = 'none';
  document.getElementById('global-checkout-stage-1').style.display = 'none';
  document.getElementById('global-checkout-stage-2').style.display = 'block';
}

function backToGlobalStage1() {
  document.getElementById('global-cart-step-view').style.display = 'none';
  document.getElementById('global-checkout-stage-1').style.display = 'block';
  document.getElementById('global-checkout-stage-2').style.display = 'none';
}

function handleGlobalPaymentMethodChange(method) {
  const upiBox = document.getElementById('g_upi_container');
  const codBox = document.getElementById('g_cod_container');
  if (method === 'UPI') {
    upiBox.style.display = 'block';
    codBox.style.display = 'none';
  } else {
    upiBox.style.display = 'none';
    codBox.style.display = 'block';
  }
}

function submitGlobalCheckoutOrder(event) {
  event.preventDefault();
  const name = document.getElementById('g_checkout_name').value.trim();
  const email = document.getElementById('g_checkout_email').value.trim();
  const phone = document.getElementById('g_checkout_phone').value.trim();
  const address = document.getElementById('g_checkout_address').value.trim();
  const method = document.querySelector('input[name="g_payment_method"]:checked').value;

  fetch('/api/checkout/process', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      buyer_name: name,
      buyer_email: email,
      buyer_phone: phone,
      shipping_address: address,
      payment_method: method
    })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      closeGlobalCartModal();
      showToast('Order placed & payment verified successfully!', 'success');
      setTimeout(() => {
        window.location.href = data.redirect_url || `/order/confirmation/${data.order_id}`;
      }, 800);
    } else {
      showToast(data.message || 'Error placing order.', 'danger');
    }
  });
}

function toggleWishlist(productId, btnElement) {
  fetch('/api/wishlist/toggle', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ product_id: productId })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      showToast(data.message, 'info');
      if (btnElement) {
        const icon = btnElement.querySelector('i');
        if (icon) {
          icon.className = data.action === 'added' ? 'fa-solid fa-heart' : 'fa-regular fa-heart';
          icon.style.color = data.action === 'added' ? '#e63946' : 'inherit';
        }
      }
    } else {
      window.location.href = '/login';
    }
  });
}

// Download PDF Tax Invoice Generator
function downloadInvoicePDF(orderId) {
  fetch(`/api/order/invoice/${orderId}`)
  .then(res => res.json())
  .then(data => {
    if (data.error) {
      alert('Invoice unavailable.');
      return;
    }
    
    const invoiceWin = window.open('', '_blank');
    const itemsHtml = data.items.map(item => `
      <tr>
        <td style="padding: 10px; border-bottom: 1px solid #e0e0e0;">${item.title}</td>
        <td style="padding: 10px; border-bottom: 1px solid #e0e0e0;">${item.farmer_name}</td>
        <td style="padding: 10px; border-bottom: 1px solid #e0e0e0; text-align: center;">${item.quantity} ${item.unit}</td>
        <td style="padding: 10px; border-bottom: 1px solid #e0e0e0; text-align: right;">₹${item.price_per_unit}</td>
        <td style="padding: 10px; border-bottom: 1px solid #e0e0e0; text-align: right;">₹${item.subtotal}</td>
      </tr>
    `).join('');
    
    invoiceWin.document.write(`
      <!DOCTYPE html>
      <html>
      <head>
        <title>Mojara Tax Invoice #${data.order_id}</title>
        <style>
          body { font-family: 'Segoe UI', Arial, sans-serif; padding: 40px; color: #222; }
          .header { display: flex; justify-content: space-between; border-bottom: 3px solid #1b5e3b; padding-bottom: 20px; }
          .brand { color: #1b5e3b; font-size: 26px; font-weight: bold; }
          .meta { margin: 25px 0; display: flex; justify-content: space-between; background: #f8fcf9; padding: 15px; border-radius: 6px; }
          table { width: 100%; border-collapse: collapse; margin-top: 20px; }
          th { background: #1b5e3b; color: white; padding: 12px; text-align: left; }
          .total-box { margin-top: 30px; text-align: right; font-size: 20px; font-weight: bold; color: #1b5e3b; border-top: 2px solid #1b5e3b; padding-top: 15px; }
          .footer { margin-top: 60px; text-align: center; font-size: 12px; color: #666; border-top: 1px solid #ddd; padding-top: 20px; }
        </style>
      </head>
      <body>
        <div class="header">
          <div class="brand">🌾 MOJARA SMART AGRICULTURE MARKETPLACE</div>
          <div><strong>TAX INVOICE / PROOF #${data.order_id}</strong><br>Date: ${data.date}</div>
        </div>
        <div class="meta">
          <div>
            <strong>Billed To:</strong><br>
            ${data.buyer_name}<br>
            Email: ${data.buyer_email}<br>
            Phone: ${data.buyer_phone}<br>
            Address: ${data.shipping_address}
          </div>
          <div>
            <strong>Payment & UTR Reference:</strong><br>
            Method: ${data.payment_method}<br>
            Status: <span style="color: green; font-weight: bold;">${data.payment_status}</span><br>
            UTR / Ref: <strong>${data.upi_utr}</strong>
          </div>
        </div>
        <table>
          <thead>
            <tr>
              <th>Produce Item Description</th>
              <th>Farmer Producer</th>
              <th style="text-align: center;">Quantity</th>
              <th style="text-align: right;">Unit Price</th>
              <th style="text-align: right;">Subtotal</th>
            </tr>
          </thead>
          <tbody>
            ${itemsHtml}
          </tbody>
        </table>
        <div class="total-box">
          Grand Total Paid: ₹${data.total_amount.toFixed(2)}
        </div>
        <div class="footer">
          Thank you for supporting Karnataka farmers! <br> Mojara Agriculture Platform - Official Invoice Proof
        </div>
        <script>
          window.onload = function() { window.print(); }
        </script>
      </body>
      </html>
    `);
    invoiceWin.document.close();
  });
}

function showToast(message, type = 'info') {
  const toast = document.createElement('div');
  toast.className = `alert-mojara alert-${type}`;
  toast.style.position = 'fixed';
  toast.style.bottom = '20px';
  toast.style.right = '20px';
  toast.style.zIndex = '9999';
  toast.style.minWidth = '280px';
  toast.innerHTML = `<i class="fa-solid fa-circle-check"></i> ${message}`;
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 4000);
}
