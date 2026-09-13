# `LinkedList.find_middle()` – Die Mitte einer verketteten Liste finden

## Ziel der Übung

Die Methode

```python
find_middle()
```

soll den Wert des mittleren Nodes bestimmen, **ohne vorher die Listenlänge zu berechnen**.

Dafür werden zwei Referenzen verwendet, die sich unterschiedlich schnell durch die Liste bewegen.

Bei einer geraden Anzahl von Nodes soll der **zweite** der beiden mittleren Nodes zurückgegeben werden.

Beispiele:

```text
5 -> 6 -> 7
     ↑
   Mitte
```

Ergebnis:

```text
6
```

und:

```text
5 -> 6 -> 7 -> 8
          ↑
     zweite Mitte
```

Ergebnis:

```text
7
```

Die allgemeinen Linked-List-Grundlagen stehen in [`README.md`](README.md).

Hier liegt der Fokus auf dem **Slow/Fast-Pointer-Muster**.

---

## Quick Summary

| Aspekt | Ergebnis |
| --- | --- |
| Muster | Slow / Fast Pointer |
| `slow` | 1 Node pro Runde |
| `fast` | 2 Nodes pro Runde |
| Laufzeit | `O(n)` |
| Zusatzspeicher | `O(1)` |
| gerade Node-Anzahl | zweiter mittlerer Node |
| Kernidee | Wenn `fast` das Ende erreicht, steht `slow` in der Mitte |

---

## Relevante Implementierung

```python
class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def find_middle(self) -> object | None:
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data if slow else None
```

Die vollständige und aktuelle Implementierung befindet sich in [`linked_list_find_middle.py`](linked_list_find_middle.py).

---

## Grundidee: zwei unterschiedlich schnelle Referenzen

Beide starten bei:

```python
self.head
```

Dann gilt pro Schleifenrunde:

```text
slow -> 1 Schritt
fast -> 2 Schritte
```

Wenn `fast` das Ende erreicht, hat `slow` ungefähr halb so viele Nodes durchlaufen.

Damit befindet sich `slow` in der Mitte.

Das Muster wird häufig als:

```text
Slow / Fast Pointer
```

oder:

```text
Tortoise and Hare
```

bezeichnet.

---

## Warum das mathematisch funktioniert

Angenommen, die Liste enthält `n` Nodes.

`fast` bewegt sich mit doppelter Geschwindigkeit und benötigt ungefähr:

```text
n / 2
```

Schleifenrunden bis zum Ende.

In denselben Runden legt `slow` genau einen Schritt zurück.

Nach ungefähr `n / 2` Schritten steht `slow` deshalb in der Mitte.

---

## Beispiel mit ungerader Anzahl

```text
5 -> 6 -> 7 -> 8 -> 9
```

Start:

```text
slow -> 5
fast -> 5
```

Nach Runde 1:

```text
slow -> 6
fast -> 7
```

Nach Runde 2:

```text
slow -> 7
fast -> 9
```

`fast.next` ist nun `None`.

Die Schleife endet und:

```text
slow -> 7
```

liefert die Mitte.

---

## Beispiel mit gerader Anzahl

```text
5 -> 6 -> 7 -> 8
```

Start:

```text
slow -> 5
fast -> 5
```

Nach Runde 1:

```text
slow -> 6
fast -> 7
```

Nach Runde 2:

```text
slow -> 7
fast -> None
```

Damit ist das Ergebnis:

```text
7
```

Bei vier Nodes sind:

```text
6 und 7
```

die beiden mittleren Werte.

Die gewählte Schleifenlogik liefert automatisch den **zweiten** davon.

---

## Warum die Schleifenbedingung wichtig ist

```python
while fast and fast.next:
```

`fast` bewegt sich mit:

```python
fast = fast.next.next
```

zwei Schritte weiter.

Dafür müssen sowohl:

```text
fast
```

als auch:

```text
fast.next
```

existieren.

Die Bedingung schützt damit vor dem Zugriff auf:

```text
None.next
```

und ist gleichzeitig dafür verantwortlich, wie gerade Listen behandelt werden.

---

## Warum die Länge nicht vorher berechnet wird

Eine andere Lösung könnte:

```text
1. alle Nodes zählen
2. Mitte berechnen
3. erneut vom Head zur Mitte laufen
```

Das wäre asymptotisch ebenfalls:

```text
O(n)
```

würde die Liste aber zweimal traversieren.

Der Slow/Fast-Ansatz erreicht das Ziel in einem einzigen Traversal und benötigt keine separate Längeninformation.

---

## Komplexität

### Laufzeit

Die Schleife läuft ungefähr:

```text
n / 2
```

Mal.

In Big O werden konstante Faktoren ignoriert:

```text
O(n / 2) = O(n)
```

Damit:

```text
find_middle() -> O(n)
```

