from interface_processor.graphic_processor import (
    GraphicInterface
)

from data_processor.data_processor_csv import(
    DataProcessor
)

from logic_processor.data_logic import (
    LogicProcessor
)


def main():
    processor = DataProcessor()
    logic = LogicProcessor()
    system = GraphicInterface(processor, logic)
    system.finance_main_window()

if __name__=="__main__":
    main()