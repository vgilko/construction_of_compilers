from lib.postfix import Postfix


def test_convert():
    # given
    regex_dict = {
        "a|b": "ab|",
        "a+b": "ab+",
        "a*b": "ab*",
        "a?b": "ab?",
        "a(b|c)d": "abc|d",
        "a(bc)+d": "abcd+",
        "a*b+c": "ab*c+",
        "(a+b)*c": "ab+c*",
        "(a|b)*c+": "ab|c*+",
        "a(b+c)d*|e(f+g)": "abc+d*efg+|",
    }

    # when
    for key, value in regex_dict.items():
        postfix = Postfix(key)
        actual_postfix = postfix.convert()

        print(key)

        # then
        assert actual_postfix == value
