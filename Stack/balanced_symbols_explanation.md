# `balanced_symbols()` – Mehrere Klammerarten mit einem Stack prüfen

## Ziel der Übung

Die Funktion

```python
balanced_symbols(symbol_string)
```

soll mehrere Klammerarten verarbeiten und prüfen, ob sie vollständig sowie in der richtigen Verschachtelungsreihenfolge geschlossen werden.

Verwendet werden:

```text
( )
[ ]
{ }
```

Beispiele für korrekt ausgeglichene Symbolketten:

```text
{{([][])}()}
[[{{(())}}]]
[][][](){}
```

Beispiele für ungültige Symbolketten:

```text
([)]
((()]))
[{()]
```

Die Funktion soll:

```python
True
```

zurückgeben, wenn alle Symbole korrekt zusammenpassen, und:

```python
False
```

wenn eine Klammer fehlt, zu früh geschlossen wird oder der falsche Klammer-Typ verwendet wird.

---

## Implementierung

```python
from pythonds3.basic import Stack


def balanced_symbols(symbol_string):
    stack = Stack()

    # Map each closing symbol to its matching opening symbol.
    matching_symbols = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for symbol in symbol_string:
        if symbol in "([{":
            stack.push(symbol)

        elif symbol in ")]}":
            # A closing symbol without an opener is always invalid.
            if stack.is_empty():
                return False

            # The most recently opened symbol must match this closer.
            if stack.pop() != matching_symbols[symbol]:
                return False

    # Balanced only if no unmatched opening symbols remain.
    return stack.is_empty()


# Test
print("The code should pass the following tests:")
print(balanced_symbols(""))
print(balanced_symbols("[[()]]"))
print(balanced_symbols("[][][]()"))
print(balanced_symbols("([)]"))
print(balanced_symbols("((()])"))
print(balanced_symbols("[{(]"))
```

Erwartete Ergebnisse:

```text
True
True
True
False
False
False
```

---

# 1. Verbindung zur vorherigen Aufgabe

In der vorherigen Übung haben wir nur eine Klammerart geprüft:

```text
( )
```

Dort reichte es aus, jede öffnende Klammer auf einen Stack zu legen und bei jeder schließenden Klammer wieder eine zu entfernen.

Mit mehreren Klammerarten reicht das nicht mehr.

Bei:

```text
([)]
```

ist die Anzahl der öffnenden und schließenden Symbole zwar korrekt.

Trotzdem ist die Verschachtelung falsch.

Die innere eckige Klammer:

```text
[
```

müsste zuerst durch:

```text
]
```

geschlossen werden.

Stattdessen erscheint:

```text
)
```

Deshalb müssen wir jetzt zusätzlich prüfen, **welcher Typ von Symbol zuletzt geöffnet wurde**.

---

# 2. Warum eignet sich ein Stack besonders gut?

Ein Stack arbeitet nach:

> **LIFO – Last In, First Out**

Das zuletzt geöffnete Symbol muss bei korrekt verschachtelten Klammern auch zuerst wieder geschlossen werden.

Beispiel:

```text
{ [ ( ) ] }
```

Die öffnenden Symbole werden nacheinander gespeichert:

```text
{
[
(
```

Der Stack sieht dann gedanklich so aus:

```text
oben
 ↓
[(]
[[]
[{]
```

Als erstes muss nun:

```text
)
```

kommen, weil oben auf dem Stack:

```text
(
```

liegt.

Danach:

```text
]
```

für:

```text
[
```

und zuletzt:

```text
}
```

für:

```text
{
```

Genau dieses Verhalten bildet ein Stack automatisch ab.

---

# 3. Das Dictionary `matching_symbols`

Der wichtigste neue Teil gegenüber der einfachen Klammerprüfung ist:

```python
matching_symbols = {
    ")": "(",
    "]": "[",
    "}": "{",
}
```

Das Dictionary beantwortet die Frage:

> Welches öffnende Symbol gehört zu diesem schließenden Symbol?

Beispiele:

```python
matching_symbols[")"]
```

ergibt:

```text
(
```

und:

```python
matching_symbols["]"]
```

ergibt:

```text
[
```

Damit müssen wir keine lange Folge von einzelnen Vergleichen schreiben.

---

# 4. Öffnende Symbole speichern

```python
if symbol in "([{":
    stack.push(symbol)
```

Wenn das aktuelle Zeichen eines dieser Symbole ist:

```text
(
[
{
```

wird es auf den Stack gelegt.

Es wartet dort auf sein späteres schließendes Gegenstück.

---

