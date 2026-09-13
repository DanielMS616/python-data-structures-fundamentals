# `LinkedList.append()` – In O(1) an eine verkettete Liste anhängen

## Ziel der Übung

Eine einfach verkettete Liste soll eine Methode

```python
append(data)
```

erhalten, die neue Nodes am Listenende in:

```text
O(1)
```

anhängt.

Dafür muss die Klasse den letzten Node direkt erreichen können. Außerdem muss der Übergang von einer leeren zu einer ein-elementigen Liste konsistent behandelt werden.

Die allgemeinen Grundlagen zu Nodes, `head`, `tail` und typischen Linked-List-Operationen sind in [`README.md`](README.md) zusammengefasst.

Hier liegt der Fokus auf der **gezielten Verwendung einer zusätzlichen `tail`-Referenz**, um eine sonst lineare Operation konstant schnell zu machen.

---

## Quick Summary

| Aspekt | Ergebnis |
| --- | --- |
| Datenstruktur | einfach verkettete Liste |
| zusätzliche Referenz | `tail` |
| Muster | gespeicherter Direktzugriff auf das Listenende |
| `append()` | `O(1)` |
| `__str__()` | `O(n)` |
| Zusatzspeicher für `tail` | `O(1)` |
| Kernidee | Das Listenende wird nicht gesucht, sondern direkt gespeichert |
| Wichtige Invariante | `tail` zeigt immer auf den letzten Node |

---

## Relevante Implementierung

Der entscheidende Teil der aktuellen Lösung ist:

```python
class Node:
    def __init__(self, data: object) -> None:
        self.data: object = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def append(self, data: object) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        assert self.tail is not None

        self.tail.next = new_node
        self.tail = new_node
```

Die vollständige und aktuelle Implementierung befindet sich in [`linked_list_append_o1.py`](linked_list_append_o1.py).

---

## Warum `tail` notwendig ist

Ohne eine zusätzliche Referenz auf das Listenende müsste `append()` bei `head` starten und so lange weiterlaufen, bis der letzte Node gefunden wurde:

```python
current = self.head

while current.next is not None:
    current = current.next
```

Bei `n` Nodes kostet diese Suche im Worst Case:

```text
O(n)
```

Mit:

```python
self.tail
```

ist der letzte Node bereits bekannt.

Dadurch kann direkt verbunden werden:

```python
self.tail.next = new_node
self.tail = new_node
```

Es ist kein Traversieren der vorhandenen Liste nötig.

---

## Der Sonderfall: leere Liste

Zu Beginn gilt:

```text
head = None
tail = None
```

Beim ersten:

```python
append(5)
```

ist der neue Node gleichzeitig:

```text
erster Node
+
letzter Node
```

Deshalb:

```python
self.head = new_node
self.tail = new_node
```

Danach gilt:

```text
head
 ↓
[5] -> None
 ↑
tail
```

Für eine Liste mit genau einem Element zeigen `head` und `tail` also auf **dasselbe Objekt**.

---

## Weitere Elemente anhängen

Nach:

```text
head
 ↓
[5] -> None
 ↑
tail
```

wird ein neuer Node `6` erzeugt.

Zuerst wird der bisherige letzte Node mit ihm verbunden:

```python
self.tail.next = new_node
```

Dann wird `tail` weitergeschoben:

```python
self.tail = new_node
```

Ergebnis:

```text
head       tail
 ↓           ↓
[5] -> [6] -> None
```

Der Aufwand bleibt unabhängig von der Listenlänge gleich.

---

## Warum das `assert` sinnvoll ist

Nach dem leeren Fall folgt:

```python
assert self.tail is not None
```

Die Klasse besitzt die Invariante:

> Wenn `head` auf einen Node zeigt, muss auch `tail` auf einen Node zeigen.

Der Type Checker kann diese Beziehung zwischen zwei Attributen nicht automatisch ableiten.

Das `assert` dokumentiert deshalb gleichzeitig:

```text
Programmlogik
+
Typannahme
+
Klasseninvariante
```

Sollte `head` gesetzt sein, `tail` aber `None`, wäre der interne Zustand der Datenstruktur bereits inkonsistent.

---

## Die zentrale Invariante

Mit der zusätzlichen `tail`-Referenz entsteht neuer Zustand, der nach jeder strukturellen Änderung korrekt bleiben muss.

Es sollten immer diese Regeln gelten:

```text
leere Liste:
head = None
tail = None

genau ein Node:
head is tail

nicht leere Liste:
head -> erster Node
tail -> letzter Node
tail.next is None
```

