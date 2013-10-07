import pytest

from pub import PINT, HALF_PINT, PITCHER
from pub import PintGlass, HalfPintGlass, Pitcher, NoContentException


@pytest.fixture
def pint_glass():
    return PintGlass()


@pytest.fixture
def half_pint_glass():
    return HalfPintGlass()


@pytest.fixture
def pitcher():
    return Pitcher()


@pytest.fixture(params=['pint_glass', 'half_pint_glass', 'pitcher'])
def glass(pint_glass, half_pint_glass, pitcher, request):
    return {'pint_glass': pint_glass,
            'half_pint_glass': half_pint_glass,
            'pitcher': pitcher}[request.param]


class TestGlass(object):

    def test_fresh_pint_glass_is_1_pint(cls, pint_glass):
        assert pint_glass.content == PINT

    def test_fresh_half_pint_glass_is_half_pint(cls, half_pint_glass):
        assert half_pint_glass.content == HALF_PINT

    def test_fresh_pitcher_is_3_pints(cls, pitcher):
        assert pitcher.content == PITCHER

    def test_fresh_glass_is_has_maximum_content(cls, glass):
        assert glass.content == glass._max

    def test_fresh_glass_is_full(cls, glass):
        assert glass.is_full()

    def test_full_refilled_glass_has_maximum_content(cls, glass):
        glass.refill()
        assert glass.content == glass._max

    def test_empty_refilled_glass_has_maximum_content(cls, glass):
        glass.content = 0
        glass.refill()
        assert glass.content == glass._max

    def test_customer_drinks_from_full_pint_glass_has_19oz(cls, pint_glass):
        pint_glass.drink()
        assert pint_glass.content == 19

    def test_refill_19oz_glass_is_full(cls, pint_glass):
        pint_glass.content = 19
        pint_glass.refill()
        assert pint_glass.is_full()

    def test_drink_from_empty_glass_raises_no_content_exception(cls, pint_glass):
        pint_glass.content = 0
        with pytest.raises(NoContentException):
            pint_glass.drink()

    def test_customer_quaffs_from_full_pint_has_16oz(cls, pint_glass):
        pint_glass.quaff()
        assert pint_glass.content == 16

    def test_0oz_glass_is_empty(cls, glass):
        glass.content = 0
        assert glass.is_empty()

    def test_quaff_from_3oz_glass_empties_glass(cls, glass):
        glass.content = 3
        glass.quaff()
        assert glass.is_empty()

    def test_downed_glass_is_empty(cls, glass):
        glass.down()
        assert glass.is_empty()

    def test_downed_empty_glass_returns_no_content_exception(cls, glass):
        glass.content = 0
        with pytest.raises(NoContentException):
            glass.down()

    def test_quaff_empty_glass_returns_no_content_exception(cls, glass):
        glass.content = 0
        with pytest.raises(NoContentException):
            glass.quaff()
