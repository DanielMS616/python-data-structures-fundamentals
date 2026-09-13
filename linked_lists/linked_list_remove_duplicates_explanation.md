# `LinkedList.remove_duplicates()` – Duplikate aus einer verketteten Liste entfernen

## Ziel der Übung

Die Methode

```python
remove_duplicates()
```

soll eine Linked List einmal durchlaufen und spätere Wiederholungen bereits gesehener Werte entfernen.

Das **erste Vorkommen** eines Werts bleibt erhalten.

Beispiel:

```text
Vorher:
5 -> 5 -> 6 -> 5 -> 7 -> 6

Nachher:
5 -> 6 -> 7
```

Ein `set` dient als Hilfsstruktur für bereits beobachtete Werte.

Die allgemeinen Linked-List-Grundlagen stehen in [`README.md`](README.md).

Hier liegt der Fokus auf der Kombination aus:

```text
Seen Set
+
previous/current
+
gezieltem Umhängen von next
```

---

## Quick Summary

| Aspekt | Ergebnis |
| --- | --- |
| Hauptstruktur | Linked List |
| Hilfsstruktur | `set` |
| Muster | Seen Set + Previous / Current |
| durchschnittliche Laufzeit | `O(n)` |
| Zusatzspeicher | `O(n)` |
| ohne Set | Worst Case `O(n²)` |
| Kernidee | Duplikate werden durch Umhängen von `previous.next` übersprungen |
| wichtige Voraussetzung | gespeicherte Werte müssen hashbar sein |

---

## Relevante Implementierung

```python
from collections.abc import Hashable


class Node:
    def __init__(self, data: Hashable) -> None:
        self.data: Hashable = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def remove_duplicates(self) -> None:
        seen: set[Hashable] = set()
        current = self.head
        previous: Node | None = None

        while current:
            if current.data in seen:
                assert previous is not None
                previous.next = current.next

            else:
                seen.add(current.data)
                previous = current

            current = current.next
```

Die vollständige und aktuelle Implementierung befindet sich in [`linked_list_remove_duplicates.py`](linked_list_remove_duplicates.py).

---

## Grundidee

Während eines einzigen Traversals merkt sich:

```python
seen
```

alle Werte, die bereits mindestens einmal vorkamen.

Für jeden Node gibt es zwei Fälle:

```text
Wert noch nicht gesehen
→ behalten
→ in seen eintragen
→ previous weiterschieben

Wert bereits gesehen
→ Node überspringen
→ previous bleibt stehen
```

Dadurch bleibt immer nur das erste Vorkommen erhalten.

---

## Warum ein Set?

Mit:

```python
current.data in seen
```

kann im Durchschnitt in:

```text
O(1)
```

geprüft werden, ob ein Wert bereits vorkam.

Auch:

```python
seen.add(current.data)
```

ist durchschnittlich:

```text
O(1)
```

Ohne Set müsste für jeden neuen Node möglicherweise ein großer Teil der bereits besuchten Liste erneut durchsucht werden.

Das könnte im Worst Case zu:

```text
O(n²)
```

führen.

---

## Die drei wichtigen Zustände

### `seen`

```python
seen: set[Hashable] = set()
```

enthält alle Werte, die bereits behalten wurden.

### `current`

```python
current = self.head
```

zeigt auf den Node, der gerade untersucht wird.

### `previous`

```python
previous: Node | None = None
```

zeigt auf den letzten Node, der **in der Liste bleiben soll**.

Diese Unterscheidung ist besonders wichtig, sobald Duplikate entfernt werden.

---

## Einen doppelten Node überspringen

Angenommen:

```text
previous          current
   ↓                 ↓
 [5] -------------> [5] -> [6]
```

Der zweite `5`-Node ist ein Duplikat.

Durch:

```python
previous.next = current.next
```

wird er aus der Kette übersprungen:

```text
[5] -> [6]
```

