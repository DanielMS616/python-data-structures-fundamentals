# `LinkedList.reverse()` – Eine verkettete Liste in-place umkehren

## Ziel der Übung

Die Methode

```python
reverse()
```

soll die Richtung aller `next`-Verknüpfungen einer Linked List **in-place** umdrehen.

In-place bedeutet:

> Die vorhandenen Nodes werden weiterverwendet. Es wird keine zweite Linked List mit neuen Nodes aufgebaut.

Beispiel:

```text
Vorher:
5 -> 6 -> 7 -> None

Nachher:
7 -> 6 -> 5 -> None
```

Die allgemeinen Linked-List-Grundlagen sind in [`README.md`](README.md) zusammengefasst.

Hier liegt der Fokus auf dem **sicheren Umhängen von Referenzen mit Previous / Current / Next**.

---

## Quick Summary

| Aspekt | Ergebnis |
| --- | --- |
| Muster | Previous / Current / Next |
| Veränderung | in-place |
| Laufzeit | `O(n)` |
| Zusatzspeicher | `O(1)` |
| Kernidee | Nächsten Node sichern, bevor `current.next` verändert wird |
| wichtigste Gefahr | Verbindung zum unbearbeiteten Rest verlieren |
| Datenintegrität | alter Head muss zum neuen Tail mit `next = None` werden |

---

## Relevante Implementierung

```python
class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def reverse(self) -> None:
        previous: Node | None = None
        current = self.head

        while current:
            next_node = current.next

            current.next = previous

            previous = current
            current = next_node

        self.head = previous
```

Die vollständige und aktuelle Implementierung befindet sich in [`linked_list_reverse.py`](linked_list_reverse.py).

---

## Was „in-place“ hier bedeutet

Die vorhandenen Nodes:

```text
[5] -> [6] -> [7] -> None
```

werden nicht kopiert.

Stattdessen werden nur ihre `next`-Referenzen umgedreht:

```text
[5] <- [6] <- [7]
               ↑
              head
```

In normaler Leserichtung:

```text
head
 ↓
[7] -> [6] -> [5] -> None
```

Damit bleiben dieselben Objekte erhalten.

---

## Die drei wichtigen Referenzen

### `previous`

```python
previous: Node | None = None
```

zeigt auf den bereits umgedrehten Teil der Liste.

Am Anfang existiert dieser Teil noch nicht.

### `current`

```python
current = self.head
```

zeigt auf den Node, der gerade bearbeitet wird.

### `next_node`

```python
next_node = current.next
```

sichert den ursprünglichen Nachfolger von `current`.

Diese Referenz ist der entscheidende Schutz davor, den noch nicht bearbeiteten Rest der Liste zu verlieren.

---

## Die entscheidende Reihenfolge

Für jeden Node passieren immer vier Schritte:

```text
1. nächsten Node sichern
2. aktuellen Link umdrehen
3. previous weiterschieben
4. current weiterschieben
```

Im Code:

```python
next_node = current.next
current.next = previous
previous = current
current = next_node
```

Die Reihenfolge ist nicht beliebig.

---

## Warum `next_node` zuerst gespeichert werden muss

Ausgang:

```text
[5] -> [6] -> [7] -> None
```

`current` zeigt auf `5`.

Wenn sofort:

```python
current.next = previous
```

ausgeführt wird, zeigt `5.next` anschließend auf:

```text
None
```

Die ursprüngliche Verbindung zu `6` wäre damit über `current` verloren.

Deshalb zuerst:

```python
next_node = current.next
```

Damit bleibt der Rest der Liste erreichbar, auch nachdem der aktuelle Link umgedreht wurde.

---

## Schritt für Schritt

Ausgang:

```text
previous -> None
current  -> 5

[5] -> [6] -> [7] -> None
```

### Iteration 1

```text
next_node -> 6
5.next    -> None
previous  -> 5
current   -> 6
```

Bereits umgedreht:

```text
5 -> None
```

Noch unbearbeitet:

```text
6 -> 7 -> None
```

### Iteration 2

```text
next_node -> 7
6.next    -> 5
previous  -> 6
current   -> 7
```

Bereits umgedreht:

```text
6 -> 5 -> None
```

### Iteration 3

```text
next_node -> None
7.next    -> 6
previous  -> 7
current   -> None
```

Die Schleife endet.

---

## Warum `self.head = previous` notwendig ist

Nach der letzten Iteration zeigt:

```python
previous
```

auf den ursprünglich letzten Node:

```text
7
```

Dieser Node ist jetzt der neue Listenanfang.

Deshalb:

```python
self.head = previous
```

Ergebnis:

```text
head
 ↓
[7] -> [6] -> [5] -> None
```

---

## Warum der alte Head korrekt zum Tail wird

Am Anfang ist:

```python
previous = None
```

Beim ersten Node wird deshalb:

```python
current.next = previous
```

zu:

```text
old_head.next = None
```

Der alte erste Node wird damit automatisch zum neuen letzten Node.

Das ist wichtig, um:

```text
keinen Zyklus
kein altes Vorwärtsende
korrektes Listenende
```

zu erhalten.

---

## Gefährlicher Fehler: falsche Reihenfolge

Problematisch wäre zum Beispiel:

```python
current.next = previous
current = current.next
```

