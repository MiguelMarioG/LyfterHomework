import csv
import os

class DataProcessor:

    def __init__(self):
        self.category_path = "Categories.csv"
        self.finance_data_path = "Finance_Data.csv"
        self.export_data_path = "Finance_Report.csv"
        self.finance_headers = [
            "Date",
            "Description",
            "Amount",
            "Categories",
            "Type",
        ]
        self.categories_csv = [
            ["Expenses", "#FF5733"],
            ["Main Entrance", "#2ECC71"],
            ["Grocery", "#FFA500"],
            ["Basic Service", "#3498DB"],
        ]


    def categories_load_data_csv(self):
        if os.path.exists(self.category_path):

            with open (self.category_path, mode= "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                loaded_categories = []

                for row in reader:
                    if row:
                        cat_name = row[0]
                        color_name = row[1] if len(row) >1 else "#000000"
                        loaded_categories.append([cat_name, color_name])

                if loaded_categories:
                    self.categories_csv = loaded_categories

        return self.categories_csv


    def categories_save_data_csv(self, categories_to_save):
        with open (self.category_path, mode= "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            for cat in categories_to_save:
                if isinstance(cat, list):
                    writer.writerow(cat)
                else:
                    writer.writerow([cat, "#000000"])


    def finance_load_data_csv(self):
        if os.path.exists(self.finance_data_path):

            with open (self.finance_data_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                finance_csv = []

                next(reader, None)

                for row in reader:
                    if row:
                        finance_csv.append(row)

        return finance_csv


    def finance_save_data_csv(self, finance_data_to_save):
        with open (self.finance_data_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(self.finance_headers)
            writer.writerows(finance_data_to_save)


    def finance_export_data_csv(self, finance_data_to_save, total_finance):
        with open (self.export_data_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer. writerow(self.finance_headers)
            writer.writerows(finance_data_to_save)
            writer.writerow([])
            writer.writerows(total_finance)
            return True