Der Node wird nicht manuell aus dem Speicher gelöscht.

Entscheidend ist, dass er von der Linked List aus nicht mehr erreichbar ist.

---

## Warum `previous` bei einem Duplikat stehen bleibt

Das ist einer der wichtigsten Punkte der Aufgabe.

Beispiel:

```text
5 -> 5 -> 5 -> 6
```

Nach dem ersten `5`:

```text
previous -> erstes 5
seen = {5}
```

Beim zweiten `5` wird:

```python
previous.next = current.next
```

gesetzt.

`previous` bleibt aber auf dem **ersten gültigen `5`**.

Dasselbe geschieht beim dritten `5`.

Erst wenn `6` erreicht wird, wandert `previous` weiter.

Dadurch funktionieren auch beliebig viele direkt aufeinanderfolgende Duplikate.

---

## Warum `current` trotzdem weiterlaufen kann

Nach jeder Runde:

```python
current = current.next
```

Auch wenn `current` gerade aus der eigentlichen Liste herausgelöst wurde, besitzt dieser lokale Node weiterhin seine ursprüngliche `next`-Referenz.

Damit kann der Traversal zum nächsten Node fortgesetzt werden.

---

## Beispiel

Ausgang:

```text
5 -> 5 -> 6 -> 5 -> 7 -> 6
```

Schrittweise:

```text
5
→ neu
→ seen = {5}

zweites 5
→ Duplikat
→ entfernen

6
→ neu
→ seen = {5, 6}

nächstes 5
→ Duplikat
→ entfernen

7
→ neu
→ seen = {5, 6, 7}

letztes 6
→ Duplikat
→ entfernen
```

Ergebnis:

```text
5 -> 6 -> 7
```

---

## Komplexität

### Laufzeit

Jeder Node wird genau einmal besucht:

```python
while current:
```

Set-Mitgliedschaft und Einfügen sind durchschnittlich:

```text
O(1)
```

Das Umhängen:

```python
previous.next = current.next
```

ist ebenfalls:

```text
O(1)
```

Damit ergibt sich im durchschnittlichen Fall:

```text
O(n)
```

### Zusatzspeicher

Im Worst Case sind alle Werte unterschiedlich und landen im Set.

Damit:

```text
O(n)
```

zusätzlicher Speicher.

---

## Trade-off ohne Set

Ohne Hilfsstruktur könnte man für jeden Node prüfen, ob sein Wert bereits irgendwo davor vorkam.

Das spart zusätzlichen Set-Speicher, kann aber zu:

```text
O(n²)
```

Laufzeit führen.

Mit Set:

```text
Laufzeit:       durchschnittlich O(n)
Zusatzspeicher: O(n)
```

Die Übung zeigt damit direkt den klassischen Trade-off:

```text
mehr Speicher
↔
weniger Laufzeit
```

---

## Randfälle

### Leere Liste

Die Schleife läuft nicht.

Die Liste bleibt leer.

### Ein Node

Der Wert wird einmal in `seen` eingetragen.

Es gibt kein Duplikat.

### Alle Werte gleich

```text
5 -> 5 -> 5 -> 5
```

wird zu:

```text
5
```

### Keine Duplikate

```text
1 -> 2 -> 3
```

bleibt unverändert.

---

## Hashbarkeit als echte Voraussetzung

Da ein Python-Set verwendet wird, müssen die gespeicherten Werte **hashbar** sein.

Beispiele für hashbare Werte:

```python
5
"hello"
(1, 2)
```

Eine veränderbare Liste:

```python
[1, 2]
```

ist dagegen nicht hashbar.

Die Type Hints machen diese Voraussetzung inzwischen explizit:

```python
data: Hashable
```

Damit wird eine Implementierungsannahme Teil des sichtbaren Typvertrags.

---

## Warum das `assert previous is not None` sinnvoll ist

Im Duplikat-Zweig steht:

```python
assert previous is not None
```

