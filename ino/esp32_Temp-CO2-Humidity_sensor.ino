// This code is for an ESP32 project that reads temperature, CO2, and Humidity data from a Sensirion SCD41 sensor and displays it on an SSH1106 OLED screen.
// It also serves a simple web page to view the data and sends the readings to an InfluxDB instance.
#include <WiFi.h>
#include <WebServer.h>
#include <Wire.h>
#include <SensirionI2cScd4x.h>
#include <Arduino.h>
#include <HTTPClient.h>
#include <GyverOLED.h>
#define SCD41_I2C_ADDR_62 0x62
#ifdef NO_ERROR
#undef NO_ERROR
#endif
#define NO_ERROR 0
const char* ssid = "<your-wifi-SSID>"; // Edit the Wi-Fi SSID
const char* password = "<your-wifi-password>"; // Edit the Wi-Fi password
const char* hostname = "<your-esp32-hostname>"; // Edit the hostname for the ESP32
const char* influxUrl = "https://<your-influx-address-or-hostname>/api/v2/write?org=<your-org-name>&bucket=<your-bucket-name>&precision=s"; // Edit URL for InfluxDB API
const char* influxToken = "<your-influxdb-token>"; // Edit InfluxDB Token for authentication
float currentTemperature = 0;
float currentHumidity = 0;
WebServer server(80); // Inizialize the web server on port 80
SensirionI2cScd4x scd4x; // Inizialize the SCD41 sensor
GyverOLED<SSH1106_128x64> oled; // Inizialize the OLED display with SSH1106 driver
void PrintUint64(uint64_t& value) {
    Serial.print("0x");
    Serial.print((uint32_t)(value >> 32), HEX);
    Serial.print((uint32_t)(value & 0xFFFFFFFF), HEX);
}
// --- Function to manage the root server request (/) ---
void handleRoot() {
  String html = "<!DOCTYPE html><html><head>";
  html += "<meta charset='UTF-8'>";  // ⬅️ Questo risolve il problema dei caratteri!
  html += "<meta http-equiv='refresh' content='5'>";
  html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>";
  html += "<title>Indoor Measurements</title>";
  html += "<style>";
  html += "body { font-family: Arial, sans-serif; background-color: #f5f5f5; color: #333; padding: 20px; }";
  html += "h1 { color: #0066cc; }";
  html += "p { font-size: 1.2em; margin: 10px 0; }";
  html += ".box { background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); max-width: 500px; margin: auto; }";
  html += "</style></head><body>";
  html += "<div class='box'>";
  html += "<h1>🌿 Temp CO₂ RH 🌿</h1>";
  html += "<p><strong>IP ESP32:</strong> " + WiFi.localIP().toString() + "</p>";
  if (currentCO2 == 0) {
    html += "<p><strong>CO₂:</strong> waiting calibration...</p>";
  } else {
    html += "<p><strong>CO₂:</strong> " + String(currentCO2) + " ppm</p>";
  }
  html += "<p><strong>Temperature:</strong> " + String(currentTemperature, 1) + " &deg;C</p>";
  html += "<p><strong>Humidity:</strong> " + String(currentHumidity, 1) + " %</p>";
  html += "<p><em>Update every 5 seconds</em></p>";
  html += "<p><small>Uptime ESP: " + String(millis() / 1000) + " secondi</small></p>";
  html += "</div></body></html>";

  server.send(200, "text/html", html);
}
// Function OLED Display
void initDisplay()
{
  oled.init();  
  oled.clear();   
  oled.update(); 
}
void printUI()
{
  oled.home();
  oled.clear(); // Clean the display
  // Temperature Labels
  oled.setScale(1);
  oled.setCursorXY(2, 2);
  oled.print("Temp:");
  oled.setCursorXY(105, 1); // Poisition "o" for grades
  oled.print("o");
  oled.setScale(2);
  oled.setCursorXY(112, 2); // Position "C" 
  oled.print("C");
  // CO2 Labels
  oled.setScale(1);
  oled.setCursorXY(2, 24);
  oled.print("CO2:");
  oled.setCursorXY(108, 24);
  oled.print("ppm");
  // Humidity Labels
  oled.setCursorXY(2, 46);
  oled.print("RH:");
  oled.setCursorXY(118, 46);
  oled.print("%");
  oled.update();
}
// Function to send data to InfluxDB
void sendToInflux(uint16_t co2, float temperature, float humidity) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(influxUrl);
    http.addHeader("Authorization", "Token " + String(influxToken));
    http.addHeader("Content-Type", "text/plain");
    // InfluxDB Line Protocol)
    String payload = String(hostname) + " CO2=" + String(co2) + ",temperature=" + String(temperature, 1) + ",humidity=" + String(humidity, 1);
    int httpResponseCode = http.POST(payload);
    if (httpResponseCode > 0) {
      Serial.print("InfluxDB POST OK: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.print("Errore InfluxDB POST: ");
      Serial.println(http.errorToString(httpResponseCode));
    }
    http.end();
  } else {
    Serial.println("WiFi not connected, can't send to InfluxDB.");
  }
}
void setup() {
  Serial.begin(115200); // Initialize Serial communication at 115200 baud rate
  while (!Serial) {
    delay(100); // wait for Serial to be ready
  }
  Serial.println("\n--- ESP32 Initialization ---");
  // Set SDA e SCL PIN for I2C Communication
  delay(1000);
  initDisplay();
  printUI();
  oled.setScale(2);
  oled.setContrast(5);
  uint16_t error;
  char errorMessage[256];
  Serial.println("SCD41 Initialization...");
  scd4x.begin(Wire, SCD41_I2C_ADDR_62); // Start the sensor
  uint64_t serialNumber = 0;
  delay(30);
  error = scd4x.wakeUp();
    if (error != NO_ERROR) {
        Serial.print("Error trying to execute wakeUp(): ");
        errorToString(error, errorMessage, sizeof errorMessage);
        Serial.println(errorMessage);
  }
  error = scd4x.stopPeriodicMeasurement();
    if (error != NO_ERROR) {
        Serial.print("Error trying to execute stopPeriodicMeasurement(): ");
        errorToString(error, errorMessage, sizeof errorMessage);
        Serial.println(errorMessage);
  }
  error = scd4x.reinit();
    if (error != NO_ERROR) {
        Serial.print("Error trying to execute reinit(): ");
        errorToString(error, errorMessage, sizeof errorMessage);
        Serial.println(errorMessage);
  }
  error = scd4x.getSerialNumber(serialNumber);
  if (error != NO_ERROR) {
      Serial.print("Error trying to execute getSerialNumber(): ");
      errorToString(error, errorMessage, sizeof errorMessage);
      Serial.println(errorMessage);
      return;
  }
  // Start continuous measurement
  error = scd4x.startPeriodicMeasurement();
  if (error) {
    Serial.print("Errore starting the measurement: ");
    errorToString(error, errorMessage, 256);
    Serial.println(errorMessage);
    while (1) delay(100); // Infinite loop in case of error
  }
  Serial.println("SCD41 Measurement started.");
  // --- WiFi Connection ---
  Serial.print("WiFi Connection: ");
  Serial.println(ssid);
  WiFi.setHostname(hostname);
  WiFi.begin(ssid, password);
  // Wait for WiFi connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Connected!");
  Serial.print("Indirizzo IP dell'ESP32: ");
  Serial.println(WiFi.localIP()); // Write ESP32 IP address to Serial Monitor
  // --- Web Server initialization ---
  server.on("/", handleRoot);
  server.begin(); // Start the Web Server
  Serial.println("Server HTTP Started!");
  Serial.println("Open a browser and go to http://" + WiFi.localIP().toString());
}
void loop() {
  // --- Reading SDC41 Data ---
  uint16_t error;
  char errorMessage[256];
  bool dataReady;
  delay(5000);
  // Check if data is ready
  error = scd4x.getDataReadyStatus(dataReady);
  if (error) {
    Serial.print("Errore checking SDC41 'dataReady': ");
    errorToString(error, errorMessage, 256);
    Serial.println(errorMessage);
  } else if (dataReady) {
    // If data is ready, read the measurement
    uint16_t co2;
    float temperature, humidity;
    error = scd4x.readMeasurement(co2, temperature, humidity);
    if (error) {
      Serial.print("Reading failed from SD41 sensor: ");
      errorToString(error, errorMessage, 256);
      Serial.println(errorMessage);
    } else if (co2 == 0) { // Sensor can return 0 ppm if not calibrated
      Serial.println("CO2 Reading not valid (0 ppm), wait initial calibration.");
    } else {
      // Update the current values
      currentCO2 = co2;
      currentTemperature = temperature;
      currentHumidity = humidity;
      sendToInflux(co2, temperature, humidity); // Send data to InfluxDB
      // Set OLED scale for numerical values
      oled.setScale(2);
      // --- Temperature ---
      // 1. Place the cursor and print spaces to clear the previous value
      oled.setCursorXY(45, 2);
      oled.print("   ");
      // 2. Replace the cursor and print the new value
      oled.setCursorXY(45, 2);
      oled.print(String(currentTemperature, 1));
      // --- CO2 ---
      oled.setCursorXY(45, 24);
      oled.print("     ");
      oled.setCursorXY(45, 24);
      oled.print(currentCO2);
      // --- Humidity ---
      oled.setCursorXY(70, 46);
      oled.print("   ");
      oled.setCursorXY(70, 46);
      oled.print(String(currentHumidity, 0));
      // Update the OLED display
      oled.update();
      delay(10000);
      // Print the values to Serial Monitor
      Serial.print("CO2: "); Serial.print(currentCO2, 0); Serial.print(" ppm\t");
      Serial.print("Temperature: "); Serial.print(currentTemperature, 2); Serial.print(" *C\t");
      Serial.print("Humidity: "); Serial.print(currentHumidity, 0); Serial.println(" %");
    }
  }
  // --- Manage web server requests ---
  // This function must be called repeatedly to handle HTTP requests
  server.handleClient();
  delay(100);
}