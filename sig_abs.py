import os
import sys
import time
import subprocess
from logzero import logger

def lcs(a, b, c):
    m = len(a)
    l = len(b)
    n = len(c)
    subs = [[[0 for k in range(n+1)] for j in range(l+1)] for i in range(m+1)]

    for i, x in enumerate(a):
        for j, y in enumerate(b):
            for k, z in enumerate(c):
                if x == y and y == z:
                    subs[i+1][j+1][k+1] = subs[i][j][k] + 1
                else:
                    subs[i+1][j+1][k+1] = max(subs[i+1][j+1][k], 
                                              subs[i][j+1][k+1], 
                                              subs[i+1][j][k+1])
    # return subs[-1][-1][-1] #if you only need the length of the lcs
    lcs = ""
    while m > 0 and l > 0 and n > 0:
        step = subs[m][l][n]
        if step == subs[m-1][l][n]:
            m -= 1
        elif step == subs[m][l-1][n]:
            l -= 1
        elif step == subs[m][l][n-1]:
            n -= 1
        else:
            lcs += str(a[m-1])
            m -= 1
            l -= 1
            n -= 1

    return lcs[::-1]
 
def load_clusters():
    content = open("clusters.log").read()
    content = eval(content)
    return content 

def call_slither(file_path):
    cmd = f"slither --print signature-abstraction {file_path}"
    result = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout, stderr = result.communicate()
    stdout, stderr = stdout.decode(), stderr.decode()
    print(stderr)
    return stdout

def main():
    content = load_clusters()
    abstracted_results = list()
    for c in content:
        file_path = c[1]
        abstracted_results.append(call_slither(file_path))
        time.sleep(1)
    logger.debug("Analzing LCS")
    lcs_result = lcs(abstracted_results[0], abstracted_results[1], abstracted_results[2])
    logger.debug(f"Raw Signature: {lcs_result}")

if __name__ == "__main__":
    main()