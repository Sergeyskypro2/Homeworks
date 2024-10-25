import pytest
from string_utils import StringUtils

#1
@pytest.mark.parametrize( "input, expected", [ ("text", "Text"), ("Text", "Text"), ("happy birthday", "Happy birthday") ] )
def test_capitilize_positive(input, expected):
    res = StringUtils()
    assert res.capitilize(input) == expected


#2
@pytest.mark.parametrize( "input, expected", [ ("   text", "text"), ("  123", "123") ] )
def test_trim_positive(input, expected):
    res = StringUtils()
    assert res.trim(input) == expected

#3
#не получается c двоеточием!
@pytest.mark.parametrize( "input, expected", [ ("a,b,c,d", ["a", "b", "c", "d"] ) ] )
def test_to_list_positive(input, expected):
    res = StringUtils()
    assert res.to_list(input) == expected



#4
@pytest.mark.parametrize( "input, symdol", [ ("Hello", "e") ] )
def test_contains_positive(input, symdol):
    res = StringUtils()
    assert res.contains(input, symdol) == True


#5
@pytest.mark.parametrize( "input, symdol, expected", [ ("Hello", "H", "ello") ] )
def test_delete_symbol_positive(input, symdol, expected):
    res = StringUtils()
    assert res.delete_symbol(input, symdol) == expected


#6
@pytest.mark.parametrize( "input, symdol", [ ("Hello", "H") ] )
def test_starts_with_positive(input, symdol):
    res = StringUtils()
    assert res.starts_with(input, symdol) == True



#7
@pytest.mark.parametrize( "input, symdol", [ ("Hello", "o") ] )
def test_end_with_positive(input, symdol):
    res = StringUtils()
    assert res.end_with(input, symdol) == True



#8
@pytest.mark.parametrize( "input", [ ("    "), ("") ] )
def test_is_empty_positive(input):
    res = StringUtils()
    assert res.is_empty(input) == True


#9
@pytest.mark.parametrize( "input, expected", [ ( "1234", "1, 2, 3, 4") ] )
def test_list_to_string_positive(input, expected):
    res = StringUtils()
    assert res.list_to_string(input) == expected