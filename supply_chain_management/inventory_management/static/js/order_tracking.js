// Fetch order data from backend
fetch('/api/orders')
    .then(response => response.json())
    .then(data => {
        const orderBody = document.getElementById('order-body');
        data.forEach(order => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${order.order_id}</td>
                <td>${order.product_name}</td>
                <td>${order.order_date}</td>
                <td>${order.status}</td>
            `;
            orderBody.appendChild(row);
        });
    })
    .catch(error => console.error('Error fetching order data:', error));