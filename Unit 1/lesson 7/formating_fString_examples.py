# formatting numbers for decmmals places
#.2f is the amount of demical places to round to
# 2 is the demical place
value = 12.3456789
print(f"{value:.2f}")
#output:123. 45


# turns value into percentage
# perentage means the amount of 0 showing after

per = 0.785
print(f"{per:.12%}")
# 78.500000000000%

# you can also round or "split" a string
text = "this is a long string"
print(f"{long_text:.15}")

#:^ centre aligned
# number is space indicated
number = 42
print(f"{number:^6}")
#output __42__

# :> right aligned
print(f"{number:>5}")
#output: ___42

#:< left aligned
print(f"{number:<5}")
#output:42___

