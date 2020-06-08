# Socket cluster client with [CodecMinBin](https://github.com/SocketCluster/sc-codec-min-bin)
A client in Python to connect to [socket cluster server](https://github.com/SocketCluster/socketcluster).  
Forked from [sacOO7/socketcluster-client-python](https://github.com/sacOO7/socketcluster-client-python).

### Install the package
`pip install sktclcli_minbin`

### Changes
* Apply codec [MinBin](https://github.com/SocketCluster/sc-codec-min-bin). I hate this codec.
* Add requirements.txt

### Usage
Example for publishing and subscribing data in `main_test.py`

### Commands for devs
* Ubuntu common python packages:  
````apt install -qy python3-dev python3-distutils python3-pip python3-setuptools python3-venv````
* Create and active virtual environment:    
`python3 -m pip venv venv && venv/bin/activate`
* Save dependencies list:  
`python -m pip freeze --local > requirements.txt`
* Packaging tools:  
````sudo python3 -m pip install --upgrade setuptools wheel twine keyrings.alt````  
* Create built distribution:  
````python3 setup.py sdist bdist_wheel````  
* Upload the distribution:  
````python3 -m twine upload --repository pypi ./dist/*````