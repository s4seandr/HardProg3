#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

//define WIFI
#define WIFI_SSID "WLAN-123"
#define WIFI_PASSWORD "0123456789"

//define pins
#define LDRPIN 34
#define SEALEVELPRESSURE_HPA (1013.25)

// BME280 object
Adafruit_BME280 bme;

// Unique device ID
#define DEVICE_ID "ESP32_indoor"

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

  // Read LDR sensor values
  int lightvalue = analogRead(LDRPIN);

  // Read BME280 sensor values
  float temperature = bme.readTemperature();
  float pressure = bme.readPressure() / 100.0F;
  float humidity = bme.readHumidity();

  // Send data to Raspberry Pi
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("http://192.168.2.192:5000/data");                         //ID of the RaspberryPI
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    http.setAuthorization("admin", "20Wetterstation24");                  //Login to the RaspberryPI server

    String httpRequestData = "device_id=" + String(DEVICE_ID)
                           + "&temperature=" + String(temperature)
                           + "&pressure=" + String(pressure)
                           + "&humidity=" + String(humidity)
                           + "&lightvalue=" + String(lightvalue);

    int httpResponseCode = http.POST(httpRequestData);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println(httpResponseCode);
      Serial.println(response);
    } else {
      Serial.print("Error on sending POST: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  }

  //deep sleep 600s / 10min
  esp_sleep_enable_timer_wakeup(600000000);
  esp_deep_sleep_start();
}

void loop() {
  //empty because of deep sleep
}
