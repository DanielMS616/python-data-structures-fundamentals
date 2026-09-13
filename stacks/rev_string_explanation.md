# `rev_string()` – String mit einem Stack umkehren

## Ziel der Übung

Ziel ist eine Funktion, die einen String mithilfe eines **Stacks** in umgekehrter Zeichenreihenfolge zurückgibt.

```python
rev_string("apple")
```

soll ergeben:

```text
elppa
```

Die allgemeinen Eigenschaften eines Stacks, das LIFO-Prinzip und typische Stack-Operationen sind in [`README.md`](README.md) zusammengefasst.

In dieser Erklärung liegt der Fokus deshalb auf der **konkreten algorithmischen Idee dieser Übung**: Ein Stack wird gezielt als Umkehrmechanismus verwendet.

---

## Quick Summary

| Aspekt | Ergebnis |
| --- | --- |
| Datenstruktur | Stack |
| Muster | Stack als Umkehrmechanismus |
| Laufzeit | `O(n)` |
| Zusatzspeicher | `O(n)` |
| Kernidee | LIFO gibt die Zeichen in umgekehrter Reihenfolge zurück |
| Python-spezifischer Punkt | Ergebnis über Liste + `"".join(...)` zusammensetzen |

---

## Relevante Implementierung

Der entscheidende Teil der aktuellen Lösung ist:

```python
def rev_string(my_str: str) -> str:
    stack = Stack()

    for character in my_str:
        stack.push(character)

    reversed_characters = []

    while not stack.is_empty():
        reversed_characters.append(stack.pop())

    return "".join(reversed_characters)
```

Die vollständige und aktuelle Implementierung befindet sich in [`rev_string.py`](rev_string.py).

---

## Schritt für Schritt

### 1. Zeichen auf den Stack legen

```python
for character in my_str:
    stack.push(character)
```

Bei:

```text
apple
```

werden die Zeichen in dieser Reihenfolge gespeichert:

```text
a
p
p
l
e
```

Gedanklich sieht der Stack danach so aus:

```text
Top
 ↓
[e]
[l]
[p]
[p]
[a]
```

Das zuletzt eingefügte Zeichen `e` liegt oben.

---

### 2. Zeichen wieder vom Stack entfernen

```python
while not stack.is_empty():
    reversed_characters.append(stack.pop())
```

Ein Stack arbeitet nach **LIFO**:

```text
Last In, First Out
```

Die Zeichen verlassen den Stack deshalb in dieser Reihenfolge:

```text
e
l
p
p
a
```

Die Ergebnisliste wird damit:

```python
["e", "l", "p", "p", "a"]
```

---

### 3. Zeichen wieder zu einem String verbinden

```python
return "".join(reversed_characters)
```

Aus:

```python
["e", "l", "p", "p", "a"]
```

wird:

```text
elppa
```

---

## Warum diese Lösung funktioniert

Die Lösung nutzt direkt die zentrale Eigenschaft eines Stacks.

Wird eine Reihenfolge vollständig auf einen Stack gelegt:

```text
a -> p -> p -> l -> e
```

liegt das zuletzt gelesene Element oben.

Beim anschließenden vollständigen Entfernen entsteht automatisch:

```text
e -> l -> p -> p -> a
```

Die Umkehrung entsteht also nicht durch eine zusätzliche Sortierung oder Indexberechnung, sondern unmittelbar durch das **LIFO-Verhalten** der verwendeten Datenstruktur.

---

## Warum eine Liste und `"".join(...)` verwendet werden

Eine frühere, ebenfalls funktionierende Variante könnte das Ergebnis direkt als String aufbauen:

```python
reversed_string = ""

while not stack.is_empty():
    reversed_string += stack.pop()
```

Für kleine Eingaben funktioniert das problemlos.

Python-Strings sind jedoch **immutable**. Beim wiederholten Anhängen kann deshalb immer wieder ein neuer String erzeugt und der bisherige Inhalt kopiert werden.

Die aktuelle Lösung sammelt die Zeichen zunächst in einer Liste:

```python
reversed_characters.append(stack.pop())
```

und verbindet sie anschließend einmal:

```python
"".join(reversed_characters)
```

Dadurch bleibt der Stack für die Umkehrung verantwortlich, während die Ergebnisbildung effizienter umgesetzt wird.

---

## Komplexität

Sei `n` die Anzahl der Zeichen im Eingabestring.

### Zeichen auf den Stack legen

```python
for character in my_str:
    stack.push(character)
```

Die Schleife läuft `n`-mal:

```text
O(n)
```

### Zeichen wieder entfernen

```python
while not stack.is_empty():
    reversed_characters.append(stack.pop())
```

Auch hier werden `n` Zeichen verarbeitet:

```text
O(n)
```

### Ergebnis verbinden

