# `par_checker()` – Ausgeglichene Klammern mit einem Stack prüfen

## Ziel der Übung

Ziel ist eine Funktion, die eine Folge runder Klammern von links nach rechts auswertet und erkennt, ob Öffnen und Schließen korrekt ausgeglichen sind.

```python
par_checker("((()))")
```

soll:

```text
True
```

liefern, während beispielsweise:

```python
par_checker(")(")
```

zu:

```text
False
```

führen muss.

Die allgemeinen Eigenschaften eines Stacks, das LIFO-Prinzip und typische Stack-Operationen sind in [`README.md`](README.md) zusammengefasst.

Hier liegt der Fokus auf der **konkreten algorithmischen Idee dieser Übung**: Noch nicht geschlossene Klammern werden als offener Zustand auf dem Stack verwaltet.

---

## Quick Summary

| Aspekt | Ergebnis |
| --- | --- |
| Datenstruktur | Stack |
| Muster | Stack für offene Zustände |
| Laufzeit | `O(n)` |
| Zusatzspeicher | Worst Case `O(n)` |
| Kernidee | Jeder Schließer benötigt eine zuvor gespeicherte öffnende Klammer |
| Wichtiger Fehlerfall | Eine schließende Klammer darf niemals erscheinen, wenn der Stack leer ist |

---

## Relevante Implementierung

Der entscheidende Teil der aktuellen Lösung ist:

```python
def par_checker(symbol_string: str) -> bool:
    stack = Stack()

    for symbol in symbol_string:
        if symbol == "(":
            stack.push(symbol)

        elif symbol == ")":
            if stack.is_empty():
                return False

            stack.pop()

    return stack.is_empty()
```

Die vollständige und aktuelle Implementierung befindet sich in [`par_checker.py`](par_checker.py).

---

## Was bedeutet „ausgeglichen“?

Für diese Aufgabe müssen zwei Bedingungen gleichzeitig erfüllt sein:

1. Jede schließende Klammer `)` benötigt eine zuvor geöffnete Klammer `(`.
2. Nach dem vollständigen Durchlaufen darf keine öffnende Klammer übrig bleiben.

Beispiel:

```text
((()))
```

ist gültig.

Dagegen ist:

```text
(()
```

ungültig, weil am Ende noch eine öffnende Klammer übrig bleibt.

Auch:

```text
)(
```

ist ungültig.

Obwohl beide Klammerarten genau einmal vorkommen, erscheint die schließende Klammer **zu früh**.

Damit ist klar:

> Nicht nur die Anzahl der Klammern ist relevant, sondern auch ihre Reihenfolge.

---

## Schritt für Schritt

### 1. Leeren Stack erzeugen

```python
stack = Stack()
```

Zu Beginn gibt es noch keine ungepaarte öffnende Klammer.

Der Stack ist deshalb leer.

---

### 2. Eingabe von links nach rechts lesen

```python
for symbol in symbol_string:
```

Jedes Zeichen wird genau einmal betrachtet.

Bei:

```text
(())
```

werden nacheinander gelesen:

```text
(
(
)
)
```

---

### 3. Öffnende Klammern speichern

```python
if symbol == "(":
    stack.push(symbol)
```

Jede `(` wird auf den Stack gelegt.

Sie repräsentiert eine Klammer, die noch auf ihr passendes `)` wartet.

Nach:

```text
((
```

sieht der Stack gedanklich so aus:

```text
Top
 ↓
[(]
[(]
```

Es existieren also zwei noch nicht geschlossene Klammern.

---

### 4. Schließende Klammern verarbeiten

```python
elif symbol == ")":
```

Bei einer schließenden Klammer muss zunächst geprüft werden, ob überhaupt eine offene Klammer vorhanden ist.

```python
if stack.is_empty():
    return False
```

Beginnt die Eingabe zum Beispiel mit:

```text
)
```

ist der Stack leer.

Es existiert keine passende `(`.

Der Ausdruck ist damit sofort ungültig.

---

### 5. Passende offene Klammer entfernen

Wenn der Stack nicht leer ist:

```python
stack.pop()
```

wird die zuletzt gespeicherte öffnende Klammer entfernt.

