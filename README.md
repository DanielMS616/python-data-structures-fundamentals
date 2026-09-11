# Abstrakte Datentypen und grundlegende Datenstrukturen

Dieses Repository ist ein persönliches Lern- und Nachschlagewerk zu grundlegenden Datenstrukturen und ihrer algorithmischen Analyse.

Dieses Repository dokumentiert meinen Lernprozess zu grundlegenden
Datenstrukturen und algorithmischer Komplexität. Übungsbeschreibungen wurden
sinngemäß zusammengefasst; Implementierungen, Erklärungen und zusätzliche
Beispiele wurden im Rahmen meiner eigenen Bearbeitung erstellt.

Im Mittelpunkt stehen aktuell:

- **Stacks**
- **Queues**
- **Linked Lists**
- **Big-O-Notation**
- wiederkehrende **Problemlösungsmuster** wie Slow/Fast Pointer, Hilfs-Sets und monotone Queues

Das Repository soll nicht nur fertigen Code sammeln. Es dokumentiert auch, **warum** eine Lösung funktioniert, welche Laufzeit sie besitzt, welche Randfälle wichtig sind und welche Designentscheidungen hinter der jeweiligen Implementierung stehen.


---

## Lernkontext

Die Inhalte bauen auf drei Ebenen auf:

1. **Theorie**  
   Was ist die Datenstruktur? Welche Eigenschaften und Operationen besitzt sie?

2. **Übungen**  
   Konkrete Problemstellungen mit ausführlich dokumentierten Lösungen.

3. **Übergreifende Muster**  
   Welche Ideen tauchen in verschiedenen Aufgaben immer wieder auf?

Ein zentraler Gedanke ist die Trennung von **abstraktem Datentyp und Implementierung**:

```text
Was soll eine Struktur können?
        ↓
     ADT / Idee
        ↓
Wie wird dieses Verhalten technisch umgesetzt?
        ↓
  Implementierung
```

Eine Queue beschreibt beispielsweise das FIFO-Verhalten. Ob sie intern mit einer Python-Liste, einer `deque` oder einer verketteten Liste umgesetzt wird, ist eine davon getrennte Entscheidung.

Mehr dazu: [`docs/adt_and_implementation.md`](docs/adt_and_implementation.md)

---

## Repository-Struktur

```text
.
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── docs
│   ├── README.md
│   ├── adt_and_implementation.md
│   ├── big_o_cheatsheet.md
│   ├── data_structure_patterns.md
│   ├── glossary.md
│   ├── learning_workflow.md
│   └── python_collections_complexity.md
├── LinkedLists
│   ├── README.md
│   ├── linked_list_append_o1.py
│   ├── linked_list_append_o1_explanation.md
│   ├── linked_list_find_middle.py
│   ├── linked_list_find_middle_explanation.md
│   ├── linked_list_remove_duplicates.py
│   ├── linked_list_remove_duplicates_explanation.md
│   ├── linked_list_reverse.py
│   └── linked_list_reverse_explanation.md
├── queue
│   ├── README.md
│   ├── max_queue.py
│   ├── max_queue_explanation.md
│   ├── priority_queue.py
│   ├── priority_queue_explanation.md
│   ├── reversable_queue.py
│   └── reversable_queue_explanation.md
└── Stack
    ├── README.md
    ├── balanced_symbols.py
    ├── balanced_symbols_explanation.md
    ├── par_checker.py
    ├── par_checker_explanation.md
    ├── rev_string.py
    └── rev_string_explanation.md
```

---

## Drei Dokumentationsebenen

### 1. Python-Dateien

Die `.py`-Dateien enthalten die eigentliche Lösung.

Kommentare werden bewusst sparsam eingesetzt:

```python
# Save the next node before reversing the current link.
next_node = current.next
```

Ein Kommentar soll vor allem dann vorhanden sein, wenn er erklärt:

- **warum** eine Zeile notwendig ist,
- welche algorithmische Entscheidung getroffen wurde,
- welcher Abschnitt besonders wichtig ist,
- oder welche Laufzeitentscheidung dahintersteht.

Selbsterklärende Zeilen werden nicht unnötig kommentiert.

---

### 2. Exercise-Explanation-Dateien

Zu jeder Übung gehört eine ausführliche Markdown-Datei:

```text
exercise.py
exercise_explanation.md
```

