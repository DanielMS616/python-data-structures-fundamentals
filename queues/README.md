# Queue

## Überblick

Eine **Queue (Warteschlange)** ist ein abstrakter Datentyp, bei dem Elemente in ihrer Ankunftsreihenfolge verarbeitet werden.

Die Regel lautet:

```text
FIFO
First In, First Out
```

Das zuerst eingefügte Element wird zuerst wieder entfernt.

---

## Vorstellung: Warteschlange

```text
Front                   Rear
  ↓                       ↓
[A] -> [B] -> [C]
```

`A` kam zuerst und wird deshalb zuerst entfernt.

Neue Elemente werden am `rear` angefügt.

---

## Zentrale Operationen

| Operation | Bedeutung |
| --- | --- |
| `Queue()` | leere Queue erzeugen |
| `enqueue(item)` | Element hinten einfügen |
| `dequeue()` | vorderstes Element entfernen |
| `is_empty()` | prüfen, ob die Queue leer ist |
| `size()` | Anzahl der Elemente |

---

## Die Implementierung bestimmt die Laufzeit

FIFO beschreibt das Verhalten.

Wie dieses Verhalten intern realisiert wird, ist eine eigene Entscheidung.

---

## Variante 1: Python-Liste, Front am Listenende

Eine mögliche Listenimplementierung:

```python
def enqueue(self, item):
    self.items.insert(0, item)

def dequeue(self):
    return self.items.pop()
```

Laufzeiten:

```text
enqueue -> O(n)
dequeue -> O(1)
```

`insert(0, ...)` ist teuer, weil vorhandene Listenelemente verschoben werden.

---

## Variante 2: Python-Liste, Front am Listenanfang

Unsere `ReversibleQueue` verwendet sinngemäß:

```python
def enqueue(self, item):
    self.queue.append(item)

def dequeue(self):
    return self.queue.pop(0)
```

Laufzeiten:

```text
enqueue -> amortisiert O(1)
dequeue -> O(n)
```

Die Kosten wurden also auf die andere Operation verschoben.

---

## Variante 3: `collections.deque`

Für eine normale Queue ist in Python häufig:

```python
from collections import deque

queue = deque()

queue.append(item)
item = queue.popleft()
```

eine passende Wahl.

Typisch:

```text
enqueue -> O(1)
dequeue -> O(1)
```

---

## Variante 4: Linked List mit `front` und `rear`

```text
front                   rear
  ↓                       ↓
[A] -> [B] -> [C] -> None
```

Mit zwei Referenzen können beide Enden direkt erreicht werden.

```python
class QueueUsingLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
```

Typisch:

```text
enqueue -> O(1)
dequeue -> O(1)
```

Wichtig ist die Invariante:

```text
Wenn die Queue nach dequeue leer wird,
müssen front und rear beide None sein.
```

---

## Vergleich

| Implementierung | Enqueue | Dequeue |
| --- | ---: | ---: |
| Liste mit `insert(0)` + `pop()` | `O(n)` | `O(1)` |
| Liste mit `append()` + `pop(0)` | amortisiert `O(1)` | `O(n)` |
| `deque` | `O(1)` | `O(1)` |
| Linked List mit `front/rear` | `O(1)` | `O(1)` |

Das zeigt sehr deutlich:

> Derselbe ADT kann je nach Implementierung unterschiedliche Laufzeiten besitzen.

---

## Priority Queue

Eine Priority Queue verändert die normale FIFO-Regel.

Zuerst entscheidet:

```text
Priorität
```

Bei gleicher Priorität bleibt in unserer Übung FIFO erhalten.

Gespeichert wird:

```python
(priority, counter, item)
```

Beispiel:

```text
A -> Priorität 1
C -> Priorität 2
D -> Priorität 2
B -> Priorität 3
```

Entnahme:

```text
A
C
D
B
```

Der Counter erhält die Reihenfolge zwischen `C` und `D`.

---

## Warum liegt das nächste Priority-Element am Listenende?

Unsere Übung erlaubt:

```text
enqueue -> O(n log n)
dequeue -> O(1)
```

Darum wird beim Einfügen sortiert.

Das nächste Element wird bewusst ans Listenende gelegt:

