# `PriorityQueue` – Prioritätswarteschlange mit stabilem FIFO-Verhalten

## Ziel der Übung

Die Queue soll Elemente nach einer numerischen **Priorität** verarbeiten, wobei `1` die höchste Priorität bezeichnet. Haben zwei Elemente denselben Prioritätswert, bleibt ihre FIFO-Reihenfolge erhalten.

Für die Implementierung gelten diese Zielkomplexitäten:

```text
enqueue() -> höchstens O(n log n)
dequeue() -> O(1)
```

Beispiel:

```python
pq.enqueue("A", 1)
pq.enqueue("B", 3)
pq.enqueue("C", 2)
pq.enqueue("D", 2)
```

Die gewünschte Entnahmereihenfolge ist:

```text
A
C
D
B
```

`A` kommt wegen Priorität `1` zuerst.

`C` und `D` haben beide Priorität `2`. Da `C` früher eingefügt wurde, muss `C` vor `D` entfernt werden.

---

## Implementierung

```python
class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0

    def enqueue(self, item, priority):
        # The counter preserves FIFO order for equal priorities.
        self.queue.append((priority, self.counter, item))
        self.counter += 1

        # Keep the next item to remove at the end of the list.
        self.queue.sort(
            key=lambda element: (element[0], element[1]),
            reverse=True,
        )

    def dequeue(self):
        if not self.queue:
            return None

        # pop() at the end of a Python list is O(1).
        _, _, item = self.queue.pop()
        return item


# Test
pq = PriorityQueue()

pq.enqueue("A", 1)
pq.enqueue("B", 3)
pq.enqueue("C", 2)
pq.enqueue("D", 2)

print(pq.dequeue())  # Expected: A
print(pq.dequeue())  # Expected: C
print(pq.dequeue())  # Expected: D
print(pq.dequeue())  # Expected: B
```

---

# 1. Wiederholung: Was ist eine normale Queue?

Eine normale Warteschlange arbeitet nach:

```text
FIFO
First In, First Out
```

Das bedeutet:

> Das zuerst eingefügte Element wird zuerst wieder entfernt.

Beispiel:

```text
A -> B -> C
```

Beim ersten `dequeue()` würde `A` entfernt.

---

# 2. Was ändert sich bei einer Priority Queue?

Bei einer Prioritätswarteschlange entscheidet zuerst die **Priorität**.

In dieser Aufgabe gilt:

```text
1 = höchste Priorität
2 = danach
3 = niedriger
```

Damit wird zum Beispiel:

```text
A, Priorität 1
B, Priorität 3
C, Priorität 2
```

nicht einfach nach Einfügereihenfolge entfernt, sondern:

```text
A
C
B
```

---

# 3. Warum brauchen wir zusätzlich einen Counter?

Nur die Priorität zu speichern reicht nicht aus.

Angenommen:

```python
pq.enqueue("C", 2)
pq.enqueue("D", 2)
```

Beide Elemente haben dieselbe Priorität.

Die Aufgabenstellung verlangt:

```text
C vor D
```

weil `C` zuerst eingefügt wurde.

Darum bekommt jedes Element zusätzlich eine fortlaufende Nummer:

```python
self.counter
```

Die gespeicherten Tupel sehen dann zum Beispiel so aus:

```text
A -> (1, 0, "A")
B -> (3, 1, "B")
C -> (2, 2, "C")
D -> (2, 3, "D")
```

Dabei bedeutet:

```text
(priority, insertion_order, item)
```

---

# 4. Warum funktioniert der Counter als FIFO-Regel?

Bei gleicher Priorität entscheidet die kleinere Counter-Zahl.

Für:

```text
C -> (2, 2, "C")
D -> (2, 3, "D")
```

wurde `C` früher eingefügt.

Deshalb soll das Tupel mit:

```text
counter = 2
```

vor dem Tupel mit:

```text
counter = 3
```

entfernt werden.

Der Counter speichert also die ursprüngliche Einfügereihenfolge.

---

# 5. Warum sortieren wir die Liste rückwärts?

Wir sortieren so:

```python
self.queue.sort(
    key=lambda element: (element[0], element[1]),
    reverse=True,
)
```

Die Sortierung betrachtet zuerst:

```text
priority
```

und bei gleicher Priorität:

