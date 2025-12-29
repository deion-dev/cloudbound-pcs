from ._anvil_designer import HomeTemplate
from anvil import *

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Checkout())
    # Any code you write here will run before the form opens.


  @handle("view_desktops", "click")
  def view_desktops_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
