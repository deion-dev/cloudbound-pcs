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

    # Example list of items (replace with actual data)
    self.items = [
      {'name': 'CPU', 'category': 'PCpart'},
      {'name': 'Graphic Card', 'category': 'PCparts'},
      {'name': 'Keyboard', 'category': 'Accessories'},
      {'name': 'Monitor', 'category': 'PCparts'}
    ]

    # Initialize the RepeatingPanel (results_panel)
    self.results_panel.items = self.items  # Display all items initially

    # Button click event handlers
  @handle("button_3", "click")
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    confirm("Buy Now?")

  @handle("addcart1", "click")
  def addcart1_click(self, **event_args):
    """This method is called when the button is clicked"""
    confirm("Add to cart?")

  @handle("button_6", "click")
  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    confirm("Add to cart?")

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    confirm("Buy Now?")

  @handle("button_7", "click")
  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    confirm("Add to cart?")

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    confirm("Buy Now?")

    # Content panel switching
  @handle("view_pcparts", "click")
  def view_pcparts_click(self, **properties):
    """This method is called when the link is clicked"""
    self.content_panel.clear() 
    self.content_panel.add_component(parts())  # Load parts component

  @handle("link_1", "click")
  def link_1_click(self, **properties):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Home())  # Load the Home component

  @handle("view_desktops", "click")
  def view_desktops_click(self, **properties):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(desktops())  # Load desktops component

  @handle("link_2", "click")
  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.login_with_form()  # Trigger login form

    # Search Bar functionality
  @handle("text_box_4", "pressed_enter")
  def text_box_4_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in the search box"""
    search_term = self.text_box_4.text.lower()  # Get the search term
    filtered_items = [item for item in self.items if search_term in item['name'].lower()]
    self.update_search_results(filtered_items)

  def update_search_results(self, filtered_items):
    """Update the RepeatingPanel with filtered items"""
    self.results_panel.items = filtered_items  # Update the items property of the RepeatingPanel

  @handle("GPU_button", "click")
  def GPU_button_click(self, **event_args):
    """This method is called when the GPU button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(parts())  # Load parts component (possibly for GPU selection)

  @handle("CPU_Button", "click")
  def CPU_Button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(parts())  # Load parts component (possibly for GPU selection)

  @handle("RAM_Button", "click")
  def RAM_Button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(parts())  # Load parts component (possibly for GPU selection)

  @handle("spec_1", "click")
  def spec_1_click(self, **event_args):
    """This method is called when spec_1 is clicked"""
    alert("You clicked on spec_1. Here are the details of the specification...")

  @handle("spec_2", "click")
  def spec_2_click(self, **event_args):
    """This method is called when spec_2 is clicked"""
    alert("You clicked on spec_2. Here are the details of the specification...")

  @handle("spec_3", "click")
  def spec_3_click(self, **event_args):
    """This method is called when spec_3 is clicked"""
    alert("You clicked on spec_3. Here are the details of the specification...")

  @handle("Spec_1", "click")
  def Spec_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

