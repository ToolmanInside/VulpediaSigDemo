import os
from ast_helper import AstHelper
from solidity_compiler import SolidityCompiler
from apted import APTED
from collections import ChainMap
from functools import reduce

def edt_distance(tree1, tree2):
    apted = APTED(tree1, tree2)
    ted = apted.compute_edit_distance()
    return ted

class Clustering(object):
    def __init__(self, target_folder_path):
        self.target_folder_path = target_folder_path
        self.ast_helper = AstHelper(self.target_folder_path, input_type = "solidity", remap = "", allow_paths = "")
        contracts = [x[0].split(":")[-1] for x in SolidityCompiler(self.target_folder_path).output()]
        normalized_trees = self.normalization(contracts)

    def normalization(self, contracts):
        trees = list()
        for contract in contracts:
            tree = self.ast_helper.get_func(contract)
            output_str = ""
            if tree == {}:
                continue
            flattree = self.flatmap(tree)
            print(flattree)
            # print(stable_str)
        return contracts

    def _flatmap(self, tree, stable_str):
        for k,v in tree.items():
            # stable_str = stable_str + "{" + str(k)
            if isinstance(v, dict):
                stable_str = stable_str + "{" + str(k)
                stable_str = self._flatmap(v, stable_str)
            elif isinstance(v, list):
                stable_str = stable_str + "{" + str(k)
                stable_str = self._flatlist(v, stable_str)
            else:
                stable_str = "{" + stable_str + str(v) + "}"
                return stable_str

    def _flatlist(self, tree, stable_str):
        stable_str = stable_str + "{"
        for e in tree:
            if isinstance(e, dict):
                self._flatmap(e, stable_str)
            elif isinstance(e, list):
                self._flatlist(e, stable_str)
        stable_str = stable_str + "}"
        return stable_str

    def flatmap(self, tree):
        stable_str = ""
        if isinstance(tree, dict):
            stable_str = self._flatmap(tree, stable_str)
        elif isinstance(tree, list):
            stable_str = self._flatlist(tree, stable_str)
        else:
            stable_str = stable_str + "}"
        return stable_str

if __name__ == "__main__":
    cluster = Clustering(os.path.join("demo_code", "com-1.sol"))
