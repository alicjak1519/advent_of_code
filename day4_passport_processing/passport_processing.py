from functools import reduce
from typing import List


class PassportProccessing:
    def __init__(self, path: str) -> None:
        self.input = self._read_input(path)

    def _read_input(self, path: str) -> List[str]:
        with open(path) as file:
            raw_input = [line for line in file.readlines()]
            input = []
            tmp_row = ''
            for line in raw_input:
                if line == '\n':
                    input.append(tmp_row)
                    tmp_row = ''
                else:
                    tmp_row += line.replace('\n', ' ')
            input.append(tmp_row)
        return input

    def _parse_row(self, row: str) -> dict:
        passport = {}
        if row.split()[-1] == ' ':
            attributes_list = row.split()[:-1]
        else:
            attributes_list = row.split()

        for expression in attributes_list:
            key = expression.split(':')[0]
            value = expression.split(':')[1]
            passport[key] = value
        return passport

    def _is_all_attributes_in(self, passport: dict) -> bool:
        return all(elem in passport.keys() for elem in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    def _is_data_valid(self, passport: dict) -> bool:
        is_byr_valid = 1920 <= int(passport['byr']) <= 2002
        is_iyr_valid = 2010 <= int(passport['iyr']) <= 2020
        is_eyr_valid = 2020 <= int(passport['eyr']) <= 2030
        is_hgt_valid = self._is_hgt_valid(passport['hgt'])
        is_hcl_valid = self._is_hcl_valid(passport['hcl'])
        is_ecl_valid = passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        is_pid_valid = self._is_pid_valid(passport['pid'])

        return is_byr_valid and is_iyr_valid and is_eyr_valid and is_hgt_valid and is_hcl_valid and is_ecl_valid and is_pid_valid

    def _is_hgt_valid(self, hgt: str) -> bool:
        if hgt[-2:] == 'cm':
            return 150 <= int(hgt[:-2]) <= 193
        elif hgt[-2:] == 'in':
            return 59 <= int(hgt[:-2]) <= 76
        else:
            return False

    def _is_hcl_valid(self, hcl: str) -> bool:
        if hcl[0] == '#' and len(hcl) == 7:
            return not set(hcl[1:]).difference(set('0123456789abcdef'))
        else:
            return False

    def _is_pid_valid(self, pid: str) -> bool:
        print(pid)
        return len(pid) == 9 and pid[-1] != '0' and not set(pid).difference(set('0123456789'))

    def _is_passport_valid(self, passport: dict) -> bool:
        if self._is_all_attributes_in(passport):
            return self._is_data_valid(passport)
        else:
            return False

    def calc_passports_with_all_attributes(self):
        return reduce(lambda x, y: x + y, [self._is_all_attributes_in(self._parse_row(row)) for row in self.input])

    def calc_valid_passports(self):
        return reduce(lambda x, y: x + y, [self._is_passport_valid(self._parse_row(row)) for row in self.input])


if __name__ == "__main__":
    passport_processing = PassportProccessing("../inputs/day4_input.csv")
    print(passport_processing.calc_passports_with_all_attributes())
    print(passport_processing.calc_valid_passports())
