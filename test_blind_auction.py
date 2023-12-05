"""
Helping test blind_auction.py
Write test function to test two pure function in blind_auction.py.
"""

from blind_auction import get_statistics_summary, get_winner


def test_get_statistics_summary() -> int:
    """
    Test for get_statistics_summary function.
    Returns the number of tests that failed.
    """
    failed = 0
    # in the dictionary {'sara': 500, 'alice': 400, 'dave': 300}
    # - should give a summary of (500, 400).
    # 500 is the highest value, and 400 is the middle value.
    dict1 = {'sara': 500, 'alice': 400, 'dave': 300}
    if get_statistics_summary(dict1) != (500, 400):
        print("Failed get_statistics_summary test with \
              {'sara': 500, 'alice': 400, 'dave': 300})")
        failed += 1
    # in the dictionary {'a': 100, 'b': 100, 'c': 100}
    # - should give a summary of (100, 100).
    # 100 is the highest value, and 100 is also the middle value.
    if get_statistics_summary({'a': 100, 'b': 100, 'c': 100}) != (100, 100):
        print("Failed get_statistics_summary test with {'a': 100, 'b': 100,\
              'c': 100}")
        failed += 1
    # in the dictionary {'alice': 10000, 'bob': 10000, 'serena': 30000}
    # - should give a summary of (30000, 16666.666666666668).
    # 30000 is the highest value, and 16666.666666666668 is the middle value.
    dict3 = {'alice': 10000, 'bob': 10000, 'serena': 30000}
    if get_statistics_summary(dict3) != (30000, 16666.666666666668):
        print("Failed get_statistics_summary test with \
              {'alice': 10000, 'bob': 10000, 'serena': 30000}")
        failed += 1
    if failed < 1:
        # if no test failed in this test function, print pass message.
        print("All get_statistics_summary tests passed.")
    return failed


def test_get_winner() -> int:
    """
    Test for get_winner function.
    Returns the number of tests that failed.
    """
    failed = 0
    # in the dictionary {'sara': 500, 'alice': 400, 'dave': 300}
    # - should give the result ('Sara', 500).
    # 500 is the highest value, and 'Sara'is the winner.
    dict1 = {'sara': 500, 'alice': 400, 'dave': 300}
    if get_winner(dict1) != ('Sara', 500):
        print("Failed get_winner test with \
              {'sara': 500, 'alice': 400, 'dave': 300})")
        failed += 1
    # in the dictionary {('a', 100), ('b', 100)}
    # -should give the result ('A', 100).
    # 100 is the highest value, and 'A' is the winner.
    if get_winner({'a': 100, 'b': 100}) != ('A', 100):
        print("Failed get_winner test with {('a', 100), ('b', 100)}")
        failed += 1
    # in the dictionary {'alice': 10000, 'bob': 10000, 'serena': 30000}
    # - should give the result ('Serena', 30000).
    # 30000 is the highest value, and 'Serena' is the winner.
    dict3 = {'alice': 10000, 'bob': 10000, 'serena': 30000}
    if get_winner(dict3) != ('Serena', 30000):
        print("Failed get_winner test with \
              {'alice': 10000, 'bob': 10000, 'serena': 30000}")
        failed += 1
    if failed < 1:
        # if no test failed in this test function, print pass message.
        print("All get_winner tests passed.")
    return failed


def run_all_test() -> None:
    fail_count = 0
    fail_count += test_get_statistics_summary()
    fail_count += test_get_winner()
    # print the total number of the failed tests.
    print(f"Failed {fail_count} tests")


if __name__ == "__main__":
    run_all_test()
