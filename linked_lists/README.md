# Linked Lists

## Überblick

Eine **Linked List (verkettete Liste)** besteht aus einzelnen Nodes, die über Referenzen miteinander verbunden sind.

Bei einer einfach verketteten Liste besitzt jeder Node typischerweise:

```text
data
next
```

Beispiel:

```text
head
 ↓
[5 | •] -> [6 | •] -> [7 | None]
```

Der letzte Node zeigt mit `next` auf:

```text
None
```

---

## Node

Eine einfache Node-Klasse:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Ein isolierter Node:

```text
[5 | None]
```

Erst über `next` wird er Teil einer Kette.

---

## `head`

`head` ist die Referenz auf den ersten Node.

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

Leere Liste:

```text
head
 ↓
None
```

Nicht leer:

```text
head
 ↓
[A] -> [B] -> [C] -> None
```

---

## Warum Linked Lists?

Eine Linked List erlaubt es, Verbindungen zwischen bekannten Nodes direkt zu ändern.

Beispiel:

```text
[A] -> [B] -> [C]
```

Wenn `A` direkt auf `C` zeigen soll:

```python
a.next = c
```

Es müssen keine nachfolgenden Elemente wie bei einem dynamischen Array verschoben werden.

Der Preis:

> Es gibt keinen direkten Indexzugriff auf beliebige Positionen.

Um zum dritten Node zu gelangen, muss vom `head` aus weitergelaufen werden.

---

## Einfaches Einfügen am Anfang

```python
def add_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

Laufzeit:

```text
O(1)
```

Es ist keine Suche notwendig.

---

## Append ohne `tail`

```python
last_node = self.head

while last_node.next:
    last_node = last_node.next

last_node.next = new_node
```

Das Ende muss gesucht werden.

Worst Case:

```text
O(n)
```

---

## Append mit `tail`

Eine zusätzliche Referenz:

```python
self.tail
```

zeigt direkt auf den letzten Node.

```text
head              tail
 ↓                  ↓
[A] -> [B] -> [C] -> None
```

Dann:

```python
self.tail.next = new_node
self.tail = new_node
```

Laufzeit:

```text
O(1)
```

---

## Neue Performance, neue Invariante

Ein `tail` macht `append()` schneller.

Dafür muss `tail` nach jeder strukturellen Änderung korrekt bleiben.

Beispiele:

```text
leere Liste:
head = None
tail = None

ein Node:
head is tail

nicht leere Liste:
tail.next is None
```

Performance-Optimierungen erzeugen also manchmal zusätzlichen Zustand, der gepflegt werden muss.

---

## Suchen

```python
current = self.head

while current:
    if current.data == target:
        ...
    current = current.next
```

Worst Case:

```text
O(n)
```

Es existiert kein direkter Sprung zu einem beliebigen Index.

---

## Typische Laufzeiten

| Operation | Typisch |
| --- | ---: |
| `head` lesen | `O(1)` |
| vorne einfügen | `O(1)` |
| Append ohne `tail` | `O(n)` |
| Append mit `tail` | `O(1)` |
| Suche | `O(n)` |
| Indexzugriff | `O(n)` |
| Head entfernen | `O(1)` |
| Wert suchen und entfernen | Worst Case `O(n)` |

Wichtig:

> Wenn der zu ändernde Node bereits bekannt ist, kann das eigentliche Umhängen einer Referenz `O(1)` sein. Häufig kostet das **Finden** des Nodes `O(n)`.

---

## Muster: Previous / Current / Next

Beim In-place-Umkehren einer Liste müssen Links verändert werden, ohne den restlichen Teil zu verlieren.

```python
previous = None
current = self.head

while current:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

self.head = previous
```

Die Reihenfolge ist entscheidend.

```text
1. nächsten Node sichern
2. Link umdrehen
3. previous weiterschieben
4. current weiterschieben
```

---

## In-place Reverse

Vorher:

```text
head
 ↓
[5] -> [6] -> [7] -> None
```

Nachher:

```text
head
 ↓
[7] -> [6] -> [5] -> None
```

Es werden keine neuen Nodes erzeugt.

Laufzeit:

```text
O(n)
```

Zusätzlicher Speicher:

```text
O(1)
```

---

## Muster: Seen Set

Bei Duplikaten wollen wir wissen:

```text
Habe ich diesen Wert schon gesehen?
```

Dafür:

```python
seen = set()
```

Bei einem Duplikat kann der aktuelle Node übersprungen werden:

```python
previous.next = current.next
```

Das Set benötigt zusätzlichen Speicher:

```text
O(n)
```

ermöglicht aber durchschnittliche Membership-Tests von:

```text
O(1)
```

---

## Warum `previous` bei einem Duplikat stehen bleibt

Beispiel:

```text
5 -> 5 -> 5 -> 6
```

`previous` zeigt nach dem ersten `5` weiterhin auf diesen gültigen Node.

Die folgenden doppelten `5` können nacheinander übersprungen werden.

Erst bei einem neuen Wert bewegt sich `previous` weiter.

---

## Muster: Slow / Fast Pointer

Mitte finden, ohne zuerst die Länge zu bestimmen:

```python
slow = self.head
fast = self.head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

```text
slow -> ein Schritt
fast -> zwei Schritte
```

Wenn `fast` das Ende erreicht, ist `slow` in der Mitte.

Bei gerader Node-Anzahl landet diese Variante auf dem zweiten mittleren Node.

