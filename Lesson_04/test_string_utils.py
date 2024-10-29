import pytest
from string_utils import StringUtils

#1
@pytest.mark.parametrize( "input, expected", [ ("sergey", "Sergey"), ("1990", "1990"), ("happy birthday", "Happy birthday") ] )
def test_capitilize_positive(input, expected):
    res = StringUtils()
    assert res.capitilize(input) == expected

@pytest.mark.parametrize( "input, expected", [ ("a", "A") ] )
def test_capitilize_negative(input, expected):
    res = StringUtils()
    assert res.capitilize(input) == expected


#2
@pytest.mark.parametrize( "input, expected", [ ("   sergey", "sergey"), ("  1990", "1990") ] )
def test_trim_positive(input, expected):
    res = StringUtils()
    assert res.trim(input) == expected

@pytest.mark.parametrize( "input, expected", [ ("  ", ""), ("", "") ] )
def test_trim_negative(input, expected):
    res = StringUtils()
    assert res.trim(input) == expected



#3
#не получается c двоеточием!
@pytest.mark.parametrize( "input, expected", [ ("a,b,c,d", ["a", "b", "c", "d"] ), ("1,2", ["1", "2"]) ] )
def test_to_list_positive(input, expected):
    res = StringUtils()
    assert res.to_list(input) == expected

@pytest.mark.parametrize( "input, expected", [ (" ", [] ) ] )
def test_to_list_negative(input, expected):
    res = StringUtils()
    assert res.to_list(input) == expected



#4
@pytest.mark.parametrize( "input, symbol", [ ("Sergey", "e") ] )
def test_contains_positive(input, symbol):
    res = StringUtils()
    assert res.contains(input, symbol) == True

@pytest.mark.parametrize( "input, symbol", [ ("", ""), ("  ", "  ") ] )
def test_contains_negative(input, symbol):
    res = StringUtils()
    assert res.contains(input, symbol) == True



#5
@pytest.mark.parametrize( "input, symbol, expected", [ ("Sergey", "S", "ergey"), ("1990", "99", "10"), ("!@#", "@", "!#") ] )
def test_delete_symbol_positive(input, symbol, expected):
    res = StringUtils()
    assert res.delete_symbol(input, symbol) == expected

@pytest.mark.parametrize( "input, symbol, expected", [ ("           ", " ", "") ] )
def test_delete_symbol_negative(input, symbol, expected):
    res = StringUtils()
    assert res.delete_symbol(input, symbol) == expected



#6
@pytest.mark.parametrize( "input, symbol", [ ("Sergey", "S"), ("1990", "1") ] )
def test_starts_with_positive(input, symbol):
    res = StringUtils()
    assert res.starts_with(input, symbol) == True

@pytest.mark.parametrize( "input, symbol", [ ("  ", " ") ] )
def test_starts_with_negative(input, symbol):
    res = StringUtils()
    assert res.starts_with(input, symbol) == True



#7
@pytest.mark.parametrize( "input, symbol", [ ("Sergey", "y"), ("1990", "0") ] )
def test_end_with_positive(input, symbol):
    res = StringUtils()
    assert res.end_with(input, symbol) == True

@pytest.mark.parametrize( "input, symbol", [ ("  ", " ") ] )
def test_end_with_negative(input, symbol):
    res = StringUtils()
    assert res.end_with(input, symbol) == True



#8
@pytest.mark.parametrize( "input", [ ("    "), ("") ] )
def test_is_empty_positive(input):
    res = StringUtils()
    assert res.is_empty(input) == True

@pytest.mark.parametrize( "input", [ (""), ("") ] )
def test_is_empty_negatibe(input):
    res = StringUtils()
    assert res.is_empty(input) == True



#9
@pytest.mark.parametrize( "input, expected", [ ( "1234", "1, 2, 3, 4"), ("ser", "s, e, r") ] )
def test_list_to_string_positive(input, expected):
    res = StringUtils()
    assert res.list_to_string(input) == expected

@pytest.mark.parametrize( "input, expected", [ ( "", "") ] )
def test_list_to_string_negative(input, expected):
    res = StringUtils()
    assert res.list_to_string(input) == expected