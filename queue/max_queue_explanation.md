# `MaxQueue` – Maximum einer Warteschlange in O(1) bestimmen

## Ziel der Übung

Die Queue soll neben den normalen FIFO-Operationen eine Methode

```python
get_max()
```

anbieten, die das aktuelle Maximum in **`O(1)`** liefert. Dafür darf zusätzlicher Zustand gepflegt werden, ohne die normale Reihenfolge der Queue zu verändern.

---

## Implementierung

```python
from collections import deque


class MaxQueue:
    def __init__(self):
        self.queue = deque()
        self.max_queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

        # Remove values that can no longer become the maximum.
        while self.max_queue and self.max_queue[-1] < item:
            self.max_queue.pop()

        self.max_queue.append(item)

    def dequeue(self):
        if not self.queue:
            return None

        item = self.queue.popleft()

        # Remove the maximum candidate as well if it leaves the main queue.
        if item == self.max_queue[0]:
            self.max_queue.popleft()

        return item

    def get_max(self):
        if not self.max_queue:
            return None

        # The current maximum is always at the front.
        return self.max_queue[0]


# Test
mq = MaxQueue()

mq.enqueue(3)
mq.enqueue(1)

print(mq.get_max())  # Expected: 3
```

---

# 1. Grundidee

Die Warteschlange verwendet zwei `deque`-Objekte:

```python
self.queue
self.max_queue
```

`queue` enthält alle Elemente in ihrer normalen Reihenfolge.

`max_queue` enthält nur Werte, die noch als aktuelles oder zukünftiges Maximum infrage kommen.

Dadurch muss `get_max()` nicht jedes Mal die gesamte Queue durchsuchen.

---

# 2. Warum wäre `max(self.queue)` nicht ausreichend?

Eine naive Lösung wäre:

```python
def get_max(self):
    return max(self.queue)
```

Das liefert zwar das richtige Ergebnis, aber `max()` muss alle Elemente durchsuchen.

Bei `n` Elementen kostet das:

```text
O(n)
```

Die Aufgabe verlangt jedoch:

```text
O(1)
```

Deshalb pflegen wir eine zusätzliche Hilfsstruktur.

---

# 3. Warum verwenden wir `deque`?

Eine Queue arbeitet nach FIFO:

```text
First In, First Out
```

Neue Elemente kommen hinten hinein:

```python
append()
```

und das älteste Element wird vorne entfernt:

```python
popleft()
```

Bei `collections.deque` sind diese Operationen jeweils:

```text
O(1)
```

Darum eignet sich `deque` sehr gut für Warteschlangen.

---

# 4. Was macht `max_queue`?

`max_queue` wird so gepflegt, dass ihre Werte von vorne nach hinten nicht größer werden.

Das größte relevante Element steht also immer vorne.

Damit ist:

```python
self.max_queue[0]
```

immer das aktuelle Maximum.

---

# 5. Der entscheidende Teil in `enqueue()`

```python
while self.max_queue and self.max_queue[-1] < item:
    self.max_queue.pop()
```

Angenommen, in `max_queue` stehen:

```text
[7, 5, 2]
```

und wir fügen ein:

```text
6
```

Dann können `5` und `2` später nicht mehr Maximum werden, solange `6` in der Queue vorhanden ist.

Sie werden deshalb entfernt.

Danach:

```text
[7]
```

und anschließend wird `6` angehängt:

```text
[7, 6]
```

---

# 6. Warum dürfen kleinere Werte entfernt werden?

Angenommen, die normale Queue enthält:

```text
7, 5, 2
```

und danach wird:

```text
6
```

eingefügt.

Solange `6` noch in der Queue ist, können `5` und `2` niemals Maximum werden.

Wenn `7` irgendwann entfernt wird, ist `6` größer als beide.

Darum müssen `5` und `2` nicht länger als Maximum-Kandidaten gespeichert werden.

---

# 7. Wichtig: Gleich große Werte bleiben erhalten

Die Bedingung lautet:

```python
self.max_queue[-1] < item
```

und nicht:

```python
self.max_queue[-1] <= item
```

Das ist wichtig bei doppelten Werten.

Beispiel:

```text
5, 5
```

Beide `5` müssen in `max_queue` erhalten bleiben.

Wenn die erste `5` später entfernt wird, muss die zweite `5` weiterhin als Maximum vorhanden sein.

Darum werden nur **kleinere**, nicht gleich große Werte entfernt.

---

# 8. Wie arbeitet `dequeue()`?

Die normale Queue entfernt das älteste Element:

```python
item = self.queue.popleft()
```

Danach prüfen wir:

```python
if item == self.max_queue[0]:
```

Wenn das entfernte Element gleichzeitig das aktuelle Maximum war, muss es auch aus `max_queue` entfernt werden:

```python
self.max_queue.popleft()
```

So bleiben beide Datenstrukturen synchron.

---

# 9. Wie arbeitet `get_max()`?

```python
return self.max_queue[0]
```

Da das Maximum immer vorne gespeichert wird, ist kein Suchen notwendig.

Die Laufzeit ist:

```text
O(1)
```

---

# 10. Verwendeter Testfall

Der tatsächliche Testcode lautet:

```python
mq = MaxQueue()

mq.enqueue(3)
mq.enqueue(1)

print(mq.get_max())
```

Die normale Queue enthält danach:

```text
[3, 1]
```

Die Hilfsqueue enthält:

```text
[3, 1]
```

Das Maximum steht vorne:

```text
3
```

Ausgabe:

```text
3
```

---

# 11. Zusätzliches Erklärbeispiel

Das folgende Beispiel gehört **nicht zum obigen Testcode**. Es dient nur dazu, die Logik von `max_queue` besser zu verstehen.

Wir fügen nacheinander ein:

```text
3, 1, 5, 2
```

Nach `3`:

```text
queue:      [3]
max_queue:  [3]
```

Nach `1`:

```text
queue:      [3, 1]
max_queue:  [3, 1]
```

Nach `5` werden `1` und `3` aus `max_queue` entfernt, weil beide kleiner als `5` sind:

```text
queue:      [3, 1, 5]
max_queue:  [5]
```

Nach `2`:

```text
queue:      [3, 1, 5, 2]
max_queue:  [5, 2]
```

Das aktuelle Maximum ist weiterhin:

```text
5
```

---

# 12. Laufzeitkomplexität

## `get_max()`

```python
self.max_queue[0]
```

Direkter Zugriff:

```text
O(1)
```

## `dequeue()`

`popleft()` auf einer `deque`:

```text
O(1)
```

Auch die mögliche Entfernung aus `max_queue` ist:

```text
O(1)
```

Also insgesamt:

```text
dequeue() -> O(1)
```

## `enqueue()`

Auf den ersten Blick enthält `enqueue()` eine `while`-Schleife.

Ein einzelner Aufruf kann mehrere Elemente aus `max_queue` entfernen.

Über viele Operationen betrachtet kann jedes Element aber nur:

1. einmal eingefügt,
2. und höchstens einmal wieder entfernt werden.

Darum ist `enqueue()` **amortisiert O(1)**.

---

# 13. Was bedeutet „amortisiert O(1)“?

Ein einzelner `enqueue()`-Aufruf kann manchmal mehr Arbeit machen.

Beispiel:

```text
1, 2, 3, 4, 100
```

Beim Einfügen von `100` können mehrere kleinere Kandidaten entfernt werden.

Diese zusätzlichen Entfernungen können aber nicht beliebig oft wiederholt werden, weil jedes Element danach endgültig aus `max_queue` verschwunden ist.

Über viele Einfügungen verteilt bleibt der durchschnittliche Aufwand deshalb konstant.

Das nennt man:

```text
amortisiert O(1)
```

---

# 14. Speicherkomplexität

Neben der normalen Queue speichern wir eine zweite Struktur:

```python
max_queue
```

Im Worst Case, zum Beispiel bei streng fallenden Werten:

```text
9, 8, 7, 6, 5
```

bleiben alle Werte in `max_queue`.

Der zusätzliche Speicherbedarf beträgt deshalb:

```text
O(n)
```

---

# 15. Fehlerfälle

Bei einer leeren Queue behandeln wir zwei Fälle:

```python
dequeue()
```

und:

```python
get_max()
```

Beide geben:

```python
None
```

zurück, wenn keine Elemente vorhanden sind.

Für diese Schulaufgabe ist das eine einfache und verständliche Lösung.

In einer größeren Anwendung könnte man alternativ bewusst eine Exception verwenden.

---

# 16. Design- und Skalierungsgedanke

Diese Aufgabe zeigt einen klassischen Trade-off:

```text
mehr Speicher
gegen
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

Dafür benötigen wir zusätzliche Daten im Speicher.

Das gleiche Grundprinzip begegnet später zum Beispiel bei:

- Datenbankindizes
- Caches
- vorberechneten Werten
- Lookup-Strukturen

---

# 17. Datenintegrität

Die wichtigste interne Regel lautet:

> `max_queue` muss immer zum Zustand von `queue` passen.

Darum reicht es nicht, nur beim Einfügen Änderungen vorzunehmen.

Auch beim Entfernen müssen wir prüfen:

```python
if item == self.max_queue[0]:
    self.max_queue.popleft()
```

Würde man diesen Schritt vergessen, könnte `get_max()` später einen Wert zurückgeben, der gar nicht mehr in der eigentlichen Queue vorhanden ist.

Das wäre ein Datenkonsistenzfehler.

---

# Zusammenfassung

Die Klasse verwendet zwei Warteschlangen:

```text
queue      -> enthält alle Elemente
max_queue  -> enthält nur mögliche Maximum-Kandidaten
```

Beim Einfügen werden kleinere Kandidaten entfernt:

```python
while self.max_queue and self.max_queue[-1] < item:
    self.max_queue.pop()
```

Beim Entfernen werden beide Strukturen synchron gehalten.

Dadurch erhalten wir:

```text
enqueue()  -> amortisiert O(1)
dequeue()  -> O(1)
get_max()  -> O(1)
```

Die wichtigste Erkenntnis lautet:

> **Durch eine zusätzliche monotone Hilfsqueue kann das aktuelle Maximum jederzeit direkt in O(1) gelesen werden.**