Nach dem ersten Befehl zeigt:

```python
current.next
```

bereits **rückwärts**.

Der zweite Befehl würde daher nicht zum ursprünglichen nächsten Node weitergehen.

Die Verbindung zum unbearbeiteten Rest wäre verloren.

Genau deshalb ist:

```python
next_node = current.next
```

vor dem Umdrehen unverzichtbar.

---

## Komplexität

### Laufzeit

Jeder Node wird genau einmal verarbeitet:

```python
while current:
```

Pro Node erfolgen nur konstante Referenzoperationen.

Damit:

```text
reverse() -> O(n)
```

### Zusatzspeicher

Es werden nur drei lokale Referenzen verwendet:

```text
previous
current
next_node
```

Ihre Anzahl hängt nicht von `n` ab.

Damit:

```text
O(1)
```

zusätzlicher Speicher.

---

## Randfälle

### Leere Liste

```text
head = None
```

`current` ist sofort `None`.

Die Schleife läuft nicht.

`self.head = previous` setzt erneut:

```text
None
```

Die Liste bleibt korrekt leer.

### Ein Node

```text
[5] -> None
```

Der einzige Link wird auf `None` gesetzt, was bereits der korrekte Zustand ist.

`head` zeigt anschließend weiterhin auf `5`.

Es ist keine Sonderlogik nötig.

---

## Datenintegrität

Bei dieser Aufgabe liegen die wichtigsten Fehler nicht in Benutzereingaben, sondern im **internen Zustand der Datenstruktur**.

Nach `reverse()` muss gelten:

```text
kein Node verloren
jeder next-Link korrekt umgedreht
kein unbeabsichtigter Zyklus
neuer head korrekt gesetzt
alter head.next == None
```

Das macht die Aufgabe zu einem guten Beispiel dafür, dass Robustheit bei Datenstrukturen oft bedeutet, **Referenz-Invarianten** zu schützen.

---

## Warum keine neue Liste verwendet wird

Eine alternative Lösung könnte:

```text
Werte lesen
neue Nodes erzeugen
neue Liste rückwärts aufbauen
```

Das würde zusätzlichen Speicher benötigen.

Die In-place-Lösung verwendet stattdessen:

```text
Laufzeit:       O(n)
Zusatzspeicher: O(1)
```

und verändert nur die vorhandenen Verknüpfungen.

---

## Hinweis zu `append()`

Die `append()`-Methode dieser eigenständigen Übungsdatei sucht das Ende weiterhin durch Traversieren:

```python
while last_node.next:
    last_node = last_node.next
```

Damit gilt dort:

```text
append() -> O(n)
```

Das ist bewusst nicht das Lernziel dieser Datei.

Die separate Übung [`linked_list_append_o1_explanation.md`](linked_list_append_o1_explanation.md) behandelt die Optimierung mit einem `tail`-Pointer.

---

## Typvertrag

Die aktuelle Methode lautet:

```python
reverse(self) -> None
```

Sie gibt keinen neuen Listenwert zurück, sondern verändert die bestehende Linked List **in-place**.

---

## Tests

Der ursprüngliche Lernfall kehrt:

```text
5 -> 6
```

um zu:

```text
6 -> 5
```

Die Implementierung wird inzwischen zusätzlich automatisiert mit `pytest` geprüft:

[`../tests/test_linked_lists.py`](../tests/test_linked_lists.py)

Dort werden unter anderem getestet:

```text
mehrere Nodes
leere Liste
ein einzelner Node
```

---

## Design- und Skalierungsgedanke

Die Aufgabe zeigt den Unterschied zwischen:

```text
Daten kopieren
```

und:

```text
bestehende Struktur verändern
```

Die In-place-Variante spart zusätzlichen Speicher, erhöht aber die Anforderungen an die korrekte Reihenfolge der Referenzänderungen.

Das ist ein typischer Trade-off:

```text
weniger Zusatzspeicher
↔
höhere Sorgfalt bei Mutation
```

Bei mutable Datenstrukturen ist es deshalb besonders wichtig, vor jeder Änderung zu fragen:

> Welche Referenz brauche ich nach diesem Schritt noch?

---

## Zentrale Lernidee

Die zentrale Erkenntnis lautet:

> **Beim In-place-Umkehren einer Linked List muss der ursprüngliche nächste Node immer zuerst gespeichert werden, bevor die aktuelle `next`-Referenz umgedreht wird.**

Der Kernalgorithmus:

```python
next_node = current.next
current.next = previous
previous = current
current = next_node
```

ist ein wiederverwendbares Referenzmuster für strukturelle Änderungen an verketteten Listen.

---

## Weiterführend

- [`README.md`](README.md) – Linked-List-Grundlagen und Referenzinvarianten
- [`linked_list_append_o1_explanation.md`](linked_list_append_o1_explanation.md) – Tail Pointer und zusätzliche Invarianten
- [`../docs/data_structure_patterns.md`](../docs/data_structure_patterns.md) – Previous / Current / Next
- [`../docs/big_o_cheatsheet.md`](../docs/big_o_cheatsheet.md) – Zeit- und Speicherkomplexität
- [`../tests/test_linked_lists.py`](../tests/test_linked_lists.py) – automatisierte Tests
