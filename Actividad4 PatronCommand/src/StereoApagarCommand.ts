import { Stereo } from "./Stereo";

export
  class StereoApagarCommand implements Command {
  constructor(private stereo: Stereo) { }

  ejecutar() {
    this.stereo.apagarStereo();
  }
}