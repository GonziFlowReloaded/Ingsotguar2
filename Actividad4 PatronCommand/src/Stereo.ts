export

  class Stereo {

  public estaEncendido = false;
  public volumen = 0;

  encenderStereo() {
    this.estaEncendido = true;
  }

  apagarStereo() {
    this.estaEncendido = false;
  }

  subirVolumen() {
    this.volumen++;
  }

  bajarVolumen() {
    this.volumen--;
  }

}