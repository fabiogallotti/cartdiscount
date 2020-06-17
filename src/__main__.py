import argparse
from src.read_input import getInputData, readFile
from src.cart import Cart


def parse_args():
    """
    Pass the input data as argument.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--products",
        help="Path of the product json file",
        default="inputs/products.json",
    )
    parser.add_argument(
        "-b",
        "--bundles",
        help="Path of the bundles json file",
        default="inputs/bundles.json",
    )
    parser.add_argument(
        "-e",
        "--expected",
        help="Path of the expected products file",
        default="inputs/expected1.txt",
    )
    args = parser.parse_args()
    return args


def main(ARGS):

    productsAvailable, bundlesAvailable = getInputData(ARGS.products, ARGS.bundles)
    expectedProducts = readFile(ARGS.expected)

    discount = Cart.fillCartAndComputeDiscount(
        productsAvailable, bundlesAvailable, expectedProducts
    )

    print(f"{discount=}")

    return discount


if __name__ == "__main__":
    ARG = parse_args()
    main(ARG)
