# Vulpedia

Demo of AST clustering and signature abstraction of Vulpedia.

### AST Clustering

To complete AST Clustering, please follow the introduction:

1. install dependencies.
```shell
pip install -r requirements.txt
```
2. run ```clustering.py```
```shell
python clustering.py
```
This script will automatically run clustering on the code provided in folder ```demo_code```, 
and output a clustering png ```clustering.png``` and clustered functions in ```clusters.log``` in current folder.

[//]: # (![]&#40;fig\clustering.png "Clustering Results"&#41;)

### Signature Abstraction

The signature abstraction is built upon Slither. For installation, please install our Slither at [here](https://github.com/ToolmanInside/slither_im).

#### Usage