```python
"".join(reversed_characters)
```

Alle `n` Zeichen müssen erneut gelesen werden:

```text
O(n)
```

Damit ergibt sich insgesamt:

```text
O(n) + O(n) + O(n)
= O(n)
```

Konstante Faktoren werden in der Big-O-Notation ignoriert.

### Speicher

Zusätzlich zur Eingabe werden die Zeichen im Stack und in der Ergebnisliste gehalten.

Der zusätzliche Speicher wächst deshalb proportional zu `n`:

```text
O(n)
```

---

## Randfälle

### Leerer String

```python
rev_string("")
```

Es wird kein Zeichen auf den Stack gelegt. Die Schleife zum Entfernen läuft ebenfalls nicht.

Ergebnis:

```text
""
```

### String mit einem Zeichen

```python
rev_string("x")
```

Ein einzelnes Zeichen bleibt beim Umkehren unverändert:

```text
x
```

### Ziffern als Zeichen

```python
rev_string("1234567890")
```

liefert:

```text
0987654321
```

Die Eingabe ist dabei weiterhin ein **String**, keine Zahl.

---

## Fehlerfälle und Typvertrag

Die aktuelle Signatur lautet:

```python
def rev_string(my_str: str) -> str:
```

Damit wird der erwartete Typ bereits dokumentiert:

```text
str -> str
```

Type Hints erzwingen den Typ zur Laufzeit jedoch nicht automatisch.

Ein Aufruf wie:

```python
rev_string(123)
```

entspricht nicht dem vorgesehenen Vertrag und würde beim Iterieren über die Eingabe scheitern.

Für diese Lernübung ist eine zusätzliche Laufzeitprüfung nicht notwendig. In einer größeren öffentlichen API könnte man den Typ bei Bedarf explizit validieren und eine gezielte Exception auslösen.

---

## Warum nicht einfach Python-Slicing?

Python kann einen String sehr kompakt umkehren:

```python
my_str[::-1]
```

Für ein kleines produktives Skript wäre das häufig die einfachste Lösung.

Hier würde Slicing jedoch das eigentliche Lernziel umgehen.

Die Übung soll zeigen, wie sich das Verhalten einer Datenstruktur gezielt für ein Problem einsetzen lässt:

```text
Stack
+
LIFO
=
Reihenfolge umkehren
```

Deshalb wird bewusst ein Stack verwendet.

---

## Tests

Der ursprüngliche Lernfall prüft unter anderem:

```python
rev_string("apple")
```

Erwartet:

```text
elppa
```

Weitere manuelle Beispiele waren:

```python
rev_string("x")
rev_string("1234567890")
```

Die Implementierung wird inzwischen zusätzlich automatisiert mit `pytest` geprüft:

[`../tests/test_stacks.py`](../tests/test_stacks.py)

Dort werden unter anderem normale Eingaben und der leere String als Randfall getestet.

---

## Design- und Skalierungsgedanke

Diese Übung zeigt zwei unterschiedliche Ebenen einer Lösung:

### Algorithmische Ebene

Der Stack bestimmt die Reihenfolge der Ausgabe.

```text
LIFO -> Umkehrung
```

### Implementierungsebene

Die Ergebniszeichen werden nicht durch wiederholte String-Konkatenation aufgebaut, sondern zunächst gesammelt und anschließend mit `"".join(...)` verbunden.

Damit werden zwei Fragen getrennt beantwortet:

```text
Welche Datenstruktur löst das eigentliche Problem?
→ Stack

Wie setze ich das Ergebnis in Python sinnvoll zusammen?
→ Liste + join()
```

Diese Trennung zwischen **algorithmischer Idee** und **sprachspezifischer Implementierungsentscheidung** ist auch bei größeren Problemen wichtig.

---

## Zentrale Lernidee

Die zentrale Erkenntnis dieser Übung ist:

> **Ein Stack kann eine Reihenfolge umkehren, weil das zuletzt eingefügte Element zuerst wieder entfernt wird.**

Die Funktion durchläuft den String einmal beim Einfügen und einmal beim Entfernen der Zeichen. Dadurch bleibt die Laufzeit linear:

```text
O(n)
```

Die Übung ist damit ein sehr direktes Beispiel dafür, wie die Eigenschaften einer Datenstruktur die Struktur eines Algorithmus bestimmen.

---

## Weiterführend

- [`README.md`](README.md) – Stack, LIFO und grundlegende Operationen
- [`../docs/data_structure_patterns.md`](../docs/data_structure_patterns.md) – Stack als wiederkehrendes Problemlösungsmuster
- [`../docs/big_o_cheatsheet.md`](../docs/big_o_cheatsheet.md) – Analyse von Zeit- und Speicherkomplexität
- [`../tests/test_stacks.py`](../tests/test_stacks.py) – automatisierte Tests
