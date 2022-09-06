# Kérjétek be, hogy a felhasználó mikor született!
# Írjátok ki, hogy ezek alapján hány éves!
# De ne csak egy számot, hanem a következő üzenetet:

# Mivel xxxx-ben születtél, ezért yy éves vagy.

# 1. Kérjük be, hogy mikor született! -int-é kell konvertálni
# 2. Számoljuk ki, hogy hány éves egy age változóban!
# 3. Írjuk ki f-stringgel a megadott üzenetet!

year_of_birth =int(input ("Mikor születtél"))
print(year_of_birth)
actual_year = 2022
age = actual_year - year_of_birth
print(age)
print(f"Mivel {year_of_birth}ben születtél, ezért {age} éves vagy")


