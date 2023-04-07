import { Stereo } from "./Stereo";

export
  class StereoBajarVolumenCommand implements Command {
  constructor(private stereo: Stereo) { }

  ejecutar() {
    this.stereo.bajarVolumen();
  }
}