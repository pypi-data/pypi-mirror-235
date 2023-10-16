# python-tbi-runner

Python TBI execution environment.

## Development

### Preparations

```shell
# Win
py -3.9 -m venv ./.venv
# *nix
python -m venv ./.venv
# Win
.\.venv\Scripts\activate
# *nix
source ./.venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For developing depending project/module, dependency can be added into **requirements.txt** as:

    python-commons @ file:///C:/sources/setmy.info/submodules/python-commons

### PyCharm

"File" -> "Settings" -> Python Integrated Tools -> Default test runner: Unittest

Running tests have a problem: working directory has to be set for tests.

### Run unit tests

```shell
python -m unittest discover -s ./test
```

### Run integration tests

```shell
python -m unittest discover -s ./test -p it_*.py
```

### All tests

```shell
python -m unittest discover -s ./test && python -m unittest discover -s ./test -p it_*.py
```

### Update version info

```shell
# Win
set NAME=smi_python_tbi_runner
set VERSION=1.0.0
# *nix
NAME=smi_python_tbi_runner
VERSION=1.0.0
# Win
python -m smi_python_commons.scm_version %NAME% %VERSION%
# *nix
python -m smi_python_commons.scm_version ${NAME} ${VERSION}
git add ./${NAME}/project.py
git commit -m "project.py updated"
git push
```

## Deploy

```shell
python setup.py sdist bdist_wheel
twine upload dist/*
git tag -a ${VERSION} -m "${VERSION}"
git push --tags
```

## Release

1. Update version info
2. Deploy

```shell
python setup.py sdist bdist_wheel && twine upload dist/*
```

## Usage

## TODO

```shell
export RUNNERS_PREFIX=smi_python_tbi_runner
python \
    -m smi_python_runner.main \
    -p profile1,profile2  \
    -c ./test/resources \
    -o ./test/resources/cli/optional.yaml \
    -r tbi-runner \
    -s sub-x \
    -t ./test/resources/tbi-376bdfaa-1195-11ee-be56-0242ac120002.yaml
```
