export

  class TV {
  public estaEncendido = false;
  public volumen = 0;

  encenderTV() {
    this.estaEncendido = true;
  }

  apagarTV() {
    this.estaEncendido = false;
  }

  subirVolumen() {
    this.volumen++;
  }

  bajarVolumen() {
    this.volumen--;
  }
}
