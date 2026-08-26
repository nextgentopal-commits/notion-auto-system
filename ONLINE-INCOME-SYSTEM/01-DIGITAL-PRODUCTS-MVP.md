# 01 DIGITAL PRODUCTS MVP

## Harte Grenze
Phase 1 funktioniert ohne OpenAI API und ohne KI-Agenten.

## Ziel
Ein einzelnes digitales PDF als MVP verkaufen und den kompletten Ablauf testen:
TikTok -> Produktseite -> Zahlung -> Download.

## Technische Basis
- Shop: TishCommerce
- Hosting: Vercel oder Netlify
- Zahlung: Stripe Testmodus und/oder PayPal Sandbox
- Produktdaten: JSON-Konfiguration
- Sprache: deutsche Lokalisierung über zentrale Locale-Datei
- Auslieferung: payment-verifizierter Download-Endpunkt

## Was keine OpenAI API braucht
- Produktseite
- Warenkorb
- Checkout
- Stripe/PayPal-Zahlung
- Download-Auslieferung
- Newsletter
- deutsche Texte
- Analytics über normale Webtools

## MVP-Schritte
1. TishCommerce in eigenes Repository übernehmen.
2. Test-Deployment auf Vercel/Netlify.
3. Deutsche Oberfläche konfigurieren.
4. Ein einziges PDF als Testprodukt anlegen.
5. Stripe Testmodus einrichten.
6. Optional PayPal Sandbox ergänzen.
7. Testkauf durchführen.
8. Download prüfen.
9. Mobile Checkout-Ansicht prüfen.
10. Erst danach Livegang vorbereiten.

## Sicherheitsbefund
Der Download-Endpunkt verifiziert Stripe/PayPal vor Freigabe, gibt danach aber die konfigurierte DownloadURL zurück. Für MVP/Test akzeptabel. Vor Verkauf wertvoller PDFs auf private Speicherung mit zeitlich begrenzten Signed URLs umstellen.

## Recht / Livegang
Vor echtem Verkauf in Deutschland prüfen und ergänzen:
- Impressum
- Datenschutzerklärung
- Widerrufsbelehrung / digitale Inhalte
- Preisangaben
- Steuerliche Behandlung
- Zahlungsanbieter-Datenschutz
- Newsletter-Einwilligung

Keine Rechts- oder Steuertexte ungeprüft live schalten.

## Kostenprinzip
- Keine OpenAI API Kosten.
- TishCommerce selbst ohne monatliche SaaS-Gebühr.
- Hosting kann im Test kostenlos starten, abhängig vom Anbieter und Traffic.
- Stripe/PayPal verursachen erst bei echten Zahlungen Transaktionsgebühren nach deren aktuellem Tarif.

## Entscheidung
TishCommerce = MVP-System.
Sellf = späterer Upgrade-Kandidat für Membership, Abos, Funnels und stärkere Automatisierung.

## Erfolgskriterium
Der MVP ist bestanden, wenn ein Testkunde mobil:
1. Produkt findet,
2. Testzahlung abschließt,
3. Bestätigung erhält,
4. PDF herunterladen kann,
5. und der Prozess ohne manuelle Nacharbeit funktioniert.
