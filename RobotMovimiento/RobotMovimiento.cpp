#include "RobotMovimiento.h"

#define PI 3.14159265

RobotMovimiento::RobotMovimiento(uint8_t motorIzq, uint8_t motorDer)
  : _motor1(motorIzq), _motor2(motorDer) {}

void RobotMovimiento::moverMotores(int rpmIzq, int rpmDer, bool adelante1, bool adelante2) {
  int vel1 = map(rpmIzq, 0, 100, 0, 255);
  int vel2 = map(rpmDer, 0, 100, 0, 255);

  _motor1.setSpeed(vel1);
  _motor2.setSpeed(vel2);

  _motor1.run(adelante1 ? FORWARD : BACKWARD);
  _motor2.run(adelante2 ? FORWARD : BACKWARD);
}

void RobotMovimiento::esperarTiempo(float distancia_cm, int rpm, float radio_cm) {
  float circunferencia = 2 * PI * radio_cm;
  float revoluciones = distancia_cm / circunferencia;
  float tiempo_min = revoluciones / rpm;
  float tiempo_ms = tiempo_min * 60.0 * 1000.0;
  delay((unsigned long)tiempo_ms);
  paro();
}

void RobotMovimiento::adelante(float distancia_cm, int rpm, float radio_cm) {
  moverMotores(rpm, rpm, true, true);
  esperarTiempo(distancia_cm, rpm, radio_cm);
}

void RobotMovimiento::izquierda(float radio_cm, float distancia_ruedas_cm, int rpm) {
  float arco = (PI * distancia_ruedas_cm) / 4.0;  // giro 90°
  moverMotores(rpm, rpm, false, true);  // motor izquierdo atrás, derecho adelante
  esperarTiempo(arco, rpm, radio_cm);
}

void RobotMovimiento::derecha(float radio_cm, float distancia_ruedas_cm, int rpm) {
  float arco = (PI * distancia_ruedas_cm) / 4.0;  // giro 90°
  moverMotores(rpm, rpm, true, false);  // motor izquierdo adelante, derecho atrás
  esperarTiempo(arco, rpm, radio_cm);
}

void RobotMovimiento::paro() {
  _motor1.run(RELEASE);
  _motor2.run(RELEASE);
}
