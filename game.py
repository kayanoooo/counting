from player import Player

class Game:
    def __init__(self):
        self.head = None
        self.last = None
        self.count = 0

    def add(self, id, name):
        new_node = Player(id, name)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            self.last = new_node
        else:
            self.last.next = new_node
            new_node.next = self.head
            self.last = new_node
        self.count +=1

    def run(self, k, log_file):
        with open(log_file, 'w', encoding='utf-8') as f:
            curr = self.head
            prev = self.last

            f.write(f'игра началась (удаляем каждого {k}-го)\n\n')

            while self.count > 0:
                for _ in range(k-1):
                    prev = curr
                    curr = curr.next

                info = f'удален: id {curr.id} - {curr.name}'
                print(info)
                f.write(info+'\n')

                prev.next = curr.next
                curr = curr.next
                self.count -= 1