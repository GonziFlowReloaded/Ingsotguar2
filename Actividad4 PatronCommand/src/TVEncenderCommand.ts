import { TV } from "./TV";

export
  class TVEncenderCommand implements Command {
  constructor(private tv: TV) { }

  ejecutar() {
    this.tv.encenderTV();
  }
}