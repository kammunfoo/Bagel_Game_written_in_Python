from interactive_game import InteractiveGame, InvalidInputException

class InteractiveGameDriver:
    def __init__(self, game):
        if not isinstance(game, InteractiveGame):
            raise InvalidGameException('Invalid Game!')

        self._game = game
        self._win = False

    def play(self):
        print(self._game.get_instruction())

        while self._game.can_continue():
            print(self._game.get_status_1())
            print(self._game.get_status_2())
            ''' For Debug Purpose '''
            #print('Secret Digits:', ''.join(self._game._secret_digits))
            user_input = input(self._game.get_prompt())
            
            try:
                validated_guess = self._game.validate(user_input)
                ''' For Debug Purpose '''
                #print(validated_guess)
                result, hint = self._game.evaluate(validated_guess)
                if result:
                    self._win = True
                    break

            except InvalidInputException as err:
                print(err)

        if self._win:
            print(self._game.get_status_1())
            print(self._game.say_congratulations())
        else:
            print(self._game.get_status_1())
            print(self._game.say_sorry())
                
if __name__ == '__main__':
    from bagels import Bagels
    dr = InteractiveGameDriver(Bagels(10))
    dr.play()
