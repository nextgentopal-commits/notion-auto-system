# Digital-Humanities-Pipeline v1.0

## 1. Zweck

Die Pipeline erschließt historische türkische und osmanisch-türkische Quellen, ohne OCR, Transkription, Modernisierung, Übersetzung oder Interpretation miteinander zu verwechseln.

## 2. Unveränderliche Stufenkette

```text
Werkidentität/Katalog → Witness/Faksimile → Bildsegmentierung → Roh-OCR/HTR
→ manuelle Kollation → diplomatische Transkription → normalisierte Transkription
→ optionale Modernisierung → philologische Übersetzung → literarische Übersetzung
→ Annotation/Analyse → DNA-Abstraktion → eigenständige Transformation
```

Jede Stufe erhält eine eigene Datei, Version, Methode, Verantwortlichkeit, Fehlerliste und Hashreferenz. Eine spätere Stufe darf die frühere nicht überschreiben.

## 3. Pflichtmetadaten

| Feld | Pflicht |
|---|---|
| Autor/Tradition und Titel | ja; Unsicherheit sichtbar |
| Bibliothek/Katalog/Signatur | ja, sofern vorhanden |
| Witness/Edition/Faksimile | ja |
| Sprache und Schrift | getrennt |
| Genre, Zeitraum, Druck/Handschrift | ja |
| Datei/Seite/Zeile | ja für Zitate |
| Repository, Pfad, Commit | ja bei GitHub-Fund |
| OCR-/HTR-Modell und Version | ja |
| Segmentierungs-/Vorverarbeitungsschritte | ja |
| manuelle Korrekturen | als Entscheidungsprotokoll |
| Rechte von Code, Modell, Daten und Quelle | getrennt |
| offene Fehler/Zweifel | ja |

## 4. Toolrouting

| Aufgabe | GitHub-Kandidaten | Integrationsmodus |
|---|---|---|
| Manuskript-/Projektfund | Fihrist-Metadaten, Turkey DH Atlas, HathiTrust-Armeno-Turkish-Workflows | `ADOPT_DISCOVERY` |
| Bild-/Zeilensegmentierung | seccily dataset; Koras0ff YOLO-Hinweise | `TEST_ISOLATED` |
| OCR/HTR | OttomanOCR-search, OtaHTR-search, OttomanTextAI | Fund-/Testschicht, kein Editionsersatz |
| Nachkorrektur | Therad445; Ottoman-NLP/OCR-Transformer | Ground-Truth-Vergleich; Synthetic-to-real-Gap dokumentieren |
| Transkriptionsentscheidung | Baki Scribe | Entscheidungsprovenienz abstrahieren |
| POS/NER/Text Mining | UD-DUDU-POS-Tagger, Ottoman NER, Ottominer | Hilfsannotation, manuelle Prüfung |
| Aruz | Taktisyen, Ottoman Aruz Predictor, Bahrmetr | automatische Hypothese plus manuelles taktîʿ |
| moderne Morphologie | Zemberek, TRmorph, Starlang, Google Turkish Morphology | moderne Sprachhilfe; historische Register separat |
| Semantik/Emotion | HisNet, SWNetTR, WordNet, Duygu-Turk | Messhilfe, niemals literarische Enddeutung |

## 5. Human-in-the-loop-Gates

1. **Identity Gate:** Ist Werk/Witness korrekt identifiziert?
2. **Image Gate:** Sind Seite, Spalten, Zeilen, Marginalien und Lesereihenfolge korrekt?
3. **OCR Gate:** Wird Zeichenunsicherheit statt erfundener Sicherheit ausgegeben?
4. **Collation Gate:** Wurde gegen Faksimile und gegebenenfalls weitere Witnesses geprüft?
5. **Transcription Gate:** Sind diplomatische und normalisierte Form getrennt?
6. **Modernization Gate:** Ist jede lexikalische/syntaktische Änderung nachvollziehbar?
7. **Translation Gate:** Ist philologische von literarischer Übersetzung getrennt?
8. **Rights Gate:** Sind Quelle, Scan, Transkription, Datensatz, Modell und Code einzeln geklärt?
9. **Interpretation Gate:** Sind Textbeobachtung und Deutung getrennt?
10. **Transformation Gate:** Entsteht ein neues Werk ohne falsche Zuschreibung oder Stilkopie?

## 6. OCR-Fehlerklassen

- Zeichen-/Ligaturenverwechslung,
- Diakritika-/Punktfehler,
- Worttrennung und Zeilenumbruch,
- Spalten- und Lesereihenfolge,
- Marginalien/Seitenkopf/Seitenzahl,
- arabisch-persische Lehnformen,
- Eigennamen und Ortsnamen,
- Vers-/Beyitgrenzen,
- Satzzeichen der Edition,
- Modernisierungshalluzination,
- synthetisch trainierte Korrektur, die reale OCR verschlechtert.

Der dokumentierte Negativbefund ist wertvoller als eine erfundene Verbesserung. Kein Modell wird als produktionsreif bezeichnet, wenn es lediglich synthetische Daten verbessert.

## 7. Minderheitenschrift-Gate

Für Armeno-Turkish und Karamanlidika werden mindestens getrennt erfasst:

```text
gesprochene/geschriebene Sprache
≠ Schrift
≠ Religion/Gemeinschaft
≠ ethnische Selbstidentifikation
≠ Katalogbezeichnung
≠ Druckort/Verlag
≠ Genre
≠ heutige Transliteration
```

Ein Klassifikationsmodell liefert Kandidaten, keine Identität. Ein Transliterationswerkzeug erzeugt keine historische Edition.

## 8. Outputvertrag

Zulässige Outputs sind Quellenregister, Variantenmatrix, Kollationsprotokoll, Transkriptionsentscheidungslog, TEI-/JSON-Annotation, statistische Exploration, gekennzeichnete Interpretation und Mechanismenkarten.

Unzulässig sind still „bereinigte“ Originaltexte, unmarkierte KI-Modernisierungen, automatisch zugeschriebene Gedichte, kommerzielle Volltextsammlungen mit ungeklärten Rechten und Autorenstilmodelle als literarische DNA.

