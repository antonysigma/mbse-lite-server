from idef0svg.plantuml_decoder import plantuml_decode, plantuml_encode


def test_decode() -> None:
    url = "SyfFKj2rKt3CoKnELR1Io4ZDoSa700=="
    decoded = plantuml_decode(url)

    assert decoded == "Bob -> Alice : hello"


def test_roundtrip() -> None:
    url = "SyfFKj2rKt3CoKnELR1Io4ZDoSa700=="
    decoded = plantuml_decode(url)

    plantuml_encode(decoded) == url


def test_large_plaintext() -> None:
    assert plantuml_encode("""Cook Pizza receives Ingredients
Cook Pizza respects Customer Order
Cook Pizza respects Recipe
Cook Pizza requires Chef
Cook Pizza requires Kitchen
Cook Pizza produces Pizza
Take Order produces Customer Order
Take Order respects Menu
Take Order requires Wait Staff
Eat Pizza receives Pizza
Eat Pizza receives Hungry Customer
Eat Pizza produces Satisfied Customer
Eat Pizza produces Mess
""")
