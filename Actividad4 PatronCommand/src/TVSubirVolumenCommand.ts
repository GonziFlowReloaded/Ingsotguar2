import { TV } from "./TV";

export
  class TVSubirVolumenCommand implements Command {
  constructor(private tv: TV) { }

  ejecutar() {
    this.tv.subirVolumen();
  }
}