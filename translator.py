from dictionary import Dictionary

class Translator:

    def __init__(self, filename):
        """
        Obiettivo:
        - Inizializzare il traduttore:
          - ricordare il nome del file del dizionario
          - creare un oggetto Dictionary per gestire i dati
          - caricare il contenuto iniziale dal file

        Scelta:
        - Delego la gestione delle parole a Dictionary.
        - Translator si occupa di file, input e menù.
        """
        self.filename = filename
        self.dictionary = Dictionary()
        self.loadDictionary(filename)

    def loadDictionary(self, filename):
        """
        Obiettivo:
        - Leggere il file "dictionary.txt" e caricare le parole nel Dictionary.

        Formato atteso:
        - Ogni riga: <parola_aliena> <traduzione1 traduzione2 ...>
        - Solo lettere [a-zA-Z], niente numeri o simboli.

        Logica:
        - Apro il file in lettura.
        - Per ogni riga:
          - strip() per togliere spazi e newline.
          - split() per separare in parole.
          - Controllo che ci sia almeno una traduzione.
          - Verifico che tutte le parole siano alfabetiche.
          - Converto tutto in minuscolo (case-insensitive).
          - Uso dictionary.addWord() per inserire i dati.
        """
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        raise ValueError("Riga vuota non ammessa.")

                    parts = line.split()
                    if len(parts) < 2:
                        raise ValueError(f"Riga non valida: {line}")

                    alien = parts[0]
                    translations = parts[1:]

                    if not alien.isalpha():
                        raise ValueError(f"Parola aliena non valida: {alien}")

                    for t in translations:
                        if not t.isalpha():
                            raise ValueError(f"Traduzione non valida: {t}")

                    alien = alien.lower()
                    translations = [t.lower() for t in translations]

                    self.dictionary.addWord(alien, translations)

        except FileNotFoundError:
            print("File non trovato. Creo un dizionario vuoto.")

    def printMenu(self):
        """
        Obiettivo:
        - Mostrare all'utente le opzioni disponibili, come richiesto dalla consegna.
        """
        print("\n--- TRADUTTORE ALIENO ---")
        print("1) Aggiungi nuova parola")
        print("2) Cerca una traduzione")
        print("3) Cerca con wildcard (?)")
        print("4) Stampa tutto il dizionario")
        print("5) Esci")

    def handleAdd(self, entry):
        """
        Obiettivo:
        - Gestire l'aggiunta di una nuova parola aliena e delle sue traduzioni.

        Parametri:
        - entry: stringa inserita dall'utente, del tipo:
          "<parola_aliena> <traduzione1 traduzione2 ...>"

        Logica:
        - split() per separare le parole.
        - Controllo che ci sia almeno una traduzione.
        - Verifico che tutte le parole siano alfabetiche.
        - Converto tutto in minuscolo.
        - Uso dictionary.addWord() per aggiornare la struttura dati.
        - Scrivo anche sul file in append, per persistenza.
        """
        parts = entry.strip().split()

        if len(parts) < 2:
            print("Errore: devi inserire almeno una traduzione.")
            return

        alien = parts[0]
        translations = parts[1:]

        if not alien.isalpha():
            print("Errore: parola aliena non valida.")
            return

        for t in translations:
            if not t.isalpha():
                print("Errore: traduzioni non valide.")
                return

        alien = alien.lower()
        translations = [t.lower() for t in translations]

        self.dictionary.addWord(alien, translations)

        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(" ".join([alien] + translations) + "\n")

        print("Parola aggiunta con successo.")

    def handleTranslate(self, query):
        """
        Obiettivo:
        - Gestire la ricerca della traduzione di una parola aliena.

        Parametri:
        - query: stringa inserita dall'utente, es: "alieno"

        Logica:
        - strip() per pulire.
        - isalpha() per controllare che siano solo lettere.
        - lower() per case-insensitive.
        - uso dictionary.translate() per ottenere le traduzioni.
        - Se None → parola non trovata.
        - Altrimenti stampo tutte le traduzioni.
        """
        word = query.strip()

        if not word.isalpha():
            print("Errore: sono ammesse solo lettere.")
            return

        word = word.lower()

        translations = self.dictionary.translate(word)

        if translations is None:
            print("Parola non trovata.")
        else:
            print("Traduzioni trovate:")
            for t in translations:
                print("-", t)

    def handleWildcard(self, pattern):
        """
        Obiettivo:
        - Gestire la ricerca con wildcard '?' (Esercizio 3).

        Parametri:
        - pattern: stringa con esattamente un '?', es: "ali?no"

        Logica:
        - Delego la logica di matching a dictionary.translateWordWildCard().
        - Se non ci sono risultati → messaggio.
        - Altrimenti stampo tutte le parole aliene e le loro traduzioni.
        """
        pattern = pattern.strip()

        # Controllo che ci sia esattamente un '?'
        if pattern.count("?") != 1:
            print("Errore: è ammesso un solo '?'.")
            return

        # Controllo che gli altri caratteri siano lettere
        for ch in pattern:
            if ch != "?" and not ch.isalpha():
                print("Errore: caratteri non validi.")
                return

        results = self.dictionary.translateWordWildCard(pattern)

        if not results:
            print("Nessuna parola trovata.")
        else:
            print("Parole trovate:")
            for alien, translations in results.items():
                print(f"{alien} -> {', '.join(translations)}")

    def printDictionary(self):
        """
        Obiettivo:
        - Stampare tutto il contenuto del dizionario:
          ogni parola aliena con tutte le sue traduzioni.
        """
        if self.dictionary.isEmpty():
            print("Dizionario vuoto.")
            return

        print("\n--- DIZIONARIO COMPLETO ---")
        for alien, translations in self.dictionary.items():
            print(f"{alien} -> {', '.join(translations)}")