```text
counter
```

Durch:

```python
reverse=True
```

stehen die größeren Werte vorne.

Nach den vier Testeinfügungen sieht die interne Liste ungefähr so aus:

```python
[
    (3, 1, "B"),
    (2, 3, "D"),
    (2, 2, "C"),
    (1, 0, "A"),
]
```

Die nächste zu entfernende Position liegt damit immer **am Ende der Liste**.

---

# 6. Warum liegt das wichtigste Element am Ende?

Wir wollen `dequeue()` in:

```text
O(1)
```

ausführen.

Bei einer Python-Liste ist:

```python
self.queue.pop()
```

am Listenende:

```text
O(1)
```

Deshalb sortieren wir die Daten absichtlich so, dass das nächste Element immer ganz hinten liegt.

Dann reicht:

```python
_, _, item = self.queue.pop()
```

---

# 7. Warum nicht vorne entfernen?

Man könnte die Liste auch so sortieren, dass das wichtigste Element vorne steht.

Dann müsste man aber:

```python
self.queue.pop(0)
```

verwenden.

Das wäre:

```text
O(n)
```

weil alle verbleibenden Elemente intern nach vorne verschoben werden müssen.

Damit würde die Anforderung der Aufgabe verletzt.

---

# 8. Schritt für Schritt durch den Test

Wir fügen ein:

```python
pq.enqueue("A", 1)
pq.enqueue("B", 3)
pq.enqueue("C", 2)
pq.enqueue("D", 2)
```

Intern:

```text
A -> (1, 0, "A")
B -> (3, 1, "B")
C -> (2, 2, "C")
D -> (2, 3, "D")
```

Nach der Sortierung:

```text
[
    B,
    D,
    C,
    A
]
```

genauer:

```python
[
    (3, 1, "B"),
    (2, 3, "D"),
    (2, 2, "C"),
    (1, 0, "A"),
]
```

---

## Erstes `dequeue()`

```python
self.queue.pop()
```

entfernt:

```text
A
```

---

## Zweites `dequeue()`

Jetzt liegt am Ende:

```text
C
```

also wird `C` entfernt.

---

## Drittes `dequeue()`

Danach:

```text
D
```

---

## Viertes `dequeue()`

Zuletzt:

```text
B
```

Ergebnis:

```text
A
C
D
B
```

Genau wie gefordert.

---

# 9. Laufzeit von `enqueue()`

Beim Einfügen passiert zuerst:

```python
self.queue.append(...)
```

Das ist bei Python-Listen amortisiert:

```text
O(1)
```

Danach:

```python
self.queue.sort(...)
```

Für `list.sort()` gilt im allgemeinen Fall:

```text
O(n log n)
```

Damit dominiert die Sortierung.

Also:

```text
enqueue() -> O(n log n)
```

Das entspricht der Aufgabenstellung.

---

# 10. Laufzeit von `dequeue()`

`dequeue()` verwendet:

```python
self.queue.pop()
```

am Listenende.

Das ist:

```text
O(1)
```

Damit erfüllt die Methode die wichtigste Laufzeitanforderung:

```text
dequeue() -> O(1)
```

---

# 11. Fehlerfall: Leere Warteschlange

Wenn:

```python
dequeue()
```

auf einer leeren Queue aufgerufen wird, gibt es kein Element zum Entfernen.

Wir prüfen deshalb:

```python
if not self.queue:
    return None
```

Für diese Schulaufgabe ist `None` eine einfache und nachvollziehbare Lösung.

In einer größeren Anwendung könnte man auch bewusst eine Exception auslösen.

Das wäre eine Designentscheidung der Schnittstelle.

---

# 12. Warum verwenden wir `_, _, item`?

Intern speichern wir:

```python
(priority, counter, item)
```

Beim Entfernen interessiert uns aber nur:

```text
item
```

Darum schreiben wir:

```python
_, _, item = self.queue.pop()
```

Der Unterstrich `_` signalisiert:

> Dieser Wert wird absichtlich nicht weiter verwendet.

Das ist in Python eine übliche Schreibweise.

---

# 13. Warum nicht einfach nur nach Priorität sortieren?

Zum Beispiel:

```python
self.queue.sort(key=lambda element: element[0])
```

würde nur die Priorität betrachten.

