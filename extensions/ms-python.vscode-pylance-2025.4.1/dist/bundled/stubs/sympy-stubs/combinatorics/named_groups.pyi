from sympy.combinatorics.perm_groups import PermutationGroup

_af_new = ...

def AbelianGroup(*cyclic_orders) -> PermutationGroup: ...
def AlternatingGroup(n) -> PermutationGroup: ...
def set_alternating_group_properties(G, n, degree) -> None: ...
def CyclicGroup(n) -> PermutationGroup: ...
def DihedralGroup(n) -> PermutationGroup: ...
def SymmetricGroup(n) -> PermutationGroup: ...
def set_symmetric_group_properties(G, n, degree) -> None: ...
def RubikGroup(n) -> PermutationGroup: ...
