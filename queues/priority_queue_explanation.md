# `PriorityQueue` – Prioritätswarteschlange mit stabilem FIFO-Verhalten

## Ziel der Übung

Die Queue soll Elemente nach einer numerischen **Priorität** verarbeiten.

Dabei gilt:

```text
1 = höchste Priorität
2 = danach
3 = niedriger
```

Haben zwei Elemente dieselbe Priorität, bleibt ihre ursprüngliche FIFO-Reihenfolge erhalten.

Die geforderten Zielkomplexitäten sind:

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

Gewünschte Entnahmereihenfolge:

```text
A
C
D
B
```

Die allgemeinen Grundlagen von Queues und FIFO sind in [`README.md`](README.md) zusammengefasst.

Hier liegt der Fokus auf der **Kombination aus Priorität, stabiler Einfügereihenfolge und bewusst verteilter Rechenarbeit**.

---

## Quick Summary

| Aspekt | Ergebnis |
| --- | --- |
| Datenstruktur | sortierte Python-Liste |
| gespeicherte Form | `(priority, counter, item)` |
| Muster | Priorität + stabiler Counter |
| `enqueue()` | `O(n log n)` |
| `dequeue()` | `O(1)` |
| Zusatzspeicher | `O(n)` |
| Kernidee | Beim Einfügen sortieren, damit das nächste Element am Listenende liegt |
| Wichtige Invariante | Bei gleicher Priorität entscheidet die kleinere Counter-Zahl |

---

## Relevante Implementierung

Der entscheidende Teil der aktuellen Lösung ist:

```python
class PriorityQueue:
    def __init__(self) -> None:
        self.queue: list[tuple[int, int, object]] = []
        self.counter: int = 0

    def enqueue(self, item: object, priority: int) -> None:
        self.queue.append((priority, self.counter, item))
        self.counter += 1

        self.queue.sort(
            key=lambda element: (element[0], element[1]),
            reverse=True,
        )

    def dequeue(self) -> object | None:
        if not self.queue:
            return None

        _, _, item = self.queue.pop()
        return item
```

Die vollständige und aktuelle Implementierung befindet sich in [`priority_queue.py`](priority_queue.py).

---

## Was ändert sich gegenüber einer normalen Queue?

Bei einer normalen Queue entscheidet ausschließlich die Einfügereihenfolge.

Eine Priority Queue fügt davor ein zusätzliches Kriterium ein:

```text
1. Priorität
2. bei Gleichstand: Einfügereihenfolge
```

Beispiel:

```text
A, Priorität 1
B, Priorität 3
C, Priorität 2
D, Priorität 2
```

führt zu:

```text
A
C
D
B
```

`C` und `D` besitzen dieselbe Priorität. Deshalb muss zwischen ihnen weiterhin FIFO gelten.

---

## Warum ein Counter notwendig ist

Nur die Priorität zu speichern reicht nicht aus, wenn die Einfügereihenfolge bei Gleichstand **explizit Teil des Datenmodells** sein soll.

Jedes Element erhält deshalb eine fortlaufende Nummer:

```python
self.counter
```

Die gespeicherten Tupel sehen zum Beispiel so aus:

```text
A -> (1, 0, "A")
B -> (3, 1, "B")
C -> (2, 2, "C")
D -> (2, 3, "D")
```

Bedeutung:

```text
(priority, insertion_order, item)
```

Bei gleicher Priorität gewinnt damit die kleinere Counter-Zahl.

---

## Warum der Counter FIFO stabil hält

Für:

```text
C -> (2, 2, "C")
D -> (2, 3, "D")
```

haben beide Elemente dieselbe Priorität.

`C` besitzt aber den kleineren Counter:

```text
2 < 3
```

und wurde deshalb früher eingefügt.

Die Einfügereihenfolge ist damit nicht nur implizit vorhanden, sondern als Metadatum gespeichert.

---

## Warum rückwärts sortiert wird

Die Liste wird so sortiert:

```python
self.queue.sort(
    key=lambda element: (element[0], element[1]),
    reverse=True,
)
```

