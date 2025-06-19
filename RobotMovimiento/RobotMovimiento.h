#ifndef RobotMovimiento_h
#define RobotMovimiento_h

#include <Arduino.h>
#include <AFMotor.h>

class RobotMovimiento {
  public:
    RobotMovimiento(uint8_t motorIzq, uint8_t motorDer);
    
    void adelante(float distancia_cm, int rpm, float radio_rueda_cm);
    void izquierda(float radio_rueda_cm, float distancia_ruedas_cm, int rpm);
    void derecha(float radio_rueda_cm, float distancia_ruedas_cm, int rpm);
    void paro();

  private:
    AF_DCMotor _motor1;
    AF_DCMotor _motor2;

    void moverMotores(int rpmIzq, int rpmDer, bool adelante1, bool adelante2);
    void esperarTiempo(float distancia_cm, int rpm, float radio_cm);
};

#endif

