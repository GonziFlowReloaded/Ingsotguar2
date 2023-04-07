import { ControlRemoto } from "../src/ControlRemoto";
import { TV } from "../src/TV";
import { TVApagarCommand } from "../src/TVApagarCommand";
import { TVBajarVolumenCommand } from "../src/TVBajarVolumenCommand";
import { TVEncenderCommand } from "../src/TVEncenderCommand";
import { TVSubirVolumenCommand } from "../src/TVSubirVolumenCommand";
import { Stereo } from "../src/Stereo";
import { StereoBajarVolumenCommand } from "../src/StereoBajarVolumenCommand";
import { StereoApagarCommand } from "../src/StereoApagarCommand";
import { StereoEncenderCommand } from "../src/StereoEncenderCommand";
import { StereoSubirVolumenCommand } from "../src/StereoSubirVolumenCommand";


describe('Pruebas para TV', () => {
  it('Debe encender la TV', () => {
    const tv = new TV();
    const control = new ControlRemoto();
    control.agregarCommand(new TVEncenderCommand(tv));

    control.ejecutarCommands();
    expect(tv.estaEncendido).toBe(true);
  });

  it('Debe apagar la TV', () => {
    const tv = new TV();
    const control = new ControlRemoto();
    control.agregarCommand(new TVApagarCommand(tv));

    control.ejecutarCommands();
    expect(tv.estaEncendido).toBe(false);
  });

  it('Debe subir el volumen de la TV', () => {
    const tv = new TV();
    const control = new ControlRemoto();
    control.agregarCommand(new TVSubirVolumenCommand(tv));

    control.ejecutarCommands();
    expect(tv.volumen).toBe(1);
  });

  it('Debe bajar el volumen de la TV', () => {
    const tv = new TV();
    const control = new ControlRemoto();
    control.agregarCommand(new TVBajarVolumenCommand(tv));

    control.ejecutarCommands();
    expect(tv.volumen).toBe(-1);
  });
});

describe('Pruebas para Stereo', () => {
  it('Debe encender el Stereo', () => {
    const stereo = new Stereo();
    const control = new ControlRemoto();
    control.agregarCommand(new StereoEncenderCommand(stereo));

    control.ejecutarCommands();
    expect(stereo.estaEncendido).toBe(true);
  });

  it('Debe apagar el Stereo', () => {
    const stereo = new Stereo();
    const control = new ControlRemoto();
    control.agregarCommand(new StereoApagarCommand(stereo));

    control.ejecutarCommands();
    expect(stereo.estaEncendido).toBe(false);
  });

  it('Debe subir el volumen del Stereo', () => {
    const stereo = new Stereo();
    const control = new ControlRemoto();
    control.agregarCommand(new StereoSubirVolumenCommand(stereo));

    control.ejecutarCommands();
    expect(stereo.volumen).toBe(1);
  });

  it('Debe bajar el volumen del Stereo', () => {
    const stereo = new Stereo();
    const control = new ControlRemoto();
    control.agregarCommand(new StereoBajarVolumenCommand(stereo));

    control.ejecutarCommands();
    expect(stereo.volumen).toBe(-1);
  });
});


