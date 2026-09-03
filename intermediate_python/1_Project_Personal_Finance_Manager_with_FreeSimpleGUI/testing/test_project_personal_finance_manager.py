import pytest
from unittest.mock import patch, mock_open
from datetime import date, timedelta

# Import classes according to project structure
from logic_processor.data_logic import LogicProcessor
from data_processor.data_processor_csv import DataProcessor


def test_date_validation_valid():
    #1. Validates that a valid date in MM-DD-YYYY format is processed correctly.
    today_str = date.today().strftime("%m-%d-%Y")
    validated = LogicProcessor.date_validation(today_str)
    assert validated == date.today()


def test_date_validation_empty_raises_error():
    #2. Validates that an empty date raises a ValueError.
    with pytest.raises(ValueError, match="The Date field cannot be empty"):
        LogicProcessor.date_validation("")


def test_date_validation_future_date_raises_error():
    #3. Validates that a future date raises a ValueError.
    future_date = (date.today() + timedelta(days=5)).strftime("%m-%d-%Y")
    with pytest.raises(ValueError, match="cannot be later than the current date"):
        LogicProcessor.date_validation(future_date)


def test_description_validation_empty_raises_error():
    #4. Validates that an empty description raises a ValueError.
    with pytest.raises(ValueError, match="Description field cannot be empty"):
        LogicProcessor.description_validation("")


def test_amount_validation_deposit_positive():
    #5. Validates that a positive deposit is accepted and returns float.
    amount = LogicProcessor.amount_validation("150.50", "Deposit")
    assert amount == 150.50


def test_amount_validation_withdrawal_negative():
    #6. Validates that a negative withdrawal is accepted and returns float.
    amount = LogicProcessor.amount_validation("-50.25", "Withdrawal")
    assert amount == -50.25


def test_amount_validation_invalid_type_raises_error():
    #7. Validates that a non-numeric amount raises a ValueError.
    with pytest.raises(ValueError, match="must be a decimal or an integer"):
        LogicProcessor.amount_validation("abc", "Deposit")


def test_total_math_calculation():
    #8. Validates the correct calculation of deposits, withdrawals, and net balance.
    logic = LogicProcessor()
    sample_data = [
        ["09-01-2026", "Payroll", "1000.00", "Main Entrance", "Deposit"],
        ["09-02-2026", "Supermarket", "-200.00", "Grocery", "Withdrawal"],
        ["09-02-2026", "Electricity", "-50.00", "Basic Service", "Withdrawal"]
    ]
    
    result = logic.total_math_calculation(sample_data)
    
    assert result[1] == ["Deposits: $1000.00"]
    assert result[2] == ["Withdrawals: $-250.00"]
    assert result[3] == ["Net Balance: $750.00"]


def test_category_empty_list_validation_raises_error():
    #9. Validates that attempting to remove a category when 1 or fewer remain raises an error.
    categories = [["Expenses", "#FF5733"]]
    with pytest.raises(ValueError, match="categories field cannot be completely empty"):
        LogicProcessor.category_empty_list_validation(categories)


def test_category_empty_field_validation_raises_error():
    #10. Validates that adding an empty category raises a ValueError.
    with pytest.raises(ValueError, match="Field cannot be empty to add a New Category"):
        LogicProcessor.category_empty_field_validation("")


def test_category_available_validation_raises_error():
    #11. Validates that attempting to record a transaction without available categories raises a ValueError.
    with pytest.raises(ValueError, match="No categories available"):
        LogicProcessor.category_available_validation([])


def test_category_not_selected_validation_raises_error():
    #12. Validates that attempting to delete without selecting a category raises a ValueError.
    with pytest.raises(ValueError, match="To delete a category, you must select one"):
        LogicProcessor.category_not_selected_validation(None)


def test_category_already_in_data_validation_raises_error():
    #13. Validates that adding an existing category in the list raises a ValueError.
    categories_data = [["Expenses", "#FF5733"], ["Grocery", "#FFA500"]]
    with pytest.raises(ValueError, match="Categorie you trying to Add is already on file"):
        LogicProcessor.category_already_in_data_validation("Expenses", categories_data)


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="Expenses,#FF5733\nGrocery,#FFA500\n")
def test_categories_load_data_csv_mock(mock_file, mock_exists):
    #14. MOCK: Simulates reading the category CSV file without accessing disk.
    processor = DataProcessor()
    categories = processor.categories_load_data_csv()
    
    assert len(categories) == 2
    assert categories[0] == ["Expenses", "#FF5733"]
    assert categories[1] == ["Grocery", "#FFA500"]
    mock_file.assert_called_once_with("Categories.csv", mode="r", newline="", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open)
def test_categories_save_data_csv_mock(mock_file):
    #15. MOCK: Simulates writing data to Categories.csv.
    processor = DataProcessor()
    data_to_save = [["Salary", "#00FF00"], ["Bills", "#FF0000"]]
    
    processor.categories_save_data_csv(data_to_save)
    
    mock_file.assert_called_once_with("Categories.csv", mode="w", newline="", encoding="utf-8")
    handle = mock_file()
    assert handle.write.called


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="Date,Description,Amount,Categories,Type\n09-01-2026,Paycheck,500.00,Main Entrance,Deposit\n")
def test_finance_load_data_csv_mock(mock_file, mock_exists):
    #16. MOCK: Simulates loading financial data while skipping the header.
    processor = DataProcessor()
    finance_data = processor.finance_load_data_csv()
    
    assert len(finance_data) == 1
    assert finance_data[0] == ["09-01-2026", "Paycheck", "500.00", "Main Entrance", "Deposit"]


@patch("builtins.open", new_callable=mock_open)
def test_finance_export_data_csv_mock(mock_file):
    #17. MOCK: Simulates exporting the final CSV report.
    processor = DataProcessor()
    finance_data = [["09-01-2026", "Paycheck", "500.00", "Main Entrance", "Deposit"]]
    total_finance = [["Totales:"], ["Deposits: $500.00"], ["Withdrawals: $0.00"], ["Net Balance: $500.00"]]
    
    success = processor.finance_export_data_csv(finance_data, total_finance)
    
    assert success is True
    mock_file.assert_called_once_with("Finance_Report.csv", mode="w", newline="", encoding="utf-8")