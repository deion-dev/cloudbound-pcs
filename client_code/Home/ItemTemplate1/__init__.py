from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
  def set_data(self, item):
    """This method is called to set the data for each item in the repeating panel"""

    # Set the 'name' and 'category' data for each item
    self.item_name_label.text = item['name']  # Set name (e.g., '7800X3D')
    self.item_category_label.text = item['category']  # Set category (e.g., 'CPU')

    # You can further customize how to handle categories like CPU, GPU, RAM if needed
    if item['category'] == 'CPU':
      # You can change the styling or do something specific for CPU category
      self.item_category_label.foreground = 'blue'  # Just an example, color the text blue for CPU

    elif item['category'] == 'GPU':
      self.item_category_label.foreground = 'green'  # Color the text green for GPU

    elif item['category'] == 'RAM':
      self.item_category_label.foreground = 'red'  # Color the text red for RAM

