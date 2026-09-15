CREATE TABLE `Products`(
    `Code` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Name` VARCHAR(255) NOT NULL,
    `Price` SMALLINT NOT NULL,
    `Entry_Date` DATE NOT NULL,
    `Brand` VARCHAR(255) NOT NULL,
    `Stock_Available` SMALLINT NOT NULL
);
CREATE TABLE `Invoices`(
    `Invoice_Number` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Purchase_Date` DATE NOT NULL,
    `Buyer_Email` VARCHAR(255) NOT NULL,
    `Total_Amount` SMALLINT NOT NULL
);
CREATE TABLE `Products Per Invoice`(
    `Invoice_Number_ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Products_Code_ID` INT NOT NULL,
    `Quantity` SMALLINT NOT NULL,
    `Total_Amount` SMALLINT NOT NULL
);
CREATE TABLE `Shopping Cart`(
    `ID` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Buyer_Email` VARCHAR(255) NOT NULL
);
CREATE TABLE `Carts Items`(
    `ID` INT NOT NULL,
    `Shopping_Cart_ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Products_Code_ID` INT NOT NULL,
    `Quantity` SMALLINT NOT NULL
);
ALTER TABLE
    `Carts Items` ADD CONSTRAINT `carts items_products_code_id_foreign` FOREIGN KEY(`Products_Code_ID`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_products_code_id_foreign` FOREIGN KEY(`Products_Code_ID`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_invoice_number_id_foreign` FOREIGN KEY(`Invoice_Number_ID`) REFERENCES `Invoices`(`Invoice_Number`);
ALTER TABLE
    `Carts Items` ADD CONSTRAINT `carts items_shopping_cart_id_foreign` FOREIGN KEY(`Shopping_Cart_ID`) REFERENCES `Shopping Cart`(`ID`);