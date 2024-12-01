import os
import sys

import requests
from dotenv import load_dotenv


def get_input_file(day: int):
    """
    Gets the input from AoC page.
    """
    load_dotenv()
    url = f"https://adventofcode.com/2024/day/{day}/input"

    session = requests.Session()
    session_cookie = os.getenv('AOC_SESSION')

    session.cookies.set('session', session_cookie)

    try:
        response = session.get(url)
        response.raise_for_status()
        return response.text

    except Exception as e:
        raise Exception(f"Error downloading input from {url}: {e}")


def start_day(day: int):
    """
    Creates the necessary files for another AoC day.
    """
    template_file = "template.txt"

    if 0 > day > 24:
        raise ValueError("There is no such day in the advent calendar, dummy! :)\n"
                         "Perhaps you forgot indexing should start at 0? (written by MATLAB haters gang)")

    if not os.path.exists(template_file):
        raise FileNotFoundError(f"Oops! Looks like you removed the template file. How silly!")

    try:
        with open(template_file, 'r') as file:
            content = file.readlines()

        folder_name = f"day_{day}"
        os.makedirs(folder_name, exist_ok=True)
        input_file, solution_file = os.path.join(folder_name, "input.txt"), os.path.join(folder_name, f"day_{day}.py")

        with open(input_file, "w") as file:
            file.write(get_input(day + 1))

        with open(solution_file, 'w') as file:
            file.writelines([line.format(day=day) for line in content])

        print(f"Go add your solution to: {solution_file}")

    except Exception as e:
        print(f"Weren't you supposed to be an engineer or something? : {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python start_day.py <day>")
        sys.exit(1)

    input_day = int(sys.argv[1])

    start_day(input_day)
