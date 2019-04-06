from interactive_game import InteractiveGame, InvalidInputException
from random_digit import RandomDigitGenerator

class Bagels(InteractiveGame):
    number_of_digits = 3
    def __init__(self, tries):
        self._tries = tries
        self._secret_digits = RandomDigitGenerator(Bagels.number_of_digits).\
                              get_random_digits()
        self._result_fermi = []
        self._result_pico = []
        self._result_bagels = []

    def get_instruction(self):
        result = '\n' + '_' * 10 + 'The Bagels Game' + '_' * 10 + '\n'
        result += 'Guess my secret {}-digit number.\n'.\
                  format(Bagels.number_of_digits)
        result += 'Instructions:\n'
        result += 'Bagels\t: no digit is correct.\n'
        result += 'Pico\t: one digit is correct but in the wrong position.\n'
        result += 'Fermi\t: one digit is correct and in the correct position.'
        return result

    def get_prompt(self):
        return 'Guess my {}-digit number: '.format(Bagels.number_of_digits)

    def get_status_1(self):
        result = ''
        if len(self._result_fermi) == Bagels.number_of_digits:
            result += 'Result: ' + ' '.join(self._result_fermi) + '\n'
        elif self._result_fermi + self._result_pico:
            result += 'Result: ' + ' '.join(self._result_fermi + \
                                            self._result_pico) + '\n'
        elif self._result_bagels:
            result += 'Result: ' + self._result_bagels[0] + '\n'         
        return result

    def get_status_2(self):
        result = 'You have {} {} to guess my secret {}-digit number.'.\
                 format(self._tries, \
                        'chances' if self._tries > 1 else 'chance', \
                        Bagels.number_of_digits)
        return result

    def validate(self, guess):
        if guess != '' and guess[0] != '0' and \
           len(guess) == Bagels.number_of_digits and \
           guess.isdecimal() and len(set(guess)) == len(guess):
            return guess
        self._result_fermi = []
        self._result_pico = []
        self._result_bagels = []
        raise InvalidInputException('Invalid Input!\nPlease enter a {}-digit '
                                    'number.\nIt cannot begin with 0 '
                                    'and cannot repeat any digit.'.\
                                    format(Bagels.number_of_digits))

    def evaluate(self, validated_guess):
        self._tries -= 1
        self._result_fermi = []
        self._result_pico = []
        self._result_bagels = []
        for index, digit in enumerate(validated_guess):
            if digit == self._secret_digits[index]:
                self._result_fermi.append('Fermi')
            elif digit in self._secret_digits:
                self._result_pico.append('Pico')
            else:
                self._result_bagels.append('Bagels')

        if len(self._result_fermi) == Bagels.number_of_digits:
            return True, None
        else:
            return False, None        
            
    def can_continue(self):
        return self._tries > 0

    def say_congratulations(self):
        return 'Congratulation! You have successfully guessed my '\
               'secret {}-digit number {}.'\
               .format(Bagels.number_of_digits, ''.join(self._secret_digits))

    def say_sorry(self):
        return 'Sorry that you lost. My secret {}-digit number was {}.'.\
               format(Bagels.number_of_digits, ''.join(self._secret_digits))