Bei nur einer Klammerart reicht das aus: Jede gespeicherte Klammer ist automatisch eine `(`.

---

### 6. Am Ende auf verbleibende Öffner prüfen

Nach dem vollständigen Durchlauf:

```python
return stack.is_empty()
```

Sind keine Elemente mehr vorhanden:

```text
True
```

Dann wurde jede öffnende Klammer geschlossen.

Bleibt mindestens eine `(` auf dem Stack:

```text
False
```

Dann fehlt mindestens eine schließende Klammer.

---

## Warum diese Lösung funktioniert

Der Stack repräsentiert zu jedem Zeitpunkt genau die **noch nicht geschlossenen öffnenden Klammern**.

Das ist die zentrale Invariante des Algorithmus.

Während des Durchlaufs gilt:

```text
Stack-Inhalt
=
alle bisher geöffneten, aber noch nicht geschlossenen Klammern
```

Eine `(` erweitert diesen Zustand:

```python
stack.push("(")
```

Eine `)` reduziert ihn:

```python
stack.pop()
```

Eine schließende Klammer bei leerem Stack verletzt die Invariante sofort:

```python
if stack.is_empty():
    return False
```

Und ein nicht leerer Stack am Ende zeigt, dass noch offene Zustände übrig sind.

---

## Beispiel: `((()))`

```text
Zeichen    Aktion     Stack
---------------------------
(          push       (
(          push       ((
(          push       (((
)          pop        ((
)          pop        (
)          pop        leer
```

Am Ende gilt:

```text
stack.is_empty() == True
```

Ergebnis:

```text
True
```

---

## Beispiel: `(()`

```text
Zeichen    Aktion     Stack
---------------------------
(          push       (
(          push       ((
)          pop        (
```

Am Ende bleibt eine öffnende Klammer übrig.

Ergebnis:

```text
False
```

---

## Beispiel: `)(`

Dieses Beispiel zeigt besonders deutlich, warum die Reihenfolge entscheidend ist.

Das erste Zeichen ist:

```text
)
```

Der Stack ist zu diesem Zeitpunkt leer.

Der Algorithmus kann deshalb sofort:

```python
return False
```

ausführen.

Dass später noch eine `(` erscheint, kann den bereits entstandenen Strukturfehler nicht mehr reparieren.

Das ist zugleich ein Beispiel für einen sinnvollen **Early Return**.

---

## Warum bloßes Zählen nicht reicht

Eine naheliegende Idee wäre:

```python
symbol_string.count("(") == symbol_string.count(")")
```

Für:

```text
()
```

würde das funktionieren.

Aber auch:

```text
)(
```

enthält genau eine öffnende und eine schließende Klammer.

Die Mengen stimmen, die Struktur aber nicht.

Der Stack speichert deshalb nicht nur **wie viele** Klammern offen sind, sondern hält den Zustand während des Lesens fest.

---

## Komplexität

Sei `n` die Länge von `symbol_string`.

### Laufzeit

Der String wird genau einmal durchlaufen:

```python
for symbol in symbol_string:
```

Die relevanten Stack-Operationen:

```text
push()
pop()
is_empty()
```

werden bei der verwendeten Stack-Implementierung als konstante Operationen betrachtet:

```text
O(1)
```

Damit ergibt sich insgesamt:

```text
O(n)
```

### Speicher

Im Worst Case besteht die Eingabe ausschließlich aus öffnenden Klammern:

```text
(((((((((
```

Dann werden bis zu `n` Elemente auf dem Stack gespeichert.

Der zusätzliche Speicherbedarf beträgt deshalb:

```text
O(n)
```

---

## Rand- und Fehlerfälle

### Leerer String

```python
par_checker("")
```

Es wird nichts auf den Stack gelegt.

Am Ende ist der Stack leer:

```text
True
```

Ein leerer Ausdruck gilt damit als ausgeglichen.

---

### Zu viele schließende Klammern

Beispiel:

```text
())
```

Sobald ein `)` erscheint, obwohl kein Öffner mehr vorhanden ist:

```python
if stack.is_empty():
    return False
```

wird die Eingabe sofort abgelehnt.

---

### Zu viele öffnende Klammern

