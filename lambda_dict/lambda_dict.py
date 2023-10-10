(
    ### main body ###
    # this is where most of the fun happens but first read the second part
    # to undestand how we get the values
    #
    # the whole lambda is written as generator expression
    # to allow calling multiple functions of "one line"
    # note: the `for`s are evaluated before the first expression so
    # eg. `print(1) for _ in [print(2)] for _ in [print(3)]` prints 2, 3 and then 1
    #
    # `globals().update(**{a: b})`` defines the variable `a` with value `b` in the global namespace
    lambda rs: next(
        (
            # call the main function "m165"
            g(r(14) + b(r(22))(r(23)))()
            # define function `r` that returns `x`-th element of the sorted resources list
            for _ in [globals().update(**{rs[17]: lambda x: rs[x]})]
            # define function `a` that when called defines the variable `y` with value `x`
            # and return [None] to make it iterable and thus allow using it in the `for _ in []`
            # construct in place of the list
            for _ in [
                globals().update(**{r(1): lambda x, y: [globals().update(**{y: x})]})
            ]
            # use `a` to define `g` that returns the value of a variable with name `x`
            for _ in a(lambda x: globals()[x], r(7))
            # define function `b` that returns the value of a builtin with name `x`
            # kinda hacky because for some reason __builtins__ is sometimes `dict` and sometimes `module`
            for _ in a(
                lambda x: type(g(r(27))) == dict
                and g(r(27))[x]
                or getattr(g(r(27)), x),
                r(2),
            )
            # define the main "m165" function
            for _ in a(
                lambda: next(
                    (
                        # `__builtins__["exec"](xx)`
                        b(r(5) + chr(r(18)) + r(5) + "c")(xx)
                        # `aa` = "print"
                        for aa in [r(21)[::-1]]
                        # `bb` = "s.gettrace() is None"
                        # `gettrace` returns a function is used to trace the execution
                        # in debugger or `None` if no debugger is used
                        for bb in [f"{r(11)[0]}.{r(24)}{r(16)[::-1]}(){r(15)}{r(12)}"]
                        # `cc` = "next(iter(()))" - to raise StopIteration exception
                        # combines odd and even characters from the resources list
                        # ''.join( (i + j) for(i, j) in zip(even_chars, odd_chars) )
                        for cc in [f"{''.join(i+j for(i,j)in zip(r(19),r(20)))}"]
                        # `dd` = "'Hello World!'"
                        # even_hex = r(25)
                        # odd_hex = r(3)
                        # ''.join(
                        #     chr(int(y, 16)) # convert hex (eg. "7a") to coresponding ASCII char
                        #        for y in (
                        # yield 2 characters from the string at a time
                        #            x[i:i + 2] for i in range(0, len(x), 2)
                        #        )
                        # ) for x in (even_hex, odd_hex) # do it for both even and odd chars
                        #
                        # results in `(even_chars, odd_chars)`
                        # then feeds this into same code as on the previous `for` line
                        # using the * to spread the generator into arguments
                        for dd in [
                            f"'{''.join((i+j for(i,j)in zip(*(''.join((chr(int(y,16))for y in(x[i:i+2]for i in range(0,len(x),2))))for x in(r(25),r(3))))))}'"
                        ]
                        # combined the strings into "print(s.gettrace() is None and next(iter(())) or 'Hello World!')"
                        # which is the same as:
                        # if s.gettrace() is None:
                        #    print('Hello World!')
                        # else:
                        #    raise StopIteration
                        for xx in [f"{aa}({bb} and {dd} or {cc})"]
                        # `s` = __import__("sys")
                        for s in [b(r(4))(r(11))]
                    )
                ),
                r(13),  # m165
            )
        )
    )
)(
    ### sorting resources ###
    # To make the code impossible to read without running it and to disallow
    # renaming variables when deobfuscating - their names are stored here as strings
    #
    # sorted resources for reference:
    # [
    #  0:    [1], # the iteration counter
    #  1:    "a", # identifier
    #  2:    "b", # identifier
    #  3:    "656c206f6c21", # hex encoded odd characters of "Hello World!"
    #  4:    "__import__", # for dynamically importing the `sys` module
    #  5:    "e", # used to construct "exec"
    #  6:    "f", # unused
    #  7:    "g", # identifier
    #  8:    "h", # identifier
    #  9:    "ch", # unused
    # 10:    "i", # identifier
    # 11:    "sys", # for `sys.gettrace()``
    # 12:    None, # used to construct "is None"
    # 13:    "m165", # identifier for "main" function
    # 14:    "m", # used to construct "m165"
    # 15:    " is ", # used to construct " is None"
    # 16:    "ecart", # reversed "trace", used to construct "sys.gettrace()"
    # 17:    "r", # identifier
    # 18:    120, # used as "chr(120)" to get "x" in "exec"
    # 19:    "nx(tr()", # even characters of "next(iter(())"
    # 20:    "etie())", # odd characters of "next(iter(())"
    # 21:    "tnirp", # reversed "print"
    # 22:    "str", # for `str(...)`
    # 23:    0xA5, # 165
    # 24:    "get", # used to construct "gettrace" and "getattr"
    # 25:    "486c6f577264", # hex encoded even characters of "Hello World!"
    # 26:    "attr", # used to construct "getattr(...)"
    # 27:    "__builtins__", # to access builtins the same way as globals()
    # ]
    (
        # Uses dict `a` to store the lambda and then call it from itself to allow recursion
        # as a replacement of a while loop.
        #
        # `a.__setitem__("r", ...)`` is a lambda friendly way to do `a["r"] = ...`.
        # It also return None so next line is chained using `or`.
        lambda a, l: a.__setitem__(
            0,
            lambda l: (
                # Each iteration it takes all `l`-th elements and puts them on the beggining
                # of the list. Then it takes the rest and adds them to the end.
                # eg.: l = 2, list = [0,1,2,3,4,5] => [0,2,4,1,3,5].
                a.__setitem__(
                    "r", a["r"][::l] + [x for x in a["r"] if x not in a["r"][::l]]
                )
                # Then it rotates the list by 3 elements to the left.
                # eg.: [0,1,2,3,4,5] => [3,4,5,0,1,2]
                or a.__setitem__("r", a["r"][3:] + a["r"][:3])
                # Then it checks if first element of the list is a another list and decrements
                # the first (and only) element of that list. This serve as a iteration counter.
                # Also it sets `l` to this new decremented value.
                or type(x := a["r"][0]) == list
                and (l := x.__setitem__(0, x[0] - 1) or x[0]) == 1  # basically (l = --x[0]) == 1
                # When this counter is 2 (and thus `--x[0] == 1`) the loop ends and the resources list
                # is returned and passed to the main body as an argument
                and a["r"]
                # Otherwise recurse with the new `l` value
                or a[0](l)
            ),
        )
        or a[0](l)
    )(
        ### resources list ###
        {
            "r": [
                "r",
                "tnirp",
                "nx(tr()",
                " is ",
                "m165",
                "656c206f6c21",
                "i",
                "ecart",
                None,
                "g",
                "b",
                "a",
                0xA5,  # 165
                "m",
                "f",
                "etie())",
                "h",
                "get",
                "e",
                120,
                "__import__",
                "str",
                "attr",
                "ch",
                "486c6f577264",
                "sys",
                "__builtins__",
                [0b11011],  # [27], the iteration counter
            ]
        },
        20,  # starting value for `l`
    )
)
