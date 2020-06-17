from src.cart import Cart
from src.read_input import getInputData, readFile, EmptyJsonFileException
import pytest


def test_cart_step1():
    PATH = "tests/resources/exampleGist"

    productsAvailable, bundlesAvailable = getInputData(
        f"{PATH}/products.json", f"{PATH}/bundles.json"
    )

    expectedProducts = ["ABC"]

    discount = Cart.fillCartAndComputeDiscount(
        productsAvailable, bundlesAvailable, expectedProducts
    )

    assert 0.0 == discount


def test_cart_step2():
    PATH = "tests/resources/exampleGist"

    productsAvailable, bundlesAvailable = getInputData(
        f"{PATH}/products.json", f"{PATH}/bundles.json"
    )

    expectedProducts = ["ABC", "DEF"]

    discount = Cart.fillCartAndComputeDiscount(
        productsAvailable, bundlesAvailable, expectedProducts
    )

    assert 32.70 == discount


def test_cart_step3():
    PATH = "tests/resources/exampleGist"

    productsAvailable, bundlesAvailable = getInputData(
        f"{PATH}/products.json", f"{PATH}/bundles.json"
    )

    expectedProducts = ["ABC", "XYZ", "DEF"]

    discount = Cart.fillCartAndComputeDiscount(
        productsAvailable, bundlesAvailable, expectedProducts
    )

    assert 104.5 == discount


def test_cart():
    PATH = "tests/resources/exampleGist"

    productsAvailable, bundlesAvailable = getInputData(
        f"{PATH}/products.json", f"{PATH}/bundles.json"
    )

    expectedProducts = readFile(f"{PATH}/expected.txt")

    discount = Cart.fillCartAndComputeDiscount(
        productsAvailable, bundlesAvailable, expectedProducts
    )

    assert 104.5 == discount


def test_cart_with_more_than_5_no_bundles():
    PATH = "tests/resources/moreThan5NoBundle"

    productsAvailable, bundlesAvailable = getInputData(
        f"{PATH}/products.json", f"{PATH}/bundles.json"
    )

    expectedProducts = readFile(f"{PATH}/expected.txt")

    discount = Cart.fillCartAndComputeDiscount(
        productsAvailable, bundlesAvailable, expectedProducts
    )

    assert 0.36 == discount


def test_no_products_in_cart():
    PATH = "tests/resources/noProductsInCart"

    productsAvailable, bundlesAvailable = getInputData(
        f"{PATH}/products.json", f"{PATH}/bundles.json"
    )

    expectedProducts = readFile(f"{PATH}/expected.txt")

    discount = Cart.fillCartAndComputeDiscount(
        productsAvailable, bundlesAvailable, expectedProducts
    )

    assert 0.0 == discount


def test_no_bundles():
    with pytest.raises(EmptyJsonFileException) as error:
        PATH = "tests/resources/noBundles"

        productsAvailable, bundlesAvailable = getInputData(
            f"{PATH}/products.json", f"{PATH}/bundles.json"
        )

        expectedProducts = readFile(f"{PATH}/expected.txt")

        discount = Cart.fillCartAndComputeDiscount(
            productsAvailable, bundlesAvailable, expectedProducts
        )

    assert error.type is EmptyJsonFileException


def test_no_products():
    with pytest.raises(EmptyJsonFileException) as error:
        PATH = "tests/resources/noProducts"

        productsAvailable, bundlesAvailable = getInputData(
            f"{PATH}/products.json", f"{PATH}/bundles.json"
        )

        expectedProducts = readFile(f"{PATH}/expected.txt")

        discount = Cart.fillCartAndComputeDiscount(
            productsAvailable, bundlesAvailable, expectedProducts
        )

    assert error.type is EmptyJsonFileException