Sie enthält unter anderem:

- das sinngemäß zusammengefasste Übungsziel,
- die fertige Lösung,
- eine schrittweise Herleitung,
- Visualisierungen in Textform,
- Laufzeit- und Speicherkomplexität,
- Rand- und Fehlerfälle,
- Skalierungs- und Designgedanken,
- zusätzliche Beispiele.

Zusätzliche Beispiele werden ausdrücklich als solche gekennzeichnet.

---

### 3. Topic-READMEs und `docs/`

Die `README.md` in jedem Themenordner erklärt das **Konzept unabhängig von einer einzelnen Aufgabe**.

Die Dateien unter `docs/` behandeln Wissen, das mehrere Themen verbindet:

| Dokument | Zweck |
| --- | --- |
| [`adt_and_implementation.md`](docs/adt_and_implementation.md) | ADT, Algorithmus und Implementierung voneinander unterscheiden |
| [`big_o_cheatsheet.md`](docs/big_o_cheatsheet.md) | Big-O verstehen und Code analysieren |
| [`python_collections_complexity.md`](docs/python_collections_complexity.md) | Laufzeiten wichtiger Python-Operationen |
| [`data_structure_patterns.md`](docs/data_structure_patterns.md) | Wiederkehrende algorithmische Muster erkennen |
| [`glossary.md`](docs/glossary.md) | Zentrale Begriffe schnell nachschlagen |
| [`learning_workflow.md`](docs/learning_workflow.md) | Dokumentations- und Lernstandard dieses Repositories |

---

## Schneller Vergleich

| Struktur | Grundprinzip | Typische Stärke | Wichtiges Bild |
| --- | --- | --- | --- |
| Stack | LIFO | letztes Element schnell bearbeiten | Tellerstapel |
| Queue | FIFO | Elemente in Ankunftsreihenfolge verarbeiten | Warteschlange |
| Linked List | verkettete Nodes | Links gezielt verändern, ohne Elemente zu verschieben | Kette von Knoten |

### Stack

```text
Top
 ↓
[C]
[B]
[A]
```

Das zuletzt eingefügte `C` wird zuerst entfernt.

Mehr: [`Stack/README.md`](Stack/README.md)

### Queue

```text
Front                   Rear
  ↓                       ↓
[A] -> [B] -> [C]
```

`A` wurde zuerst eingefügt und wird zuerst entfernt.

Mehr: [`queue/README.md`](queue/README.md)

### Linked List

```text
head
 ↓
[5 | •] -> [6 | •] -> [7 | None]
```

Jeder Node speichert Daten und eine Referenz auf den nächsten Node.

Mehr: [`LinkedLists/README.md`](LinkedLists/README.md)

---

## Übungen

### Stack

| Übung | Lernidee |
| --- | --- |
| [`rev_string.py`](Stack/rev_string.py) | LIFO zum Umkehren einer Reihenfolge |
| [`par_checker.py`](Stack/par_checker.py) | offene Klammern auf einem Stack verwalten |
| [`balanced_symbols.py`](Stack/balanced_symbols.py) | verschachtelte Symboltypen korrekt zuordnen |

### Queue

| Übung | Lernidee |
| --- | --- |
| [`priority_queue.py`](queue/priority_queue.py) | Priorität und stabile Einfügereihenfolge kombinieren |
| [`max_queue.py`](queue/max_queue.py) | Maximum über eine monotone Hilfsqueue in O(1) lesen |
| [`reversable_queue.py`](queue/reversable_queue.py) | Queue und Stack kombinieren |

### Linked Lists

| Übung | Lernidee |
| --- | --- |
| [`linked_list_append_o1.py`](LinkedLists/linked_list_append_o1.py) | Tail-Referenz für O(1)-Append |
| [`linked_list_reverse.py`](LinkedLists/linked_list_reverse.py) | Previous/Current/Next und In-place-Änderung |
| [`linked_list_remove_duplicates.py`](LinkedLists/linked_list_remove_duplicates.py) | Hilfs-Set zum Erkennen bereits gesehener Werte |
| [`linked_list_find_middle.py`](LinkedLists/linked_list_find_middle.py) | Slow/Fast Pointer |

---

## Big O als gemeinsame Sprache

