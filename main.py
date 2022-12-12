import time
from utils.Utils import Utils
import lib.day_10 as day

DAY = "10"
EXPECTED_TEST = None
FUNC = day.draw_screen


def main():
    inputs = Utils.file_to_lines(f"input_{DAY}.txt")
    inputs_test = Utils.file_to_lines(f"test/test_{DAY}.txt")
    output = None

    output_test = FUNC(inputs_test)
    if output_test == EXPECTED_TEST:
        print('\n >>> The test passed successfully')
        output = FUNC(inputs)

    print(f"\n TEST: Expected: {EXPECTED_TEST}, Output: {output_test}")
    print(f"\n Answer: {output}")
    print(f'\n Time: {time.process_time()}')


if __name__ == "__main__":
    main()
