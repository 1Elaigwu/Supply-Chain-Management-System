# Database Design

## Introduction
The Supply Chain Management System is a comprehensive software solution designed to streamline and optimize various aspects of supply chain operations for businesses. From inventory 
management to order tracking and reporting, this system provides essential tools for effectively managing the flow of goods and services from suppliers to customers.

## Key Features
1. **Scalability:** Designed to handle a large volume of suppliers, products, and orders as the project grows.
2. **Data Integrity:** Ensures data accuracy and consistency through the use of foreign key constraints and data validation.
3. **Real-time Updates:** Utilizes timestamps to track the latest stock updates and shipment dates for efficient inventory management.
4. **Order Tracking:** Allows tracking of order history, including order dates, quantities, and statuses (Pending, Delivered, Cancelled).
5. **Supplier Management:** Stores supplier information such as name, contact details, and address for effective supplier management.
6. **Comprehensive Reporting:** Provides a solid foundation for generating reports on inventory levels, product sales, and supplier performance.

## Entity-Relationship Diagram (ERD)
![ERD](link_to_erd_image)

## Tables

### Suppliers Table
- **supplier_id**: Unique identifier for each supplier.
- **supplier_name**: Name of the supplier.
- **supplier_contact**: Contact information for the supplier.
- **supplier_address**: Address of the supplier.

### Products Table
- **product_id**: Unique identifier for each product.
- **product_name**: Name of the product.
- **unit_price**: Price of the product per unit.
- **quantity_in_stock**: Quantity of the product available in stock.

### Inventory Table
- **inventory_id**: Unique identifier for each inventory item.
- **product_id**: Foreign key referencing the product ID.
- **quantity_available**: Quantity of the product available in inventory.
- **last_stock_update**: Timestamp indicating the last update to the stock quantity.

### Shipments Table
- **shipment_id**: Unique identifier for each shipment.
- **product_id**: Foreign key referencing the product ID.
- **supplier_id**: Foreign key referencing the supplier ID.
- **quantity_shipped**: Quantity of the product shipped in the shipment.
- **shipment_date**: Date of the shipment.

### Order History Table
- **order_id**: Unique identifier for each order.
- **product_id**: Foreign key referencing the product ID.
- **order_date**: Date when the order was placed.
- **order_quantity**: Quantity of the product ordered.
- **total_cost**: Total cost of the order.
- **status**: Status of the order (Pending, Delivered, Cancelled).

## Relationships

### Suppliers to Shipments
- Each shipment in the **Shipments** table is associated with a supplier through the **supplier_id** foreign key, establishing a one-to-many relationship between suppliers and shipments. This relationship indicates that a supplier can have multiple shipments.

### Products to Inventory and Shipments
- The **Inventory** table maintains the current stock of products, where each inventory item is linked to a specific product through the **product_id** foreign key. This establishes a one-to-one relationship between products and inventory items, indicating that each product has only one corresponding inventory item.
- The **Shipments** table also relates to products through the **product_id** foreign key, indicating that each shipment involves a specific product. This creates a one-to-many relationship between products and shipments, implying that a product can be part of multiple shipments.

### Products to Order History
- The **Order History** table links to products through the **product_id** foreign key, establishing a one-to-many relationship between products and orders. This relationship indicates that a product can be associated with multiple orders over time.

