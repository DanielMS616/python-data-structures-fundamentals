# `ReversableQueue.reverse_first_k()` – Die ersten k Elemente einer Queue umkehren

## Ziel der Übung

Die Queue erhält eine Methode:

```python
reverse_first_k(k)
```

die genau die ersten `k` Elemente umkehrt.

Alle nachfolgenden Elemente behalten ihre relative Reihenfolge.

Ein Stack darf als Hilfsstruktur eingesetzt werden.

Die geforderten Zielkomplexitäten sind:

```text
enqueue()         -> O(1)
dequeue()         -> O(n)
reverse_first_k() -> O(k)
```

Beispiel:

```text
Vorher:
1 -> 2 -> 3

reverse_first_k(2)

Nachher:
2 -> 1 -> 3
```

Die allgemeinen Grundlagen zu Queue/FIFO und Stack/LIFO stehen in [`README.md`](README.md) beziehungsweise [`../stacks/README.md`](../stacks/README.md).

Hier liegt der Fokus auf der **Kombination beider Datenstrukturen** und darauf, die geforderte `O(k)`-Laufzeit tatsächlich einzuhalten.

---

## Quick Summary

| Aspekt | Ergebnis |
| --- | --- |
| Hauptstruktur | Python-Liste als Queue |
| Hilfsstruktur | Stack |
| Muster | Stack als Umkehrmechanismus |
| `enqueue()` | schulisch `O(1)`, technisch amortisiert `O(1)` |
| `dequeue()` | `O(n)` |
| `reverse_first_k()` | `O(k)` |
| Zusatzspeicher | `O(k)` |
| Kernidee | Erste `k` Werte per Index lesen, über LIFO rückwärts zurückschreiben |

---

## Relevante Implementierung

Der entscheidende Teil der aktuellen Lösung ist:

```python
from pythonds3.basic import Stack


class ReversableQueue:
    def __init__(self) -> None:
        self.queue: list[object] = []

    def enqueue(self, item: object) -> None:
        self.queue.append(item)

    def dequeue(self) -> object | None:
        if not self.queue:
            return None

        return self.queue.pop(0)

    def reverse_first_k(self, k: int) -> None:
        if k < 0 or k > len(self.queue):
            raise ValueError("k must be between 0 and the queue length")

        stack = Stack()

        for index in range(k):
            stack.push(self.queue[index])

        for index in range(k):
            self.queue[index] = stack.pop()
```

Die vollständige und aktuelle Implementierung befindet sich in [`reversable_queue.py`](reversable_queue.py).

---

## Was `reverse_first_k()` genau verändert

Angenommen:

```text
queue = [1, 2, 3, 4, 5]
```

und:

```python
reverse_first_k(3)
```

wird aufgerufen.

Dann sollen nur:

```text
1, 2, 3
```

umgekehrt werden.

Ergebnis:

```text
[3, 2, 1, 4, 5]
```

Der hintere Teil:

```text
4, 5
```

bleibt unverändert.

---

## Warum ein Stack geeignet ist

Die ersten `k` Elemente werden in normaler Reihenfolge auf den Stack gelegt.

Für:

```text
1, 2, 3
```

entsteht:

```text
Top
 ↓
[3]
[2]
[1]
```

Beim anschließenden `pop()` liefert der Stack:

```text
3
2
1
```

Damit entsteht die Umkehrung automatisch durch LIFO.

---

## Eingabe `k` validieren

Vor der eigentlichen Arbeit:

```python
if k < 0 or k > len(self.queue):
    raise ValueError("k must be between 0 and the queue length")
```

Gültig sind:

```text
0 <= k <= len(queue)
```

Beispiel bei drei Elementen:

```text
k = 0
k = 1
k = 2
k = 3
```

Ungültig:

```text
k = -1
k = 4
```

Eine `ValueError` macht sichtbar, dass der übergebene Parameter außerhalb des erlaubten Bereichs liegt.

---

## Die ersten k Elemente lesen

```python
for index in range(k):
    stack.push(self.queue[index])
```

Bei:

```text
queue = [1, 2, 3, 4, 5]
k = 3
```

werden die Indizes:

```text
0, 1, 2
```

gelesen.

Dadurch landen:

```text
1, 2, 3
```

auf dem Stack.

Die Queue selbst wird in diesem Schritt noch nicht verändert.

---

## Werte rückwärts zurückschreiben

```python
for index in range(k):
    self.queue[index] = stack.pop()
```

Der Stack liefert:

```text
3, 2, 1
```

Diese Werte werden zurück auf die Positionen:

```text
0, 1, 2
```

geschrieben.

Aus:

```text
[1, 2, 3, 4, 5]
```

wird:

```text
[3, 2, 1, 4, 5]
```

Nur der gewünschte Prefix wird verändert.

---

## Warum direkter Indexzugriff wichtig ist

Eine zunächst intuitive Variante wäre:

```python
for _ in range(k):
    stack.push(self.queue.pop(0))
```

Das würde die ersten Werte tatsächlich entfernen.

Das Problem ist jedoch:

```python
list.pop(0)
```

kostet:

```text
O(n)
```

weil die verbleibenden Elemente verschoben werden müssen.

Würde diese Operation `k`-mal ausgeführt, wäre die geforderte:

```text
O(k)
```

Laufzeit nicht mehr garantiert.

Deshalb verwendet die Lösung:

```python
self.queue[index]
```

und:

```python
self.queue[index] = ...
```

Der Zugriff auf eine bekannte Listenposition ist:

```text
O(1)
```

---

## Warum zwei Schleifen trotzdem O(k) sind

Die Methode besitzt zwei Schleifen über `k` Elemente:

```text
erste Schleife  -> k Schritte
zweite Schleife -> k Schritte
```

Damit:

```text
k + k = 2k
```

In Big O werden konstante Faktoren ignoriert:

```text
O(2k) = O(k)
```

Die Gesamtmethode bleibt deshalb:

```text
reverse_first_k() -> O(k)
```

---

## Beispiel

Ausgangslage:

```text
[10, 20, 30, 40, 50]
```

Aufruf:

```python
reverse_first_k(4)
```

Der Prefix:

```text
10, 20, 30, 40
```

wird umgekehrt.

Ergebnis:

```text
[40, 30, 20, 10, 50]
```

Das letzte Element bleibt unverändert.

---

## Komplexität

### `enqueue()`

```python
self.queue.append(item)
```

In typischen Grundlagenaufgaben wird dies als:

```text
O(1)
```

behandelt.

Technisch präziser gilt für eine Python-Liste:

```text
amortisiert O(1)
```

weil gelegentlich interner Speicher vergrößert werden muss.

Damit unterscheiden wir bewusst:

```text
Schulmodell        -> O(1)
technische Präzision -> amortisiert O(1)
```

### `dequeue()`

```python
self.queue.pop(0)
```

entfernt das erste Listenelement.

Alle nachfolgenden Werte müssen verschoben werden:

```text
dequeue() -> O(n)
```

### `reverse_first_k()`

Zwei lineare Durchläufe über genau `k` Positionen:

```text
reverse_first_k() -> O(k)
```

### Zusatzspeicher

Der Stack speichert maximal genau `k` Elemente:

```text
O(k)
```

Es wird keine vollständige Kopie der Queue erzeugt.

---

## Randfälle

### `k = 0`

```python
reverse_first_k(0)
```

Keine der beiden Schleifen läuft.

Die Queue bleibt unverändert.

---

### `k = 1`

Ein einzelnes Element umzukehren verändert nichts.

```text
[1, 2, 3]
```

bleibt:

```text
[1, 2, 3]
```

---

### `k == len(queue)`

Dann wird die komplette Queue umgekehrt.

```text
[1, 2, 3]
```

wird zu:

```text
[3, 2, 1]
```

---

### Ungültiges `k`

Für:

```text
k < 0
```

oder:

```text
k > len(queue)
```

wird:

```python
ValueError
```

ausgelöst.

Dieser Fehlerfall ist Teil der aktuellen Schnittstelle und wird automatisiert getestet.

---

## Typvertrag

Die aktuelle Methode lautet:

```python
def reverse_first_k(self, k: int) -> None:
```

Damit ist sichtbar:

```text
k
→ Integer

Rückgabewert
→ keiner; die bestehende Queue wird verändert
```

Die Queue selbst speichert aktuell:

```python
list[object]
```

und ist damit nicht auf einen einzelnen Nutzdatentyp beschränkt.

---

## Tests

Der ursprüngliche Lernfall verwendet:

```text
[1, 2, 3]
```

mit:

```python
reverse_first_k(2)
```

und erwartet danach:

```text
[2, 1, 3]
```

beziehungsweise beim nächsten `dequeue()`:

```text
2
```

Die Implementierung wird inzwischen zusätzlich automatisiert mit `pytest` geprüft:

[`../tests/test_queues.py`](../tests/test_queues.py)

Dort werden unter anderem getestet:

```text
normale Umkehrung
k = 0
negatives k
k größer als die Queue-Länge
```

---

## Design- und Skalierungsgedanke

Diese Aufgabe zeigt besonders gut:

> Eine funktionierende Lösung erfüllt nicht automatisch die geforderte Komplexität.

Ein wiederholtes:

```python
pop(0)
```

wäre logisch nachvollziehbar, aber asymptotisch zu teuer.

Die eigentliche Designfrage lautet daher:

```text
Welche Operationen stellt meine konkrete Datenstruktur günstig bereit?
```

Hier ist:

```text
Listenindex lesen/schreiben -> O(1)
pop(0)                      -> O(n)
```

Die Wahl der Operationen ist deshalb genauso wichtig wie die grobe algorithmische Idee.

---

## Warum die Klasse `ReversableQueue` heißt

Der vorgegebene Klassenname lautet:

```python
ReversableQueue
```

Die üblichere englische Schreibweise wäre:

```python
ReversibleQueue
```

Der Name bleibt in diesem Lernbeispiel bewusst erhalten, damit die Implementierung mit der ursprünglichen Übungsstruktur konsistent bleibt.

In neuem produktivem Code würde man die korrekte Schreibweise bevorzugen.

---

## Zentrale Lernidee

Die zentrale Erkenntnis lautet:

> **Durch die Kombination aus direktem Listenindex und dem LIFO-Prinzip eines Stacks lassen sich genau die ersten k Elemente in O(k) umkehren.**

Dabei werden zwei Ebenen kombiniert:

```text
Stack
→ liefert die umgekehrte Reihenfolge

direkter Listenindex
→ erhält die geforderte Laufzeit
```

Die Übung zeigt damit sehr gut, wie mehrere Datenstrukturen und ihre jeweiligen Operationseigenschaften gemeinsam eine Lösung formen.

---

## Weiterführend

- [`README.md`](README.md) – Queue, FIFO und Implementierungsvarianten
- [`../stacks/README.md`](../stacks/README.md) – Stack und LIFO
- [`../docs/data_structure_patterns.md`](../docs/data_structure_patterns.md) – Stack als Umkehrmechanismus
- [`../docs/big_o_cheatsheet.md`](../docs/big_o_cheatsheet.md) – Laufzeitanalyse und amortisierte Komplexität
- [`../docs/python_collections_complexity.md`](../docs/python_collections_complexity.md) – Kosten von Listenoperationen
- [`../tests/test_queues.py`](../tests/test_queues.py) – automatisierte Tests
