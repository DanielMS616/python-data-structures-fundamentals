# Glossar

## ADT – Abstract Data Type

Logische Beschreibung einer Datenstruktur über ihr Verhalten und ihre Operationen, unabhängig von einer konkreten Implementierung.

---

## Algorithmus

Endliche und eindeutige Folge von Schritten zur Lösung eines Problems.

---

## Implementierung

Konkrete technische Umsetzung eines Algorithmus oder ADT in einer Programmiersprache.

---

## Big O

Notation zur Beschreibung der Wachstumsrate von Zeit- oder Speicherbedarf bei wachsender Eingabegröße.

---

## `n`

Übliche Variable für die relevante Eingabegröße.

Beispiele:

```text
Anzahl Listenelemente
Anzahl Nodes
Länge eines Strings
```

---

## Worst Case

Eingabe, bei der ein Algorithmus die größte relevante Arbeit benötigt.

---

## Amortisierte Laufzeit

Durchschnittliche Kosten einer Operation über eine ganze Folge von Operationen.

Beispiel:

```text
list.append() -> amortisiert O(1)
```

---

## LIFO

**Last In, First Out**

Das zuletzt eingefügte Element wird zuerst entfernt.

Typische Struktur:

```text
Stack
```

---

## FIFO

**First In, First Out**

Das zuerst eingefügte Element wird zuerst entfernt.

Typische Struktur:

```text
Queue
```

---

## Stack

ADT mit Operationen wie:

```text
push
pop
peek
is_empty
```

und LIFO-Verhalten.

---

## Queue

ADT mit Operationen wie:

```text
enqueue
dequeue
is_empty
```

und FIFO-Verhalten.

---

## Node

Ein einzelnes Element einer verketteten Datenstruktur.

Bei einer einfach verketteten Liste typischerweise:

```text
data
next
```

---

## Linked List

Datenstruktur aus miteinander verknüpften Nodes.

```text
[A] -> [B] -> [C] -> None
```

---

## `head`

Referenz auf den ersten Node einer Linked List.

---

## `tail`

Referenz auf den letzten Node einer Linked List.

---

## `front`

Bei einer Queue häufig die Position des nächsten Elements, das entfernt wird.

---

## `rear`

Bei einer Queue häufig die Position, an der neue Elemente angehängt werden.

---

## Referenz / Pointer

Verweis auf ein anderes Objekt bzw. einen anderen Node.

In Python arbeiten Variablen mit Objektreferenzen. Der Begriff „Pointer“ wird bei Algorithmen oft konzeptionell verwendet.

---

## In-place

Eine bestehende Struktur wird direkt verändert, statt eine vollständige neue Struktur aufzubauen.

Beispiel:

```text
Linked List durch Umhängen der next-Referenzen umkehren
```

---

## Invariante

Bedingung, die nach jeder gültigen Operation einer Datenstruktur weiterhin stimmen muss.

Beispiel:

```text
tail.next is None
```

---

## Hashbar

Ein Wert besitzt einen stabilen Hash und kann beispielsweise als Set-Element oder Dictionary-Key verwendet werden.

Typisch hashbar:

```text
int
str
tuple
```

Typisch nicht hashbar:

```text
list
dict
set
```

---

## `deque`

Double-ended Queue aus `collections`.

Effiziente Operationen an beiden Enden:

```python
append()
appendleft()
pop()
popleft()
```

---

## Monotone Queue

Hilfsqueue, deren Elemente in einer geordneten Form gehalten werden, sodass z. B. ein aktuelles Maximum oder Minimum direkt verfügbar ist.

---

## Slow/Fast Pointer

Zwei Referenzen bewegen sich mit unterschiedlichen Geschwindigkeiten durch eine Struktur.

Typische Anwendungen:

```text
Mitte einer Linked List
Zyklenerkennung
```

---

## Stable Order / stabile Reihenfolge

Bei gleichem Sortier- oder Prioritätskriterium bleibt die ursprüngliche relative Reihenfolge erhalten.

In der PriorityQueue wird das explizit über einen Counter modelliert.

---

## Early Return

Eine Funktion wird sofort verlassen, sobald das Ergebnis bereits eindeutig feststeht.

Beispiel:

```python
if stack.is_empty():
    return False
```

---

## Trade-off

Bewusster Austausch eines Vorteils gegen einen anderen.

Beispiele:

```text
mehr Speicher <-> weniger Laufzeit
mehr Zustand <-> schnellere Operation
teurere enqueue-Operation <-> schnelleres dequeue
```
