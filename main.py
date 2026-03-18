import translator as tr

def main():
    """
    Obiettivo:
    - Punto di ingresso del programma.
    - Creare un Translator con il file "dictionary.txt".
    - Mostrare il menù in un ciclo.
    - Leggere la scelta dell'utente.
    - Chiamare il metodo appropriato del Translator.
    """
    t = tr.Translator("dictionary.txt")

    while True:
        # Mostro il menù
        t.printMenu()

        # Leggo la scelta
        choice = input("Seleziona un'opzione: ").strip()

        # Controllo che sia un numero
        if not choice.isdigit():
            print("Errore: devi inserire un numero.")
            continue

        choice = int(choice)

        # Gestione delle scelte
        if choice == 1:
            # Aggiungi nuova parola
            entry = input("Inserisci <parola_aliena> <traduzione1 traduzione2 ...>: ")
            t.handleAdd(entry)

        elif choice == 2:
            # Cerca traduzione
            query = input("Inserisci la parola aliena da tradurre: ")
            t.handleTranslate(query)

        elif choice == 3:
            # Cerca con wildcard
            pattern = input("Inserisci la parola con '?': ")
            t.handleWildcard(pattern)

        elif choice == 4:
            # Stampa tutto il dizionario
            t.printDictionary()

        elif choice == 5:
            # Esci
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()