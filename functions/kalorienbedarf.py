def calculate_calories(age, height, weight, gender, activity_level):
    """
    Berechnet BMR (Grundumsatz) nach Mifflin-St-Jeor
    und TDEE (Gesamtumsatz) mit Aktivitätsfaktor.
    
    Args:
        age: Alter in Jahren
        height: Größe in cm
        weight: Gewicht in kg
        gender: "m" oder "w"
        activity_level: Aktivitätslevel-String
    
    Returns:
        tuple: (bmr, tdee)
    """
    if gender.lower().startswith("m"):
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_factors = {
        "Keine": 1.2,
        "Leicht": 1.375,
        "Mäßig": 1.55,
        "Aktiv": 1.725,
        "Sehr aktiv": 1.9,
    }

    factor = activity_factors.get(activity_level, 1.2)
    tdee = bmr * factor
    return bmr, tdee