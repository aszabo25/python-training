# Egy teszteset az egy függvény
# Egy tezsteset mindig csak egy dolgot tesztel
# Teszteset neve konvenció szerint a teszt szóval kezdődik



from __future__ import absolute_import


def test_absolute_with_positive():
    #BDD = Behavior Driven Development
    # 3 részből áll: given-when-then
    # given
    input = 5
    # when
    result = absolute(input)
    # then
    expected = 5
    assert result == expected


def test_absolute_with_negative():
    assert absolute(-5) == 5

def test_absolute_with_zero():
    assert absolute(0) == 0