---

## Beispiel

```text
5 -> 6 -> 7 -> 8
```

Start:

```text
slow = 5
fast = 5
```

Dann:

```text
slow = 6
fast = 7
```

Dann:

```text
slow = 7
fast = None
```

Ergebnis:

```text
7
```

---

## Zyklen

Eine normale einfach verkettete Liste endet bei:

```text
None
```

Eine fehlerhafte oder bewusst zyklische Struktur könnte dagegen so aussehen:

```text
[A] -> [B] -> [C]
       ↑        |
       └────────┘
```

Dann existiert kein normales Ende.

Ein einfacher Traversal-Loop könnte endlos laufen.

Slow/Fast Pointer können auch zur Zyklenerkennung verwendet werden, obwohl das in den aktuellen Übungen noch nicht implementiert wird.

---

## Bewusst eigenständige Übungsdateien

Die Implementierungen in diesem Ordner sind bewusst in sich geschlossen. Gemeinsame Bestandteile wie `Node`, `append()` oder `__str__()` wiederholen sich daher teilweise zwischen den einzelnen Dateien.

Dadurch kann jede Übung unabhängig gelesen, ausgeführt und nachvollzogen werden, ohne zuerst gemeinsame Hilfsmodule oder eine übergeordnete Klassenstruktur verstehen zu müssen.

In produktivem Code würde gemeinsam verwendete Logik normalerweise extrahiert werden, um Duplikation zu reduzieren und Änderungen zentral pflegen zu können. In diesem Lern-Repository ist die Wiederholung jedoch eine bewusste didaktische Entscheidung:

```text
Unabhängigkeit der Beispiele
+
direkte Nachvollziehbarkeit
+
vollständiger Übungskontext
```

Diese Aspekte haben hier Vorrang vor einer strikt angewendeten DRY-Struktur.

Die Duplikation entsteht damit nicht aus fehlender Wiederverwendung, sondern aus dem Ziel, jede Übung als eigenständiges Lern- und Referenzbeispiel erhalten zu können.

---

## Übungen in diesem Ordner

### Append in O(1)

- [`linked_list_append_o1.py`](linked_list_append_o1.py)
- [`linked_list_append_o1_explanation.md`](linked_list_append_o1_explanation.md)

Lernideen:

```text
tail
direkter Endzugriff
Invarianten
```

### In-place Reverse

- [`linked_list_reverse.py`](linked_list_reverse.py)
- [`linked_list_reverse_explanation.md`](linked_list_reverse_explanation.md)

Lernideen:

```text
previous / current / next
Referenzen sicher verändern
O(1) zusätzlicher Speicher
```

### Duplikate entfernen

- [`linked_list_remove_duplicates.py`](linked_list_remove_duplicates.py)
- [`linked_list_remove_duplicates_explanation.md`](linked_list_remove_duplicates_explanation.md)

Lernideen:

```text
Set
previous bleibt bei Duplikat stehen
Speicher-vs.-Laufzeit-Trade-off
```

### Mitte finden

- [`linked_list_find_middle.py`](linked_list_find_middle.py)
- [`linked_list_find_middle_explanation.md`](linked_list_find_middle_explanation.md)

Lernideen:

```text
slow / fast
Mitte ohne Längenberechnung
O(1) Zusatzspeicher
```

---

## Typische Randfälle

Bei Linked Lists sollten häufig mindestens diese Fälle gedanklich geprüft werden:

```text
leere Liste
nur ein Node
zwei Nodes
Head wird verändert
letzter Node wird verändert
mehrere gleiche Werte hintereinander
zyklische Struktur
```

Nicht jede Übung muss alle Fälle explizit unterstützen.

Wichtig ist, die zugrunde liegenden Annahmen zu kennen.

---

## Datenintegrität statt nur Input-Validierung

Bei Linked Lists liegen viele Fehler nicht in falschen Benutzereingaben, sondern in einer beschädigten internen Struktur.

Beispiele:

```text
Node geht verloren
next zeigt auf falschen Node
tail wird nicht aktualisiert
Zyklus entsteht unbeabsichtigt
head zeigt nicht mehr auf den Listenanfang
```

Darum ist bei Pointer-Algorithmen besonders wichtig:

> Vor jeder Änderung überlegen, welche Referenz danach noch benötigt wird.

---

## Technischer Python-Hinweis

In Python ist es normalerweise nicht notwendig, einen lokal entfernten Node zusätzlich manuell auf:

```python
current = None
```

zu setzen, damit sein Speicher freigegeben wird.

Sobald keine erreichbare Referenz mehr auf das Objekt existiert, kann Python es automatisch verwalten.

Der entscheidende Schritt beim Entfernen ist die korrekte Änderung der Verkettung:

```python
previous.next = current.next
```

---

## Kurzreferenz

```text
Linked List
-----------
Node:
data + next

head:
erster Node

tail:
optionale Referenz auf letzten Node

Stärken:
Links gezielt ändern
am Anfang O(1) einfügen
mit tail O(1) anhängen

Schwächen:
kein direkter Indexzugriff
Suche typischerweise O(n)

Wichtige Muster:
previous/current/next
slow/fast
seen set
head/tail invariants
```

Weiterführend:

- [`../docs/data_structure_patterns.md`](../docs/data_structure_patterns.md)
- [`../docs/python_collections_complexity.md`](../docs/python_collections_complexity.md)
- [`../docs/glossary.md`](../docs/glossary.md)
