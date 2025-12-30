from ._anvil_designer import HomeTemplate
from anvil import *
from ..Checkout.ItemTemplate2 import ItemTemplate2
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

  @handle("button_5", "click")
  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    pass

  @handle("link_6", "click")
  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    
    pass
    

  



 

alert("Welcome to CloudBound PCs")

