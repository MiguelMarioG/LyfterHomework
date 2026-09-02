from datetime import date, datetime


class LogicProcessor:
    def __init__(self):
        self.total_list = []


    @staticmethod
    def date_validation (date_to_validate):
        date_today = date.today()

        if not date_to_validate:
            raise ValueError ("Error: The Date field cannot be empty. Please use MM-DD-YYYY!!!")
        
        try:
            date_to_validate = datetime.strptime(date_to_validate, "%m-%d-%Y").date()
        except ValueError:
            raise ValueError ("Error: Invalid date format. Please use MM-DD-YYYY!!!")
        
        if date_to_validate > date_today:
            raise ValueError ("Error: The date you entered cannot be later than the current date!!!")
        
        return date_to_validate


    @staticmethod
    def description_validation (description_to_validate):
        if not description_to_validate:
            raise ValueError ("Error: The Description field cannot be empty!!!")


    @staticmethod
    def amount_validation (amount_to_validate, transaction_type):
        if not amount_to_validate:
            raise ValueError ("Error: The Amount field cannot be empty!!!")
        
        try:
            amount_to_validate = float (amount_to_validate)
        except ValueError:
            raise ValueError ("Error: The entered value must be a decimal or an integer!!!")
        
        if transaction_type == "Deposit" and amount_to_validate <= 0:
            raise ValueError ("Error: The entered value cannot be zero or negative!!!")
        
        elif transaction_type == "Withdrawal" and amount_to_validate >= 0:
            raise ValueError ("Error: The entered value cannot be zero or positive!!!")
        
        return amount_to_validate


    @staticmethod
    def category_empty_list_validation(categories_to_validate):
        if len(categories_to_validate) <= 1:
            raise ValueError ("Error: The categories field cannot be completely empty!!!")


    @staticmethod
    def category_empty_field_validation(category_to_validate):
        if not category_to_validate:
            raise ValueError ("Error: The Field cannot be empty to add a New Category!!!")


    @staticmethod
    def category_available_validation(categories_to_validate):
        if not categories_to_validate:
            raise ValueError("Error: No categories available. You must create at least one category before recording a transaction!!!")


    @staticmethod
    def category_not_selected_validation(category_to_validate):
        if not category_to_validate:
            raise ValueError("Error: To delete a category, you must select one!!!")


    @staticmethod
    def category_already_in_data_validation(category_to_validate, categories_data):
        names = [category[0] if isinstance(category, list) else category for category in categories_data]
        if category_to_validate in names:
            raise ValueError("Error: The Categorie you trying to Add is already on file!!!")


    def total_math_calculation(self, finance_data)->list:
        self.total_list = []
        total_deposit = sum(float(row[2]) for row in finance_data if row[4] == 'Deposit')
        total_withdrawal = sum(float(row[2]) for row in finance_data if row[4] == 'Withdrawal')
        total_balance = total_withdrawal + total_deposit

        self.total_list.append(["Totales:"])
        self.total_list.append([f"Deposits: ${total_deposit:.2f}"])
        self.total_list.append([f"Withdrawals: ${total_withdrawal:.2f}"])
        self.total_list.append([f"Net Balance: ${total_balance:.2f}"])

        return self.total_list
