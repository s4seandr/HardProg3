# Wetterstation mit ESP32 und RaspberryPI Zero

## 1. Einleitung und Motivation zur Wetterstation
Da Wetterdienste das aktuelle Wetter für meine Region (gefühlt) immer schlechter anzeigen und voraussagen, mich diese Daten jedoch interessieren, wollte ich mir schon länger eine Wetterstation für zuhause kaufen. Mit diesem Projekt habe ich nun die Möglichkeit, eine Wetterstation selbst umzusetzen. Dadurch werde ich nun in Zukunft selbst meine aktuellen Wetterdaten für Innen- und Außenbereich erfassen können und diese auf einem geeigneten Medium ausgeben oder auch für andere Anwendungen weiterverwenden können.

Bei meinem Projekt nutze ich zwei ESP32, die mit jeweils einem BME280 und einem Lichtsensor ausgestattet sind. Ein ESP-Modul soll mit Hilfe eines Batteriemoduls die Wetterdaten außen messen, während der zweite ESP die Werte in der Wohnung misst. Die gemessenen Werte sollen anschließend über das Wifi an den RaspberryPi Zero übermittelt werden, der mit Hilfe einer RGB-LED-Matrix (64x32) die Daten ausgibt.

## 2. Beschreibung der genutzten Hardware-Komponenten
- 2x ESP32 (12,99€)
    Bei den genutzten ESPs handelt es sich um ESP32 Typ C NodeMCU Entwicklungsboards. Jedes Board ist mit einem ESP-WROOM-32 Modul ausgestattet, das einen leistungsstarken Mikrocontroller mit Dual-Core-Prozessoren und integrierter 2.4GHz Dual-Mode WiFi und Bluetooth-Funktionalität bietet.
- 2x BME280
- 2x Lichtsensor
- 1x Batteriemodul mit 2x wiederaufladbaren Akkus
- 1x RaspberryPI Zero (WH)
- 1x RGB-Matrix-Bonnet für einen RaspberryPI
- 1x RGB-Matrix (64x32)
- 7x Jumper Cable

## 3. Implementierung

## 4. Evaluation

## 5. Fazit