Das ist der Preis der Optimierung:

```text
mehr gespeicherter Zustand
→ schnellere Operation
→ zusätzliche Konsistenzregel
```

---

## Warum `append()` O(1) ist

Die Methode führt nur eine konstante Anzahl von Operationen aus:

```text
Node erzeugen
Referenzen prüfen
next setzen
tail aktualisieren
```

Es gibt:

```text
keine Suche
keine Schleife über bestehende Nodes
keinen von n abhängigen Traversal
```

Damit gilt:

```text
append() -> O(1)
```

Ob die Liste 10 oder 1.000.000 Nodes enthält, verändert die Anzahl der notwendigen Schritte nicht.

---

## Speicherkomplexität

Die eigentliche Linked List benötigt für `n` Nodes insgesamt:

```text
O(n)
```

Speicher.

Die zusätzliche Referenz:

```python
self.tail
```

benötigt nur:

```text
O(1)
```

zusätzlichen Speicher.

Wir investieren also eine einzelne Referenz, um `append()` von:

```text
O(n)
```

auf:

```text
O(1)
```

zu verbessern.

---

## `__str__()` ist bewusst weiterhin O(n)

Für eine lesbare Darstellung muss jeder Node besucht werden:

```python
current = self.head

while current:
    ...
    current = current.next
```

Deshalb gilt:

```text
__str__() -> O(n)
```

Das widerspricht der Optimierung von `append()` nicht.

Unterschiedliche Operationen derselben Datenstruktur können unterschiedliche Laufzeiten besitzen.

---

## Rand- und Konsistenzfälle

### Leere Liste

```text
head = None
tail = None
```

### Erster Node

```text
head is tail
```

### Mehrere Nodes

```text
head -> erster Node
tail -> letzter Node
tail.next -> None
```

Der wichtigste Robustheitsaspekt dieser Übung ist nicht Eingabevalidierung, sondern die **Konsistenz dieser Referenzen**.

---

## Typvertrag

Die aktuelle Schnittstelle lautet:

```python
append(self, data: object) -> None
```

Die Liste akzeptiert damit zunächst beliebige Python-Objekte.

`append()` verändert die bestehende Struktur und gibt keinen Wert zurück.

---

## Tests

Der ursprüngliche Lernfall hängt nacheinander an:

```text
5
6
7
```

und erwartet:

```text
5->6->7
```

Die Implementierung wird inzwischen automatisiert mit `pytest` geprüft:

[`../tests/test_linked_lists.py`](../tests/test_linked_lists.py)

Besonders wichtig sind dort die strukturellen Invarianten:

```text
head zeigt auf den ersten Node
tail zeigt auf den letzten Node
tail.next is None
bei einem Node: head is tail
```

---

## Design- und Skalierungsgedanke

Diese Übung zeigt einen klassischen Trade-off:

```text
ohne tail:
weniger Zustand
append() -> O(n)

mit tail:
eine zusätzliche Referenz
append() -> O(1)
```

Dasselbe Grundprinzip taucht in vielen Bereichen wieder auf:

```text
Caches
Datenbankindizes
Lookup-Strukturen
vorberechnete Metadaten
```

Zusätzliche Information wird gespeichert, damit eine häufige oder kritische Operation schneller wird.

---

## Zentrale Lernidee

Die zentrale Erkenntnis lautet:

> **Ein zusätzlicher `tail`-Zeiger speichert direkt, wo sich das Ende der Linked List befindet, und macht `append()` dadurch zu einer O(1)-Operation.**

Die Optimierung bringt gleichzeitig eine neue Verantwortung mit sich:

> Jede Methode, die die Struktur verändert, muss künftig auch die `tail`-Invariante berücksichtigen.

Damit zeigt die Übung nicht nur eine Performance-Optimierung, sondern auch den Zusammenhang zwischen **zusätzlichem Zustand und Datenintegrität**.

---

## Weiterführend

- [`README.md`](README.md) – Grundlagen, `head`, `tail` und typische Linked-List-Operationen
- [`../docs/data_structure_patterns.md`](../docs/data_structure_patterns.md) – Tail Pointer und gespeicherte Zusatzinformation
- [`../docs/big_o_cheatsheet.md`](../docs/big_o_cheatsheet.md) – `O(1)` gegenüber `O(n)`
- [`../tests/test_linked_lists.py`](../tests/test_linked_lists.py) – automatisierte Tests
