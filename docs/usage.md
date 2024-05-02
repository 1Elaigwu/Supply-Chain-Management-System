# Schema Setup and Usage

## Schema Setup
The supply chain management database system is structured to efficiently manage various aspects of the supply chain process. The schema setup includes tables for key entities such as suppliers, products, 
orders, customers, inventory, and shipments. Relationships between these entities are established to facilitate data flow and ensure data integrity.

### Suppliers Table
```sql
CREATE TABLE Suppliers (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    supplier_contact VARCHAR(100),
    supplier_address TEXT
);
```
### Products Table
```sql
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL,
    quantity_in_stock INTEGER NOT NULL CHECK (quantity_in_stock >= 0)
);
```
### Inventory Table
```sql
CREATE TABLE Inventory (
    inventory_id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES Products(product_id),
    quantity_available INTEGER NOT NULL CHECK (quantity_available >= 0),
    last_stock_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
### Shipments Table
```sql
CREATE TABLE Shipments (
    shipment_id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES Products(product_id),
    supplier_id INTEGER NOT NULL REFERENCES Suppliers(supplier_id),
    quantity_shipped INTEGER NOT NULL CHECK (quantity_shipped >= 0),
    shipment_date DATE NOT NULL DEFAULT CURRENT_DATE
);
```
### Order History Table
```sql
CREATE TABLE OrderHistory (
    order_id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES Products(product_id),
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    order_quantity INTEGER NOT NULL CHECK (order_quantity > 0),
    total_cost NUMERIC(10, 2) NOT NULL CHECK (total_cost >= 0),
    status VARCHAR(20) NOT NULL,
    CONSTRAINT valid_status CHECK (status IN ('Pending', 'Delivered', 'Cancelled'))
);
```

## Usage
To effectively utilize the supply chain management database system, follow these usage instructions:

1. **Dashboard Navigation:**
   - Navigate to the dashboard to access essential supply chain metrics and insights.
   - Monitor key performance indicators such as order fulfillment rate, inventory turnover, and shipment tracking.

2. **Module Access:**
   - Use the navigation menu to access different modules within the system, including:
     - Order Tracking: View and track the status of orders in real-time.
     - Inventory Management: Manage inventory levels, track stock movements, and receive alerts for low stock items.
     - Reports: Generate custom reports to analyze data trends and identify areas for optimization.

3. **CRUD Operations:**
   - Perform CRUD (Create, Read, Update, Delete) operations on orders and inventory items as needed.
   - Create new orders, update order details, and mark orders as fulfilled.
   - Manage inventory by adding new items, updating stock quantities, and removing obsolete items.

4. **Data Analysis:**
   - Generate reports and analyze data to optimize supply chain performance.
   - Identify trends, patterns, and bottlenecks in the supply chain process.
   - Use insights from data analysis to make informed decisions and improve operational efficiency.

By following these usage instructions, stakeholders can effectively leverage the supply chain management database system to streamline supply chain operations, enhance visibility and control, and drive
business success.
