# Reescrever toRoman
def toRoman(num):

  centenas = {1: 'C'}
  dezenas = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L',
            6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
  unidades = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI',
              7: 'VII', 8: 'VIII', 9: 'IX'}

  result = ""
  
  if num >= 100:
    result += centenas[1]
    num -= 100

  if num >= 10:
    digito = num // 10
    if digito in dezenas:
      result += dezenas[digito]
    num = num % 10

  if num > 0 and num in unidades:
    result += unidades[num]
    
  
  return result


# Não modificar deste ponto para baixo

# Testes


def test(value, expected):
  result = toRoman(value)
  if result == expected:
    print("✓ Teste {value} correto".format(value=value))
  else:
    print(
      "✗ Teste {value} incorreto. Esperado {expected}, obtido {result}".
      format(value=value, expected=expected, result=result))


test(1, "I")
test(2, "II")
test(3, "III")
test(4, "IV")
test(5, "V")
test(6, "VI")
test(7, "VII")
test(8, "VIII")
test(9, "IX")


test(10, "X")
test(12, "XII")
test(15, "XV")
test(18, "XVIII")
test(19, "XIX")
test(29, "XXIX")
test(38, "XXXVIII")
test(47, "XLVII")
test(56, "LVI")
test(65, "LXV")
test(74, "LXXIV")
test(83, "LXXXIII")
test(90, "XC")
test(92, "XCII")
test(100, "C")
