import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    coxinha = Dish('Coxinha', 3.5)
    assert coxinha.name == 'Coxinha'

    frango = Ingredient('frango')
    ovo = Ingredient('ovo')
    coxinha.add_ingredient_dependency(frango, 1)
    coxinha.add_ingredient_dependency(ovo, 6)
    assert len(coxinha.get_ingredients()) == 2

    another_coxinha = Dish('Coxinha', 3.5)
    assert coxinha.__eq__(another_coxinha)

    assert len(coxinha.get_restrictions()) == 2

    pastel = Dish('Pastel de Queijo', 8)
    assert coxinha.__hash__() != pastel.__hash__()

    assert coxinha.__hash__() == another_coxinha.__hash__()

    assert coxinha.__repr__() == "Dish('Coxinha', R$3.50)"

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Pastel de Carne", "Oito Reais")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
            ):
        Dish("Pastel de Frango", -8.5)
