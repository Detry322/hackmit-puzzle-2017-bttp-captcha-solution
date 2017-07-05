import base64
import json

def main():
  with open('challenge.json') as f:
    result = json.load(f)

  for image in result['images']:
    with open('images/' + image['name'] + '.jpg', 'w') as f:
      f.write(base64.b64decode(image['jpg_base64']))

if __name__ == "__main__":
  main()
