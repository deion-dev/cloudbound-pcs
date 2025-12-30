from ._anvil_designer import HomeTemplate
from anvil import *
from anvile_extras import popover
class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  @handle("button_3", "click")
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = confirm("Add to cart?")
    pass

  self.button = button_3_click()
  self.button.popover(content='example text', title=)


alert("Welcome to CloudBound PCs")

