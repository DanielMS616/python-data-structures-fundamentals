# `balanced_symbols()` – Mehrere Klammerarten mit einem Stack prüfen

## Ziel der Übung

Die Funktion soll mehrere Klammerarten verarbeiten und prüfen, ob sie vollständig und in der richtigen Reihenfolge verschachtelt sind.

Unterstützt werden:

```text
( )
[ ]
{ }
```

Beispiele:

```text
[[()]]      -> True
[][][]()    -> True
([)]        -> False
((()])      -> False
```

Die allgemeinen Eigenschaften eines Stacks und das LIFO-Prinzip sind in [`README.md`](README.md) zusammengefasst.

Diese Erklärung konzentriert sich auf die **Erweiterung gegenüber der einfachen Klammerprüfung**: Jetzt muss nicht nur erkannt werden, ob ein Öffner existiert, sondern auch, ob er zum aktuellen Schließer gehört.

---

## Quick Summary

| Aspekt | Ergebnis |
| --- | --- |
| Datenstruktur | Stack + Dictionary |
| Muster | Stack für Verschachtelung + Lookup-Tabelle |
| Laufzeit | `O(n)` |
| Zusatzspeicher | Worst Case `O(n)` |
| Kernidee | Der aktuelle Schließer muss zum zuletzt geöffneten Symbol passen |
| Wichtiges Beispiel | `([)]` ist trotz korrekter Anzahl ungültig |

---

## Relevante Implementierung

Der entscheidende Teil der aktuellen Lösung ist:

```python
def balanced_symbols(symbol_string: str) -> bool:
    stack = Stack()

    matching_symbols = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for symbol in symbol_string:
        if symbol in "([{":
            stack.push(symbol)

        elif symbol in ")]}":
            if stack.is_empty():
                return False

            if stack.pop() != matching_symbols[symbol]:
                return False

    return stack.is_empty()
```

Die vollständige und aktuelle Implementierung befindet sich in [`balanced_symbols.py`](balanced_symbols.py).

---

## Weiterentwicklung gegenüber `par_checker()`

Bei der einfachen Klammerprüfung existiert nur:

```text
( )
```

Dort reicht es bei einem Schließer zu prüfen:

```text
Ist überhaupt ein Öffner vorhanden?
```

und anschließend:

```python
stack.pop()
```

Bei mehreren Symboltypen reicht das nicht mehr.

Beispiel:

```text
([)]
```

Die Anzahl aller Öffner und Schließer stimmt.

Trotzdem ist die Verschachtelung falsch.

Nach:

```text
(
[
```

liegt `[` oben auf dem Stack.

Als Nächstes erscheint aber:

```text
)
```

Der zuletzt geöffnete Typ passt also nicht zum aktuellen Schließer.

Die neue Aufgabe lautet deshalb:

```text
Existiert ein offenes Symbol?
+
Ist es vom richtigen Typ?
```

---

## Das Dictionary `matching_symbols`

Die Zuordnung:

```python
matching_symbols = {
    ")": "(",
    "]": "[",
    "}": "{",
}
```

beantwortet für jeden Schließer direkt die Frage:

> Welcher Öffner wird an dieser Stelle erwartet?

Beispiele:

```python
matching_symbols[")"]
```

liefert:

```text
(
```

und:

```python
matching_symbols["]"]
```

liefert:

```text
[
```

Damit ist die Zuordnungsregel explizit als Datenstruktur modelliert und muss nicht durch mehrere verschachtelte `if`-Bedingungen ausgedrückt werden.

---

## Schritt für Schritt

### 1. Öffnende Symbole speichern

```python
if symbol in "([{":
    stack.push(symbol)
```

Jedes öffnende Symbol wird auf den Stack gelegt.

Beispiel:

```text
{[(
```

führt gedanklich zu:

```text
Top
 ↓
[(]
[[]
[{]
```

Das oberste Element ist immer das **zuletzt geöffnete Symbol**.

---

### 2. Schließendes Symbol erkennen

```python
elif symbol in ")]}":
```

Bei einem Schließer sind zwei Prüfungen notwendig.

---

### 3. Prüfen, ob überhaupt ein Öffner existiert

```python
if stack.is_empty():
    return False
```

Beispiel:

```text
]
```

Der Stack ist leer.

Es wurde vorher kein `[` geöffnet.

Die Eingabe ist damit sofort ungültig.

---

### 4. Passenden Symboltyp prüfen

```python
if stack.pop() != matching_symbols[symbol]:
    return False
```

Hier werden zwei Werte verglichen:

```text
stack.pop()
→ zuletzt geöffneter Symboltyp

matching_symbols[symbol]
→ für den aktuellen Schließer erwarteter Öffner
```