Dann wäre die gewünschte Reihenfolge bei identischen Prioritäten nicht ausdrücklich Teil unseres Datenmodells.

Der Counter macht die Regel dagegen klar und zuverlässig:

```text
Priorität zuerst
Einfügereihenfolge danach
```

Damit ist die FIFO-Anforderung bei gleicher Priorität direkt im Sortierschlüssel enthalten.

---

# 14. Design- und Skalierungsgedanke

Die Aufgabe zwingt uns zu einer bewussten Entscheidung:

> Wann soll die aufwendigere Arbeit stattfinden?

Wir könnten beim Einfügen nur anhängen:

```text
enqueue -> sehr günstig
```

und erst beim Entfernen das Element mit der höchsten Priorität suchen.

Dann wäre aber:

```text
dequeue -> O(n)
```

Die Aufgabenstellung verlangt genau das Gegenteil:

```text
enqueue -> darf teurer sein
dequeue -> muss O(1) sein
```

Deshalb sortieren wir beim Einfügen.

Das ist ein wichtiger allgemeiner Software-Engineering-Gedanke:

> Man kann Rechenarbeit bewusst in die Operation verschieben, bei der sie weniger kritisch ist.

---

# 15. Skalierbarkeit: Ist Sortieren bei jedem Einfügen optimal?

Für die konkrete Aufgabe ist diese Lösung passend, weil ausdrücklich erlaubt wird:

```text
enqueue -> O(n log n)
```

Bei sehr großen Datenmengen wäre es jedoch nicht unbedingt die effizienteste allgemeine Priority-Queue-Implementierung.

In der Praxis verwendet man dafür häufig spezielle Datenstrukturen wie einen:

```text
Heap
```

Ein Heap kann Einfügen und Entfernen typischerweise effizienter organisieren.

Das gehört jedoch nicht zur Anforderung dieser Aufgabe.

Für diese Übung ist die sortierte Python-Liste eine klare und gut nachvollziehbare Lösung.

---

# 16. Eingabevalidierung

Die Aufgabe geht davon aus, dass `priority` sinnvoll übergeben wird, zum Beispiel:

```python
1
2
3
```

Wir prüfen aktuell nicht:

- ob `priority` wirklich eine Zahl ist,
- ob sie positiv ist,
- ob `1` oder größer verwendet wird.

Für die Schulaufgabe ist das vollkommen ausreichend.

In einer produktiveren Klasse müsste man vorher festlegen, welche Werte als gültige Priorität gelten und diese Regel gegebenenfalls validieren.

---

# 17. Speicherkomplexität

Für jedes Element speichern wir zusätzlich:

```text
priority
counter
```

Die Anzahl gespeicherter Tupel wächst mit der Anzahl der Queue-Elemente.

Damit beträgt der Speicherbedarf:

```text
O(n)
```

Der Counter selbst ist nur ein einzelner zusätzlicher Klassenwert.

---

# 18. Zentrale Lernidee

Die Lösung kombiniert drei Ideen:

### 1. Priorität

```text
kleinere Zahl = höhere Priorität
```

### 2. Einfügereihenfolge

```python
self.counter
```

erhält FIFO bei gleicher Priorität.

### 3. Geeignete Sortierreihenfolge

Das nächste Element liegt absichtlich am Ende der Python-Liste, damit:

```python
pop()
```

in:

```text
O(1)
```

arbeiten kann.

---

# Zusammenfassung

Intern speichern wir jedes Element als:

```python
(priority, counter, item)
```

Der Counter hält die Einfügereihenfolge fest.

Beim Einfügen wird die Liste so sortiert, dass das als Nächstes benötigte Element am Ende steht:

```python
self.queue.sort(
    key=lambda element: (element[0], element[1]),
    reverse=True,
)
```

Beim Entfernen reicht deshalb:

```python
_, _, item = self.queue.pop()
```

Die geforderten Laufzeiten werden erfüllt:

```text
enqueue() -> O(n log n)
dequeue() -> O(1)
```

Die wichtigste Erkenntnis lautet:

> **Durch zusätzliche Metadaten und eine bewusst gewählte Sortierreihenfolge können wir Priorität und FIFO-Verhalten kombinieren und gleichzeitig `dequeue()` in O(1) ermöglichen.**
