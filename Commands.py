import re

class Command:
    def __init__(self):
        self.variables = {}
        self.commands = []
        self.forvariable = {}

    def movecommand(self, command: str, square_x: int, square_y: int) -> tuple[int, int]:
        match = re.match(r'move\((-?\d+),(-?\d+)\)', command)
        if match:
            x, y = map(int, match.groups())
            square_x += x
            square_y -= y
        return square_x, square_y

    # def colorcommand(self, command:str, color: list):
    #     match = re.match(r'move\((-?\d+),(-?\d+)\)', command)
    #
    def intcommand(self, command: str):
        match = re.match(r'int\s+([a-zA-Z])\s*=\s*(-?\d+)', command)
        if match:
            varname, varvalue = match.groups()
            self.variables[varname] = int(varvalue)

        print(self.variables.items())

    def forcommand(self, command: str):
        match = re.match(r'for\s+([a-zA-Z]{1,10})\s+in\s+(?:\(\s*(\d+)?\s*,\s*(\d+)+\s*\)|(\w+(?:\s*&&?\s*\w+)*))\s*:\s*(.*)',
                         command)
        if match:
            var_name, start_val, end_val, condition, block = match.groups()

            if start_val is None:
                start_val = 0
            else:
                start_val = int(start_val)

            end_val = int(end_val)

            # if condition:
            #     block = f"for {var_name} in range({start_val}, {end_val}): if {condition}: {block}"
            # else:
            #     block = f"for {var_name} in range({start_val}, {end_val}): {block}"

            for value in range(start_val, end_val):
                self.forvariable[var_name] = int(value)
                #exec(block)
                self.movecommand(command, value, value)

            print(self.forvariable.items())
            raise ValueError(f"Invalid for loop: {block}")



    def printcommand(self):
        pass
