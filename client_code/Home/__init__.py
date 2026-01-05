from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..parts import parts
from ..desktops import desktops


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  @handle("button_3", "click")
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now?")
    pass


  @handle("addcart1", "click")
  def addcart1_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to cart?")
    pass

  @handle("button_6", "click")
  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to cart?")
    pass

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now?")
    pass

  @handle("button_7", "click")
  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to cart?")
    pass

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now?")
    pass



  @handle("view_pcparts", "click")
  def view_pcparts_click(self, **properties):
    """This method is called when the link is clicked"""
    self.content_panel.clear() 
    self.init_components(**properties)
    self.content_panel.add_component(parts())
    pass


  @handle("link_1", "click")
  def link_1_click(self, **properties):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.init_components(**properties)
    self.content_panel.add_component(Home())
    pass

  @handle("view_desktops", "click")
  def view_desktops_click(self, **properties):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.init_components(**properties)
    self.content_panel.add_component(desktops())
   
    pass

  @handle("link_2", "click")
  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.login_with_form()
    pass

  @handle("text_box_4", "pressed_enter")
  def text_box_4_pressed_enter(self, **properties):
    """This method is called when the user presses Enter in this text box"""
    self.items = [
      {'name': 'CPU', 'category': 'PCpart'},
      {'name': 'Graphic Card', 'category': 'PCparts'},
      {'name': 'Keyboard', 'category': 'Accessories'},
      {'name': 'Monitor', 'category': 'PCparts'}
    ]

    @handle("text_box_4", "pressed_enter")
    def text_box_4_pressed_enter(self, **event_args):
      """This method is called when the user presses Enter in this text box"""
      search_term = self.text_box_4.text.lower()
      filtered_items = [item for item in self.items if search_term in item['name'].lower()]
      self.update_search_results(filtered_items)

    def update_search_results(self, filtered_items):
      """Update the RepeatingPanel with filtered items"""
      self.results_panel.items = filtered_items
      
      
    pass


      
  



 

alert("Welcome to CloudBound PCs")