Der Sortierschlüssel betrachtet:

```text
1. priority
2. counter
```

Durch:

```python
reverse=True
```

stehen größere Werte weiter vorne.

Nach den vier Beispiel-Einfügungen sieht die Liste ungefähr so aus:

```python
[
    (3, 1, "B"),
    (2, 3, "D"),
    (2, 2, "C"),
    (1, 0, "A"),
]
```

Das als Nächstes benötigte Element liegt bewusst **am Listenende**.

---

## Warum das wichtigste Element am Ende liegt

Die Aufgabe verlangt:

```text
dequeue() -> O(1)
```

Bei einer Python-Liste ist:

```python
self.queue.pop()
```

am Listenende:

```text
O(1)
```

Deshalb wird die Sortierreihenfolge so gewählt, dass das nächste Element immer genau dort liegt.

Dann reicht:

```python
_, _, item = self.queue.pop()
```

---

## Warum nicht vorne entfernen?

Eine alternative Sortierung könnte das wichtigste Element an Index `0` ablegen.

Dann wäre nötig:

```python
self.queue.pop(0)
```

Bei einer Python-Liste ist das:

```text
O(n)
```

weil die verbleibenden Elemente verschoben werden müssen.

Damit würde die zentrale Laufzeitanforderung verletzt.

---

## Schritt für Schritt am Beispiel

Einfügungen:

```python
pq.enqueue("A", 1)
pq.enqueue("B", 3)
pq.enqueue("C", 2)
pq.enqueue("D", 2)
```

Gespeicherte Metadaten:

```text
A -> (1, 0, "A")
B -> (3, 1, "B")
C -> (2, 2, "C")
D -> (2, 3, "D")
```

Sortierte interne Liste:

```python
[
    (3, 1, "B"),
    (2, 3, "D"),
    (2, 2, "C"),
    (1, 0, "A"),
]
```

Jedes:

```python
self.queue.pop()
```

entfernt nun nacheinander:

```text
A
C
D
B
```

---

## Warum `_, _, item`?

Intern speichern wir:

```python
(priority, counter, item)
```

Beim Entfernen interessiert die öffentliche Queue-Schnittstelle aber nur das eigentliche Element.

Darum:

```python
_, _, item = self.queue.pop()
```

Der Unterstrich `_` signalisiert:

> Dieser Wert wird bewusst nicht weiter verwendet.

Damit bleiben die internen Metadaten verborgen und nur `item` wird zurückgegeben.

---

## Komplexität

### `enqueue()`

Zunächst:

```python
self.queue.append(...)
```

Das ist bei Python-Listen:

```text
amortisiert O(1)
```

Danach:

```python
self.queue.sort(...)
```

Für `list.sort()` gilt im Worst Case:

```text
O(n log n)
```

Die Sortierung dominiert daher:

```text
enqueue() -> O(n log n)
```

### `dequeue()`

```python
self.queue.pop()
```

am Listenende:

```text
O(1)
```

Damit:

```text
dequeue() -> O(1)
```

### Speicher

Für jedes Queue-Element wird ein Tupel gespeichert:

```text
(priority, counter, item)
```

Die Zahl der Tupel wächst mit `n`.

Damit:

```text
O(n)
```

Der einzelne Klassen-Counter verändert die asymptotische Speicherkomplexität nicht.

---

## Leere Queue

Bei:

```python
dequeue()
```

auf einer leeren Queue gilt:

```python
if not self.queue:
    return None
```

`None` ist damit Teil der aktuellen Schnittstellenentscheidung.

Eine andere Implementierung könnte stattdessen eine Exception verwenden.

---

## Eingabevalidierung

Die aktuelle Signatur lautet:

```python
enqueue(self, item: object, priority: int) -> None
```

Sie dokumentiert, dass:

```text
item
→ beliebiges Objekt

priority
→ Integer
```

erwartet wird.

Aktuell wird nicht zusätzlich geprüft:

