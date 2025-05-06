# validator.py
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def check_email(input_email):
    """
    Die Funktion checkt, ob der String ‘input_email‘ eine valide Adresse darstellt.

    Parameters: input_email (str)
    Returns: str
    """
    logging.debug(f"Eingegebene Email ist {input_email}.")
    logging.info("Funktion 'check_email' wurde aufgerufen.")
    assert len(input_email) >= 5 and '@' in input_email and '.' in input_email, "Ungültige Emailadresse"
    return True

def check_age(input_age):
    """
    Die Funktion checkt, ob der String ‘input_age‘ ein valides Alter darstellt.

    Parameters: input_age (str)
    Returns: int
    """
    logging.debug(f"Eingegebenes Alter ist {input_age}.")
    logging.info("Funktion 'check_age' wurde aufgerufen.")
    try:
        age = int(input_age)
        assert 10 <= age <= 99, "Alter muss zwischen 10 und 99 liegen"
        return True
    except ValueError:
        logging.error("Eingabe konnte nicht in eine Zahl umgewandelt werden.")
        return False
    except AssertionError as e:
        logging.warning(e)
        return False

def check_password_strength(password):
    """
    Überprüft ein Passwort auf Mindestanforderungen:
    - Mindestlänge 8
    - mindestens ein Großbuchstabe
    - mindestens eine Zahl
    - mindestens ein Sonderzeichen
    """
    import re
    logging.debug(f"Eingegebenes Passwort: {password}")
    errors = []
    if len(password) < 8:
        errors.append("Passwort zu kurz")
    if not re.search(r"[A-Z]", password):
        errors.append("Kein Großbuchstabe enthalten")
    if not re.search(r"\d", password):
        errors.append("Keine Zahl enthalten")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Kein Sonderzeichen enthalten")

    if errors:
        for err in errors:
            logging.warning(err)
        return False
    logging.info("Passwort ist stark genug.")
    return True
