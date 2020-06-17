# Cart-Bundle-Discount

Solution implemented using the python programming language in a docker container.

Specifically I used python3.8, starting from the [base image](https://hub.docker.com/layers/python/library/python/3.8/images/sha256-b8c37d821abb6d1bb4110bbad9368ae2da3b100a57ef14ed25ce5c1f6b79a2c9?context=explore), on top of which I installed [pytest](https://pypi.org/project/pytest/) to run the tests.

I then published the image on [dockerhub](https://hub.docker.com/repository/docker/fabiogallotti/pytest), in order to have a consistent Continuous Integration.

The image is pulled by the CircleCI pipeline, and the tests are runned automatically per each commit.

## How to run the code

### Enter the container

I created a simple script to build and run the docker image.

`sh docker/run.sh`

This way you can easily access the container and run the code and the tests inside it, without polluting your local env.
I'm also improving the portability and the reusability of my code.

### Execute the code

You can run the tool with the following command:

`python -m src -p <productsPath> -b <bundlesPath> -e <expectedInCartPath>`

You will get as an output a print of the discount.

The default values for the arguments are:

* productsPath = `inputs/products.json`
* bundlesPath = `inputs/bundles.json`
* expectedInCartPath = `inputs/expected1.txt`

Examples:

1) * `python -m src -p inputs/products.json -b inputs/bundles.json -e inputs/expected1.txt`
   * `discount=12.21`

2) * `python -m src -e inputs/expected2.txt`
   * `discount=83.18`

## How to run the test cases

The test case are runned automatically at each commit thanks to the CircleCI pipeline.

To run locally the test we can use pytest: `python -m pytest`

## Shortcuts

* I store the Products in a dict, where the key is the sku and the value is the NamedTuple Product. This way I can search faster for the price of a product in the cart (method Cart.__calculateDiscount()); the Bundles are stored instead in a list of the NamedTuple Bundle.
* I defined the two NamedTuple in the read_input file for sake of semplicity. They could have been in a dedicated file.
* I add the available products and the available discount as private variables of the cart. Functionally it isn't the cleanest solution but it helped me for the computations.
* In the tests I'm taking as assumption that the products are passed through a `products.json` file, the bundles through a `bundles.json` file and the expected products in cart through an `expected.txt` one, or manually passed via a list.
* Complexity is the length of the cart times the length of the bundles.

## Improvements

* I created some basic test only for the calculation of the discount. In a real project there should be unit tests for all the function, plus some static analysis and coverage analysis of the code, that can be integrated in the CI pipeline (CodeClimate, CodeCov).
* Use type hints and mypy to make the code more robust.
