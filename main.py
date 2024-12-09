import sys
from solves import day01
from solves import day02
from solves import day03
from solves import day04
from solves import day05
from solves import day06
from solves import day07
from solves import day08
from solves import day09

def main():
    if len(sys.argv) < 2:
        print("enter the day")
        return

    day = sys.argv[1]

    solns = {
        "1a": day01.solve1,
        "1b": day01.solve2,
        "2a": day02.solve1,
        "2b": day02.solve2,
        "3a": day03.solve1,
        "3b": day03.solve2,
        "4a": day04.solve1,
        "4b": day04.solve2,
        "5a": day05.solve1,
        "5b": day05.solve2,
        "6a": day06.solve1,
        "6b": day06.solve2,
        "7a": day07.solve1,
        "7b": day07.solve2,
        "8a": day08.solve1,
        "8b": day08.solve2,
        "9a": day09.solve1,
        "9b": day09.solve2,
    }

    if day in solns:
        print(f"day {day} solution: ", end="")
        solns[day]()
    else:
        print("invalid day")

if __name__ == "__main__":
    main()

