# Wetterstation mit ESP32 und RaspberryPI Zero

## 1. Einleitung und Motivation zur Wetterstation
Da Wetterdienste das aktuelle Wetter für meine Region (gefühlt) immer schlechter anzeigen und voraussagen, mich diese Daten jedoch interessieren, wollte ich mir schon länger eine Wetterstation für zuhause kaufen. Mit diesem Projekt habe ich nun die Möglichkeit, eine Wetterstation selbst umzusetzen. Dadurch werde ich nun in Zukunft selbst meine aktuellen Wetterdaten für Innen- und Außenbereich erfassen können und diese auf einem geeigneten Medium ausgeben oder auch für andere Anwendungen weiterverwenden können.

Bei meinem Projekt nutze ich zwei ESP32, die mit jeweils einem BME280 und einem Lichtsensor ausgestattet sind. Ein ESP-Modul soll mit Hilfe eines Batteriemoduls die Wetterdaten außen messen, während der zweite ESP die Werte in der Wohnung misst. Die gemessenen Werte sollen anschließend über das Wifi an den RaspberryPi Zero übermittelt werden, der mit Hilfe einer RGB-LED-Matrix (64x32) die Daten ausgibt.

## 2. Beschreibung der genutzten Hardware-Komponenten
- 2x ESP32 (12,99€)
        Bei den genutzten ESPs handelt es sich um ESP32 Typ C NodeMCU Entwicklungsboards. Jedes Board ist mit einem ESP-WROOM-32 Modul ausgestattet, das einen leistungsstarken Mikrocontroller mit Dual-Core-Prozessoren und integrierter 2.4GHz Dual-Mode WiFi und Bluetooth-Funktionalität bietet.
        ![image](https://github.com/user-attachments/assets/5f817885-a866-432a-8d2b-a6fd6bf78989)

- 2x BME280 (15,99€)
         Der BME280 ist ein Sensor-Modul, dass die Temperatur, Luftfeuchtigkeit und Luftdruck messen kann. Sie nutzen eine Spannung von 5V und sind mit einem IIC/I2C Interface ausgestattet, was sie kompatibel mit Arduino und Raspberry Pi macht. Ein Nachteil des BME280 ist jedoch, dass er sich beim Dauereinstatz erwärmt, was zu falschen Messergebnissen führen             kann. Da die Daten jedoch nur alle 10 Minuten aktualiesert werden, ist das für dieses Projekt kein Problem. 
         ![image](https://github.com/user-attachments/assets/4e1ee3b0-edd7-4a2a-b240-b7e364605037)

- 2x Lichtsensor (5,49€)
         Als Lichtsensoren wurden KY-018 LDR (Light Dependent Resistor) Lichtsensor-Module genutzt. Diese Sensoren messen die Helligkeit des Umgebungslichts und bestehen aus einer Fotodiode, die an einen Widerstand gekoppelt ist. Der Widerstandswert des Sensors ändert sich je nach Lichtintensität
         ![image](https://github.com/user-attachments/assets/26e6f839-9e0a-4e8f-9716-f92a50a15c58)
  
  - 14x Jumper Cable (10cm Male-Female) (6,99€)
          Die Jumper Cables werden benötigt, um die Sensoren mit den ESP32 zu verbinden.
          ![image](https://github.com/user-attachments/assets/005a0532-5370-4d0a-a3a9-bdcc0f8b3182)

- 1x Batteriemodul mit 2x wiederaufladbaren Akkus
           Das Batteriemodul hat Platz für 2 Batterien und verfügt über einen integrierten Überspannschutz und hat im Gegensatz zu hat mehrere nutzbare Ausgänge und im Gegensatz zu den meisten herkömmlichen Powerbanks die Möglichkeit ein automatisches Abstellen des Stromflusses bei zu geringem Verbrauch zu verhindern.
           Da bei diesem Projekt der Deep-Sleep-Modus des ESP32 genutzt wird, ist das unerlässlich.
           ![image](https://github.com/user-attachments/assets/e0545760-7253-477e-8b14-d6c34914deab)
                
          Die genutzten Akkus sind 3.7V NiMH Akkus mit einer Kapazität von 3000mAh. Sie haben das Format 18650.
          ![image](https://github.com/user-attachments/assets/652f8ff0-d77d-4a0f-960b-caca0fa136df)

- 1x RaspberryPI Zero (WH) (23,49€)
          Der Raspberry Pi Zero WH ist eine kompakte und kostengünstige Version des Raspberry Pi, die mit einer vorinstallierten GPIO-Stiftleiste geliefert wird. Dies erleichtert die Verbindung mit anderen Geräten und Sensoren, ohne dass Löten erforderlich ist.
          ![image](https://github.com/user-attachments/assets/e6eb409b-535b-4562-9659-08018a718a17)

- 1x RGB-Matrix-Bonnet für einen RaspberryPI (25,99€)
          Das Adafruit RGB Matrix Bonnet ist ein Erweiterungsmodul für den Raspberry Pi, das die Steuerung von RGB-LED-Matrizen vereinfacht. Es wird direkt auf den Raspberry Pi gesteckt und ermöglicht die einfache Ansteuerung von RGB-Matrizen.
          ![image](https://github.com/user-attachments/assets/97870010-1886-4e30-beee-abe3eaa504a7)

- 1x RGB-Matrix (64x32) (29,99€)
          Die Matrix besteht aus 2048 RGB-LEDs und ermöglicht die Darstellung von Texten, farbigen Bildern und Animationen.
          ![image](https://github.com/user-attachments/assets/3d109b13-05a8-4769-8cd5-41f64850c5a8)
  
- 1x 3d-gedruckte Hülle für den Outdoor-Sensor (1 Kasten Bayreuther Bier)

        
## 3. Implementierung
Die Implementierung setzt sich aus 2 Teilen zusammen: Den beiden ESP32-Sensormodulen und der Basisstation mit einem lokalen Server auf dem Raspberry PI Zero.

## 4. Evaluation

## 5. Fazit
