from collections.abc import Sequence
from enum import Enum

from antlr4.atn.ATN import ATN as ATN
from antlr4.atn.ATNConfig import ATNConfig as ATNConfig
from antlr4.atn.ATNConfigSet import ATNConfigSet as ATNConfigSet
from antlr4.atn.ATNState import RuleStopState as RuleStopState
from antlr4.atn.SemanticContext import SemanticContext as SemanticContext

class PredictionMode(Enum):
    SLL = 0
    LL = 1
    LL_EXACT_AMBIG_DETECTION = 2
    @classmethod
    def hasSLLConflictTerminatingPrediction(cls, mode: PredictionMode, configs: ATNConfigSet): ...
    @classmethod
    def hasConfigInRuleStopState(cls, configs: ATNConfigSet): ...
    @classmethod
    def allConfigsInRuleStopStates(cls, configs: ATNConfigSet): ...
    @classmethod
    def resolvesToJustOneViableAlt(cls, altsets: Sequence[set[int]]): ...
    @classmethod
    def allSubsetsConflict(cls, altsets: Sequence[set[int]]): ...
    @classmethod
    def hasNonConflictingAltSet(cls, altsets: Sequence[set[int]]): ...
    @classmethod
    def hasConflictingAltSet(cls, altsets: Sequence[set[int]]): ...
    @classmethod
    def allSubsetsEqual(cls, altsets: Sequence[set[int]]): ...
    @classmethod
    def getUniqueAlt(cls, altsets: Sequence[set[int]]): ...
    @classmethod
    def getAlts(cls, altsets: Sequence[set[int]]): ...
    @classmethod
    def getConflictingAltSubsets(cls, configs: ATNConfigSet): ...
    @classmethod
    def getStateToAltMap(cls, configs: ATNConfigSet): ...
    @classmethod
    def hasStateAssociatedWithOneAlt(cls, configs: ATNConfigSet): ...
    @classmethod
    def getSingleViableAlt(cls, altsets: Sequence[set[int]]): ...