### Zusatzspeicher

Es werden nur zwei zusätzliche Referenzen benötigt:

```python
slow
fast
```

Die Anzahl dieser Referenzen hängt nicht von `n` ab:

```text
O(1)
```

---

## Randfälle

### Leere Liste

```text
head = None
```

Dann sind:

```text
slow = None
fast = None
```

Die Schleife läuft nicht.

Durch:

```python
return slow.data if slow else None
```

wird:

```text
None
```

zurückgegeben.

---

### Ein Node

```text
[5] -> None
```

`fast.next` existiert nicht.

Die Schleife läuft nicht und `slow` bleibt auf `5`.

Ergebnis:

```text
5
```

---

### Zwei Nodes

```text
5 -> 6
```

Nach einer Runde:

```text
slow -> 6
fast -> None
```

Ergebnis:

```text
6
```

Damit wird wie gefordert die zweite Mitte gewählt.

---

## Versteckte Annahme: keine Zyklen

Die Methode setzt eine normale, endende Linked List voraus:

```text
... -> None
```

Bei einer zyklischen Struktur:

```text
5 -> 6 -> 7
     ↑    |
     └────┘
```

existiert kein normales Listenende.

Die Schleife könnte dann dauerhaft weiterlaufen.

Für diese Lernübung ist eine azyklische Linked List vorausgesetzt.

Das ist ein gutes Beispiel dafür, dass Algorithmen oft **strukturelle Vorbedingungen** besitzen, auch wenn diese nicht als Funktionsparameter sichtbar sind.

---

## Die Methode verändert die Liste nicht

`find_middle()` liest nur:

```python
next
```

und verändert lediglich lokale Referenzen.

Es werden:

```text
keine Nodes gelöscht
keine next-Links geändert
head nicht verändert
```

Damit ist das Risiko struktureller Beschädigungen deutlich geringer als bei Methoden wie `reverse()` oder `remove_duplicates()`.

---

## Hinweis zu `append()`

Die `append()`-Methode in dieser eigenständigen Übungsdatei sucht das Listenende weiterhin:

```python
while last_node.next:
    last_node = last_node.next
```

Damit gilt dort:

```text
append() -> O(n)
```

Das ist bewusst nicht das Lernziel dieser Datei.

Die separate Übung [`linked_list_append_o1_explanation.md`](linked_list_append_o1_explanation.md) zeigt, wie ein `tail`-Pointer `append()` auf `O(1)` verbessert.

---

## Typvertrag

Die aktuelle Schnittstelle lautet:

```python
find_middle(self) -> object | None
```

Das bedeutet:

```text
nicht leere Liste -> gespeicherter Wert
leere Liste       -> None
```

---

## Tests

Die ursprünglichen Lernfälle prüfen unter anderem:

```text
5 -> 6
→ 6

5 -> 6 -> 7
→ 6
```

Die Implementierung wird inzwischen automatisiert mit `pytest` geprüft:

[`../tests/test_linked_lists.py`](../tests/test_linked_lists.py)

Dort werden unter anderem getestet:

```text
ungerade Länge
gerade Länge
leere Liste
ein einzelner Node
```

---

## Design- und Skalierungsgedanke

Die Aufgabe zeigt ein wichtiges algorithmisches Muster:

> Positionsinformation kann manchmal aus der relativen Bewegung mehrerer Referenzen gewonnen werden, ohne zusätzliche Daten zu speichern.

Statt:

```text
Länge speichern
Werte kopieren
zusätzliche Liste anlegen
```

werden nur zwei Traversal-Referenzen verwendet.

Das gleiche Grundmuster kann später unter anderem bei:

```text
Zyklenerkennung
Abständen zwischen Nodes
Bestimmung bestimmter Positionen
```

wieder auftauchen.

---

## Zentrale Lernidee

Die zentrale Erkenntnis lautet:

> **Wenn sich ein Zeiger doppelt so schnell durch eine Linked List bewegt wie ein anderer, befindet sich der langsamere Zeiger in der Mitte, sobald der schnelle Zeiger das Ende erreicht.**

Damit erreicht die Methode:

```text
Laufzeit:       O(n)
Zusatzspeicher: O(1)
```

ohne vorherige Berechnung der Listenlänge.

---

## Weiterführend

- [`README.md`](README.md) – Linked-List-Grundlagen
- [`linked_list_append_o1_explanation.md`](linked_list_append_o1_explanation.md) – Tail Pointer
- [`../docs/data_structure_patterns.md`](../docs/data_structure_patterns.md) – Slow / Fast Pointer
- [`../docs/big_o_cheatsheet.md`](../docs/big_o_cheatsheet.md) – lineare Laufzeit und konstanter Zusatzspeicher
- [`../tests/test_linked_lists.py`](../tests/test_linked_lists.py) – automatisierte Tests
