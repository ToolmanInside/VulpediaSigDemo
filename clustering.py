import os
from .ast_helper import AstHelper
from .solidity_compiler import SolidityCompiler
from apted import APTED

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
            self.format_transfer(tree, output_str)
            print(output_str)
        return contracts

    def format_transfer(self, tree, output_str):
        for node in tree.keys():
            if isinstance(tree[node], dict):
                output_str += "{" + node
                self.format_transfer(tree[node], output_str)
            elif isinstance(tree[node], list):
                output_str += "{" + node
                for ele in tree[node]:
                    self.format_transfer(ele, output_str)
            else:
                output_str.append("}")


if __name__ == "__main__":
    cluster = Clustering(os.path.join("demo_code", "com-1.sol"))
