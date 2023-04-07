import { Stereo } from "./Stereo";

export
  class StereoEncenderCommand implements Command {
  constructor(private stereo: Stereo) { }

  ejecutar() {
    this.stereo.encenderStereo();
  }
}