Ein Wert kann nur bereits in `seen` sein, wenn zuvor mindestens ein Node mit diesem Wert behalten wurde.

Deshalb muss es in diesem Zweig einen gültigen `previous`-Node geben.

Das `assert` dokumentiert diese algorithmische Invariante für:

```text
Leser
+
Laufzeit
+
statische Typanalyse
```

---

## Datenintegrität beim Entfernen

Bei Linked Lists besteht das eigentliche Risiko nicht darin, „ein Objekt zu löschen“, sondern die Verkettung falsch zu verändern.

Entscheidend ist:

```python
previous.next = current.next
```

Dadurch muss weiterhin gelten:

```text
keine gültigen Nodes gehen verloren
der Traversal kann fortgesetzt werden
die Reihenfolge der behaltenen Nodes bleibt erhalten
```

---

## Zusammenhang mit `tail`

Diese konkrete Übungsdatei besitzt kein `tail`-Attribut.

Würde `remove_duplicates()` jedoch in eine Linked-List-Variante mit gespeichertem `tail` integriert, entstünde eine zusätzliche Invariante:

> Wird der letzte Node als Duplikat entfernt, muss `tail` auf den neuen letzten Node aktualisiert werden.

Das zeigt sehr gut, wie eine Performance-Optimierung in einer Methode zusätzliche Konsistenzanforderungen für andere Methoden erzeugen kann.

---

## Typvertrag

Die aktuelle Implementierung verwendet:

```python
append(self, data: Hashable) -> None
remove_duplicates(self) -> None
```

Damit wird die Set-Voraussetzung bereits über den Typ sichtbar gemacht.

---

## Tests

Die dokumentierte Beispielliste:

```text
5 -> 5 -> 6 -> 5 -> 7 -> 6
```

wird zu:

```text
5 -> 6 -> 7
```

Die Implementierung wird inzwischen automatisiert mit `pytest` geprüft:

[`../tests/test_linked_lists.py`](../tests/test_linked_lists.py)

Dabei werden unter anderem getestet:

```text
spätere Duplikate
direkt aufeinanderfolgende Duplikate
leere Liste
Erhalt des ersten Vorkommens
```

---

## Design- und Skalierungsgedanke

Die Lösung kombiniert zwei Datenstrukturen mit unterschiedlichen Stärken:

```text
Linked List
→ Nodes können durch Referenzänderung direkt übersprungen werden

Set
→ bereits gesehene Werte können durchschnittlich in O(1) erkannt werden
```

Zusammen entsteht ein linearer Algorithmus auf Kosten zusätzlichen Speichers.

Diese Kombination ist ein typisches Beispiel dafür, dass Algorithmen häufig **mehrere Datenstrukturen gezielt zusammen einsetzen**, statt nur eine einzige Struktur isoliert zu verwenden.

---

## Zentrale Lernidee

Die zentrale Erkenntnis lautet:

> **Ein Set ermöglicht eine schnelle Prüfung bereits gesehener Werte, während `previous.next = current.next` einen doppelten Node direkt aus der Linked List überspringt.**

Besonders wichtig ist dabei:

```text
Duplikat
→ previous bleibt stehen

neuer Wert
→ previous bewegt sich weiter
```

Genau diese Invariante sorgt dafür, dass auch aufeinanderfolgende Duplikate korrekt entfernt werden.

---

## Weiterführend

- [`README.md`](README.md) – Linked-List-Grundlagen und Referenzänderungen
- [`linked_list_append_o1_explanation.md`](linked_list_append_o1_explanation.md) – zusätzliche `tail`-Invariante
- [`../docs/data_structure_patterns.md`](../docs/data_structure_patterns.md) – Seen Set und Previous / Current
- [`../docs/python_collections_complexity.md`](../docs/python_collections_complexity.md) – Set-Mitgliedschaft
- [`../tests/test_linked_lists.py`](../tests/test_linked_lists.py) – automatisierte Tests