# 5. Schließende Symbole behandeln

```python
elif symbol in ")]}":
```

Bei:

```text
)
]
}
```

müssen zwei Dinge geprüft werden.

---

## Prüfung 1: Gibt es überhaupt ein offenes Symbol?

```python
if stack.is_empty():
    return False
```

Beispiel:

```text
]
```

Der Stack ist leer.

Es wurde vorher keine:

```text
[
```

geöffnet.

Damit ist die Zeichenkette sofort ungültig.

Wir können direkt:

```python
False
```

zurückgeben.

---

## Prüfung 2: Ist es der richtige Symboltyp?

```python
if stack.pop() != matching_symbols[symbol]:
    return False
```

Hier passiert etwas Wichtiges.

`stack.pop()` liefert das **zuletzt geöffnete Symbol**.

`matching_symbols[symbol]` liefert das Symbol, das wir für den aktuellen Schließer erwarten.

Beispiel:

```text
([)]
```

Nach:

```text
(
[
```

liegt oben auf dem Stack:

```text
[
```

Jetzt erscheint:

```text
)
```

Das Dictionary sagt:

```python
matching_symbols[")"]
```

ergibt:

```text
(
```

Wir vergleichen also:

```text
[ != (
```

Das stimmt nicht.

Ergebnis:

```python
False
```

Genau dadurch erkennen wir falsche Verschachtelung.

---

# 6. Warum ist `([)]` ungültig?

Schritt für Schritt:

```text
Zeichen    Aktion                 Stack
--------------------------------------
(          push                   (
[          push                   ( [
)          erwartet (, findet [   Fehler
```

Ob später noch ein `]` erscheint, spielt keine Rolle.

Die Verschachtelung ist bereits ungültig.

---

# 7. Beispiel `[[()]]`

Schritt für Schritt:

```text
Zeichen    Aktion          Stack
--------------------------------
[          push            [
[          push            [ [
(          push            [ [ (
)          pop (           [ [
]          pop [           [
]          pop [           leer
```

Am Ende:

```python
stack.is_empty()
```

liefert:

```text
True
```

Die Zeichenkette ist korrekt ausgeglichen.

---

# 8. Warum prüfen wir am Ende noch den Stack?

Auch wenn während des Durchlaufens kein falscher Schließer gefunden wurde, können noch offene Symbole übrig bleiben.

Beispiel:

```text
[{(
```

Alle drei Zeichen sind gültige öffnende Symbole.

Aber keines wurde geschlossen.

Der Stack enthält am Ende noch:

```text
[
    "{",
    "[",
    "("
]
```

Deshalb:

```python
return stack.is_empty()
```

Wenn der Stack leer ist:

```text
True
```

Wenn noch offene Symbole übrig sind:

```text
False
```

---

# 9. Warum reicht bloßes Zählen nicht?

Eine naive Lösung könnte prüfen:

```text
Anzahl ( == Anzahl )
Anzahl [ == Anzahl ]
Anzahl { == Anzahl }
```

Das würde aber diesen Fehler nicht erkennen:

```text
([)]
```

Die Anzahl jeder Symbolart stimmt.

Trotzdem ist die Reihenfolge falsch.

Deshalb brauchen wir eine Datenstruktur, die zusätzlich speichert, **in welcher Reihenfolge die Symbole geöffnet wurden**.

Genau dafür ist der Stack geeignet.

---

# 10. Laufzeitkomplexität

Sei `n` die Anzahl der Zeichen in `symbol_string`.

Wir durchlaufen den String genau einmal:

```python
for symbol in symbol_string:
```

Jedes Zeichen wird einmal betrachtet.

Die Stack-Operationen:

```python
push()
pop()
is_empty()
```

werden als:

```text
O(1)
```

betrachtet.

Auch der Zugriff auf das Dictionary:

```python
matching_symbols[symbol]
```

ist im Durchschnitt:

```text
O(1)
```

Damit ergibt sich insgesamt:

```text
O(n)
```

---

# 11. Speicherkomplexität

Im Worst Case besteht der String nur aus öffnenden Symbolen:

```text
(([[{{
```

Dann landen alle `n` Symbole auf dem Stack.

Der zusätzliche Speicherbedarf beträgt deshalb:

```text
O(n)
```

---

# 12. Sonderfälle

## Leerer String

```python
balanced_symbols("")
```

Es wird kein Symbol verarbeitet.

Der Stack bleibt leer.

Damit:

```python
stack.is_empty()
```

ergibt:

```text
True
```

Ein leerer String gilt also als ausgeglichen.

