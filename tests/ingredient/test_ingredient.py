# import pytest
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    frango = Ingredient('frango')
    another_frango = Ingredient('frango')
    ovo = Ingredient('ovo')

    assert frango.__eq__(another_frango)
    assert frango.__hash__() != ovo.__hash__()
    assert frango.__hash__() == another_frango.__hash__()
    assert frango.__repr__() == "Ingredient('frango')"
    assert frango.name == 'frango'
    assert len(frango.restrictions) == 2
