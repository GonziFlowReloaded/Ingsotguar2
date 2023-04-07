export

  class ControlRemoto {
  private commands: Command[] = [];

  agregarCommand(command: Command) {
    this.commands.push(command);
  }

  ejecutarCommands() {
    this.commands.forEach((command) => {
      command.ejecutar();
    });
  }
}