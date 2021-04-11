# 関数の作成
def fizzbuzz_convert(number):
    # もしnumberが3の倍数のとき
    if number % 3 == 0:
        # Fizzと返す
        return 'Fizz'
    # もしnumberが5の倍数のとき
    if number % 5 == 0:
        # Buzzと返す
        return 'Buzz'


# fizzbuzz_convertが3の時Fizz
assert fizzbuzz_convert(3) == 'Fizz'
# fizzbuzz_convertが5の時Buzz
assert fizzbuzz_convert(5) == 'Buzz'
# fizzbuzz_convertが5の時Buzz
assert fizzbuzz_convert(15) == 'FizzBuzz'
