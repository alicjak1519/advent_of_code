import pandas as pd


class ReportRepair:
    def __init__(self, path: str) -> None:
        self.input = self._read_input(path)

    def _read_input(self, path):
        return pd.read_csv(path, header=None)

    def find_2020_elements(self):
        for element in self.input[0]:
            if (2020 - element) in self.input.values:
                return element
        raise

    def find_product_result(self):
        element = self.find_2020_elements()
        return element * (2020 - element)
