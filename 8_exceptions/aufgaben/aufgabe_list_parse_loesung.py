a = ["2", "a3", "0.2", "0,4", "a01", "3", ",", "a.a", "a,a"]


def list_parse(a: list[str]) -> tuple[list, list]:
    res = []
    errorlist = []

    for el in a:
        try:
            res.append(float(el.replace(",", ".")))
        except ValueError:
            errorlist.append(el)
    return res, errorlist


res, errorlist = list_parse(a)
print("Result: ", res)
print("Fehler:", errorlist)
