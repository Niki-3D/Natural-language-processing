class Processor:

  def __init__(self, data):
    self.data = data
    self.names = {}

  def process(self):
    self._extract_names(self.data)
    return self.names

  def _extract_names(self, data):
    for key, value in data.items():
      if isinstance(value, dict):
        self._extract_names(value)
      else:
        # Handle case where value is not a dictionary
        self.names[f"{key}"] = round(value, 2)

  def display_names(self):
    for name, value in sorted(self.names.items()):
      print(f"{name}: {value:.2f}")

  def capitalize_names(self):
    capitalized_names = {}
    for name, value in self.names.items():
      capitalized_name = " ".join([part.capitalize() for part in name.split()])
      capitalized_names[capitalized_name] = value
    self.names = capitalized_names

  def run_processor(self, data):
    processor = Processor(data)
    names = processor.process()
    processor.capitalize_names()
    processor.display_names()

