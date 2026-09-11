# `rev_string()` – String mit einem Stack umkehren

## Ziel der Übung

Ziel ist eine Funktion

```python
rev_string(my_str)
```

die einen String mithilfe eines **Stacks** in umgekehrter Zeichenreihenfolge zurückgibt.

Beispiel:

```python
rev_string("apple")
```

soll ergeben:

```text
elppa
```

Im Mittelpunkt steht dabei das **LIFO-Prinzip** eines Stacks:

> **Last In, First Out**

Das zuletzt eingefügte Element wird als Erstes wieder entfernt.

---

## Implementierung

```python
from pythonds3.basic import Stack


def rev_string(my_str):
    stack = Stack()

    # Store all characters on the stack.
    for character in my_str:
        stack.push(character)

    reversed_characters = []

    # LIFO returns the characters in reverse order.
    while not stack.is_empty():
        reversed_characters.append(stack.pop())

    return "".join(reversed_characters)


# Test
print("Test with 'apple', 'x', and '1234567890'")
print(f"apple: {rev_string('apple')}")
print(f"x: {rev_string('x')}")
print(f"1234567890: {rev_string('1234567890')}")
```

Erwartete Ausgabe:

```text
apple: elppa
x: x
1234567890: 0987654321
```

---

## 1. Wiederholung: Was ist ein Stack?

Ein Stack ist eine Datenstruktur, die man sich wie einen Stapel Teller vorstellen kann.

Neue Elemente werden oben auf den Stapel gelegt:

```python
stack.push(item)
```

Das oberste Element wird wieder heruntergenommen:

```python
stack.pop()
```

Dabei gilt:

```text
LIFO = Last In, First Out
```

Also:

> Was zuletzt hineingelegt wurde, kommt zuerst wieder heraus.

---

## 2. Warum eignet sich ein Stack zum Umkehren?

Nehmen wir den String:

```text
apple
```

Die Zeichen werden von links nach rechts auf den Stack gelegt:

```text
a
p
p
l
e
```

Nach allen `push()`-Operationen sieht der Stack gedanklich so aus:

```text
oben
 ↓
[e]
[l]
[p]
[p]
[a]
```

Das zuletzt eingefügte Zeichen `e` liegt oben.

Wenn wir nun immer wieder `pop()` aufrufen, erhalten wir:

```text
e
l
p
p
a
```

also:

```text
elppa
```

Der Stack dreht die Reihenfolge durch sein LIFO-Verhalten automatisch um.

---

## 3. Schritt für Schritt durch den Code

### Stack erzeugen

```python
stack = Stack()
```

Zuerst erzeugen wir einen leeren Stack.

### Alle Zeichen speichern

```python
for character in my_str:
    stack.push(character)
```

Eine Python-`for`-Schleife läuft Zeichen für Zeichen durch den String.

Bei:

```text
apple
```

werden nacheinander gespeichert:

```text
a
p
p
l
e
```

### Ergebnis vorbereiten

```python
reversed_characters = []
```

Hier sammeln wir die Zeichen, die wir wieder vom Stack herunternehmen.

Wir verwenden dafür eine Liste.

### Zeichen vom Stack entfernen

```python
while not stack.is_empty():
    reversed_characters.append(stack.pop())
```

Solange der Stack noch Elemente enthält, wird das oberste Element entfernt und an die Ergebnisliste angehängt.

Da der Stack nach LIFO arbeitet, kommen die Zeichen in umgekehrter Reihenfolge heraus.

### Liste wieder in einen String umwandeln

```python
return "".join(reversed_characters)
```

Nach dem Beispiel `"apple"` enthält die Liste:

```python
["e", "l", "p", "p", "a"]
```

Mit:

```python
"".join(...)
```

werden die einzelnen Zeichen wieder zu einem String:

```text
elppa
```

---

## 4. Warum wurde der ursprüngliche Code leicht verändert?

Die ursprüngliche Version hat das Ergebnis so aufgebaut:

```python
reversed_string = ""

while not stack.is_empty():
    reversed_string += stack.pop()
```

Das ist für eine kleine Übung funktional vollkommen korrekt und leicht verständlich.

Python-Strings sind allerdings **unveränderlich (immutable)**.

Bei:

```python
reversed_string += character
```

kann deshalb bei jedem Schritt ein neuer String erzeugt und der bisherige Inhalt kopiert werden.

Bei langen Strings kann das unnötig teuer werden.

Darum verwenden wir in der überarbeiteten Version:

```python
reversed_characters.append(...)
```

und am Ende:

```python
"".join(reversed_characters)
```

Das ist die üblichere und skalierbarere Python-Lösung.

Wichtig:

> Der Stack bleibt weiterhin die Datenstruktur, die die Reihenfolge umkehrt.

Die Liste dient nur dazu, das Ergebnis effizient zusammenzusetzen.

---

## 5. Laufzeitkomplexität

Sei `n` die Anzahl der Zeichen im String.

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

Auch diese Schleife läuft `n`-mal:

```text
O(n)
```

### Zeichen verbinden

```python
"".join(reversed_characters)
```

Auch das verarbeitet alle `n` Zeichen:

```text
O(n)
```

Insgesamt:

```text
O(n) + O(n) + O(n)
```

Konstante Faktoren werden bei Big-O ignoriert:

```text
O(n)
```

Die überarbeitete Funktion hat also insgesamt lineare Laufzeit.

---

## 6. Speicherkomplexität

Wir speichern die Zeichen zusätzlich im Stack und anschließend in der Ergebnisliste.

Beide wachsen proportional zur Eingabelänge.

Die zusätzliche Speicherkomplexität ist deshalb:

```text
O(n)
```

Das ist für diese Aufgabe erwartbar, weil ausdrücklich ein Stack verwendet werden soll.

---

## 7. Sonderfälle

### Leerer String

```python
rev_string("")
```

Es wird kein Zeichen auf den Stack gelegt.

Die `while`-Schleife läuft nicht und:

```python
"".join([])
```

ergibt:

```text
""
```

Die Funktion funktioniert also auch für einen leeren String.

### String mit nur einem Zeichen

```python
rev_string("x")
```

Ein einzelnes Zeichen bleibt beim Umkehren unverändert:

```text
x
```

### Zahlen als Zeichen

```python
rev_string("1234567890")
```

liefert:

```text
0987654321
```

Wichtig:

Die Eingabe ist hier ein **String**, keine Zahl.

---

## 8. Fehlerfälle und Robustheit

Die Aufgabenstellung erwartet einen String.

Wenn stattdessen zum Beispiel eine Zahl übergeben wird:

```python
rev_string(123)
```

kann die `for`-Schleife nicht wie vorgesehen über einzelne Zeichen laufen.

Für diese Schulaufgabe müssen wir deshalb nicht zwingend eine Typprüfung ergänzen.

In einer größeren Anwendung könnte man beispielsweise prüfen:

```python
if not isinstance(my_str, str):
    raise TypeError("my_str must be a string")
```

Für die aktuelle Übung wäre das jedoch eher zusätzliche Robustheit als Kernbestandteil der Aufgabe.

---

## 9. Warum nicht einfach Python-Slicing verwenden?

In Python könnte man einen String sehr einfach so umkehren:

```python
my_str[::-1]
```

Zum Beispiel:

```python
"apple"[::-1]
```

ergibt ebenfalls:

```text
elppa
```

Das wäre für ein echtes kleines Python-Programm vermutlich die einfachste Lösung.

Aber hier wäre es die falsche Lösung für das Lernziel.

Die Aufgabe soll ausdrücklich zeigen, wie ein **Stack und das LIFO-Prinzip** funktionieren.

Deshalb verwenden wir bewusst:

```python
Stack()
push()
pop()
```

---

## 10. Zentrale Lernidee

Diese Aufgabe demonstriert sehr direkt den Zusammenhang zwischen einer Datenstruktur und ihrem Verhalten.

Ein Stack arbeitet nach:

```text
Last In, First Out
```

Wenn Elemente in einer bestimmten Reihenfolge hineingelegt werden, kommen sie automatisch in umgekehrter Reihenfolge wieder heraus.

Deshalb eignet sich ein Stack unter anderem gut für:

- Umkehren von Reihenfolgen
- Undo-Funktionen
- Backtracking
- Auswertung von Klammern und Ausdrücken
- Verwaltung von Funktionsaufrufen

---

## Zusammenfassung

Die Funktion:

1. erzeugt einen leeren Stack,
2. legt jedes Zeichen des Strings auf den Stack,
3. entfernt anschließend alle Zeichen wieder,
4. nutzt dabei das LIFO-Prinzip,
5. und setzt die Zeichen wieder zu einem String zusammen.

Beispiel:

```text
apple
```

wird auf dem Stack zu:

```text
oben
 ↓
[e]
[l]
[p]
[p]
[a]
```

und beim Entfernen zu:

```text
elppa
```

Die wesentliche Erkenntnis lautet:

> **Ein Stack kann eine Reihenfolge umkehren, weil das zuletzt eingefügte Element zuerst wieder entfernt wird.**

Die überarbeitete Version verwendet zusätzlich eine Liste und `"".join(...)`, damit auch das Zusammensetzen langer Strings effizient bleibt.