Beispiel:

```text
((()
```

Der Durchlauf selbst verursacht keinen unmittelbaren Fehler.

Am Ende bleibt jedoch mindestens eine `(` auf dem Stack:

```python
return stack.is_empty()
```

liefert:

```text
False
```

---

## Andere Zeichen und Eingabevalidierung

Der aktuelle Algorithmus reagiert nur auf:

```text
(
)
```

Andere Zeichen werden ignoriert.

Zum Beispiel:

```python
par_checker("(a+b)")
```

prüft nur die enthaltenen Klammern und liefert:

```text
True
```

Ob dieses Verhalten gewünscht ist, hängt von der Schnittstelle ab.

Mögliche Varianten wären:

```text
andere Zeichen ignorieren
nur reine Klammerketten erlauben
bei unerwarteten Zeichen einen Fehler auslösen
```

Für diese Übung ist das Ignorieren anderer Zeichen ausreichend. In einer größeren Anwendung wäre es eine bewusste **Input-Validation-Entscheidung**.

---

## Typvertrag

Die aktuelle Signatur lautet:

```python
def par_checker(symbol_string: str) -> bool:
```

Damit wird dokumentiert:

```text
str -> bool
```

Type Hints machen die erwartete Schnittstelle sichtbar, erzwingen sie zur Laufzeit aber nicht automatisch.

Eine zusätzliche Laufzeitvalidierung wäre für diese Lernübung nicht notwendig.

---

## Tests

Zu den ursprünglichen Lernfällen gehören:

```text
((()))      -> True
((()()))    -> True
(()         -> False
)(          -> False
```

Die Implementierung wird inzwischen zusätzlich automatisiert mit `pytest` geprüft:

[`../tests/test_stacks.py`](../tests/test_stacks.py)

Die Tests decken unter anderem ab:

```text
korrekt verschachtelte Klammern
zu frühe schließende Klammer
übrig bleibende öffnende Klammer
```

---

## Design- und Skalierungsgedanke

Der Algorithmus ist bereits gut auf das Problem zugeschnitten:

```text
ein Durchlauf
+
konstante Stack-Operationen
=
O(n)
```

Es ist keine wiederholte Suche im bereits gelesenen Teil der Eingabe notwendig.

Die Datenstruktur speichert nur den Zustand, der für die zukünftige Entscheidung noch relevant ist:

```text
Welche öffnenden Klammern warten noch auf einen Schließer?
```

Dieses Muster erscheint später auch in komplexeren Parsern und bei anderen verschachtelten Strukturen.

---

## Abgrenzung zur nächsten Übung

Bei `par_checker()` existiert nur eine Symbolart:

```text
( )
```

Deshalb genügt beim Schließen:

```python
stack.pop()
```

Sobald mehrere Symboltypen unterstützt werden, reicht diese Information nicht mehr aus.

Dann muss zusätzlich geprüft werden:

> Passt der aktuelle Schließer zum zuletzt gespeicherten Öffner?

Genau diese Erweiterung behandelt [`balanced_symbols_explanation.md`](balanced_symbols_explanation.md).

---

## Zentrale Lernidee

Die zentrale Erkenntnis lautet:

> **Ein Stack eignet sich für verschachtelte Strukturen, weil das zuletzt geöffnete Element zuerst wieder geschlossen werden muss.**

Der Stack hält während des gesamten Durchlaufs den noch offenen Zustand fest.

Dadurch können sowohl eine falsche Reihenfolge als auch übrig gebliebene Öffner in linearer Zeit erkannt werden.

---

## Weiterführend

- [`README.md`](README.md) – Stack, LIFO und grundlegende Operationen
- [`balanced_symbols_explanation.md`](balanced_symbols_explanation.md) – Erweiterung auf mehrere Symboltypen
- [`../docs/data_structure_patterns.md`](../docs/data_structure_patterns.md) – Stack für verschachtelte Strukturen und Early Return
- [`../docs/big_o_cheatsheet.md`](../docs/big_o_cheatsheet.md) – Analyse von Zeit- und Speicherkomplexität
- [`../tests/test_stacks.py`](../tests/test_stacks.py) – automatisierte Tests
