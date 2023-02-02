from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Adam","Sandland") == "Sandland; Adam"
    assert make_full_name("Alexa","Mills") == "Mills; Alexa"
    assert make_full_name("Dillon","Thurgood") == "Thurgood; Dillon"
    assert make_full_name("Maggie","Macfarlane") == "Macfarlane; Maggie"
    assert make_full_name("John","Cina") == "Cina; John"

def test_extract_family_name():
    assert extract_family_name("Sandland; Adam")
    assert extract_family_name("Mills; Alexa")
    assert extract_family_name("Thurgood; Dillon")
    assert extract_family_name("Macfarlane; Maggie")
    assert extract_family_name("Cina; John")

def test_extract_given_name():
    assert extract_given_name("Sandland; Adam")
    assert extract_given_name("Mills; Alexa")
    assert extract_given_name("Thurgood; Dillon")
    assert extract_given_name("Macfarlane; Maggie")
    assert extract_given_name("Cina; John")
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
