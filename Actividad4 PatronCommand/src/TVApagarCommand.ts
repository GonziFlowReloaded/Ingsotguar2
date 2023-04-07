import { TV } from "./TV";

export
  class TVApagarCommand implements Command {
  constructor(private tv: TV) { }

  ejecutar() {
    this.tv.apagarTV();
  }
}