Nur wenn beide übereinstimmen, ist dieser Teil der Verschachtelung korrekt.

---

### 5. Am Ende auf verbleibende Öffner prüfen

```python
return stack.is_empty()
```

Auch wenn während des Durchlaufs kein falscher Schließer gefunden wurde, können noch offene Symbole übrig bleiben.

Beispiel:

```text
[{(
```

Der Stack ist am Ende nicht leer.

Ergebnis:

```text
False
```

---

## Warum diese Lösung funktioniert

Die zentrale Invariante lautet:

> Der Stack enthält jederzeit genau die geöffneten Symbole, die noch nicht geschlossen wurden – in ihrer Öffnungsreihenfolge.

Da ein Stack nach LIFO arbeitet, steht oben immer das Symbol, das **als Nächstes geschlossen werden muss**.

Bei:

```text
{ [ ( ) ] }
```

geschieht deshalb logisch:

```text
öffnen {
öffnen [
öffnen (

schließen ) -> muss zu ( passen
schließen ] -> muss zu [ passen
schließen } -> muss zu { passen
```

Genau diese Verschachtelungsregel wird durch Stack + Lookup-Tabelle direkt modelliert.

---

## Zentrales Gegenbeispiel: `([)]`

Schritt für Schritt:

```text
Zeichen    Aktion                 Stack
--------------------------------------
(          push                   (
[          push                   ( [
)          erwartet (, findet [   Fehler
```

Beim `)` gilt:

```python
matching_symbols[")"] == "("
```

Oben auf dem Stack liegt aber:

```text
[
```

Damit:

```text
[ != (
```

Der Ausdruck ist sofort ungültig.

Dass später noch `]` erscheint, kann die falsche Verschachtelung nicht mehr reparieren.

---

## Gültiges Beispiel: `[[()]]`

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

Die Symbolkette ist korrekt verschachtelt.

---

## Warum bloßes Zählen nicht reicht

Eine naive Prüfung könnte vergleichen:

```text
Anzahl ( == Anzahl )
Anzahl [ == Anzahl ]
Anzahl { == Anzahl }
```

Das erkennt jedoch:

```text
([)]
```

nicht als Fehler.

Die Häufigkeit jeder Symbolart stimmt.

Falsch ist die **Reihenfolge der Schließvorgänge**.

Der Stack speichert genau diese Reihenfolge und macht deshalb die strukturelle Prüfung möglich.

---

## Warum das Dictionary eine gute Designentscheidung ist

Man könnte die Zuordnung auch mit mehreren Bedingungen ausdrücken:

```python
if symbol == ")" and opening_symbol != "(":
    return False
elif symbol == "]" and opening_symbol != "[":
    return False
elif symbol == "}" and opening_symbol != "{":
    return False
```

Das funktioniert, verteilt die Paarungsregel aber über mehrere Codezweige.

Mit:

```python
matching_symbols = {
    ")": "(",
    "]": "[",
    "}": "{",
}
```

wird die Regel direkt sichtbar:

```text
Schließer -> erwarteter Öffner
```

Vorteile:

```text
kompakter
leichter lesbar
leichter erweiterbar
Zuordnung zentral definiert
```

Der Dictionary-Zugriff ist im Durchschnitt:

```text
O(1)
```

---

## Komplexität

Sei `n` die Länge von `symbol_string`.

### Laufzeit

Die Eingabe wird einmal durchlaufen:

```python
for symbol in symbol_string:
```

Pro relevantem Zeichen erfolgen nur konstante Operationen:

```text
Stack push/pop/is_empty -> O(1)
Dictionary-Lookup       -> durchschnittlich O(1)
```

Damit beträgt die gesamte Laufzeit:

```text
O(n)
```

### Speicher

Im Worst Case besteht die Eingabe nur aus öffnenden Symbolen:

```text
(([[{{
```

Dann werden bis zu `n` Symbole auf dem Stack gespeichert.

Der zusätzliche Speicherbedarf beträgt:

```text
O(n)
```

Das Dictionary selbst besitzt für diese Aufgabe eine konstante Größe und verändert die asymptotische Speicherkomplexität nicht.

---

## Rand- und Fehlerfälle

### Leerer String

```python
balanced_symbols("")
```

Es wird kein Symbol verarbeitet.

Der Stack bleibt leer.

Ergebnis:

```text
True
```

---

### Nur ein öffnendes Symbol

```python
balanced_symbols("(")
```

Am Ende liegt noch ein Öffner auf dem Stack.

Ergebnis:

```text
False
```

---

### Nur ein schließendes Symbol

