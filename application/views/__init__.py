from . import auth, compare, index, sandbox
bp_list = [auth.auth_bp, compare.compare_bp, sandbox.sandbox_bp,
           index.index_bp]
