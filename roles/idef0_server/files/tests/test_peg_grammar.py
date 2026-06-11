from parsimonious.grammar import Grammar

from idef0svg.parser import IdefVisitor, grammar

# Low level IDEF0 syntax from the original author
idef0svg_original_grammar = Grammar(
    r"""
FunctionalBlockDiagram = Statement+
Statement = Function Verb Signal newline+

Function = FunctionID? Capitalized (whitespace Capitalized)*
Signal = PascalCase
Verb = whitespace ("receives" / "respects" / "requires" / "produces") whitespace

FunctionID = ~r"[A-Z][a-z]{2}" "-" integer ("." integer)* ": "
PascalCase = Capitalized+
Capitalized = ~r"[A-Z][a-z0-9]*"

integer = ~r"\d+"
newline = "\n"
whitespace = ~" +"
"""
)


def test_idef0_parsing() -> None:
    tree = grammar.parse("""[CookPizza]
    in Ingredients
    res CustomerOrder
    res Recipe
    ctrl Chef
    ctrl Kitchen
    out Pizza

[TakeOrder]
    out CustomerOrder
    res Menu
    ctrl WaitStaff
    in Pizza
    in HungryCustomer
    out SatisfiedCustomer
    out Mess
""")

    iv = IdefVisitor()
    low_level_code = iv.visit(tree)

    assert idef0svg_original_grammar.parse(low_level_code)


def test_function_name_in_plain_english() -> None:
    tree = grammar.parse("""[A quick brown fox jumps over the lazy dog]
    in DummyInput
    out DummyOutput
""")

    iv = IdefVisitor()
    low_level_code = iv.visit(tree)

    assert idef0svg_original_grammar.parse(low_level_code)


def test_function_id() -> None:
    tree = grammar.parse("""[INT-2.1: Function name]
    in DummyInput
    out DummyOutput

[FNC-1.2.3.404: Function name]
    in DummyInput
    out DummyOutput
""")

    iv = IdefVisitor()
    low_level_code = iv.visit(tree)

    assert idef0svg_original_grammar.parse(low_level_code)