```python
balanced_symbols("]")
```

Der Stack ist beim Auftreten des Schließers leer.

Ergebnis sofort:

```text
False
```

---

### Falscher Symboltyp

```python
balanced_symbols("([)]")
```

Ein Öffner existiert, aber nicht vom erwarteten Typ.

Ergebnis:

```text
False
```

---

### Offene Symbole bleiben übrig

```python
balanced_symbols("[{(")
```

Es tritt kein falscher Schließer auf, aber am Ende ist der Stack nicht leer.

Ergebnis:

```text
False
```

---

## Andere Zeichen und Eingabevalidierung

Der aktuelle Algorithmus reagiert nur auf:

```text
( ) [ ] { }
```

Andere Zeichen werden ignoriert.

Zum Beispiel:

```python
balanced_symbols("result = [a + (b * c)]")
```

prüft nur die enthaltenen Klammern.

Das kann für echten Programmtext sogar sinnvoll sein.

Eine strengere Schnittstelle könnte dagegen ausschließlich Klammerzeichen erlauben.

Welche Variante richtig ist, hängt vom gewünschten Vertrag ab und ist eine **Input-Validation-Entscheidung**.

---

## Typvertrag

Die aktuelle Signatur lautet:

```python
def balanced_symbols(symbol_string: str) -> bool:
```

Damit wird die erwartete Schnittstelle dokumentiert:

```text
str -> bool
```

Type Hints erzwingen diese Bedingung zur Laufzeit nicht automatisch.

Für die aktuelle Lernübung ist zusätzliche Typvalidierung nicht notwendig.

---

## Tests

Zu den ursprünglichen Lernfällen gehören unter anderem:

```text
""          -> True
[[()]]      -> True
[][][]()    -> True
([)]        -> False
((()])      -> False
[{(]        -> False
```

Die Implementierung wird inzwischen zusätzlich automatisiert mit `pytest` geprüft:

[`../tests/test_stacks.py`](../tests/test_stacks.py)

Dort werden unter anderem getestet:

```text
korrekt verschachtelte Symbole
falsche Verschachtelung
leere Eingabe
```

---

## Design- und Skalierungsgedanke

Der Algorithmus verarbeitet die Eingabe in einem einzigen Durchlauf.

Es sind keine wiederholten Suchen oder Teilstring-Operationen notwendig.

```text
n Zeichen
×
konstante Arbeit pro Zeichen
=
O(n)
```

Der Stack enthält außerdem nur Informationen, die für zukünftige Entscheidungen noch relevant sind:

```text
Welche Symbole sind aktuell noch offen?
```

Das Dictionary trennt zusätzlich die **Paarungsregeln** von der eigentlichen Kontrolllogik.

Diese Aufteilung:

```text
Stack
→ Reihenfolge und Zustand

Dictionary
→ Zuordnung der Symboltypen
```

macht die Lösung sowohl algorithmisch klar als auch gut erweiterbar.

---

## Unterschied zu `par_checker()`

Bei [`par_checker()`](par_checker_explanation.md) reicht die Frage:

> Gibt es für diesen Schließer überhaupt einen offenen Vorgänger?

Bei `balanced_symbols()` kommt eine zweite Bedingung hinzu:

> Ist der zuletzt geöffnete Symboltyp genau derjenige, den dieser Schließer erwartet?

Der entscheidende zusätzliche Vergleich lautet:

```python
stack.pop() == matching_symbols[symbol]
```

Damit entwickelt sich aus der einfachen Klammerprüfung eine echte Prüfung verschachtelter Symboltypen.

---

## Zentrale Lernidee

Die zentrale Erkenntnis lautet:

> **Bei korrekt verschachtelten Symbolen muss immer das zuletzt geöffnete Symbol als Nächstes passend geschlossen werden.**

Der Stack modelliert die Reihenfolge der offenen Symbole.

Das Dictionary modelliert, welche Typen zusammengehören.

Gemeinsam ermöglichen beide Strukturen eine vollständige Prüfung in:

```text
O(n)
```

Zeit.

---

## Weiterführend

- [`README.md`](README.md) – Stack, LIFO und grundlegende Operationen
- [`par_checker_explanation.md`](par_checker_explanation.md) – einfachere Variante mit nur einer Klammerart
- [`../docs/data_structure_patterns.md`](../docs/data_structure_patterns.md) – Stack für verschachtelte Strukturen und Lookup-Muster
- [`../docs/big_o_cheatsheet.md`](../docs/big_o_cheatsheet.md) – Analyse von Zeit- und Speicherkomplexität
- [`../tests/test_stacks.py`](../tests/test_stacks.py) – automatisierte Tests
