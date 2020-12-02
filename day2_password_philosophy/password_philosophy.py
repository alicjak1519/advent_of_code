from typing import List


class PasswordPhilosophy:
    def __init__(self, path: str) -> None:
        self.input = self._read_input(path)

    def _read_input(self, path: str) -> List[str]:
        with open(path) as file:
            return [line.replace('\n', '') for line in file.readlines()]

    def _parse_expression(self, expression: str) -> dict:
        elements = expression.split(' ')
        return {
            'min': int(elements[0].split('-')[0]),
            'max': int(elements[0].split('-')[1]),
            'letter': elements[1].replace(':', ''),
            'password': elements[2]
        }

    def _is_password_valid(self, structure: dict) -> bool:
        return structure['min'] <= structure['password'].count(structure['letter']) <= structure['max']

    def _is_password_still_valid(self, structure: dict) -> bool:
        return (structure['password'][structure['min'] - 1] == structure['letter']) ^ (
                    structure['password'][structure['max'] - 1] == structure['letter'])

    def count_valid_passwords(self) -> int:
        return sum([self._is_password_valid(self._parse_expression(expression)) for expression in self.input])

    def count_still_valid_passwords(self) -> int:
        return sum([self._is_password_still_valid(self._parse_expression(expression)) for expression in self.input])


if __name__ == "__main__":
    password_philosophy = PasswordPhilosophy("../inputs/day2_input.csv")
    number_of_valid_passwords = password_philosophy.count_valid_passwords()
    number_of_still_valid_passwords = password_philosophy.count_still_valid_passwords()
    print(f"Number of valid passwords: {number_of_valid_passwords}")
    print(f"Number of still valid passwords: {number_of_still_valid_passwords}")
