import os
from ast_helper import AstHelper
from solidity_compiler import SolidityCompiler
from apted import APTED, helpers
import numpy as np

class Clustering(object):
    def __init__(self, target_folder_path):
        self.target_folder_path = target_folder_path
        self.file_list = os.listdir(self.target_folder_path)
        self.normalized_trees = list()
        for ff in self.file_list:
            file_path = os.path.join(self.target_folder_path, ff)
            ast = AstHelper(file_path, input_type = "solidity", remap = "", allow_paths = "")
            contracts = [x[0].split(":")[-1] for x in SolidityCompiler(file_path).output()]
            self.normalized_trees.append(self.normalization(ast, contracts))
        self.distanceMat = self.computeEdtDist(self.normalized_trees)
        print(self.distanceMat)

    def edt_distance(self, tree1, tree2):
        apted = APTED(tree1, tree2)
        ted = apted.compute_edit_distance()
        return ted

    def computeEdtDist(self, trees):
        length = len(trees)
        mat = np.zeros((length, length))
        for i in range(length):
            for j in range(length):
                dist = self.edt_distance(trees[i][0], trees[j][0])
                mat[i][j] = dist
        return mat

    def normalization(self, ast_helper, contracts):
        trees = list()
        for contract in contracts:
            tree = ast_helper.get_func(contract)
            if tree == {}:
                continue
            trees.append(helpers.Tree.from_text(self.transform(tree)))
        return trees

    def transform_recusion(self, d):
        if type(d) == type('s'):
            return '{%s}' % d
        if type(d) == type(1):
            return '{%d}' % d
        if type(d) == type({}):
            s = ''
            for key in d:
                s += self.transform_recusion(d[key])
            return '{%s}' % s
        if type(d) == type([]):
            s = ''
            for key in d:
                s += self.transform_recusion(key)
            return '%s' % s
        return ''

    def transform(self, d):
        s = ''
        for key in d:
            s += '{' + key + self.transform_recusion(d[key]) + '}'
        return '{root' + s + '}'

if __name__ == "__main__":
    cluster = Clustering(os.path.join("demo_code"))
