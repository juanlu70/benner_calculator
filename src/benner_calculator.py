import argparse
import time


class BennerCalculator:
    def __init__(self):
        self.initial_year = 1924
        self.long_term_cycle = 56
        self.input_year = None

        self.cycle_a = {
            'initial_year': self.initial_year + 3,
            'years_distance': [18, 20, 16],
            'years': [self.initial_year + 3],
            'explanation': "\"A\" Years which panics have ocurred and it "
                           "will occur again."
        }
        self.cycle_b = {
            'initial_year': self.initial_year + 2,
            'years_distance': [9, 10, 8],
            'years': [self.initial_year + 2],
            'explanation': "\"B\" Years of good times, high prices and the "
                           "time to sell stocks and values of all kinds"
        }
        self.cycle_c = {
            'initial_year': self.initial_year,
            'years_distance': [7, 11, 9],
            'years': [self.initial_year],
            'explanation': "\"C\" years of hard times, low prices and good "
                           "time to buy stocks, goods and hold it till the "
                           "\"Boom\" reaches the years of good times; "
                           "then unload"
        }

    def make_long_term_cycles(self) -> None:
        self.cycle_a['years'] = self.cycle_discovery_loop(self.cycle_a)
        self.cycle_b['years'] = self.cycle_discovery_loop(self.cycle_b)
        self.cycle_c['years'] = self.cycle_discovery_loop(self.cycle_c)

        self.show_cycles()

        return

    def cycle_discovery_loop(self, year_data: dict) -> list:
        cycle_year = year_data['initial_year']
        end_year = self.input_year + self.long_term_cycle

        while cycle_year < end_year:
            for cycle in year_data['years_distance']:
                cycle_year += cycle
                year_data['years'].append(cycle_year)

        return year_data['years']

    def show_cycles(self):
        print("\n" + self.cycle_a['explanation'])
        print(self.cycle_a['years'])
        print("\n" + self.cycle_b['explanation'])
        print(self.cycle_b['years'])
        print("\n" + self.cycle_c['explanation'])
        print(self.cycle_c['years'])
        print("\n")

        return


if __name__ == "__main__":
    bc = BennerCalculator()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        default=time.strftime("%Y", time.localtime()),
        help="Reference year for cvycles, it will appear in the center."
    )
    args = parser.parse_args()
    bc.input_year = args.year

    bc.make_long_term_cycles()
