# Deployment Checklist – TishCommerce MVP

## 1. Technische Basis
- [ ] TishCommerce-Code in eigenes Shop-Repository übernehmen oder lokal klonen
- [ ] Node.js/npm verfügbar
- [ ] `npm install`
- [ ] lokale Testinstanz starten

## 2. Shop-Konfiguration
- [x] deutscher MVP-Text vorbereitet
- [x] Produkt 001 als Testprodukt definiert
- [x] Stripe als primäre Testzahlung gewählt
- [ ] Produktbild hinterlegen
- [ ] finales PDF hinterlegen

## 3. Zahlung
- [ ] Stripe-Konto/Testmodus verfügbar
- [ ] Publishable Test Key setzen
- [ ] Secret Test Key setzen
- [ ] Stripe Webhook Secret setzen
- [ ] Testzahlung durchführen

## 4. Download
- [ ] Zahlung serverseitig verifizieren
- [ ] PDF erst nach erfolgreicher Zahlung freigeben
- [ ] vor Livegang permanente öffentliche Download-URL durch private/signed URL ersetzen

## 5. Deployment
- [ ] Vercel oder Netlify verbinden
- [ ] Environment Variables nur im Hosting-Dashboard speichern
- [ ] keine Secrets in GitHub committen
- [ ] mobile Darstellung testen

## 6. Recht vor Livegang
- [ ] Impressum
- [ ] Datenschutzerklärung
- [ ] Widerrufs-/Erlöschensregel für digitale Inhalte fachlich prüfen
- [ ] Preisangaben prüfen
- [ ] steuerliche Behandlung prüfen
- [ ] TishCommerce-Attribution/Lizenz einhalten

## Definition of Done
MVP bestanden, wenn auf dem Smartphone der komplette Ablauf funktioniert:
Produktseite -> Warenkorb/Checkout -> Stripe-Testzahlung -> Bestätigung -> geschützter PDF-Download.
