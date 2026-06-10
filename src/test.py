from main import calculadora

def test_suma_numeros():
    calc = calculadora()
    result = calc.suma(1,2)
    assert result == 3, f"Se esperaba 3 pero se obtuvo {result}"