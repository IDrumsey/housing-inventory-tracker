import src.utility as utility

import pytest


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ([39151, 39153], "Housing Inventory over Time: Stark Summit"),
        ([39151], "Stark County Housing Inventory over Time"),
        ([39153], "Summit County Housing Inventory over Time"),
    ),
)
def test_generatePlotTitle(input, expected):
    assert utility.generatePlotTitle(input) == expected
