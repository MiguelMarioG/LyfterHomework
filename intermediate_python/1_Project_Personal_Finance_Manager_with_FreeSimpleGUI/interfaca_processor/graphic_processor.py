import FreeSimpleGUI as sg
from datetime import date, datetime


class GraphicInterface:
    def __init__(self, Processor, Logic):
        self.processor = Processor
        self.logic = Logic
        self.categories_data = self.processor.categories_load_data_csv()
        self.finance_data = self.processor.finance_load_data_csv()
        self.heading = ["Date", "Description", "Amount", "Categories", "Type"]


    @property
    def today_date (self):
        return date.today().strftime("%m-%d-%Y")


    @property
    def _get_category_names(self):
        return [category[0] for category in self.categories_data ]


    def _get_category_color(self, category_name):
        for category in self.categories_data:
            if category[0] == category_name:
                return category[1]
        return None


    def _built_row_colors(self, dataset):
        row_colors = []
        for main_index, value in enumerate(dataset):
            for row in self.categories_data:
                if value[3]== row[0]:
                    cat_name = row[0]
                    color = self._get_category_color(cat_name)
                    if color:
                        row_colors.append((main_index, color))
        return row_colors


    def _get_filtered_finance_data (self, transaction_type):
        if transaction_type == None:
            return self.finance_data
        return [row for row in self.finance_data if row[4] == transaction_type]


    def finance_main_window (self):
        layout = [
            [
                sg.Table(
                    values=self.finance_data, 
                    headings=self.heading, 
                    key='-MAIN-TABLE-', 
                    auto_size_columns=True, 
                    display_row_numbers=True,
                    starting_row_number= 1,
                    justification="left",
                    row_colors= self._built_row_colors(self.finance_data)
                    )
            ],
            [sg.HSep(color="gray")],
            [
            sg.Text("Menu to filter by date:"),
            sg.Button('Filter by Dates'),
            sg.Button('Reset Filter'),
            ],
            [
                sg.Text("Start Date: "),
                sg.Input(key="-S-DATE-", size=(15,10)),
                sg.CalendarButton("Open Calendar", target="-S-DATE-", format= "%m-%d-%Y", close_when_date_chosen=True ),
                sg.Text("End Date: "),
                sg.Input(default_text=self.today_date, key="-E-DATE-", size=(15,1)),
                sg.CalendarButton("Open Calendar", target="-E-DATE-", format= "%m-%d-%Y", close_when_date_chosen=True ),
            ],
            [sg.HSep(color="gray")],
            [
                sg.Button('Add Categories'), 
                sg.Button('Add Deposit'), 
                sg.Button('Add Withdrawal'),
                sg.Button('Export CSV File'),
                sg.Button('Exit'),
            ],
        ]

        window = sg.Window('Personal Finance Manager', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Exit':
                break

            if event == 'Filter by Dates':
                start_date = values["-S-DATE-"].strip()
                end_date = values["-E-DATE-"].strip()
                try:
                    start_date= self.logic.date_validation(start_date)
                    end_date= self.logic.date_validation(end_date)
                except ValueError as error:
                    sg.popup_error(str(error), title="System Error")
                    continue
                filtered_rows = []
                for row in self.finance_data:
                    date_to_verify = datetime.strptime(row[0], "%m-%d-%Y").date()
                    if start_date <= date_to_verify <= end_date:
                        filtered_rows.append(row[:3])
                window['-MAIN-TABLE-'].update(values=filtered_rows)
                window['-MAIN-TABLE-'].Widget['displaycolumns'] = (0,1,2,3)

            if event == 'Reset Filter':
                window["-S-DATE-"].update("")
                window["-E-DATE-"].update(self.today_date)
                window['-MAIN-TABLE-'].update(values=self.finance_data, row_colors=self._built_row_colors(self.finance_data))
                window["-MAIN-TABLE-"].Widget['displaycolumns'] = ("#all")

            if event == 'Add Categories':
                self.add_or_remove_category_new_window()
                window['-MAIN-TABLE-'].update(values=self.finance_data, row_colors=self._built_row_colors(self.finance_data))

            if event in ('Add Deposit', 'Add Withdrawal'):
                try:
                    self.logic.category_available_validation(self.categories_data)
                except ValueError as error:
                    sg.popup_error(str(error), title= "System Error")
                    continue        
                transaction_type = "Deposit" if event == "Add Deposit" else "Withdrawal"
                self.add_or_remove_transaction_type_finance_new_window(transaction_type)
                window['-MAIN-TABLE-'].update(values=self.finance_data, row_colors=self._built_row_colors(self.finance_data))

            if event == 'Export CSV File':
                total_finance = self.logic.total_math_calculation(self.finance_data)
                if self.processor.finance_export_data_csv(self.finance_data, total_finance):
                    sg.popup ("Your information was successfully exported", title="System Success")

        window.close()


    def add_or_remove_transaction_type_finance_new_window(self, transaction_type):
        filtered_data = self._get_filtered_finance_data(transaction_type)
        layout_deposit_finance = [
            [sg.Text("Finance Data on File:")],
            [
                sg.Table(
                values=filtered_data, 
                headings=self.heading, 
                key="-TRANSACTION-TABLE-", 
                auto_size_columns=True, 
                display_row_numbers=True,
                starting_row_number= 1,
                enable_events=True,
                justification= "left",
                select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                row_colors=self._built_row_colors(filtered_data)
                )
            ],
            [sg.HSep(color="gray")],
            [sg.Text(f"Introduce the Information of your {transaction_type}: ")],
            [
            sg.Text("Date"), sg.Input(default_text= self.today_date,  key="-DATE-", size=(15,1)), 
            sg.CalendarButton('Open Calender', target='-DATE-', format="%m-%d-%Y", close_when_date_chosen=True),
            sg.Text("Default Type"),
            sg.Input(
                transaction_type, 
                key="-TYPE-", 
                readonly=True, 
                disabled_readonly_background_color="lightgray",
                disabled_readonly_text_color="black",
                size=(10,1),
                font=("Any", 11, "bold"),
                justification="center"
                ),
            ],
            [sg.Text("Description"), sg.Input(key="-DESCRIPTION-", size=(60,1))],
            [
            sg.Text("Categories"),
            sg.Combo(
                values=self._get_category_names, 
                default_value=self._get_category_names[0],
                key="-CATEGORY-COMBO-", 
                readonly=True, 
                size=(35,1)
                ),
            sg.Text("Amount"), 
            sg.Input(key="-AMOUNT-", size= (13,1)),
            ],
            [sg.Button(f"Add New {transaction_type}"), sg.Button(f"Remove {transaction_type}"), sg.Button("Exit")],
        ]

        window = sg.Window ( 
            f"{transaction_type} Finance Window", 
            layout_deposit_finance, 
            modal=True,
            finalize=True,
            )
        
        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            if event == f"Add New {transaction_type}":
                date_raw = values ["-DATE-"].strip()  
                try:
                    self.logic.date_validation (date_raw)
                except ValueError as error:
                    sg.popup_error(str(error), title= "System Error")
                    continue
                description_raw = values ["-DESCRIPTION-"].strip()
                try:
                    self.logic.description_validation (description_raw)
                except ValueError as error:
                    sg.popup_error(str(error), title= "System Error")
                    continue
                amount_raw = values ["-AMOUNT-"].strip()
                amount_raw = amount_raw.replace (",", ".")
                try:
                    amount_raw = self.logic.amount_validation (amount_raw, transaction_type)
                except ValueError as error:
                    sg.popup_error(str(error), title= "System Error")
                    continue
                category_raw = values ["-CATEGORY-COMBO-"].strip()
                type_raw = values ["-TYPE-"].strip()
                new_data = [date_raw, description_raw, amount_raw, category_raw, type_raw]
                self.finance_data.append(new_data)
                self.processor.finance_save_data_csv(self.finance_data)
                updated_filtered_data = self._get_filtered_finance_data(transaction_type)
                window ["-TRANSACTION-TABLE-"].update(values= updated_filtered_data, row_colors=self._built_row_colors(updated_filtered_data))
                [window[empty].update("") for empty in ("-DESCRIPTION-", "-AMOUNT-")]

            if event == f"Remove {transaction_type}":
                selected_row = values ["-TRANSACTION-TABLE-"]
                if selected_row:
                    selected_index = selected_row[0]
                    current_data = self._get_filtered_finance_data(transaction_type)
                    data_to_remove = current_data[selected_index]
                    if data_to_remove in self.finance_data:
                        self.finance_data.remove(data_to_remove)
                        self.processor.finance_save_data_csv(self.finance_data)
                        updated_filtered_data = self._get_filtered_finance_data(transaction_type)
                        window ["-TRANSACTION-TABLE-"].update(values= updated_filtered_data, row_colors=self._built_row_colors(updated_filtered_data))

        window.close()


    def add_or_remove_category_new_window (self):
        layout_categories = [
            [sg.Text('Categories on File:')],
            [
                sg.Listbox(
                    values = self._get_category_names,
                    size=(42, 10),
                    key="-CAT-LIST-",
                    enable_events=True,
                    )
            ],
            [sg.HSep(color="gray")],
            [
                sg.Text("Name of the Category", size=(16,1)), 
                sg.Input(key='-CATEGORY-', size=(24,1)),
            ],
            [
                sg.Input(key="-COLOR-PICKED-", visible=False, enable_events=True),
                sg.ColorChooserButton("Add Color to Category", target="-COLOR-PICKED-"),
            ],
            [sg.HSep(color="gray")],
            [sg.Button("Add New Category"),sg.Button("Remove Category"), sg.Button("Exit")],
        ]

        window = sg.Window ( 
            "Add New Category Window", 
            layout_categories, 
            modal=True,
            finalize=True,
            )
        
        window ['-CATEGORY-'].bind("<Return>", "-ENTER-")

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            if event == 'Remove Category':
                selected_category = values["-CAT-LIST-"]
                if selected_category:
                    try:
                        self.logic.category_empty_list_validation(self.categories_data)
                    except ValueError as error:
                        sg.popup_error(str(error), title= "System Error")
                        continue
                    category_to_remove = selected_category[0]
                    self.categories_data = [c for c in self.categories_data if c[0] != category_to_remove]
                    self.processor.categories_save_data_csv(self.categories_data)
                    window["-CAT-LIST-"].update(values=self._get_category_names)
                    window["-CATEGORY-"].update(value="")
                else:
                    try:
                        self.logic.category_not_selected_validation(selected_category)
                    except ValueError as error:
                        sg.popup_error(str(error), title="System Error")
                        continue
                    
            if event in ('Add New Category', '-CATEGORY-' + "-ENTER-"):
                new_category = values['-CATEGORY-'].strip()
                chosen_color = values["-COLOR-PICKED-"] if values["-COLOR-PICKED-"] else "#000000"
                category_names = self._get_category_names
                if new_category and new_category not in category_names:
                    self.categories_data.append([new_category, chosen_color])
                    self.processor.categories_save_data_csv(self.categories_data)
                    window["-CAT-LIST-"].update(values=self._get_category_names)
                    window["-CATEGORY-"].update(value="")
                else:
                    try:
                        self.logic.category_empty_field_validation(new_category)
                        try:
                            self.logic.category_already_in_data_validation(new_category, self.categories_data)
                        except ValueError as error:
                            sg.popup_error(str(error), title="System Error")
                            window["-CATEGORY-"].update(value="")
                    except ValueError as error:
                        sg.popup_error(str(error), title= "System Error")
                        continue
        window.close()