from ._anvil_designer import Create_AccountTemplate
from anvil import *


class Create_Account(Create_AccountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
