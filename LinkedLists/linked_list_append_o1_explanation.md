# `LinkedList.append()` – In O(1) an eine verkettete Liste anhängen

## Ziel der Übung

Eine einfach verkettete Liste soll eine Methode

```python
append(data)
```

bekommen, die neue Nodes am Listenende in **`O(1)`** anfügt. Dafür muss die Klasse den letzten Node direkt erreichen können. Auch der Übergang von einer leeren zu einer ein-elementigen Liste muss konsistent behandelt werden.

---

## Implementierung

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        # An empty list gets its first and last node at the same time.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # tail gives direct access to the current last node -> O(1).
        self.tail.next = new_node
        self.tail = new_node

    def __str__(self):
        elements = []
        current = self.head

        while current:
            elements.append(current.data)
            current = current.next

        return "->".join(map(str, elements))


# Test
ll = LinkedList()

ll.append(5)
ll.append(6)
ll.append(7)

print(ll)
```

Erwartete Ausgabe:

```text
5->6->7
```

---

# 1. Wiederholung: Was ist eine verkettete Liste?

Eine verkettete Liste besteht aus einzelnen **Knoten (Nodes)**.

Jeder Knoten enthält:

1. einen Wert,
2. eine Referenz auf den nächsten Knoten.

Ein Knoten sieht gedanklich so aus:

```text
[data | next]
```

Zum Beispiel:

```text
[5 | • ] -> [6 | • ] -> [7 | None]
```

Die Knoten liegen nicht zwingend direkt nebeneinander im Speicher.

Stattdessen kennt jeder Knoten nur den nächsten Knoten.

---

# 2. Die Klasse `Node`

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Jeder neue Knoten bekommt einen Wert:

```python
self.data = data
```

und zunächst keinen Nachfolger:

```python
self.next = None
```

Wenn wir schreiben:

```python
node = Node(5)
```

können wir ihn uns zunächst so vorstellen:

```text
[5 | None]
```

Er ist noch mit keinem weiteren Knoten verbunden.

---

# 3. Was ist `head`?

Die verkettete Liste braucht einen Einstiegspunkt.

Dafür verwenden wir:

```python
self.head
```

`head` zeigt immer auf den **ersten Knoten** der Liste.

Bei:

```text
5 -> 6 -> 7
```

zeigt `head` auf:

```text
5
```

Gedanklich:

```text
head
 ↓
[5] -> [6] -> [7] -> None
```

Bei einer leeren Liste gibt es noch keinen ersten Knoten:

```python
self.head = None
```

---

# 4. Warum brauchen wir zusätzlich `tail`?

Die entscheidende Ergänzung dieser Aufgabe ist:

```python
self.tail = None
```

`tail` zeigt auf den **letzten Knoten** der Liste.

Bei:

```text
5 -> 6 -> 7
```

haben wir:

```text
head             tail
 ↓                 ↓
[5] -> [6] -> [7] -> None
```

Damit kennen wir jederzeit sowohl:

- den ersten Knoten,
- als auch den letzten Knoten.

Das ist wichtig für die geforderte Laufzeit von `append()`.

---

# 5. Was wäre ohne `tail`?

Angenommen, wir hätten nur:

```python
self.head
```

und wollten einen neuen Knoten am Ende einfügen.

Dann müssten wir beim ersten Knoten starten:

```python
current = self.head
```

und immer weitergehen:

```python
while current.next is not None:
    current = current.next
```

Bei:

```text
5 -> 6 -> 7
```

müssten wir also durch:

```text
5
6
7
```

laufen, nur um herauszufinden, wo das Ende ist.

Je länger die Liste wird, desto mehr Knoten müssen wir besuchen.

Das hätte die Laufzeit:

```text
O(n)
```

Die Aufgabe verlangt aber:

```text
O(1)
```

---

# 6. Wie löst `tail` das Problem?

Da:

```python
self.tail
```

immer direkt auf den letzten Knoten zeigt, müssen wir die Liste nicht durchsuchen.

Wir können sofort auf das Ende zugreifen.

Das ist der entscheidende Vorteil:

```python
self.tail.next = new_node
self.tail = new_node
```

Diese beiden Operationen benötigen keine Schleife.

Ihre Laufzeit hängt deshalb nicht von der Länge der Liste ab.

Damit arbeitet `append()` in:

```text
O(1)
```

---

# 7. Schritt für Schritt durch `append()`

Die Methode beginnt mit:

```python
new_node = Node(data)
```

Wenn wir aufrufen:

```python
ll.append(5)
```

entsteht zunächst:

```text
[5 | None]
```

Jetzt müssen wir entscheiden, ob die Liste bereits Elemente enthält.

---

# 8. Randfall: Die Liste ist leer

Am Anfang gilt:

```python
self.head = None
self.tail = None
```

Wir prüfen:

```python
if self.head is None:
```

Wenn das stimmt, ist `new_node` gleichzeitig:

- der erste Knoten,
- und der letzte Knoten.

Deshalb:

```python
self.head = new_node
self.tail = new_node
```

Nach:

```python
ll.append(5)
```

sieht die Liste gedanklich so aus:

```text
head
 ↓
