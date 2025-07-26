def dollars_to_float(d: str) -> float:
    float_d = float(d.replace('$', ''))
    return float_d


def percent_to_float(p: str) -> float:
    float_p = float(p.replace('%', '')) / 100
    return float_p


if __name__ == "__main__":
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")