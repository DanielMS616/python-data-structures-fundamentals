# Wiederkehrende Datenstruktur- und Algorithmusmuster

Ein wichtiges Lernziel ist, nicht nur einzelne Aufgaben wiederzuerkennen, sondern **Problemmuster**.

Statt:

> „Wie ging Aufgabe 4 nochmal?“

soll mit der Zeit die Frage entstehen:

> „Welches bekannte Muster passt zu diesem Problem?“

---

## 1. Stack als Umkehrmechanismus

### Erkennungszeichen

```text
Reihenfolge soll umgedreht werden.
```

### Idee

Ein Stack arbeitet nach:

```text
LIFO
Last In, First Out
```

Was in normaler Reihenfolge hineingelegt wird, kommt rückwärts wieder heraus.

### Muster

```python
for item in items:
    stack.push(item)

while not stack.is_empty():
    reversed_items.append(stack.pop())
```

### Im Repository

- `Stack/rev_string.py`
- `queue/reversable_queue.py`

---

## 2. Stack für verschachtelte Strukturen

### Erkennungszeichen

```text
Etwas wird geöffnet und später wieder geschlossen.
Das zuletzt Geöffnete muss zuerst geschlossen werden.
```

Beispiele:

```text
()
[]
{}
HTML/XML-Tags
verschachtelte Ausdrücke
```

### Muster

```python
if opening_symbol:
    stack.push(symbol)

elif closing_symbol:
    opening = stack.pop()

    if not matches(opening, symbol):
        return False
```

### Im Repository

- `Stack/par_checker.py`
- `Stack/balanced_symbols.py`

---

## 3. Previous / Current / Next

### Erkennungszeichen

```text
Links einer einfach verketteten Liste sollen verändert werden,
ohne den restlichen Teil der Liste zu verlieren.
```

### Muster

```python
previous = None
current = head

while current:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node
```

### Warum `next_node`?

Sobald:

```python
current.next = previous
```

ausgeführt wird, zeigt `current.next` nicht mehr auf den ursprünglichen Nachfolger.

Darum muss dieser vorher gesichert werden.

### Im Repository

- `LinkedLists/linked_list_reverse.py`

---

## 4. Slow / Fast Pointer

Auch bekannt als:

```text
Tortoise and Hare
```

### Erkennungszeichen

```text
Mitte einer Linked List finden
Zyklus erkennen
relative Positionen ohne Längenberechnung bestimmen
```

### Muster

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

Wenn `fast` das Ende erreicht, befindet sich `slow` ungefähr in der Mitte.

### Im Repository

- `LinkedLists/linked_list_find_middle.py`

---

## 5. Seen Set

### Erkennungszeichen

```text
Habe ich diesen Wert schon gesehen?
```

Eine wiederholte lineare Suche wäre möglicherweise teuer.

### Muster

```python
seen = set()

for value in values:
    if value in seen:
        ...
    else:
        seen.add(value)
```

Durchschnittlich:

```text
Membership-Test -> O(1)
```

### Im Repository

- `LinkedLists/linked_list_remove_duplicates.py`

---

## 6. Head / Tail als direkte Endpunkt-Referenzen

### Erkennungszeichen

```text
Eine häufige Operation benötigt immer wieder das Ende einer Linked List.
```

Ohne `tail`:

```text
head -> ... -> ... -> Ende suchen
```

Mit `tail`:

```text
head                         tail
 ↓                             ↓
[A] -> [B] -> [C] -> ... -> [Z]
```

### Muster

```python
self.tail.next = new_node
self.tail = new_node
```

### Nutzen

```text
append:
O(n) -> O(1)
```

### Preis

Es entsteht eine zusätzliche Invariante:

```text
tail muss nach jeder strukturellen Änderung korrekt sein.
```

### Im Repository

- `LinkedLists/linked_list_append_o1.py`

---

## 7. Monotone Hilfsqueue

### Erkennungszeichen

```text
Eine Queue soll das aktuelle Maximum oder Minimum sehr schnell liefern.
```

### Idee

