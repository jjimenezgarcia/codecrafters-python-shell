from dataclasses import dataclass


@dataclass
class State:
    exit: bool = False

    def set_exit(self, valor: bool = True) -> None:
        self.exit = valor


state = State()