```python
self.queue.pop()
```

ist dort:

```text
O(1)
```

Würde es vorne liegen:

```python
self.queue.pop(0)
```

wäre die Operation:

```text
O(n)
```

---

## MaxQueue

Die MaxQueue soll zusätzlich:

```python
get_max()
```

in:

```text
O(1)
```

ermöglichen.

Dafür werden zwei Queues gepflegt:

```text
queue
max_queue
```

`max_queue` enthält nur Werte, die noch Maximum werden können.

Beispiel:

```python
while self.max_queue and self.max_queue[-1] < item:
    self.max_queue.pop()
```

Das Maximum liegt danach direkt bei:

```python
self.max_queue[0]
```

---

## Warum gleiche Maximalwerte bleiben müssen

Die Bedingung verwendet:

```python
<
```

nicht:

```python
<=
```

Bei:

```text
5, 5
```

müssen beide Maximalwerte intern erhalten bleiben.

Wenn die erste `5` die Hauptqueue verlässt, bleibt die zweite weiterhin Maximum.

---

## Queue + Stack

Die Übung `reverse_first_k()` verbindet FIFO und LIFO.

Queue:

```text
1 -> 2 -> 3 -> 4
```

Die ersten drei Werte werden auf einen Stack gelegt:

```text
Top
 ↓
[3]
[2]
[1]
```

Zurückgeschrieben:

```text
3 -> 2 -> 1 -> 4
```

Das zeigt:

> Datenstrukturen können kombiniert werden, wenn ihre jeweiligen Eigenschaften gut zum Teilproblem passen.

---

## Übungen in diesem Ordner

### Priority Queue

- [`priority_queue.py`](priority_queue.py)
- [`priority_queue_explanation.md`](priority_queue_explanation.md)

Lernideen:

```text
Priorität
stabile Einfügereihenfolge
Arbeit von dequeue zu enqueue verschieben
```

### MaxQueue

- [`max_queue.py`](max_queue.py)
- [`max_queue_explanation.md`](max_queue_explanation.md)

Lernideen:

```text
monotone Hilfsqueue
zusätzlicher Speicher für schnelleren Zugriff
amortisierte Laufzeit
```

### Erste k Elemente umkehren

- [`reversible_queue.py`](reversible_queue.py)
- [`reversible_queue_explanation.md`](reversible_queue_explanation.md)

Lernideen:

```text
Queue + Stack
LIFO zum Umkehren
direkter Indexzugriff statt wiederholtem pop(0)
```

Hinweis:

Der Startercode verwendet den Namen:

```text
ReversibleQueue
```

Die übliche englische Schreibweise wäre:

```text
ReversibleQueue
```

Der verwendete Name bleibt in der Übung bestehen, damit Code und begleitende Erklärung konsistent bleiben.

---

## Typische Fehler und Randfälle

### `dequeue()` auf leerer Queue

Die Schnittstelle muss definieren, was passiert.

In den Übungen wird häufig:

```python
return None
```

verwendet.

Alternativ könnte eine Klasse bewusst eine Exception auslösen.

---

### Hilfsstruktur nicht synchron halten

Bei der MaxQueue müssen:

```text
queue
max_queue
```

konsistent bleiben.

Wird das aktuelle Maximum aus `queue` entfernt, muss es gegebenenfalls auch aus `max_queue` entfernt werden.

---

### Datenstruktur nur nach Bequemlichkeit wählen

Eine Python-Liste kann eine Queue darstellen.

Das heißt nicht automatisch, dass jede Queue-Operation damit effizient ist.

---

## Kurzreferenz

```text
Queue
-----
Prinzip: FIFO

enqueue -> hinten hinein
dequeue -> vorne heraus

Python:
deque ist für eine normale FIFO-Queue häufig sehr passend.

Varianten:
Priority Queue -> Priorität entscheidet
MaxQueue        -> zusätzliche Maximum-Kandidaten
```

Weiterführend:

- [`../docs/adt_and_implementation.md`](../docs/adt_and_implementation.md)
- [`../docs/python_collections_complexity.md`](../docs/python_collections_complexity.md)
- [`../docs/data_structure_patterns.md`](../docs/data_structure_patterns.md)
