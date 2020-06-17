import json
from typing import NamedTuple


class Bundle(NamedTuple):
    id: int
    products: list
    discount: int


class Product(NamedTuple):
    sku: str
    price: int


class EmptyJsonFileException(Exception):
    pass


def __getProductsFromJson(file):
    jsonProducts = __jsonParser(file)
    return {
        product["sku"]: Product(product["sku"], product["price"])
        for product in jsonProducts
    }


def __getBundlesFromJson(file):
    jsonBundles = __jsonParser(file)
    return [
        Bundle(bundle["id"], bundle["products"], bundle["discount"])
        for bundle in jsonBundles
    ]


def __jsonParser(file):
    try:
        with open(file) as jsonFile:
            return json.load(jsonFile)
    except Exception:
        raise EmptyJsonFileException("Empty json file not expected.")


def readFile(file):
    with open(file) as f:
        return f.read().split(",")


def getInputData(productPath, bundlesPath):
    productsAvailable = __getProductsFromJson(productPath)
    bundlesAvailable = __getBundlesFromJson(bundlesPath)
    return productsAvailable, bundlesAvailable
