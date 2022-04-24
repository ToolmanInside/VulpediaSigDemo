from crytic_compile import CryticCompile

class SolidityCompiler(object):
    def __init__(self, source_path):
        self.source = source_path
        self.allow_paths = ""
        self.remap = ""
        self.compiled_contracts = self.compile_solidity()

    def _extract_bin_obj(self, com: CryticCompile):
        return [(com.contracts_filenames[name].absolute + ':' + name, com.bytecode_runtime(name)) for name in com.contracts_names if com.bytecode_runtime(name)]

    def compile_solidity(self):
        options = []
        if self.allow_paths:
            options.append(F"--allow-paths {self.allow_paths}")
            
        com = CryticCompile(self.source, solc_remaps = self.remap, solc_args=' '.join(options))
        contracts = self._extract_bin_obj(com)

        libs = com.contracts_names.difference(com.contracts_names_without_libraries)
        if libs:
            return self._link_libraries(self.source, libs)
        return contracts

    def output(self):
        return self.compiled_contracts

    def _link_libraries(self, filename, libs):
        options = []
        for idx, lib in enumerate(libs):
            lib_address = "0x" + hex(idx+1)[2:].zfill(40)
            options.append("--libraries %s:%s" % (lib, lib_address))
        if self.allow_paths:
            options.append(F"--allow-paths {self.allow_paths}")
        com = CryticCompile(target=self.source, solc_args=' '.join(options), solc_remaps=self.remap)

        return self._extract_bin_obj(com)