set -e
app="cart_bundle_discount"
docker build -t ${app} ./docker/
docker run -it --rm -w /app -v $(pwd):/app ${app} /bin/bash
