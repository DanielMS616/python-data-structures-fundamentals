# ADT, Algorithmus und Implementierung

## 1. Was ist ein abstrakter Datentyp?

Ein **abstrakter Datentyp (ADT)** beschreibt eine Datenstruktur aus Sicht ihres **Verhaltens**:

```text
Welche Daten werden logisch verwaltet?
Welche Operationen sind erlaubt?
Welche Regeln gelten für diese Operationen?
```

Er beschreibt dagegen nicht zwingend:

```text
Wie liegen die Daten konkret im Speicher?
Welche Python-Klasse wird verwendet?
Welche interne Datenstruktur speichert die Werte?
```

Diese Trennung heißt **Abstraktion**.

---

## 2. Beispiel: Stack

Ein Stack wird durch sein Verhalten beschrieben:

```text
push(item)
pop()
peek()
is_empty()
size()
```

und durch die Regel:

```text
LIFO
Last In, First Out
```

Das ist die abstrakte Idee.

Eine mögliche Python-Implementierung ist:

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
```

Hier wird eine Python-Liste verwendet.

Der Stack selbst ist aber nicht mit „Python-Liste“ gleichzusetzen.

---

## 3. Beispiel: Queue

Die abstrakte Queue besitzt typischerweise:

```text
enqueue(item)
dequeue()
is_empty()
size()
```

und die Regel:

```text
FIFO
First In, First Out
```

Sie könnte technisch umgesetzt werden mit:

```text
Python list
collections.deque
Linked List mit front/rear
```

Das Verhalten kann gleich bleiben, obwohl sich die Laufzeiten unterscheiden.

---

## 4. ADT und Implementierung auseinanderhalten

```text
Queue
│
├── Verhalten: FIFO
│
└── mögliche Implementierungen
    ├── Python-Liste
    ├── deque
    └── Linked List
```

Das ist wichtig, weil eine schlechte interne Wahl ein korrektes Verhalten liefern kann, aber unnötig langsam sein kann.

---

## 5. Algorithmus und Implementierung

Auch ein **Algorithmus** ist zunächst unabhängig von einer konkreten Programmiersprache.

Ein Algorithmus ist eine eindeutige Folge von Schritten zur Lösung eines Problems.

Beispiel:

```text
Lineare Suche

1. Beginne beim ersten Element.
2. Vergleiche es mit dem Ziel.
3. Bei Übereinstimmung: Position zurückgeben.
4. Sonst zum nächsten Element gehen.
5. Wenn das Ende erreicht ist: nicht gefunden.
```

Eine konkrete Python-Implementierung könnte sein:

```python
def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index

    return None
```

Der Algorithmus ist die Idee. Der Python-Code ist eine Implementierung davon.

---

## 6. Warum diese Trennung wichtig ist

Sie hilft bei mehreren Fragen:

### Korrektheit

```text
Erfüllt meine Implementierung überhaupt die Regeln des ADT?
```

### Austauschbarkeit

```text
Kann ich die interne Struktur ändern, ohne das äußere Verhalten zu verändern?
```

### Performance

```text
Welche Implementierung liefert die benötigten Laufzeiten?
```

### Kommunikation

```text
Kann ich das Problem erklären, ohne mich sofort in Syntaxdetails zu verlieren?
```

---

## 7. Gleiche Logik, unterschiedliche Laufzeit

### Stack mit Listenende als Top

```python
items.append(value)
items.pop()
```

Typisch:

```text
push -> amortisiert O(1)
pop  -> O(1)
```

### Stack mit Listenanfang als Top

```python
items.insert(0, value)
items.pop(0)
```

Typisch:

```text
push -> O(n)
pop  -> O(n)
```

Beide Varianten können logisch LIFO implementieren.

Die erste ist für eine Python-Liste aber deutlich günstiger.

---

## 8. Queue als besonders gutes Beispiel

### Variante A: Python-Liste, Front am Listenende

```python
items.insert(0, value)
items.pop()
```

```text
enqueue -> O(n)
dequeue -> O(1)
```

### Variante B: Python-Liste, Front am Listenanfang

```python
items.append(value)
items.pop(0)
```

```text
enqueue -> amortisiert O(1)
dequeue -> O(n)
```

### Variante C: `deque`

```python
queue.append(value)
queue.popleft()
```

```text
enqueue -> O(1)
dequeue -> O(1)
```

### Variante D: Linked List mit `front` und `rear`

```text
enqueue -> O(1)
dequeue -> O(1)
```

Das **Queue-Verhalten bleibt FIFO**. Die Implementierung bestimmt aber die Kosten der Operationen.

---

## 9. Interface und interne Repräsentation

Eine gute Denkweise:

```text
Außen:
Was darf ein Benutzer der Klasse tun?

Innen:
Wie speichert die Klasse ihren Zustand?
```

Beispiel:

```python
class Queue:
    def enqueue(self, item):
        ...

    def dequeue(self):
        ...
```

Ein Benutzer der Queue sollte nicht davon abhängig sein, ob intern:

```python
list
```

oder:

```python
deque
```

verwendet wird.

---

## 10. Verträge und Randfälle

Ein ADT besteht nicht nur aus Methodennamen.

Auch Randfälle gehören zur Schnittstelle.

Beispiel:

```python
queue.dequeue()
```

auf einer leeren Queue.

Mögliche Entscheidungen:

```text
None zurückgeben
Exception auslösen
speziellen Sentinel zurückgeben
```

Keine Variante ist automatisch immer richtig.

Wichtig ist:

> Das Verhalten sollte bewusst entschieden und konsistent dokumentiert werden.

---

## 11. Invarianten

Eine **Invariante** ist eine Bedingung, die nach jeder gültigen Operation weiterhin stimmen muss.

Beispiel Linked List mit `head` und `tail`:

```text
leere Liste:
head = None
tail = None
```

Bei genau einem Knoten:

```text
head is tail
```

Bei einer nicht leeren Liste:

```text
tail.next is None
```

Wird eine Methode ergänzt, muss sie diese Regeln weiterhin erhalten.

---

## 12. Verbindung zu den Übungen

Dieses Repository enthält mehrere Beispiele dafür, dass die richtige Implementierung aus den geforderten Operationen abgeleitet wird:

```text
PriorityQueue:
Sortierarbeit wird in enqueue verschoben,
damit dequeue O(1) sein kann.

MaxQueue:
Eine zusätzliche Hilfsqueue wird gepflegt,
damit get_max O(1) ist.

LinkedList mit tail:
Eine zusätzliche Referenz wird gespeichert,
damit append O(1) ist.

remove_duplicates:
Ein Set verbraucht zusätzlichen Speicher,
damit die Duplikatprüfung durchschnittlich O(1) ist.
```

---

## Merksatz

> **ADT = Was soll die Struktur tun?**  
> **Implementierung = Wie wird dieses Verhalten technisch realisiert?**  
> **Algorithmusanalyse = Was kostet diese konkrete Lösung?**
