class Dictionary:
    def __init__(self):
        """
        Obiettivo:
        - Inizializzare la struttura dati che conterrà le parole aliene e le loro traduzioni.

        Scelta:
        - Uso un dizionario Python interno:
          {
              "alieno": ["trad1", "trad2"],
              "zorgo": ["ciao"]
          }
        - La chiave è la parola aliena (stringa in minuscolo).
        - Il valore è una LISTA di traduzioni (stringhe in minuscolo).
        """
        self._data = {}

    def addWord(self, alien, translations):
        """
        Obiettivo:
        - Aggiungere una parola aliena con una o più traduzioni.

        Parametri:
        - alien: stringa già validata e in minuscolo.
        - translations: lista di stringhe già validate e in minuscolo.

        Logica:
        - Se la parola aliena non esiste ancora, la creo con lista vuota.
        - Aggiungo ogni traduzione se non è già presente (evito duplicati).
        """
        if alien not in self._data:
            self._data[alien] = []

        for t in translations:
            if t not in self._data[alien]:
                self._data[alien].append(t)

    def translate(self, alien):
        """
        Obiettivo:
        - Restituire tutte le traduzioni associate a una parola aliena.

        Parametri:
        - alien: stringa in minuscolo.

        Ritorno:
        - Lista di traduzioni se la parola esiste.
        - None se la parola non è presente nel dizionario.
        """
        return self._data.get(alien, None)

    def translateWordWildCard(self, pattern):
        """
        Obiettivo:
        - Trovare tutte le parole aliene che matchano un pattern con un solo '?'.

        Parametri:
        - pattern: stringa in minuscolo, con esattamente un '?'.

        Logica:
        - Scorro tutte le parole aliene nel dizionario.
        - Confronto lunghezza: devono avere la stessa lunghezza del pattern.
        - Confronto carattere per carattere:
          - Se nel pattern c'è '?', accetto qualsiasi carattere.
          - Altrimenti i caratteri devono essere uguali.
        - Se tutti i caratteri matchano, aggiungo la parola ai risultati.

        Ritorno:
        - Dizionario {parola_aliena: [traduzioni]} per tutte le parole che matchano.
        """
        pattern = pattern.lower()
        results = {}

        for alien in self._data.keys():
            if len(alien) != len(pattern):
                continue

            ok = True
            for pc, ac in zip(pattern, alien):
                if pc == "?":
                    continue
                if pc != ac:
                    ok = False
                    break

            if ok:
                results[alien] = self._data[alien]

        return results

    def items(self):
        """
        Obiettivo:
        - Fornire un modo per iterare su tutte le coppie (parola_aliena, traduzioni).

        Ritorno:
        - self._data.items(), come un normale dizionario Python.
        """
        return self._data.items()

    def isEmpty(self):
        """
        Obiettivo:
        - Sapere se il dizionario è vuoto.

        Ritorno:
        - True se non ci sono parole, False altrimenti.
        """
        return len(self._data) == 0