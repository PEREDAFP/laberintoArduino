
#include <AFMotor.h>
#include <RobotMovimiento.h>

RobotMovimiento robot(1, 2);

// Debes ajustar el radio, la distancia de ruedas y los rpm a tu robot en particular.
//Ten en cuenta que cada motor, cada batería es un mundo diferente.
void setup() {
  float radio_rueda = 1.5;
  float distancia_ruedas = 16.0;
  int rpm = 100;
  
  robot.adelante(60, rpm, radio_rueda);
  delay(1000);
  robot.izquierda(radio_rueda, distancia_ruedas, rpm);
  delay(1000);
  robot.derecha(radio_rueda, distancia_ruedas, rpm);
  delay(1000);
  robot.derecha(radio_rueda, distancia_ruedas, rpm);
  delay(1000);
  robot.izquierda(radio_rueda, distancia_ruedas, rpm);
  delay(1000);
  robot.adelante(60, rpm, radio_rueda);
  delay(1000);
  
  robot.paro();
}

void loop() {}
