import torch
import torch.nn as nn
import matplotlib.pyplot as plt

from utils import ALL_LETTERS, N_LETTERS
from utils import load_data, letter_to_tensor, line_to_tensor, random_training_example

#creating basic RNN network arch with desired sizes
class RNN(nn.Module):
  def __init__(self, input_size, hidden_size, output_size):
    super(RNN, self).__init__()
    self.hidden_size = hidden_size
    self.i2h = nn.Linear(input_size+hidden_size, hidden_size)
    self.i2o = nn.Linear(input_size+hidden_size, output_size)
    self.softmax = nn.LogSoftmax(dim=1)

  def forward(self, input_tensor, hidden_tensor):
    compined = torch.cat((input_tensor, hidden_tensor), 1)
    hidden = self.i2h(compined)
    output = self.i2o(compined)
    output = self.softmax(output)
    return output, hidden

  def init_hidden(self):
        return torch.zeros(1, self.hidden_size)



#----------------------------loading data and creating instance of RNN class--------------------------------------------------------
category_lines, all_categories = load_data()
n_hidden = 256
rnn = RNN(N_LETTERS, n_hidden, len(all_categories))


#--------------Helper function to transfrom catrgories from vertor form into textual form-------------------------------
def category_from_output(output):
  inx = tensor.argmax(output).item()
  return all_categories[inx]

#-------------------------function for training network on single word-------------------------------------------------------------
criterion = nn.NLLLoss()
learning_rate = 0.005
optimizer = torch.optim.SGD(rnn.parameters(), lr=learning_rate)

def train(line_tensor, category_tensor):
  hidden = rnn.init_hidden()
  for i in range(line_tensor.size()[0]):
    output, hidden = rnn(line_tensor[i], hidden)
  loss = criterion(output, category_tensor)
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

  return output, loss.item()

#-------------------iterating on all training data using the train function for epoc number's times---------------------
current_loss = 0
all_loses = []
n_iters = 150000
print_steps = 5000

for i in range(n_iters):
  line, category, line_tensor, category_tensor = random_training_example(category_lines, all_categories)
  output, loss = train(line_tensor, category_tensor)
  current_loss += loss

  if(i+1) % print_steps == 0:  #every 5000 iter these massage will be displayed
    guess = category_from_output(output)
    correct = "correct" if guess == category else "wrong"
    print(f"{i+1}:{correct}")

#-----------------------------finally, using the network for predection--------------------------------------------------
def predict(input_line):
    print(f"\n> {input_line}")
    with torch.no_grad():
        line_tensor = line_to_tensor(input_line)
        
        hidden = rnn.init_hidden()
    
        for i in range(line_tensor.size()[0]):
            output, hidden = rnn(line_tensor[i], hidden)
        
        guess = category_from_output(output)
        print(guess)




while True:
  name = input("write a name: ")
  if name == "quit":
    break
  predict(name)


















  

    