---

## Nur ein öffnendes Symbol

```python
balanced_symbols("(")
```

Am Ende liegt noch:

```text
(
```

auf dem Stack.

Ergebnis:

```text
False
```

---

## Nur ein schließendes Symbol

```python
balanced_symbols("]")
```

Der Stack ist beim Auftreten des Symbols leer.

Ergebnis sofort:

```text
False
```

---

# 13. Was passiert mit anderen Zeichen?

Der aktuelle Algorithmus reagiert nur auf:

```text
( ) [ ] { }
```

Andere Zeichen werden ignoriert.

Zum Beispiel:

```python
balanced_symbols("result = [a + (b * c)]")
```

würde nur die darin enthaltenen Klammern prüfen.

Das kann für echten Programmcode sogar sinnvoll sein.

Für eine reine Symbolketten-Aufgabe könnte man alternativ verlangen, dass ausschließlich Klammerzeichen erlaubt sind.

Welche Variante korrekt ist, hängt von der gewünschten Schnittstelle ab.

Das ist eine typische **Eingabevalidierungs- und Designentscheidung**.

---

# 14. Warum das Dictionary eine gute Designentscheidung ist

Man könnte auch so programmieren:

```python
if symbol == ")" and opening_symbol != "(":
    return False
elif symbol == "]" and opening_symbol != "[":
    return False
elif symbol == "}" and opening_symbol != "{":
    return False
```

Das funktioniert.

Das Dictionary:

```python
matching_symbols = {
    ")": "(",
    "]": "[",
    "}": "{",
}
```

ist aber kompakter und leichter erweiterbar.

Wenn später eine weitere Symbolart hinzukäme, müsste hauptsächlich die Zuordnung ergänzt werden.

Die Regel:

```text
Schließer -> erwarteter Öffner
```

ist außerdem direkt in der Datenstruktur sichtbar.

---

# 15. Fehlerfälle und Robustheit

Der Algorithmus erkennt drei zentrale Fehlerarten:

### 1. Schließendes Symbol ohne Öffner

```text
]
```

Ergebnis:

```text
False
```

### 2. Falscher Symboltyp

```text
([)]
```

Ergebnis:

```text
False
```

### 3. Offene Symbole bleiben übrig

```text
[{(
```

Ergebnis:

```text
False
```

Damit sind die wesentlichen strukturellen Fehlerfälle der Aufgabe abgedeckt.

---

# 16. Skalierungs- und Designgedanke

Der Algorithmus ist effizient, weil der String nur einmal durchlaufen wird.

Wir müssen weder:

- Zeichen mehrfach suchen,
- Teilstrings erzeugen,
- noch immer wieder von vorne beginnen.

Bei doppelt so vielen Zeichen wächst die Arbeit ungefähr ebenfalls auf das Doppelte.

Das entspricht:

```text
O(n)
```

Der Stack speichert nur die Symbole, die noch auf ein passendes Gegenstück warten.

Damit ist die Datenstruktur direkt auf das Problem zugeschnitten.

---

# 17. Unterschied zur vorherigen Aufgabe

Bei `par_checker()` reichte:

```python
stack.pop()
```

weil es nur eine einzige Klammerart gab.

Hier müssen wir zusätzlich prüfen:

```python
stack.pop() == matching_symbols[symbol]
```

Das ist der entscheidende neue Schritt.

Wir prüfen jetzt nicht nur:

> Gibt es überhaupt eine offene Klammer?

sondern zusätzlich:

> Ist die zuletzt geöffnete Klammer genau diejenige, die jetzt geschlossen werden darf?

---

# Zusammenfassung

Die Funktion kombiniert zwei wichtige Werkzeuge:

## Stack

Speichert die Reihenfolge der offenen Symbole nach dem LIFO-Prinzip.

## Dictionary

Speichert die korrekten Symbolpaare:

```text
) -> (
] -> [
} -> {
```

Bei jedem schließenden Symbol prüfen wir:

1. Ist überhaupt ein offenes Symbol vorhanden?
2. Ist das zuletzt geöffnete Symbol vom richtigen Typ?

Am Ende darf nichts mehr auf dem Stack liegen.

Die Laufzeit beträgt:

```text
O(n)
```

und der zusätzliche Speicherbedarf im Worst Case:

```text
O(n)
```

Die zentrale Lernidee lautet:

> **Bei korrekt verschachtelten Symbolen muss immer das zuletzt geöffnete Symbol als Nächstes passend geschlossen werden – genau dieses Verhalten bildet ein Stack mit LIFO ab.**
