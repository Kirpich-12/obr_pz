def test( name):
         asc = [ord(char) for char in name]
         print(asc)
         for i in asc:
              if i not in range(97, 123) and i != 45:
                   raise ValueError
print(test('qwe'))