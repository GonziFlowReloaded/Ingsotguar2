import { Stereo } from "./Stereo";

export
  class StereoSubirVolumenCommand implements Command {
  constructor(private stereo: Stereo) { }

  ejecutar() {
    this.stereo.subirVolumen();
  }
}