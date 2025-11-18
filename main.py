import sys
from classes.Zen import Zen
from time import sleep
import argparse

if __name__ == "__main__":

    argv = sys.argv[1:]
    parser = argparse.ArgumentParser(description="PROBot")

    parser.add_argument(
        "--item",
        required=False,
        help="A list of items that you want to pick up comma separated. e.g.: --item=Jewel,Box"
    )

    parser.add_argument(
        "--zen",
        default=True,
        help="If true, it will pick up the zen around you.",
        type=lambda x: (str(x).lower() != 'false')
    )

    args = parser.parse_args(argv)

    #print("Bot will start in 5s...")
    #sleep(5)

    print("Starting...")
    z = Zen()
    z.start()
