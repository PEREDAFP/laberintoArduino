#include <AFMotor.h>
#include <RobotMovimiento.h>
#include <ArduinoJson.h>

// Instancia del robot: motores en M1 y M2
RobotMovimiento robot(1, 2);

// Parámetros físicos del robot
const float radio_rueda = 1.5;
const float distancia_ruedas = 16.0;
const int rpm = 100;


// Buffer para lectura desde Serial
String inputString = "";

void setup() {
  Serial.begin(9600); // En nuestro caso no utilizaremos la librería SoftwareSerial.h ya que utilizamos
                      //Los pines 0 y 1 de Arduino por ocupar el resto el SHIELD
  Serial.println("Esperando comandos JSON...");
}

void loop() {
  if (Serial.available()>0) {
    char c = Serial.read();
    if (c == '\n') {
      procesarComando(inputString);
      inputString = "";
    } else {
      inputString += c;
    }
  }
}

void procesarComando(String jsonStr) {
  StaticJsonDocument<128> doc;
  DeserializationError error = deserializeJson(doc, jsonStr);

  if (error) {
    Serial.print("Error al parsear JSON: ");
    Serial.println(error.f_str());
    return;
  }

  String accion = doc["accion"];
  float espacio = doc["espacio"];  // En metros si viene de fuera

  Serial.print("Acción: ");
  Serial.println(accion);

  if (accion == "avanza") {
    
    robot.adelante(espacio, rpm, radio_rueda);
  } 
  else if (accion == "izquierda") {
    robot.izquierda(radio_rueda, distancia_ruedas,rpm);
  } 
  else if (accion == "derecha") {
    robot.derecha(radio_rueda, distancia_ruedas, rpm);
  } 
  else if (accion == "paro") {
    robot.paro();
  } 
  else {
    Serial.println("Acción no reconocida.");
  }
}