[5] -> None
 ↑
tail
```

`head` und `tail` zeigen also auf denselben Knoten.

Das ist bei einer Liste mit genau einem Element korrekt.

---

# 9. Warum folgt danach `return`?

Nach:

```python
self.head = new_node
self.tail = new_node
```

ist der Einfügevorgang vollständig abgeschlossen.

Deshalb:

```python
return
```

Damit verlassen wir die Methode sofort.

Ohne das `return` würde der Code darunter ebenfalls ausgeführt werden.

Das wäre zwar in manchen Varianten lösbar, aber hier unnötig und weniger klar.

---

# 10. Zweites Element anhängen

Nach:

```python
ll.append(5)
```

haben wir:

```text
head
 ↓
[5] -> None
 ↑
tail
```

Jetzt:

```python
ll.append(6)
```

erstellt:

```text
[6 | None]
```

Die Liste ist nicht mehr leer.

Deshalb wird ausgeführt:

```python
self.tail.next = new_node
```

Bisher zeigt `tail` auf den Knoten `5`.

Wir setzen also:

```text
5.next -> 6
```

Danach:

```text
[5] -> [6] -> None
```

Jetzt muss `tail` noch aktualisiert werden:

```python
self.tail = new_node
```

Ergebnis:

```text
head       tail
 ↓           ↓
[5] -> [6] -> None
```

---

# 11. Drittes Element anhängen

Bei:

```python
ll.append(7)
```

zeigt `tail` bereits direkt auf:

```text
6
```

Deshalb können wir sofort:

```python
self.tail.next = new_node
```

setzen.

Danach:

```text
[5] -> [6] -> [7] -> None
```

und:

```python
self.tail = new_node
```

ergibt:

```text
head              tail
 ↓                  ↓
