// Fetch inventory data from backend
fetch('/api/inventory')
    .then(response => response.json())
    .then(data => {
        const inventoryList = document.getElementById('inventory-list');
        data.forEach(item => {
            const itemDiv = document.createElement('div');
            itemDiv.classList.add('item');
            itemDiv.innerHTML = `
                <h2>${item.product_name}</h2>
                <p>Available Quantity: ${item.quantity_available}</p>
                <p>Last Stock Update: ${item.last_stock_update}</p>
            `;
            inventoryList.appendChild(itemDiv);
        });
    })
    .catch(error => console.error('Error fetching inventory data:', error));