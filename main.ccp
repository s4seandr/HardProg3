#include <Arduino.h>
#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

//define WIFI
#define WIFI_SSID "WLAN-1234"
#define WIFI_PASSWORD "1234567890"

//define pins
#define LDRPIN 34
#define SEALEVELPRESSURE_HPA (1013.25)

// BME280 object
Adafruit_BME280 bme;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  // put your setup code here, to run once:
  Serial.begin(921600);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected!");

  // Initialize BME280 sensor
  if (!bme.begin(0x76)) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }

  // Read LDR sensor value
  int lightvalue = analogRead(LDRPIN);
  Serial.print("Lightvalue: ");
  Serial.println(lightvalue);

  // Read BME280 sensor values
  Serial.print("Temperature = ");
  Serial.print(bme.readTemperature());
  Serial.println(" °C");

  Serial.print("Pressure = ");
  Serial.print(bme.readPressure() / 100.0F);
  Serial.println(" hPa");

  Serial.print("Humidity = ");
  Serial.print(bme.readHumidity());
  Serial.println(" %");

  //deep sleep 60s 
  esp_sleep_enable_timer_wakeup(60000000);
  esp_deep_sleep_start();
}

void loop() {
  //empty because of deep sleep
}
