# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
#function to create a new beginning to a linked list

  def insert_beginning(self, new_value):
    new_node = Node(value = new_value, next_node = self.head_node)
    self.head_node = new_node
  
  #This function is to return a string representation of a linked list
  
  def stringify_list(self):
    string_list = ''
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list = string_list + str(current_node.get_value()) + '\n'
      current_node = current_node.get_next_node()
    return string_list
  
  #removes node with a specific value
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node        
    
# function to swap nodes places in a linked list
  def swap_nodes(input_list, val1, val2):
    print(f'Swapping {val1} with {val2}')

    node1_prev = None
    node2_prev = None
    node1 = input_list.head_node
    node2 = input_list.head_node

    if val1 == val2:
      print("Elements are the same - no swap needed")
      return

    while node1 is not None:
      if node1.get_value() == val1:
        break
      node1_prev = node1
      node1 = node1.get_next_node()

    while node2 is not None:
      if node2.get_value() == val2:
        break
      node2_prev = node2
      node2 = node2.get_next_node()

    if (node1 is None or node2 is None):
      print("Swap not possible - one or more element is not in the list")
      return

    if node1_prev is None:
      input_list.head_node = node2
    else:
      node1_prev.set_next_node(node2)

    if node2_prev is None:
      input_list.head_node = node1
    else:
      node2_prev.set_next_node(node1)

    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)
 #finds the nth last node in a linked list using two parralel pointers   
def nth_last_node(linked_list, n):
  current = None
  tail_seeker = linked_list.head_node
  count = 1
  while tail_seeker:
    tail_seeker = tail_seeker.get_next_node()
    count += 1
    if count >= n + 1:
      if current is None:
        current = linked_list.head_node
      else:
        current = current.get_next_node()
  return current    
# finds the middle node in a linked list using two pointers
def find_middle(linked_list):
  fast_pointer = linked_list.get_head_node()
  slow_pointer = linked_list.get_head_node()
  while fast_pointer:
    fast_pointer = fast_pointer.get_next_node()
    if fast_pointer:
      fast_pointer = fast_pointer.get_next_node()
      slow_pointer = slow_pointer.get_next_node()
  return slow_pointer