Viele Entscheidungen in diesem Repository ergeben erst Sinn, wenn die Laufzeit einzelner Operationen berücksichtigt wird.

Einige Beispiele:

```text
Listenindex                     -> O(1)
list.pop() am Ende              -> O(1)
list.pop(0)                     -> O(n)
Linked-List-Suche               -> O(n)
Set-Mitgliedschaft              -> durchschnittlich O(1)
list.sort()                     -> O(n log n)
```

Daraus entstehen konkrete Designentscheidungen:

```text
Warum liegt das nächste PriorityQueue-Element am Listenende?
→ Weil pop() dort O(1) ist.

Warum speichert die Linked List einen tail?
→ Damit das Ende nicht jedes Mal in O(n) gesucht werden muss.

Warum verwenden wir beim Entfernen von Duplikaten ein Set?
→ Damit die Prüfung eines bereits gesehenen Wertes durchschnittlich O(1) ist.
```

Mehr: [`docs/big_o_cheatsheet.md`](docs/big_o_cheatsheet.md)

---

## Wiederkehrende Problemlösungsmuster

Die Übungen sind nicht nur einzelne Lösungen. Sie zeigen Muster, die sich auf andere Probleme übertragen lassen:

```text
Stack / LIFO
    → Reihenfolgen umkehren
    → verschachtelte Strukturen prüfen

Previous + Current + Next
    → Links einer Linked List sicher verändern

Slow + Fast Pointer
    → Mitte einer Linked List
    → Zyklenerkennung

Seen Set
    → Duplikate erkennen
    → bereits verarbeitete Werte merken

Monotone Helper Queue
    → Maximum ohne erneute vollständige Suche

Tail Pointer
    → direkten Zugriff auf das Listenende erhalten
```

Mehr: [`docs/data_structure_patterns.md`](docs/data_structure_patterns.md)

---

## Qualitätsfragen

Neben der reinen Funktionalität werden bei den Übungen bewusst weitere Fragen betrachtet:

```text
Korrektheit
    Funktioniert die Lösung für die normale Eingabe?

Randfälle
    Was passiert bei einer leeren Struktur oder nur einem Element?

Datenintegrität / Invarianten
    Bleiben head, tail und next-Referenzen konsistent?

Komplexität
    Welche Operationen werden mit wachsender Eingabe teuer?

Skalierung
    Funktioniert die Idee auch noch bei sehr vielen Elementen?

Schnittstelle
    Soll ein leerer dequeue-Aufruf None liefern oder eine Exception auslösen?
```

Bei größeren Softwareprojekten kommen zusätzlich Themen wie Persistenz, Fehlerbehandlung, Datenbank-Constraints und Betriebsreife hinzu.

---

## Python-Umgebung

Einige Stack-Aufgaben verwenden die Bibliothek `pythonds3`. Die verwendete Version ist in [`requirements.txt`](requirements.txt) festgehalten.

Installation der Projektabhängigkeiten:

```bash
python3 -m pip install -r requirements.txt
```

Typischer Import:

```python
from pythonds3.basic import Stack
```

---

## Eigenständige Aufbereitung

Die Dokumentation verbindet persönliche Mitschriften, praktische Implementierungen und ergänzende technische Einordnungen zu einer eigenständigen Lernreferenz.

Die Übungsziele werden bewusst sinngemäß beschrieben. Im Mittelpunkt stehen die eigene Implementierung, die Herleitung der Lösung sowie Komplexität, Randfälle und übertragbare Problemlösungsmuster.

---

## Lizenz

Die eigenen Implementierungen und Dokumentationen dieses Repositories stehen unter der [MIT License](LICENSE). Sie dürfen unter den Bedingungen dieser Lizenz verwendet, verändert und weitergegeben werden.

---

## Lernziel

Am Ende soll nicht nur bekannt sein, **wie** eine bestimmte Übung gelöst wurde.

Wichtiger ist, bei neuen Problemen Fragen wie diese stellen zu können:

```text
Welche Datenstruktur passt zu meinem Zugriffsmuster?

Welche Operation ist hier teuer?

Kann ich zusätzliche Informationen speichern,
um spätere Operationen schneller zu machen?

Welche Invariante muss nach jeder Änderung noch stimmen?

Erkenne ich hier ein bekanntes Muster?
```

Genau diese Denkweise macht aus einzelnen Übungen übertragbares Wissen.
