import { TV } from "./TV";

export
  class TVBajarVolumenCommand implements Command {
  constructor(private tv: TV) { }

  ejecutar() {
    this.tv.bajarVolumen();
  }
}