class Postfix:

    def __init__(self, reg_exp: str):
        self.reg_exp = reg_exp

        self.operators_priority = [(symb, 3) for symb in ['(', ')']
                                   ] + [(symb, 2) for symb in ['*', '+', '?', '.']
                                        ] + [(symb, 1) for symb in ['|']]
        self.operators_priority = dict(self.operators_priority)

        self.allowable_operators = ['*', '+', '?', '.', '|', '(', ')']

        self.operators_stack = []
        self.out_queue = []

    def convert(self):
        self.__convert_to_postfix_notation()
        self.__move_operators_from_stack()

        return ''.join(self.out_queue)

    def __convert_to_postfix_notation(self):
        for symbol in self.reg_exp:
            if self.__is_operator(symbol):
                self.__process_operator(symbol)
            else:
                self.__process_symbol(symbol)

    def __move_operators_from_stack(self):
        while self.operators_stack:
            self.out_queue.append(self.operators_stack.pop())

    def __is_operator(self, symbol) -> bool:
        return symbol in self.allowable_operators

    def __process_symbol(self, symbol):
        self.out_queue.append(symbol)

    def __process_operator(self, symbol):
        if symbol == '(':
            self.operators_stack.append(symbol)
        elif symbol == ')':
            while self.operators_stack:
                last_stack_operator = self.operators_stack.pop()

                if last_stack_operator == '(':
                    break

                self.out_queue.append(last_stack_operator)
        else:
            symbol_priority = self.operators_priority.get(symbol)

            while self.operators_stack and self.__get_last_operator_priority() >= symbol_priority:
                last_operator = self.operators_stack.pop()

                if last_operator == '(':
                    self.operators_stack.append('(')
                    break
                else:
                    self.out_queue.append(last_operator)

            self.operators_stack.append(symbol)

    def __get_last_operator_priority(self):
        return self.operators_priority.get(self.operators_stack[-1])