[5] -> [6] -> [7] -> None
```

---

# 12. Warum ist `append()` wirklich O(1)?

Schauen wir uns die Operationen an:

```python
new_node = Node(data)
```

konstante Arbeit.

Dann eventuell:

```python
self.head = new_node
self.tail = new_node
```

ebenfalls konstante Arbeit.

Oder:

```python
self.tail.next = new_node
self.tail = new_node
```

ebenfalls konstante Arbeit.

Es gibt:

- keine Schleife,
- keine Suche,
- keinen Durchlauf durch die Liste.

Deshalb ist die Laufzeit unabhängig von `n`.

Also:

```text
O(1)
```

---

# 13. Was bedeutet O(1) hier praktisch?

Angenommen, die Liste enthält:

```text
10 Elemente
```

oder:

```text
1.000.000 Elemente
```

Das Anhängen läuft in beiden Fällen nach demselben Prinzip:

```text
tail finden? -> bereits bekannt
tail.next setzen
tail aktualisieren
```

Wir müssen nicht durch die vorhandenen Elemente laufen.

Genau das bedeutet hier konstante Zeit.

---

# 14. Die wichtige Klassen-Invariante

Mit `head` und `tail` führen wir eine wichtige Regel ein:

> `head` muss immer auf den ersten Knoten und `tail` immer auf den letzten Knoten zeigen.

Diese Regel muss bei jeder zukünftigen Methode erhalten bleiben.

Zum Beispiel später bei:

- Löschen des letzten Knotens,
- Löschen des einzigen Knotens,
- Leeren der Liste,
- Einfügen in eine leere Liste.

Wenn eine Methode `head` oder die Struktur der Liste verändert, muss man immer überlegen:

> Muss auch `tail` aktualisiert werden?

Das ist ein Beispiel für eine **Invariante** einer Datenstruktur.

Eine Invariante ist eine Bedingung, die nach jeder gültigen Operation weiterhin stimmen muss.

---

# 15. `__str__()` – Liste lesbar ausgeben

Die Aufgabe enthält zusätzlich:

```python
def __str__(self):
```

Diese Methode bestimmt, wie unser Objekt dargestellt wird, wenn wir schreiben:

```python
print(ll)
```

Ohne eine eigene `__str__()`-Methode würde Python eher etwas wie:

```text
<__main__.LinkedList object at 0x...>
```

anzeigen.

Das hilft uns beim Verständnis kaum.

---

# 16. Wie funktioniert `__str__()`?

Zunächst:

```python
elements = []
current = self.head
```

`current` startet beim ersten Knoten.

Dann:

```python
while current:
```

laufen wir durch die gesamte Liste.

Bei jedem Knoten:

```python
elements.append(current.data)
```

speichern wir den Wert.

Anschließend:

```python
current = current.next
```

gehen wir zum nächsten Knoten.

Bei:

```text
5 -> 6 -> 7
```

entsteht:

```python
elements = [5, 6, 7]
```

---

# 17. Warum `map(str, elements)`?

Am Ende steht:

```python
return "->".join(map(str, elements))
```

`join()` erwartet Strings.

Unsere Daten können aber zum Beispiel Integer sein:

```python
[5, 6, 7]
```

Darum wandelt:

```python
map(str, elements)
```

sie gedanklich um in:

```text
"5", "6", "7"
```

Dann verbindet:

```python
"->".join(...)
```

sie zu:

```text
5->6->7
```

---

# 18. Laufzeit von `__str__()`

Hier müssen wir jeden Knoten besuchen:

```python
while current:
```

Bei `n` Knoten läuft die Schleife `n`-mal.

Deshalb ist:

```text
__str__() -> O(n)
```

Das ist völlig in Ordnung.

Die Aufgabe verlangt nur, dass:

```text
append() -> O(1)
```

arbeitet.

Nicht jede Methode einer Datenstruktur muss dieselbe Laufzeit haben.

---

# 19. Speicherkomplexität

Jeder neue Knoten speichert:

```text
data
next
```

Bei `n` Knoten benötigt die gesamte Liste deshalb:

```text
O(n)
```

Speicher.

Das zusätzliche `tail`-Attribut selbst benötigt nur eine einzelne Referenz:

```text
O(1)
```

Wir investieren also sehr wenig zusätzlichen Speicher, um `append()` von:

```text
O(n)
```

auf:

```text
O(1)
```

zu verbessern.

---

# 20. Design- und Skalierungsgedanke

Diese Aufgabe ist ein gutes Beispiel für einen klassischen Trade-off.

Ohne:

```python
self.tail
```

haben wir weniger Zustand zu verwalten, aber:

```text
append() -> O(n)
```

Mit:

```python
self.tail
```

speichern wir eine zusätzliche Referenz, bekommen dafür aber:

```text
append() -> O(1)
```

Das ist ein ähnlicher Grundgedanke wie bei:

- Datenbankindizes,
- Caches,
- vorberechneten Werten,
- zusätzlichen Lookup-Strukturen.

Man speichert zusätzliche Information, um häufige Operationen schneller zu machen.

---

# 21. Fehlerfälle und Datenintegrität

Bei dieser Aufgabe gibt es keinen klassischen Fehlerfall wie eine ungültige Eingabe.

`append()` kann grundsätzlich verschiedene Werte speichern:

```python
ll.append(5)
ll.append("hello")
ll.append(None)
```

Ob das erlaubt sein soll, hängt von der gewünschten Datenstruktur ab.

Für eine allgemeine Linked List ist das zunächst vollkommen in Ordnung.

Der wichtigere Robustheitsaspekt ist hier die **Konsistenz von `head` und `tail`**.

Bei einer leeren Liste sollte gelten:

```text
head = None
tail = None
```

Bei einer nicht leeren Liste sollten beide auf gültige Knoten zeigen.

Insbesondere bei genau einem Knoten gilt:

```text
head is tail
```

Diese Zustände sauber zu halten ist wichtiger als zusätzliche Eingabevalidierung.

---

# 22. Warum nicht einfach eine Python-Liste verwenden?

In echtem Python-Code würde man für viele alltägliche Aufgaben einfach:

```python
my_list.append(value)
```

verwenden.

Die Aufgabe soll jedoch nicht zeigen, wie man am bequemsten Daten speichert.

Sie soll vermitteln:

- wie verkettete Listen intern aufgebaut sind,
- wie Referenzen zwischen Knoten funktionieren,
- wie `head` und `tail` verwendet werden,
- und wie sich Designentscheidungen auf die Laufzeit auswirken.

Darum implementieren wir die Struktur hier bewusst selbst.

---

# 23. Zentrale Lernidee

Ohne direkten Verweis auf das Ende einer verketteten Liste muss man dieses Ende erst suchen.

Das kostet:

```text
O(n)
```

Durch ein zusätzliches Attribut:

```python
self.tail
```

kennen wir den letzten Knoten jederzeit direkt.

Dadurch wird:

```python
append()
```

zu:

```text
O(1)
```

Der Preis dafür ist, dass wir `tail` bei jeder strukturellen Änderung korrekt mitpflegen müssen.

---

# Zusammenfassung

Die `LinkedList` speichert zwei wichtige Referenzen:

```python
self.head
self.tail
```

Dabei gilt:

```text
head -> erster Knoten
tail -> letzter Knoten
```

Beim ersten Element:

```text
head
 ↓
[5]
 ↑
tail
```

Bei weiteren Elementen:

```python
self.tail.next = new_node
self.tail = new_node
```

Dadurch ist keine Suche nach dem Listenende notwendig.

Die wichtigsten Laufzeiten sind:

```text
append()  -> O(1)
__str__() -> O(n)
```

Die zentrale Erkenntnis lautet:

> **Ein zusätzlicher `tail`-Zeiger speichert direkt, wo sich das Ende der verketteten Liste befindet, und ermöglicht dadurch das Anhängen eines Knotens in konstanter Zeit O(1).**
