## Building Docker Image

Follow bellow steps to create CometQE docker image.

### 1.Getting Dependencies

Run bellow commnad to save depenedcies in cache directory.

`pip wheel --no-deps --wheel-dir ./cache/ -r requirements.txt`

### 2.Downloading checkpoint

Download the `model.ckpt` file from Google-Drive and put it in the /checkpoints/ directory.

### 3.Building Docker Image

Build the docker image with below command.

`docker build -t comet-qe .`

## QE Webservice

The service runs on port 5000.
