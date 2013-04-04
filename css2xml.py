import cssutils, gnosis.xml.pickle

css = {}
sheet = cssutils.parseFile("css.css")

for rule in sheet:
  if rule.type == rule.STYLE_RULE:
    css[rule.selectorText] = {}
    for sel in rule.selectorList:
      print sel.selectorText
    for property in rule.style:
      css[rule.selectorText][property.name] = property.value

print gnosis.xml.pickle.dumps(css)