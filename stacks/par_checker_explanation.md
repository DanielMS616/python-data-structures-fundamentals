# `par_checker()` – Ausgeglichene Klammern mit einem Stack prüfen

## Ziel der Übung

Ziel ist ein Algorithmus, der eine Folge runder Klammern von links nach rechts auswertet und erkennt, ob Öffnen und Schließen korrekt ausgeglichen sind.

Die Funktion

```python
par_checker(symbol_string)
```

soll

```python
True
```

zurückgeben, wenn jede öffnende Klammer `(` eine passende schließende Klammer `)` besitzt und die Reihenfolge korrekt ist.

Andernfalls soll die Funktion

```python
False
```

zurückgeben.

Beispiele:

```text
((()))      -> True
((()()))    -> True
(()         -> False
)(          -> False
```

---

## Implementierung

```python
from pythonds3.basic import Stack


def par_checker(symbol_string):
    stack = Stack()

    # Opening parentheses wait on the stack for a matching closing one.
    for symbol in symbol_string:
        if symbol == "(":
            stack.push(symbol)

        elif symbol == ")":
            # A closing parenthesis without an opener makes the string invalid.
            if stack.is_empty():
                return False

            stack.pop()

    # Balanced only if no unmatched opening parentheses remain.
    return stack.is_empty()


# Test
print("The code should pass the following tests:")
print(f"((())): {par_checker('((()))')}")
print(f"((()())): {par_checker('((()()))')}")
print(f"((): {par_checker('(()')}")
print(f")(: {par_checker(')(')}")
```

Erwartete Ausgabe:

```text
((())): True
((()())): True
((): False
)(: False
```

---

## 1. Was bedeutet „ausgeglichene Klammern“?

Eine Klammerkette ist ausgeglichen, wenn zwei Bedingungen erfüllt sind:

1. Jede schließende Klammer `)` besitzt vorher eine passende öffnende Klammer `(`.
2. Am Ende bleibt keine öffnende Klammer übrig.

Beispiel:

```text
((()))
```

Hier kann jede schließende Klammer einer zuvor geöffneten Klammer zugeordnet werden.

Dagegen:

```text
(()
```

ist nicht ausgeglichen, weil am Ende noch eine öffnende Klammer übrig bleibt.

Auch:

```text
)(
```

ist nicht ausgeglichen.

Obwohl insgesamt eine öffnende und eine schließende Klammer vorhanden sind, kommt die schließende Klammer **zu früh**.

Die Reihenfolge ist also genauso wichtig wie die Anzahl.

---

## 2. Warum eignet sich ein Stack?

Ein Stack arbeitet nach dem Prinzip:

> **LIFO – Last In, First Out**

Das zuletzt eingefügte Element wird zuerst wieder entfernt.

Bei verschachtelten Klammern passt genau dieses Verhalten.

Beispiel:

```text
((()))
```

Die drei öffnenden Klammern werden nacheinander auf den Stack gelegt:

```text
oben
 ↓
[(]
[(]
[(]
```

Sobald eine schließende Klammer `)` erscheint, wird die zuletzt geöffnete Klammer wieder vom Stack entfernt.

Damit behandelt der Stack automatisch die innerste offene Klammer zuerst.

---

## 3. Schritt für Schritt durch den Code

### Stack erzeugen

```python
stack = Stack()
```

Zu Beginn ist noch keine öffnende Klammer vorhanden.

Der Stack ist deshalb leer.

---

### String von links nach rechts lesen

```python
for symbol in symbol_string:
```

Der Algorithmus betrachtet jedes Zeichen genau einmal.

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

## 4. Öffnende Klammer

```python
if symbol == "(":
    stack.push(symbol)
```

Jede öffnende Klammer wird auf den Stack gelegt.

Sie wartet dort auf eine passende schließende Klammer.

Beispiel:

```text
((
```

führt zu:

```text
Stack:

oben
 ↓
[(]
[(]
```

Es gibt also zwei noch nicht geschlossene Klammern.

---

## 5. Schließende Klammer

Bei:

```python
elif symbol == ")":
```

muss geprüft werden, ob überhaupt eine passende öffnende Klammer vorhanden ist.

### Fehlerfall: Stack ist leer

```python
if stack.is_empty():
    return False
```

Angenommen, der String beginnt mit:

```text
)
```

Dann wurde vorher keine öffnende Klammer gespeichert.

Die schließende Klammer kann also zu nichts gehören.

Der String ist sofort ungültig.

Deshalb können wir direkt:

```python
return False
```

ausführen.

Wir müssen den restlichen String nicht mehr prüfen.

---

## 6. Passende öffnende Klammer entfernen

Wenn der Stack nicht leer ist:

```python
stack.pop()
```

wird die zuletzt gespeicherte öffnende Klammer entfernt.

Beispiel:

Vorher:

```text
Stack:

oben
 ↓
[(]
[(]
```

Eine `)` wird gelesen.

Danach:

```text
Stack:

oben
 ↓
[(]
```

Eine offene Klammer wurde erfolgreich geschlossen.

---

## 7. Warum reicht am Ende `stack.is_empty()`?

Nach dem Durchlaufen des gesamten Strings gibt es zwei Möglichkeiten.

### Stack ist leer

```text
[]
```

Dann wurde jede öffnende Klammer wieder geschlossen.

Die Klammern sind ausgeglichen:

```python
return True
```

### Stack enthält noch Elemente

Zum Beispiel bei:

```text
(()
```

bleibt eine öffnende Klammer übrig:

```text
Stack:

[(]
```

Dann fehlt eine schließende Klammer.

Deshalb:

```python
return False
```

Genau beides können wir kompakt ausdrücken mit:

```python
return stack.is_empty()
```

Ist der Stack leer, liefert die Methode `True`.

Ist er nicht leer, liefert sie `False`.

---

## 8. Beispiel `((()))`

Wir verfolgen den Zustand des Stacks:

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

Am Ende:

```text
stack.is_empty() == True
```

Ergebnis:

```text
True
```

---

## 9. Beispiel `(()`

```text
Zeichen    Aktion     Stack
---------------------------
(          push       (
(          push       ((
)          pop        (
```

Am Ende befindet sich noch eine öffnende Klammer auf dem Stack.

Ergebnis:

```text
False
```

---

## 10. Beispiel `)(`

Dieses Beispiel zeigt, warum es nicht reicht, nur die Anzahl der Klammern zu vergleichen.

Die erste Klammer ist:

```text
)
```

Der Stack ist aber noch leer.

Es gibt also keine passende öffnende Klammer.

Der Algorithmus beendet sich sofort mit:

```python
False
```

Ob später noch eine `(` kommt, spielt keine Rolle mehr.

Die Reihenfolge war bereits ungültig.

---

## 11. Laufzeitkomplexität

Sei `n` die Anzahl der Zeichen im String.

Der Algorithmus läuft einmal durch den String:

```python
for symbol in symbol_string:
```

Jedes Zeichen wird höchstens einmal betrachtet.

Die Stack-Operationen

```python
push()
pop()
is_empty()
```

werden jeweils als konstante Operationen betrachtet:

```text
O(1)
```

Damit ergibt sich insgesamt:

```text
O(n)
```

Die Laufzeit wächst also linear mit der Länge der Eingabe.

---

## 12. Speicherkomplexität

Im ungünstigsten Fall besteht der gesamte String nur aus öffnenden Klammern:

```text
(((((((((
```

Dann werden alle `n` Zeichen auf dem Stack gespeichert.

Der zusätzliche Speicherbedarf beträgt deshalb im Worst Case:

```text
O(n)
```

---

## 13. Fehlerfälle und Robustheit

Die Funktion behandelt zwei wichtige logische Fehlerfälle bereits korrekt:

### Zu viele schließende Klammern

Beispiel:

```text
())
```

Sobald eine `)` erscheint, obwohl der Stack leer ist:

```python
return False
```

### Zu viele öffnende Klammern

Beispiel:

```text
((()
```

Am Ende ist der Stack nicht leer:

```python
return stack.is_empty()
```

liefert:

```text
False
```

---

## 14. Was passiert mit anderen Zeichen?

Der aktuelle Code reagiert nur auf:

```text
(
)
```

Andere Zeichen werden ignoriert.

Zum Beispiel:

```python
par_checker("(a+b)")
```

würde ebenfalls:

```text
True
```

zurückgeben.

Für die Aufgabenstellung ist das unproblematisch, wenn tatsächlich nur eine Klammerkette erwartet wird.

In einer produktiveren Variante müsste man bewusst entscheiden:

- Sollen andere Zeichen erlaubt sein?
- Sollen sie ignoriert werden?
- Oder soll bei unerwarteten Zeichen ein Fehler ausgelöst werden?

Das ist ein gutes Beispiel dafür, dass **Eingabevalidierung eine Designentscheidung** ist.

---

## 15. Kleine Korrektur im Testcode

Beim letzten Test muss die f-String-Syntax korrekt geschlossen werden.

Richtig ist:

```python
print(f")(: {par_checker(')(')}")
```

Damit wird der String `")("` an `par_checker()` übergeben.

---

## 16. Warum nicht einfach die Anzahl vergleichen?

Eine naive Idee wäre:

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

Die Anzahl ist gleich, trotzdem ist die Reihenfolge ungültig.

Deshalb brauchen wir eine Datenstruktur, die den **aktuellen Zustand während des Lesens** speichert.

Der Stack ist dafür ideal.

---

## 17. Zentrale Lernidee

Die Aufgabe zeigt sehr schön, wofür ein Stack praktisch eingesetzt werden kann.

Bei verschachtelten Strukturen gilt häufig:

> Das zuletzt geöffnete Element muss zuerst wieder geschlossen werden.

Genau das entspricht:

```text
LIFO
Last In, First Out
```

Dieses Prinzip begegnet später unter anderem bei:

- Klammerprüfung
- HTML- und XML-Strukturen
- Parsern
- mathematischen Ausdrücken
- Funktionsaufrufen
- Undo-Funktionen
- Backtracking

---

## Zusammenfassung

Der Algorithmus liest die Klammerkette von links nach rechts.

Bei einer öffnenden Klammer:

```python
stack.push("(")
```

Bei einer schließenden Klammer:

1. prüfen wir, ob überhaupt eine offene Klammer vorhanden ist,
2. entfernen wir diese mit `pop()`.

Am Ende gilt:

```python
return stack.is_empty()
```

Nur wenn keine offene Klammer übrig geblieben ist, ist die Klammerkette ausgeglichen.

Die Laufzeit beträgt:

```text
O(n)
```

und der zusätzliche Speicherbedarf im Worst Case:

```text
O(n)
```

Die wichtigste Erkenntnis lautet:

> **Ein Stack eignet sich für verschachtelte Strukturen, weil das zuletzt geöffnete Element zuerst wieder geschlossen werden muss.**
