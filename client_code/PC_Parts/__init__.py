from ._anvil_designer import PC_PartsTemplate
from anvil import *


class PC_Parts(PC_PartsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