Neben der normalen Queue wird eine zweite Struktur gepflegt, die nur noch relevante Kandidaten enthält.

Für ein Maximum:

```python
while max_queue and max_queue[-1] < item:
    max_queue.pop()

max_queue.append(item)
```

Das Maximum liegt danach direkt vorne:

```python
max_queue[0]
```

### Im Repository

- `queue/max_queue.py`

---

## 8. Stable Priority über einen Counter

### Erkennungszeichen

```text
Elemente werden nach Priorität verarbeitet.
Bei gleicher Priorität soll die ursprüngliche Reihenfolge erhalten bleiben.
```

### Muster

Zusätzliche Metadaten speichern:

```python
(priority, counter, item)
```

Der Counter dokumentiert die Einfügereihenfolge.

Beispiel:

```text
C -> (2, 5, "C")
D -> (2, 6, "D")
```

Beide Priorität `2`, aber `C` kam früher.

### Im Repository

- `queue/priority_queue.py`

---

## 9. Arbeit bewusst verschieben

### Erkennungszeichen

Die Aufgabe verlangt:

```text
Operation A darf teuer sein.
Operation B muss sehr schnell sein.
```

Beispiel Priority Queue:

```text
enqueue darf O(n log n) sein
dequeue soll O(1) sein
```

Lösung:

```text
Beim Einfügen sortieren.
Beim Entfernen nur pop().
```

Allgemeiner Gedanke:

> Nicht nur fragen, **wie viel** Arbeit anfällt, sondern **wann** sie anfällt.

---

## 10. Speicher gegen Laufzeit tauschen

### Beispiel: Duplikate

Ohne Set:

```text
weniger Zusatzspeicher
möglicherweise O(n²)
```

Mit Set:

```text
O(n) zusätzlicher Speicher
durchschnittlich O(n) Laufzeit
```

### Beispiel: MaxQueue

Ohne Hilfsstruktur:

```text
get_max -> O(n)
```

Mit Hilfsqueue:

```text
zusätzlicher Speicher
get_max -> O(1)
```

Dieses Muster erscheint später auch bei:

```text
Caches
Datenbankindizes
Lookup-Tabellen
vorberechneten Werten
```

---

## 11. In-place-Transformation

### Erkennungszeichen

```text
Vorhandene Struktur soll verändert werden.
Keine vollständige Kopie erzeugen.
```

Beispiel:

```text
Linked List umkehren
```

In-place bedeutet:

```text
bestehende Nodes weiterverwenden
next-Referenzen verändern
keine neue Linked List aufbauen
```

Dadurch kann der zusätzliche Speicher auf:

```text
O(1)
```

begrenzt werden.

---

## 12. Early Return bei definitivem Fehler

### Erkennungszeichen

Ein Zustand kann nicht mehr repariert werden.

Beispiel:

```text
")("
```

Beim ersten `)` existiert kein Öffner.

Der restliche String kann das nicht nachträglich korrigieren.

Darum:

```python
if stack.is_empty():
    return False
```

Das macht Code oft:

```text
klarer
schneller
leichter zu begründen
```

---

## Mustererkennung – Kurzreferenz

```text
Reihenfolge umkehren?
→ Stack

Verschachtelung prüfen?
→ Stack

Schon gesehen?
→ Set

Linked-List-Links umdrehen?
→ previous / current / next

Mitte oder Zyklus?
→ slow / fast

Listenende ständig benötigt?
→ tail

Maximum einer Queue sofort benötigt?
→ monotone Hilfsqueue

Gleiche Priorität + FIFO?
→ Priority + Counter

Eine Operation muss besonders schnell sein?
→ Arbeit eventuell in eine andere Operation verschieben
```

---

## Lernziel

Ein gutes Zeichen für Fortschritt ist, wenn bei einer neuen Aufgabe zuerst eine strukturelle Frage entsteht:

```text
Welche Eigenschaft des Problems erkenne ich?
```

und erst danach:

```text
Welche Syntax muss ich schreiben?
```

Das macht aus einzelnen Lösungen übertragbares algorithmisches Wissen.
