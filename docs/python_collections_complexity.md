# Python-Datenstrukturen und ihre typischen Laufzeiten

Diese Datei ist eine schnelle Referenz für Operationen, die in den Übungen dieses Repositories häufig vorkommen.

> Die Werte sind algorithmische Richtwerte. Bei Hash-Strukturen werden durchschnittliche Laufzeiten genannt; bei `list.append()` wird die amortisierte Laufzeit angegeben.

---

## Python `list`

Python-Listen sind dynamische Arrays.

```python
values = [10, 20, 30]
```

### Typische Operationen

| Operation | Laufzeit |
| --- | ---: |
| `values[index]` | `O(1)` |
| `values[index] = x` | `O(1)` |
| `values.append(x)` | amortisiert `O(1)` |
| `values.pop()` | `O(1)` |
| `values.insert(0, x)` | `O(n)` |
| `values.pop(0)` | `O(n)` |
| `x in values` | `O(n)` |
| `len(values)` | `O(1)` |
| `values.sort()` | `O(n log n)` Worst Case |

Warum sind Operationen am Anfang teuer?

```text
[10, 20, 30, 40]
```

Wird `10` entfernt, müssen die nachfolgenden Elemente intern nach vorne verschoben werden.

---

## `collections.deque`

`deque` steht für **double-ended queue**.

```python
from collections import deque

queue = deque()
```

Sie ist für Operationen an beiden Enden optimiert.

| Operation | Laufzeit |
| --- | ---: |
| `append(x)` | `O(1)` |
| `appendleft(x)` | `O(1)` |
| `pop()` | `O(1)` |
| `popleft()` | `O(1)` |

Darum eignet sich `deque` sehr gut für eine normale FIFO-Queue:

```python
queue.append(item)
item = queue.popleft()
```

---

## Python `set`

Ein Set speichert eindeutige, hashbare Werte.

```python
seen = set()
```

Typische durchschnittliche Laufzeiten:

| Operation | Durchschnitt |
| --- | ---: |
| `seen.add(x)` | `O(1)` |
| `x in seen` | `O(1)` |
| `seen.remove(x)` | `O(1)` |

Das macht Sets besonders nützlich für:

```text
Duplikaterkennung
bereits besuchte Elemente
Membership-Tests
```

Beispiel:

```python
if current.data in seen:
    ...
else:
    seen.add(current.data)
```

### Hashbarkeit

Set-Elemente müssen hashbar sein.

Typischerweise geeignet:

```text
int
str
tuple aus hashbaren Werten
```

Nicht direkt geeignet:

```text
list
dict
set
```

---

## Python `dict`

Ein Dictionary ist eine Hash-Tabelle mit Schlüssel-Wert-Paaren.

```python
matching_symbols = {
    ")": "(",
    "]": "[",
    "}": "{",
}
```

Typische durchschnittliche Laufzeiten:

| Operation | Durchschnitt |
| --- | ---: |
| `mapping[key]` | `O(1)` |
| `mapping[key] = value` | `O(1)` |
| `key in mapping` | `O(1)` |

Beispiel aus der Symbolprüfung:

```python
matching_symbols[symbol]
```

liefert direkt den erwarteten Öffner.

---

## `pythonds3.basic.Stack`

Die Stack-Übungen verwenden:

```python
from pythonds3.basic import Stack
```

Konzeptionell wichtige Operationen:

```text
push(item)
pop()
peek()
is_empty()
size()
```

Bei einer üblichen Listenimplementierung mit dem **Listenende als Stack-Top** sind `push()` und `pop()` effizient.

Gedanklich:

```python
items.append(item)
items.pop()
```

---

## Linked List

Eine einfach verkettete Liste besitzt keinen direkten Indexzugriff wie eine Python-Liste.

```text
head
 ↓
[A] -> [B] -> [C] -> None
```

Typische Laufzeiten:

| Operation | Laufzeit |
| --- | ---: |
| Zugriff auf `head` | `O(1)` |
| Vorne einfügen | `O(1)` |
| Suche | `O(n)` |
| Zugriff auf Position `k` | `O(k)`, Worst Case `O(n)` |
| Append ohne `tail` | `O(n)` |
| Append mit `tail` | `O(1)` |
| Entfernen des Head | `O(1)` |
| beliebigen Wert suchen und entfernen | Worst Case `O(n)` |

Wichtig:

> Das eigentliche Umhängen einer bekannten Referenz kann `O(1)` sein. Teuer ist häufig das **Finden** des richtigen Nodes.

---

## Warum die konkrete Implementierung zählt

Eine Queue kann mit einer Python-Liste auf verschiedene Arten umgesetzt werden.

### Variante A

```python
queue.append(item)
queue.pop(0)
```

```text
enqueue -> amortisiert O(1)
dequeue -> O(n)
```

### Variante B

```python
queue.insert(0, item)
queue.pop()
```

```text
enqueue -> O(n)
dequeue -> O(1)
```

### Variante C

```python
queue = deque()

queue.append(item)
queue.popleft()
```

```text
enqueue -> O(1)
dequeue -> O(1)
```

Das logische FIFO-Verhalten kann gleich sein, obwohl die Performance unterschiedlich ist.

---

## Praktischer Merksatz

Bei Python-Listen:

```text
Ende günstig
Anfang oft teuer
Index günstig
Suche linear
```

Bei `deque`:

```text
beide Enden günstig
```

Bei `set` und `dict`:

```text
Hash-Lookups durchschnittlich sehr günstig
```

Bei Linked Lists:

```text
Links ändern günstig
Position finden oft linear
```
