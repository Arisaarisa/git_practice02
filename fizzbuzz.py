# 関数の作成
def fizzbuzz_convert(number):
    # もしnumberが3の倍数のとき
    if number % 3 == 0:
        return 'Fizz'


# fizzbuzz_convertが3の時Fizz
assert fizzbuzz_convert(3) == 'Fizz'
