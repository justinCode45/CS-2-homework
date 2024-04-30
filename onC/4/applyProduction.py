def applyProduction(axiom: str, rules: dict[str, str], depth: int):
    production = axiom
    for i in range(depth):
        newProduction = ""
        for ch in production:
            newProduction += rules.get(ch, ch)
        production = newProduction
    return production


axiom = "F"
rules = {"F": "F-F++F-F"}
depth = 2
print(applyProduction(axiom, rules, depth)) 