```text
ob priority positiv ist
ob 1 der kleinste erlaubte Wert sein muss
ob bestimmte Prioritätsbereiche gelten
```

Für die Lernübung reicht der dokumentierte Vertrag aus.

In einer produktiven API müssten gültige Prioritätswerte explizit definiert und gegebenenfalls validiert werden.

---

## Warum diese Lösung die Arbeit bewusst verschiebt

Man könnte beim Einfügen nur:

```text
append
```

verwenden und das wichtigste Element erst beim `dequeue()` suchen.

Dann wäre:

```text
enqueue() -> günstig
dequeue() -> O(n)
```

Die Aufgabe verlangt jedoch:

```text
enqueue() -> darf teurer sein
dequeue() -> muss O(1) sein
```

Deshalb wird die aufwendige Sortierung bewusst in `enqueue()` verschoben.

Das ist ein allgemeines Designmuster:

> Rechenarbeit kann gezielt in die Operation verlagert werden, bei der sie weniger kritisch ist.

---

## Skalierung: wäre ein Heap besser?

Für die konkrete Aufgabenstellung ist die sortierte Liste passend, weil:

```text
enqueue() -> O(n log n)
```

ausdrücklich erlaubt ist.

Für eine allgemeine Priority Queue mit großen Datenmengen wäre Sortieren nach **jedem** Einfügen jedoch nicht optimal.

In der Praxis wird häufig ein:

```text
Heap
```

verwendet.

Ein Heap organisiert Einfügen und Entfernen typischerweise effizienter.

Das ist jedoch eine weiterführende Implementierungsentscheidung und nicht notwendig, um die Anforderungen dieser Übung zu erfüllen.

---

## Tests

Der zentrale Lernfall ist:

```text
A, Priorität 1
B, Priorität 3
C, Priorität 2
D, Priorität 2
```

mit erwarteter Entnahmereihenfolge:

```text
A
C
D
B
```

Die Implementierung wird inzwischen automatisiert mit `pytest` geprüft:

[`../tests/test_queues.py`](../tests/test_queues.py)

Der Test sichert dabei gleichzeitig:

```text
Prioritätsreihenfolge
+
FIFO bei gleicher Priorität
```

ab.

---

## Design- und Skalierungsgedanke

Die Lösung kombiniert drei verschiedene Entscheidungen:

```text
Priorität
→ bestimmt grundsätzlich die Reihenfolge

Counter
→ erhält FIFO bei gleicher Priorität

reverse sort
→ legt das nächste Element ans günstige Listenende
```

Die Performance-Anforderung beeinflusst damit unmittelbar die interne Repräsentation.

Das ist ein wichtiges Muster:

> Nicht nur die Daten selbst, sondern auch ihre Anordnung kann gezielt auf die häufigsten oder kritischsten Operationen optimiert werden.

---

## Zentrale Lernidee

Die zentrale Erkenntnis lautet:

> **Durch zusätzliche Metadaten und eine bewusst gewählte Sortierreihenfolge können Priorität und FIFO-Verhalten kombiniert werden, während `dequeue()` in O(1) bleibt.**

Die Übung zeigt damit sehr anschaulich, dass Datenstruktur-Design nicht nur aus „Speichern und Entfernen“ besteht.

Entscheidend ist auch:

```text
Welche Information speichere ich zusätzlich?
Wo soll die teure Arbeit stattfinden?
Welche interne Reihenfolge macht die kritische Operation günstig?
```

---

## Weiterführend

- [`README.md`](README.md) – Queue, FIFO und Priority-Queue-Grundlagen
- [`../docs/data_structure_patterns.md`](../docs/data_structure_patterns.md) – stabile Priorität und bewusstes Verschieben von Arbeit
- [`../docs/big_o_cheatsheet.md`](../docs/big_o_cheatsheet.md) – `O(n log n)` und Operationen vergleichen
- [`../docs/python_collections_complexity.md`](../docs/python_collections_complexity.md) – Python-Listenoperationen
- [`../tests/test_queues.py`](../tests/test_queues.py) – automatisierte Tests
