# input_validation.py
from validator import check_email, check_age, check_password_strength
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def main():
    """
    Hauptfunktion: Steuert den Programmablauf
    """
    while True:
        print("""
Drücke '?' um Hilfe zu bekommen.
Drücke 'q' um die App zu verlassen.
Drücke 'w' um weiterzumachen.
""")
        user_input = input("> ").strip()
        try:
            assert user_input in ['?', 'w', 'q'], "Bitte gib einen korrekten Input an!"
        except AssertionError as e:
            logging.error(e)
            continue

        if user_input == '?':
            print("check_email:")
            print(check_email.__doc__)
            print("\ncheck_age:")
            print(check_age.__doc__)
            print("\ncheck_password_strength:")
            print(check_password_strength.__doc__)

        elif user_input == 'w':
            while True:
                email = input("Wie lautet deine Email?\n> ")
                try:
                    if check_email(email):
                        break
                except AssertionError:
                    logging.error("Bitte gib eine korrekte Email an!")

            while True:
                age = input("Wie alt bist du?\n> ")
                if check_age(age):
                    break
                else:
                    logging.error("Bitte gib ein korrektes Alter an!")

            password = input("Bitte gib ein Passwort ein:\n> ")
            check_password_strength(password)

        elif user_input == 'q':
            logging.debug("Das Program wurde beendet.")
            break

if __name__ == "__main__":
    main()
