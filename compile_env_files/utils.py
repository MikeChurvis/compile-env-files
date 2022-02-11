def islist(obj, type):
  return isinstance(obj, list) and all(isinstance(element, type) for element in obj)