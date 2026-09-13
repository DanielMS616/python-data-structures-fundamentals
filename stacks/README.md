# Stack

## Überblick

Ein **Stack (Stapel)** ist ein abstrakter Datentyp, bei dem Elemente an derselben Seite hinzugefügt und entfernt werden.

Die entscheidende Regel lautet:

```text
LIFO
Last In, First Out
```

Das zuletzt eingefügte Element wird zuerst wieder entfernt.

---

## Vorstellung: Tellerstapel

```text
Top
 ↓
[C]
[B]
[A]
```

Wird jetzt ein Element entfernt, kommt zuerst:

```text
C
```

Danach:

```text
B
```

und zuletzt:

```text
A
```

---

## Zentrale Operationen

| Operation | Bedeutung |
| --- | --- |
| `Stack()` | neuen leeren Stack erzeugen |
| `push(item)` | Element oben hinzufügen |
| `pop()` | oberstes Element entfernen und zurückgeben |
| `peek()` | oberstes Element ansehen, ohne es zu entfernen |
| `is_empty()` | prüfen, ob der Stack leer ist |
| `size()` | Anzahl der Elemente |

---

## Einfache Python-Idee

Ein Stack kann mit einer Python-Liste umgesetzt werden:

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    def size(self):
        return len(self.items)
```

---

## Warum das Listenende als `Top` sinnvoll ist

Mit:

```python
self.items.append(item)
```

und:

```python
self.items.pop()
```

arbeiten wir am Listenende.

Typische Laufzeiten:

```text
push -> amortisiert O(1)
pop  -> O(1)
```

Würde man das Stack-Top dagegen an Index `0` legen:

```python
items.insert(0, item)
items.pop(0)
```

müssten Elemente verschoben werden:

```text
O(n)
```

Die logische Stack-Regel wäre gleich, die Implementierung aber ungünstiger.

---

## `pythonds3`

Die Übungen dieses Repositories verwenden teilweise:

```python
from pythonds3.basic import Stack
```

Installation:

Install the repository's runtime dependencies from the project root:

```bash
python3 -m pip install -r requirements.txt
```

Damit liegt der Fokus in den Übungen auf dem Algorithmus und nicht jedes Mal auf einer neuen Stack-Implementierung.

---

## Typische Einsatzfälle

Stacks sind sinnvoll, wenn das zuletzt bearbeitete Element als Nächstes wieder benötigt wird.

Beispiele:

```text
Undo / Rückgängig
Browser-Zurück-Navigation
Funktionsaufrufe / Call Stack
Backtracking
Klammerprüfung
Ausdrucksauswertung
Reihenfolgen umkehren
```

---

## Muster 1: Reihenfolge umkehren

Eingabe:

```text
a b c d
```

Auf Stack:

```text
Top
 ↓
[d]
[c]
[b]
[a]
```

`pop()` liefert:

```text
d c b a
```

Genau dieses Muster verwendet:

- [`rev_string.py`](rev_string.py)
- [`../queues/reversable_queue.py`](../queues/reversable_queue.py)

---

## Muster 2: Verschachtelte Strukturen

Bei:

```text
{ [ ( ) ] }
```

wird zuletzt:

```text
(
```

geöffnet.

Darum muss zuerst:

```text
)
```

geschlossen werden.

Das passt exakt zu LIFO.

---

## Einfache Klammerprüfung

```python
for symbol in symbol_string:
    if symbol == "(":
        stack.push(symbol)

    elif symbol == ")":
        if stack.is_empty():
            return False

        stack.pop()

return stack.is_empty()
```

Zwei unterschiedliche Fehlerarten werden erkannt:

```text
")("
→ Schließer erscheint ohne Öffner.

"(()"
→ Öffner bleibt am Ende übrig.
```

---

## Mehrere Symboltypen

Bei:

```text
()
[]
{}
```

reicht es nicht nur zu zählen.

Beispiel:

```text
([)]
```

Die Anzahl der einzelnen Klammern passt, aber die Verschachtelung ist falsch.

Darum muss der aktuelle Schließer zum **obersten Stack-Element** passen:

```python
matching_symbols = {
    ")": "(",
    "]": "[",
    "}": "{",
}
```

und:

```python
if stack.pop() != matching_symbols[symbol]:
    return False
```

---

## Übungen in diesem Ordner

### String umkehren

- [`rev_string.py`](rev_string.py)
- [`rev_string_explanation.md`](rev_string_explanation.md)

Lernidee:

```text
LIFO als Umkehrmechanismus
```

### Einfache Klammerprüfung

- [`par_checker.py`](par_checker.py)
- [`par_checker_explanation.md`](par_checker_explanation.md)

Lernidee:

```text
offene Zustände auf einem Stack speichern
Early Return bei ungültigem Schließer
```

### Mehrere Symboltypen

- [`balanced_symbols.py`](balanced_symbols.py)
- [`balanced_symbols_explanation.md`](balanced_symbols_explanation.md)

Lernidee:

```text
Stack + Dictionary
Verschachtelung statt bloßer Anzahl prüfen
```

---

## Typische Fehler

### Stack vor `pop()` nicht prüfen

```python
stack.pop()
```

auf einem leeren Stack kann fehlschlagen.

Bei Parser-ähnlichen Aufgaben deshalb vorher:

```python
if stack.is_empty():
    ...
```

---

### Nur zählen statt Reihenfolge berücksichtigen

```text
([)]
```

hat dieselbe Anzahl von Öffnern und Schließern.

Trotzdem ist die Struktur falsch.

---

### Ungünstiges Listenende verwenden

```python
insert(0, ...)
pop(0)
```

kann aus konstanten Stack-Operationen lineare Operationen machen.

---

## Laufzeitgedanke

Ein Stack ist besonders nützlich, wenn seine Hauptoperationen am günstigen Ende der zugrunde liegenden Struktur ausgeführt werden.

Für eine typische listenbasierte Implementierung:

| Operation | Typisch |
| --- | ---: |
| `push` | amortisiert `O(1)` |
| `pop` | `O(1)` |
| `peek` | `O(1)` |
| `is_empty` | `O(1)` |
| `size` | `O(1)` |

---

## Kurzreferenz

```text
Stack
-----
Prinzip: LIFO

push    -> hinzufügen
pop     -> entfernen
peek    -> ansehen
is_empty
size

Erkennungsfragen:
- Muss etwas rückwärts herauskommen?
- Muss das zuletzt Geöffnete zuerst geschlossen werden?
- Muss ich den zuletzt gespeicherten Zustand wiederherstellen?
```

Weiterführend:

- [`../docs/data_structure_patterns.md`](../docs/data_structure_patterns.md)
- [`../docs/big_o_cheatsheet.md`](../docs/big_o_cheatsheet.md)
