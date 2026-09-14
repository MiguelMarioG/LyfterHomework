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
    `Users_ID` INT NOT NULL,
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
    `Users_ID` VARCHAR(255) NOT NULL
);
CREATE TABLE `Carts Items`(
    `ID` INT NOT NULL,
    `Shopping_Cart_ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Products_Code_ID` INT NOT NULL,
    `Quantity` SMALLINT NOT NULL
);
CREATE TABLE `Users`(
    `User_ID` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Full_Name` VARCHAR(255) NOT NULL,
    `Buyer_Email` VARCHAR(255) NOT NULL,
    `Registration_Date` DATE NOT NULL
);
ALTER TABLE
    `Users` ADD UNIQUE `users_buyer_email_unique`(`Buyer_Email`);
CREATE TABLE `Reviews`(
    `Review_ID` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Products_Code_ID` INT NOT NULL,
    `Comment` VARCHAR(255) NOT NULL,
    `Rating_(1 a 5)` TINYINT NOT NULL,
    `Date` DATE NOT NULL,
    `Users_ID` INT NOT NULL
);
CREATE TABLE `Payment Methods`(
    `Method_ID` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Method_Type` VARCHAR(255) NOT NULL,
    `Bank_name` VARCHAR(255) NULL
);
CREATE TABLE `Invoice Payment`(
    `Payment_ID` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Invoice_Number_ID` INT NOT NULL,
    `Payment_Method_ID` INT NOT NULL,
    `Amount_Paid` SMALLINT NOT NULL
);
ALTER TABLE
    `Carts Items` ADD CONSTRAINT `carts items_products_code_id_foreign` FOREIGN KEY(`Products_Code_ID`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_users_id_foreign` FOREIGN KEY(`Users_ID`) REFERENCES `Users`(`User_ID`);
ALTER TABLE
    `Invoice Payment` ADD CONSTRAINT `invoice payment_payment_method_id_foreign` FOREIGN KEY(`Payment_Method_ID`) REFERENCES `Payment Methods`(`Method_ID`);
ALTER TABLE
    `Reviews` ADD CONSTRAINT `reviews_products_code_id_foreign` FOREIGN KEY(`Products_Code_ID`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_products_code_id_foreign` FOREIGN KEY(`Products_Code_ID`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_invoice_number_id_foreign` FOREIGN KEY(`Invoice_Number_ID`) REFERENCES `Invoices`(`Invoice_Number`);
ALTER TABLE
    `Invoice Payment` ADD CONSTRAINT `invoice payment_invoice_number_id_foreign` FOREIGN KEY(`Invoice_Number_ID`) REFERENCES `Invoices`(`Invoice_Number`);
ALTER TABLE
    `Reviews` ADD CONSTRAINT `reviews_users_id_foreign` FOREIGN KEY(`Users_ID`) REFERENCES `Users`(`User_ID`);
ALTER TABLE
    `Carts Items` ADD CONSTRAINT `carts items_shopping_cart_id_foreign` FOREIGN KEY(`Shopping_Cart_ID`) REFERENCES `Shopping Cart`(`ID`);
ALTER TABLE
    `Shopping Cart` ADD CONSTRAINT `shopping cart_users_id_foreign` FOREIGN KEY(`Users_ID`) REFERENCES `Users`(`User_ID`);