from ._anvil_designer import partsTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users


class parts(partsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart?")
    pass

  @handle("button_5", "click")
  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now?")
    pass

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart?")
    pass

  @handle("button_4", "click")
  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now?")
    pass

  @handle("button_6", "click")
  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart?")
    pass

  @handle("button_3", "click")
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now?")
    pass

  @handle("button_7", "click")
  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart?")
    pass

  @handle("button_8", "click")
  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now?")
    pass

  @handle("button_9", "click")
  def button_9_click(self, **event_args):
    c = confirm("Add to Cart?")
    """This method is called when the button is clicked"""
    pass

  @handle("button_10", "click")
  def button_10_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now?")
    pass

  @handle("button_12", "click")
  def button_12_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart?")
    pass

  @handle("button_11", "click")
  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now?")
    pass

  @handle("button_26", "click")
  def button_26_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart?")
    pass

  @handle("button_27", "click")
  def button_27_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now?")
    pass

  @handle("button_24", "click")
  def button_24_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart?")
    pass

  @handle("button_25", "click")
  def button_25_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now")
    pass

  @handle("button_22", "click")
  def button_22_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart")
    pass

  @handle("button_23", "click")
  def button_23_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now")
    pass

  @handle("button_35", "click")
  def button_35_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart")
    pass

  @handle("button_36", "click")
  def button_36_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now")
    pass

  @handle("button_33", "click")
  def button_33_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart")
    pass

  @handle("button_34", "click")
  def button_34_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now")
    pass

  @handle("button_31", "click")
  def button_31_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart")
    pass

  @handle("button_32", "click")
  def button_32_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now")
    pass

  @handle("button_37", "click")
  def button_37_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart")
    pass

  @handle("button_39", "click")
  def button_39_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now")
    pass

  @handle("button_40", "click")
  def button_40_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart")
    pass

  @handle("button_41", "click")
  def button_41_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now")
    pass

  @handle("button_42", "click")
  def button_42_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to Cart")
    pass

  @handle("button_43", "click")
  def button_43_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Buy Now")
    pass

