
class Authentication:
    def __init__(self, path_file = 'users/'):
        # Attributes
        self.state_list = []
        self.path_file = path_file

    # Methods
    def set_state(self, message = None, state = None):
        if message is None:
            print("Message must be Enter")
            raise Exception("Message must be Enter")
        if not self.state_list:
            print("State list must be declared first")
            raise Exception("State list not declared")
        if state is None:
            state = self.state_list[0]
        chat_id = message.chat.id
        # Check File users/972345
        with open(self.path_file + str(chat_id), 'w', encoding='utf-8-sig') as f:
            f.write(str(state))
        
    def set_state_list(self, state_list):
        self.state_list = state_list

    def get_state(self, message):
        chat_id = message.chat.id
        try:
            with open(self.path_file + str(chat_id), 'r', encoding='utf-8-sig') as f:
                lines = f.readlines()
                state = lines[0].strip()
            return state
        except:
            print("User does not exist")
            return None

    def reset_state(self, message):
        self.set_state(message)

    def next_state(self, message):
        current_state = self.get_state(message)
        if current_state is None:
            print("User does not exist")
            raise Exception("User does not exist, Can't change state")
        next_state_index = self.state_list.index(current_state) + 1
        if next_state_index == len(self.state_list):
            next_state_index = 0
        next_state = self.state_list[next_state_index]
        self.set_state(message, next_state)