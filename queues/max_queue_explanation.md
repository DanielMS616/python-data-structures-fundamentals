# `MaxQueue` – Maximum einer Queue in O(1) bestimmen

## Ziel der Übung

Die Queue soll neben den normalen FIFO-Operationen eine Methode

```python
get_max()
```

bereitstellen, die das aktuelle Maximum in:

```text
O(1)
```

zurückgibt.

Dafür darf zusätzlicher Zustand gepflegt werden, solange die normale Reihenfolge der Queue unverändert bleibt.

Die allgemeinen Eigenschaften einer Queue und typische Implementierungen sind in [`README.md`](README.md) zusammengefasst.

Hier liegt der Fokus auf der **zusätzlichen Anforderung**, das Maximum jederzeit ohne vollständige Suche verfügbar zu halten.

---

## Quick Summary

| Aspekt | Ergebnis |
| --- | --- |
| Hauptstruktur | `deque` |
| Hilfsstruktur | monotone `max_queue` |
| Muster | Zusatzstruktur für schnellen Zugriff |
| `enqueue()` | amortisiert `O(1)` |
| `dequeue()` | `O(1)` |
| `get_max()` | `O(1)` |
| Zusatzspeicher | `O(n)` |
| Kernidee | Nur Werte behalten, die noch Maximum werden können |

---

## Relevante Implementierung

```python
from collections import deque


class MaxQueue:
    def __init__(self) -> None:
        self.queue: deque[int] = deque()
        self.max_queue: deque[int] = deque()

    def enqueue(self, item: int) -> None:
        self.queue.append(item)

        while self.max_queue and self.max_queue[-1] < item:
            self.max_queue.pop()

        self.max_queue.append(item)

    def dequeue(self) -> int | None:
        if not self.queue:
            return None

        item = self.queue.popleft()

        if item == self.max_queue[0]:
            self.max_queue.popleft()

        return item

    def get_max(self) -> int | None:
        if not self.max_queue:
            return None

        return self.max_queue[0]
```

Die vollständige und aktuelle Implementierung befindet sich in [`max_queue.py`](max_queue.py).

---

## Grundidee: zwei synchronisierte Queues

Die Klasse verwaltet zwei `deque`-Objekte:

```text
queue
→ alle Elemente in normaler FIFO-Reihenfolge

max_queue
→ nur Werte, die noch als Maximum infrage kommen
```

`max_queue` wird monoton fallend gehalten. Das größte relevante Element steht dadurch immer vorne:

```python
self.max_queue[0]
```

Damit muss `get_max()` nicht jedes Mal die vollständige Queue durchsuchen.

---

## Warum `max(self.queue)` nicht ausreicht

Eine einfache Lösung wäre:

```python
return max(self.queue)
```

Sie ist funktional korrekt, benötigt aber:

```text
O(n)
```

weil alle Elemente betrachtet werden müssen.

Die Aufgabe verlangt:

```text
O(1)
```

Deshalb wird die Information über mögliche Maxima bereits beim Einfügen vorbereitet.

---

## Der entscheidende Teil von `enqueue()`

```python
while self.max_queue and self.max_queue[-1] < item:
    self.max_queue.pop()
```

Angenommen:

```text
max_queue = [7, 5, 2]
```

und wir fügen ein:

```text
6
```

`5` und `2` können danach kein zukünftiges Maximum mehr werden, solange `6` in der Queue vorhanden ist.

Sie werden entfernt:

```text
[7]
```

Danach wird `6` angehängt:

```text
[7, 6]
```

Die Hilfsqueue enthält damit nur noch **relevante Maximum-Kandidaten**.

---

## Wichtig: gleiche Maximalwerte bleiben erhalten

Die Bedingung lautet bewusst:

```python
self.max_queue[-1] < item
```

und nicht:

```python
self.max_queue[-1] <= item
```

Bei:

```text
5, 5
```

müssen beide Werte erhalten bleiben.

Wird die erste `5` entfernt, muss die zweite weiterhin als Maximum vorhanden sein.

Dieser kleine Unterschied schützt eine wichtige Invariante der Struktur.

---

## `dequeue()` hält beide Strukturen synchron

Das älteste Element verlässt zunächst die Hauptqueue:

```python
item = self.queue.popleft()
```

War dieses Element gleichzeitig der aktuelle Maximum-Kandidat:

```python
if item == self.max_queue[0]:
    self.max_queue.popleft()
```

wird es auch aus der Hilfsqueue entfernt.

Die zentrale Invariante lautet:

> `max_queue` darf niemals ein Maximum enthalten, das in `queue` nicht mehr existiert.

---

## Beispiel

Wir fügen ein:

```text
3, 1, 5, 2
```

Entwicklung:

```text
nach 3:
queue:      [3]
max_queue:  [3]

nach 1:
queue:      [3, 1]
max_queue:  [3, 1]

nach 5:
queue:      [3, 1, 5]
max_queue:  [5]

nach 2:
queue:      [3, 1, 5, 2]
max_queue:  [5, 2]
```

Das Maximum ist direkt:

```text
5
```

---

## Komplexität

### `get_max()`

```python
self.max_queue[0]
```

Direkter Zugriff:

```text
O(1)
```

### `dequeue()`

`popleft()` auf einer `deque` ist:

```text
O(1)
```

Auch die optionale Entfernung aus `max_queue` bleibt:

```text
O(1)
```

Damit:

```text
dequeue() -> O(1)
```

### `enqueue()`

Ein einzelner Aufruf kann mehrere Werte aus `max_queue` entfernen.

Über eine ganze Folge von Einfügungen kann jedoch jedes Element:

```text
einmal eingefügt
und höchstens einmal entfernt
```

werden.

Deshalb gilt:

```text
enqueue() -> amortisiert O(1)
```

Das ist ein klassisches Beispiel dafür, dass eine `while`-Schleife nicht automatisch eine lineare Laufzeit **pro Operation** bedeutet.

### Zusatzspeicher

Im Worst Case, etwa bei:

```text
9, 8, 7, 6, 5
```

bleiben alle Werte in `max_queue`.

Der zusätzliche Speicherbedarf beträgt deshalb:

```text
O(n)
```

---

## Rand- und Fehlerfälle

### Leere Queue

Sowohl:

```python
dequeue()
```

als auch:

```python
get_max()
```

geben bei einer leeren Queue:

```python
None
```

zurück.

Das ist Teil der aktuellen Schnittstellenentscheidung.

### Doppelte Maximalwerte

```text
5, 5, 3
```

ist ein besonders wichtiger Fall.

Nach dem Entfernen der ersten `5` muss die zweite `5` weiterhin als Maximum verfügbar sein.

Genau dieser Fall wird heute automatisiert getestet.

---

## Typvertrag

Die aktuelle Schnittstelle lautet:

```python
enqueue(self, item: int) -> None
dequeue(self) -> int | None
get_max(self) -> int | None
```

Damit ist sichtbar:

```text
gespeicherte Werte -> int
leere Queue        -> None bei dequeue/get_max
```

Eine generische Variante für beliebige vergleichbare Typen wäre möglich, gehört aber nicht zum Umfang dieser Lernübung.

---

## Tests

Der ursprüngliche Lernfall prüft:

```python
mq.enqueue(3)
mq.enqueue(1)
```

mit erwartetem Ergebnis:

```text
get_max() -> 3
```

Die Implementierung wird inzwischen zusätzlich automatisiert mit `pytest` geprüft:

[`../tests/test_queues.py`](../tests/test_queues.py)

Besonders relevant ist der Test mit **doppelten Maximalwerten**, weil er die Entscheidung für `<` statt `<=` direkt absichert.

---

## Design- und Skalierungsgedanke

Die Übung zeigt einen klassischen Trade-off:

```text
mehr Speicher
↔
schnellere Abfrage
```

Ohne Hilfsstruktur:

```text
get_max() -> O(n)
```

Mit `max_queue`:

```text
get_max() -> O(1)
```

Dafür muss zusätzlicher Zustand gepflegt und konsistent gehalten werden.

Dieses Muster begegnet später auch bei:

```text
Caches
Datenbankindizes
Lookup-Strukturen
vorberechneten Werten
```

Die Optimierung besteht also nicht darin, weniger Information zu speichern, sondern **gezielt mehr Information vorzuhalten**, damit spätere Operationen billiger werden.

---

## Zentrale Lernidee

Die zentrale Erkenntnis lautet:

> **Durch eine zusätzliche monotone Hilfsqueue kann das aktuelle Maximum jederzeit direkt in O(1) gelesen werden.**

Die Lösung kombiniert drei wichtige Ideen:

```text
monotone Kandidatenstruktur
+
Synchronisation mit der Hauptqueue
+
amortisierte Analyse
```

Dadurch entsteht eine schnelle Maximum-Abfrage, ohne die FIFO-Reihenfolge der eigentlichen Queue zu verändern.

---

## Weiterführend

- [`README.md`](README.md) – Queue, FIFO und Implementierungsvarianten
- [`../docs/data_structure_patterns.md`](../docs/data_structure_patterns.md) – monotone Hilfsqueue und Speicher-Laufzeit-Trade-offs
- [`../docs/big_o_cheatsheet.md`](../docs/big_o_cheatsheet.md) – amortisierte Laufzeit
- [`../docs/python_collections_complexity.md`](../docs/python_collections_complexity.md) – `deque` und typische Python-Operationen
- [`../tests/test_queues.py`](../tests/test_queues.py) – automatisierte Tests
